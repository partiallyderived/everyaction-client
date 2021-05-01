import json
import urllib.parse
from collections import OrderedDict

from requests import Response

from http_router import Router

import pytest

from everyaction import EAClient, EAFindFailedException
from everyaction.objects import ActivistCode, ActivistCodeData, Note, Person, ResultCode


router = Router()
ENDPOINT = 'http://example.com'


class EAData(OrderedDict):
    # Storage for data which have IDs.
    def __init__(self, prefix, **kwargs):
        super().__init__(**kwargs)
        self.id_key = f'{prefix}Id'
        self._next_id = 1

    def add(self, data):
        next_id = self.next_id()
        self[next_id] = data
        data[self.id_key] = next_id
        return next_id

    def next_id(self):
        next_id = self._next_id
        self._next_id += 1
        return next_id


class MockServer:
    # Simulates an EveryAction server so that derived convenience methods, such as EAClient.people.lookup, may be
    # tested without having to consider mocking for every method.
    # May be expanded as more convenience methods are added and need to be tested.
    NOT_FOUND = {'errors': [{'text': 'Not found'}]}, 404

    def __init__(self):
        self.activist_codes = EAData('activistCode')
        self.people = EAData('van')
        self.result_codes = EAData('resultCode')

        self.my_activists = set()
        self.person_to_activist_code_data = {}
        self.person_to_codes = {}
        self.person_to_disclosure_fields = {}
        self.person_to_membership = {}
        self.person_to_next_note_id = {}
        self.person_to_notes = {}
        self.person_to_result_codes = {}

    @staticmethod
    def _match(person, candidate):
        # This is not how find actually works on EveryAction, but this is fine for testing.
        for key, value in candidate.items():
            if person.get(key) != value:
                return False
        return True

    @staticmethod
    def _paginated(records, query):
        records = list(records)
        top = query.get('$top', 50)
        skip = query.get('$skip', 0)
        end = skip + top
        result = records[skip:end]
        if len(result) > end:
            query[skip] = end
            query_str = urllib.parse.urlencode(query)
            next_page_link = f'{ENDPOINT}?{query_str}'
        else:
            next_page_link = None
        return {
            'items': result,
            'count': len(result),
            'nextPageLink': next_page_link
        }

    def _find(self, match_candidate):
        for person in self.people.values():
            if self._match(person, match_candidate):
                return person
        return None

    def add_activist_code(self, data):
        self.activist_codes.add(data)

    def add_person(self, data):
        van_id = self.people.add(data)
        self.person_to_membership[van_id] = {}

    def add_result_code(self, data):
        self.result_codes.add(data)

    @router.route('/activistCodes/{code_id:int}', methods=['GET'])
    def activist_code_get(self, code_id, query, data):
        return list(self.activist_codes.get(code_id, self.NOT_FOUND))

    @router.route('/activistCodes', methods=['GET'])
    def activist_codes_list(self, query, data):
        return self._paginated(self.activist_codes.values(), query)

    @router.route('/canvassResponses/resultCodes', methods=['GET'])
    def canvass_response_result_codes(self, query, data):
        return list(self.result_codes.values())

    @router.route('/people/{van_id:int}/activistCodes', methods=['GET'])
    def person_activist_codes(self, van_id, query, data):
        return self._paginated(
            [self.activist_codes[x] for x in self.person_to_activist_code_data.get(van_id, [])],
            query
        )

    @router.route('/people/{van_id:int}/canvassResponses', methods=['POST'])
    def person_add_canvass_responses(self, van_id, query, data):
        result_code_id = data.get('resultCodeId')
        if result_code_id is not None:
            self.person_to_result_codes.setdefault(van_id, set()).add(result_code_id)
        else:
            for response in data['responses']:
                if response['type'] == 'ActivistCode':
                    activist_code_data = self.person_to_activist_code_data.setdefault(van_id, OrderedDict())
                    activist_code_id = response['activistCodeId']
                    activist_code = self.activist_codes.get(activist_code_id)
                    if activist_code is None:
                        return {'errors': [{'text': f'No such activist code: {activist_code_id}'}]}, 404
                    if response['action'] == 'Apply':
                        activist_code_data[activist_code_id] = {
                            'activistCodeId': activist_code_id,
                            'activistCodeName': activist_code['name']
                        }
                    elif response['action'] == 'Remove':
                        if activist_code_id in activist_code_data:
                            del activist_code_data[activist_code_id]
                    else:
                        return {'errors': [{'text': 'Expected action to be "Apply" or "Remove"'}]}, 400

    @router.route('/people/{van_id:int}/notes', methods=['POST'])
    def person_add_notes(self, van_id, query, data):
        self.person_to_notes.setdefault(van_id, EAData('note')).add(data)

    @router.route('/people/find', methods=['POST'])
    def person_find(self, query, data):
        result = self._find(data)
        if result is not None:
            return result
        # 404, but no error object when failing to find through this endpoint.
        return {}, 404

    @router.route('/people/findOrCreate', methods=['POST'])
    def person_find_or_create(self, query, data):
        result = self._find(data)
        if result is None:
            self.add_person(data)
            result = data
        return result

    @router.route('/people/{van_id:int}', methods=['GET'])
    def person_get(self, van_id, query, data):
        return self.people.get(van_id, self.NOT_FOUND)

    @router.route('/people/{van_id:int}/notes', methods=['GET'])
    def person_notes(self, van_id, query, data):
        return self._paginated(self.person_to_notes.get(van_id, {}).values(), query)

    @router.route('/people/{van_id:int}', methods=['POST'])
    def person_update(self, van_id, query, data):
        person = self.people.get(van_id)
        if person is None:
            return self.NOT_FOUND
        person.update(data)
        return person


class MockSession:
    # Simulated session which calls the appropriate method in MockServer.
    def __init__(self, server):
        self.server = server

    def handle(self, url, method, **kwargs):
        data = json.loads(kwargs.get('data', '{}'))
        params = kwargs.get('params', {})
        query_in_url = urllib.parse.urlparse(url).query
        if query_in_url:
            params |= urllib.parse.parse_qs(query_in_url)
        route = url[len(ENDPOINT):]
        match = router(route, method=method)
        path_params = match.params or {}
        result = match.target(self.server, **path_params, query=params, data=data)
        resp = Response()
        resp.reason = 'OK'
        resp.status_code = 200
        if isinstance(result, tuple):
            data, code = result
            resp.status_code = code
            if code >= 400 and 'errors' in data:
                resp.reason = data['errors'][0]['text']
            resp._content = json.dumps(data).encode()
        else:
            resp._content = json.dumps(result).encode()
        return resp

    def close(self):
        pass

    def delete(self, route, **kwargs):
        return self.handle(route, 'DELETE', **kwargs)

    def get(self, route, **kwargs):
        return self.handle(route, 'GET', **kwargs)

    def patch(self, route, **kwargs):
        return self.handle(route, 'PATCH', **kwargs)

    def post(self, route, **kwargs):
        return self.handle(route, 'POST', **kwargs)

    def put(self, route, **kwargs):
        return self.handle(route, 'PUT', **kwargs)


@pytest.fixture
def server():
    return MockServer()


@pytest.fixture
def client(server):
    client = EAClient('app', 'key', endpoint=ENDPOINT, mode=1)
    client._session = MockSession(server)
    return client


def test_people(client, server):
    server.add_person({'emails': [{'email': 'alice@bob.com'}]})

    # Try looking up with both email and ID.
    assert client.people.lookup(email='alice@bob.com') == Person(id=1, email='alice@bob.com')
    assert client.people.lookup(id=1) == Person(id=1, email='alice@bob.com')

    # Try updating Alice with update_if_exists.
    assert client.people.update_if_exists({'email': 'alice@bob.com'}, {'first': 'Alice'})
    assert client.people.lookup(email='alice@bob.com') == Person(id=1, email='alice@bob.com', first='Alice')

    # update_if_exists should result in None if no such person record is found.
    assert client.people.update_if_exists({'email': 'bob@alice.com'}, {'first': 'Bob'}) is None

    # Confirm looking up with a bad email results in None.
    assert client.people.lookup(email='bob@alice.com') is None

    server.add_activist_code({'name': 'Cool Activist'})
    server.add_activist_code({'name': 'Activist Person'})

    # Add activist code with activist code ID.
    client.people.apply_activist_code(1, email='alice@bob.com')
    assert client.people.activist_codes(1) == [ActivistCodeData(id=1, name='Cool Activist')]

    # Remove activist code with activist code ID.
    client.people.remove_activist_code(1, email='alice@bob.com')
    assert client.people.activist_codes(1) == []

    # Add activist code with activist code name.
    client.people.apply_activist_code('Activist Person', email='alice@bob.com')
    assert client.people.activist_codes(1) == [ActivistCodeData(id=2, name='Activist Person')]

    # Remove activist code with activist code name.
    client.people.remove_activist_code('Activist Person', email='alice@bob.com')
    assert client.people.activist_codes(1) == []

    # Confirm that trying to add activist code to person who can't be found results in exception.
    with pytest.raises(EAFindFailedException, match='Could not find'):
        client.people.apply_activist_code(1, email='bob@alice.com')

    # Add some notes.
    client.people.apply_notes(Note(text='Is neat'), email='alice@bob.com')
    assert client.people.notes(1) == [Note(id=1, text='Is neat')]

    client.people.apply_notes(Note(text='Has a cool shirt'), email='alice@bob.com')
    assert client.people.notes(1) == [Note(id=1, text='Is neat'), Note(id=2, text='Has a cool shirt')]

    server.add_result_code({'name': 'No call'})
    server.add_result_code({'name': 'No text'})

    # Apply some result codes.
    # First by ID.
    client.people.apply_result_code(1, email='alice@bob.com')
    assert server.person_to_result_codes == {1: {1}}

    # Then by name.
    client.people.apply_result_code('No text', email='alice@bob.com')
    assert server.person_to_result_codes == {1: {1, 2}}


def test_activist_codes(client, server):
    # Test that failing to find an activist code results in an EAFindFailedException.
    with pytest.raises(EAFindFailedException, match='No activist codes named'):
        client.activist_codes.find('Cool Activist')

    # Add an activist code and try to find it.
    server.add_activist_code({'name': 'Cool Activist'})
    assert client.activist_codes.find('Cool Activist') == ActivistCode(id=1, name='Cool Activist')

    # Add more activist codes and try to find multiple with find_each.
    server.add_activist_code({'name': 'Cooler Activist'})
    server.add_activist_code({'name': 'Coolest Activist'})
    server.add_activist_code({'name': 'Someone Else'})
    assert client.activist_codes.find_each(['Cooler Activist', 'Someone Else']) == {
        'Cooler Activist': ActivistCode(id=2, name='Cooler Activist'),
        'Someone Else': ActivistCode(id=4, name='Someone Else')
    }

    with pytest.raises(EAFindFailedException, match='The following activist codes could not be found: Not An Activist'):
        client.activist_codes.find_each(['Cooler Activist', 'Not An Activist'])

    # Test that trying to find an activist code out of multiple of the same name results in an exception.
    server.add_activist_code({'name': 'Cool Activist'})
    with pytest.raises(EAFindFailedException, match='Multiple activist codes named "Cool Activist"'):
        client.activist_codes.find('Cool Activist')
    with pytest.raises(EAFindFailedException, match='Multiple activist codes named "Cool Activist"'):
        client.activist_codes.find_each(['Cool Activist', 'Someone Else'])


def test_result_codes(client, server):
    # Test that failing to find a result code results in an EAFindFailedException.
    with pytest.raises(EAFindFailedException, match='No such result code'):
        client.canvass_responses.find_result_code('No call')

    # Add a result code and try to find it.
    server.add_result_code({'name': 'No call'})
    assert client.canvass_responses.find_result_code('No call') == ResultCode(id=1, name='No call')
