import json
import textwrap
import time
import traceback
import unittest.mock as mock
import urllib.parse
from collections import OrderedDict
from datetime import datetime
from threading import Thread
from unittest.mock import call

from requests import Response

from http_router import Router

import pytest

from everyaction import EAClient, EAChangedEntityJobFailedException, EAFindFailedException
from everyaction.objects import *
from everyaction.services import ChangedEntities


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
        return data

    def next_id(self):
        next_id = self._next_id
        self._next_id += 1
        return next_id


class MockServer:
    # Simulates an EveryAction server so that derived convenience methods, such as EAClient.people.lookup, may be
    # tested without having to consider mocking for every method.
    # May be expanded as more convenience methods are added and need to be tested.

    # Message associated with a pending changed entity export job.
    CE_PENDING_MSG = 'Created export job'

    # Returned when a resource could not be found.
    NOT_FOUND = {'errors': [{'text': 'Not found'}]}, 404

    def __init__(self):
        self.activist_codes = EAData('activistCode')
        self.changed_entity_export_jobs = EAData('exportJob')
        self.contact_types = EAData('contactType')
        self.export_job_types = EAData('exportJobType')
        self.input_types = EAData('inputType')
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

        self.changed_entity_default_changed_to = '2000-01-01T00:00:00.000000+00:00'
        self.changed_entity_resources = {}

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
        return self.activist_codes.add(data)

    def add_changed_entity_export_job(self, data):
        return self.changed_entity_export_jobs.add(data)

    def add_changed_entity_resource(self, name, change_types, fields):
        self.changed_entity_resources[name] = (change_types, fields)

    def add_contact_type(self, data):
        return self.contact_types.add(data)

    def add_export_job_type(self, data):
        return self.export_job_types.add(data)

    def add_input_type(self, data):
        return self.input_types.add(data)

    def add_person(self, data):
        van_id = self.people.add(data)['vanId']
        self.person_to_membership[van_id] = {}
        return van_id

    def add_result_code(self, data):
        return self.result_codes.add(data)

    def update_changed_entity_export_job(self, job_id, with_data):
        self.changed_entity_export_jobs.get(job_id).update(with_data)

    @router.route('/activistCodes/{code_id:int}', methods=['GET'])
    def activist_code_get(self, code_id, query, data):
        return self.activist_codes.get(code_id, self.NOT_FOUND)

    @router.route('/activistCodes', methods=['GET'])
    def activist_codes_list(self, query, data):
        return self._paginated(self.activist_codes.values(), query)

    @router.route('/canvassResponses/contactTypes', methods=['GET'])
    def canvass_response_contact_types(self, query, data):
        return list(self.contact_types.values())

    @router.route('/canvassResponses/inputTypes', methods=['GET'])
    def canvass_response_input_types(self, query, data):
        return list(self.input_types.values())

    @router.route('/canvassResponses/resultCodes', methods=['GET'])
    def canvass_response_result_codes(self, query, data):
        return list(self.result_codes.values())

    @router.route('/changedEntityExportJobs/changeTypes/{resource}', methods=['GET'])
    def changed_entity_change_types(self, resource, query, data):
        return self.changed_entity_resources[resource][0]

    @router.route('/changedEntityExportJobs', methods=['POST'])
    def changed_entity_create_job(self, query, data):
        date_changed_to = data.get('dateChangedTo', self.changed_entity_default_changed_to)
        job_id = self.add_changed_entity_export_job({
            'dateChangedFrom': data['dateChangedFrom'],
            'dateChangedTo': date_changed_to,
            'exportedRecordCount': 0,
            'files': [],
            'jobStatus': 'Pending',
            'message': self.CE_PENDING_MSG
        })['exportJobId']
        return {
            'exportJobId': job_id,
            'dateChangedFrom': data['dateChangedFrom'],
            'dateChangedTo': date_changed_to,
            'excludeChangesFromSelf': data.get('excludeChangesFromSelf', False),
            'includeInactive': data.get('includeInactive', False),
            'requestedCustomFieldIds': data.get('requestedCustomFieldIds', []),
            'requestedFields': data.get('requestedFields', []),
            'requestedIds': data.get('requestedIds', []),
            'resourceType': data['resourceType']
        }

    @router.route('/changedEntityExportJobs/{job_id:int}', methods=['GET'])
    def changed_entities_job(self, job_id, query, data):
        return self.changed_entity_export_jobs.get(job_id)

    @router.route('/changedEntityExportJobs/fields/{resource}', methods=['GET'])
    def changed_entity_fields(self, resource, query, data):
        return self.changed_entity_resources[resource][1]

    @router.route('/changedEntityExportJobs/resources', methods=['GET'])
    def changed_entity_resources(self, query, data):
        return list(self.changed_entity_resources)

    @router.route('/exportJobTypes', methods=['GET'])
    def export_job_types(self, query, data):
        return self._paginated(list(self.export_job_types.values()), query)

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
        self.auth = ('user', 'pass|1')
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

    # Test People.preferred_email.
    assert Person().preferred_email is None
    assert Person(email='nopreferreddata@example.com').preferred_email is None
    assert (
        Person(email=Email('preferreddataavailable@example.com', preferred=True)).preferred_email ==
        'preferreddataavailable@example.com'
    )

    assert Person(emails=[Email('email1@example.com'), Email('email2@example.com')]).preferred_email is None
    assert (
        Person(emails=[Email('email1@example.com'), Email('email2@example.com', preferred=True)]).preferred_email ==
        'email2@example.com'
    )
    assert (
        Person(emails=[Email('email1@example.com', preferred=True), Email('email2@example.com')]).preferred_email ==
        'email1@example.com'
    )
    # Two preferred emails should result in an AssertionError.
    with pytest.raises(AssertionError):
        Person(
            emails=[Email('email1@example.com', preferred=True), Email('email2@example.com', preferred=True)]
        ).preferred_email

    # Test People.preferred_phone.
    assert Person().preferred_phone is None
    assert Person(phone='0000000000').preferred_phone is None
    assert Person(phone=Phone('1111111111', preferred=True)).preferred_phone == '1111111111'

    assert Person(phones=[Phone('1111111111'), Phone('2222222222')]).preferred_phone is None
    assert Person(phones=[Phone('1111111111'), Phone('2222222222', preferred=True)]).preferred_phone == '2222222222'
    assert Person(phones=[Phone('1111111111', preferred=True), Phone('2222222222')]).preferred_phone == '1111111111'

    # Two preferred phones should result in an AssertionError.
    with pytest.raises(AssertionError):
        Person(phones=[Phone('1111111111', preferred=True), Phone('2222222222', is_preferred=True)]).preferred_phone

    # Test People.preferred_address.
    assert Person().preferred_address is None
    assert Person(address=Address(line1='123 Fake Street')).preferred_address is None
    assert Person(
        address=Address(line1='123 Fake Street', preferred=True)
    ).preferred_address == Address(line1='123 Fake Street', preferred=True)

    assert Person(
        addresses=[Address(line1='123 Fake Street'), Address(line1='742 Evergreen Terrace')]
    ).preferred_address is None
    assert Person(
        addresses=[Address(line1='123 Fake Street'), Address(line1='742 Evergreen Terrace', preferred=True)]
    ).preferred_address == Address(line1='742 Evergreen Terrace', preferred=True)
    assert Person(
        addresses=[Address(line1='123 Fake Street', preferred=True), Address(line1='742 Evergreen Terrace')]
    ).preferred_address == Address(line1='123 Fake Street', preferred=True)

    # Two preferred addresses should result in an AssertionError.
    with pytest.raises(AssertionError):
        Person(addresses=[
            Address(line1='123 Fake Street', preferred=True),
            Address(line1='742 Evergreen Terrace', preferred=True)
        ]).preferred_address

    # Test detecting and modifying suppressions.
    person = Person()
    assert person.has_suppression(Suppression.DO_NOT_MAIL) is None
    assert person.do_not_call is None
    assert person.do_not_email is None
    assert person.do_not_mail is None
    assert person.do_not_walk is None

    assert person.add_suppression(Suppression.DO_NOT_CALL)
    assert not person.add_suppression(Suppression.DO_NOT_CALL)
    assert person.do_not_call
    assert person.remove_suppression(Suppression.DO_NOT_CALL)
    assert not person.remove_suppression(Suppression.DO_NOT_CALL)
    assert person.do_not_call is False
    assert person.set_suppression(Suppression.DO_NOT_CALL, True)
    assert not person.set_suppression(Suppression.DO_NOT_CALL, True)
    assert person.do_not_call
    assert person.set_suppression(Suppression.DO_NOT_CALL, False)
    assert not person.set_suppression(Suppression.DO_NOT_CALL, False)
    assert not person.do_not_call

    person.do_not_email = True
    assert person.do_not_email
    assert not person.do_not_call
    person.do_not_email = False
    assert not person.do_not_email

    person.do_not_mail = True
    assert person.do_not_mail
    person.do_not_mail = False
    assert not person.do_not_mail

    person.do_not_walk = True
    assert person.do_not_walk
    person.do_not_walk = False
    assert not person.do_not_walk

    # Test that we can construct a Person with do_not_call, do_not_email, and do_not_walk.
    person = Person(id=3, do_not_call=True, do_not_email=True, do_not_walk=False)
    assert person.do_not_call
    assert person.do_not_email
    assert person.do_not_walk is False


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


def test_changed_entities(client, server):
    bool_field = ChangedEntityField('bool', type='B')
    date_field = ChangedEntityField('date', type='D')
    money_field = ChangedEntityField('money', type='M')
    num_field = ChangedEntityField('num', type='N')
    text_field = ChangedEntityField('text', type='T')

    assert bool_field.parse('true')
    assert not bool_field.parse('FALSE')
    with pytest.raises(ValueError):
        bool_field.parse('fals')

    assert date_field.parse('2000-01-01') == datetime(2000, 1, 1)
    assert money_field.parse('$3.50') == '$3.50'
    assert num_field.parse('314') == 314
    assert text_field.parse('314') == '314'

    # Patch this so the test isn't needlessly long.
    ChangedEntities._WAIT_INTERVAL = 0.001
    change_types = [{'id': 1, 'name': 'ct1'}, {'id': 2, 'name': 'ct2'}]

    # Convert to dict since we are using default JSON serialization.
    change_fields = [dict(f) for f in [bool_field, date_field, money_field, num_field, text_field]]
    server.add_changed_entity_resource('TestResource', change_types, change_fields)
    with mock.patch('requests.get') as mock_get:
        changes_result = []

        def target(cache=None, expect_failure=False):
            try:
                changes_result.append(
                    client.changed_entities.changes(cache, changed_from='2000-01-01', resource='TestResource')
                )
            except Exception as e:
                if expect_failure:
                    changes_result.append(e)
                else:
                    changes_result.append(traceback.format_exc())

        next_job = 1

        def update_and_wait(data_to_update_with):
            nonlocal next_job

            # First, wait for client to request a new export job.
            # This may be done by waiting for the server to have export jobs up to job_id.
            deadline = time.time() + 5
            while len(server.changed_entity_export_jobs) < next_job and time.time() < deadline:
                time.sleep(0.001)

            if len(server.changed_entity_export_jobs) < next_job:
                raise AssertionError('Job not created in time.')

            # Now, update status of job so that changes can proceed.
            server.update_changed_entity_export_job(next_job, data_to_update_with)
            changes_thread.join(5)
            if changes_thread.is_alive():
                raise AssertionError('Changes thread did not stop in time.')

            next_job += 1

        # Have changed_entities.changes run in the background while we complete the job.
        changes_thread = Thread(target=target)
        changes_thread.start()

        result_data1 = textwrap.dedent('''\
        bool,date,money,num,text
        true,1818-05-05,$50.00,272,Hi everybody
        false,1928-12-07,$10.00,141,Hello Dr. Nick''')

        result_data2 = textwrap.dedent('''\
        bool,date,money,num,text
        false,1922-08-24,,173,milk steak
        true,1953-06-02,$111.11,693,little green ghouls''')

        files = [{
            'downloadUrl': 'fake://example.com/1',
            'dateExpired': '3000-12-31'
        }, {
            'downloadUrl': 'fake://example.com/2',
            'dateExpired': '2500-06-15'
        }]

        update_data = {
            'exportedRecordCount': 4,
            'files': files,
            'jobStatus': 'Complete',
            'message': 'Finished processing export job'
        }

        class MockResp:
            def __init__(self, text):
                self.text = text

        mock_get.side_effect = [MockResp(result_data1), MockResp(result_data2)]

        update_and_wait(update_data)
        if isinstance(changes_result[0], str):
            raise AssertionError(f'Unexpected exception: {changes_result[0]}')
        assert changes_result == [[
            {'bool': True, 'date': datetime(1818, 5, 5), 'money': '$50.00', 'num': 272, 'text': 'Hi everybody'},
            {'bool': False, 'date': datetime(1928, 12, 7), 'money': '$10.00', 'num': 141, 'text': 'Hello Dr. Nick'},
            {'bool': False, 'date': datetime(1922, 8, 24), 'money': None, 'num': 173, 'text': 'milk steak'},
            {'bool': True, 'date': datetime(1953, 6, 2), 'money': '$111.11', 'num': 693, 'text': 'little green ghouls'},
        ]]
        assert mock_get.call_args_list == [call('fake://example.com/1'), call('fake://example.com/2')]

        # Now try with field cache specified.
        # This field should not be found and thus should not be present in the results.
        ignored_field = ChangedEntityField('ignored', type='N')
        field_cache = [bool_field, num_field, ignored_field, text_field]

        changes_result.clear()
        changes_thread = Thread(target=target, args=(field_cache,))
        changes_thread.start()

        mock_get.reset_mock()
        mock_get.side_effect = [MockResp(result_data1), MockResp(result_data2)]
        update_and_wait(update_data)

        if isinstance(changes_result[0], str):
            raise AssertionError(f'Unexpected exception: {changes_result[0]}')

        assert changes_result == [[
            {'bool': True, 'num': 272, 'text': 'Hi everybody'},
            {'bool': False, 'num': 141, 'text': 'Hello Dr. Nick'},
            {'bool': False, 'num': 173, 'text': 'milk steak'},
            {'bool': True, 'num': 693, 'text': 'little green ghouls'},
        ]]

        # Same test, but with only 1 file.
        changes_result.clear()
        changes_thread = Thread(target=target)
        changes_thread.start()

        mock_get.reset_mock()
        mock_get.side_effect = None
        mock_get.return_value = MockResp(result_data1)
        del files[1]
        update_data['exportedRecordCount'] = 2

        update_and_wait(update_data)
        if isinstance(changes_result[0], str):
            raise AssertionError(f'Unexpected exception: {changes_result[0]}')

        assert changes_result == [[
            {'bool': True, 'date': datetime(1818, 5, 5), 'money': '$50.00', 'num': 272, 'text': 'Hi everybody'},
            {'bool': False, 'date': datetime(1928, 12, 7), 'money': '$10.00', 'num': 141, 'text': 'Hello Dr. Nick'}
        ]]
        assert mock_get.call_args_list == [call('fake://example.com/1')]

        # Now with error job status.
        changes_result.clear()
        mock_get.reset_mock()
        mock_get.side_effect = AssertionError('Get should not have been called.')
        changes_thread = Thread(target=target, kwargs={'expect_failure': True})
        changes_thread.start()
        update_and_wait({'jobStatus': 'Error'})

        assert len(changes_result) == 1
        assert isinstance(changes_result[0], EAChangedEntityJobFailedException)

        # Now with unknown job status.
        changes_result.clear()
        changes_thread = Thread(target=target, kwargs={'expect_failure': True})
        changes_thread.start()
        update_and_wait({'jobStatus': 'FakeStatus'})

        assert len(changes_result) == 1
        assert isinstance(changes_result[0], AssertionError)
        assert 'Unexpected job status: FakeStatus' in str(changes_result[0])


def test_finds(client, server):
    def test_find(find_fn, name_fn, add_fn, factory, obj_name):
        # Test that failing to find a record results in an EAFindFailedException.
        with pytest.raises(EAFindFailedException, match=f'No such {obj_name}'):
            find_fn('obj 1')

        # Add a record and try to find it.
        data1 = factory(**add_fn({'name': 'obj 1'}))
        assert find_fn('obj 1') == data1

        # Add another record. Try to find both.
        data2 = factory(**add_fn({'name': 'obj 2'}))
        assert find_fn('obj 1') == data1
        assert find_fn('obj 2') == data2
        with pytest.raises(EAFindFailedException, match=f'No such {obj_name}'):
            find_fn('obj 3')

        assert name_fn() == {
            'obj 1': data1,
            'obj 2': data2
        }

    change_types = []
    fields = []
    server.add_changed_entity_resource('TestResource', change_types, fields)

    next_ct_id = 1

    def add_change_type(data):
        nonlocal next_ct_id
        data['changeTypeID'] = next_ct_id
        next_ct_id += 1
        change_types.append(data)
        return data

    def add_field(data):
        fields.append(data)
        return data

    test_find(
        lambda name: client.changed_entities.find_change_type('TestResource', name),
        lambda: client.changed_entities.name_to_change_type('TestResource'),
        add_change_type,
        ChangeType,
        'change type'
    )
    test_find(
        lambda name: client.changed_entities.find_field('TestResource', name),
        lambda: client.changed_entities.name_to_field('TestResource'),
        add_field,
        ChangedEntityField,
        'field'
    )
    test_find(
        client.canvass_responses.find_contact_type,
        client.canvass_responses.name_to_contact_type,
        server.add_contact_type,
        ContactType,
        'contact type'
    )
    test_find(
        client.canvass_responses.find_input_type,
        client.canvass_responses.name_to_input_type,
        server.add_input_type,
        InputType,
        'input type'
    )
    test_find(
        client.canvass_responses.find_result_code,
        client.canvass_responses.name_to_result_code,
        server.add_result_code,
        ResultCode,
        'result code'
    )
    test_find(
        client.export_jobs.find_type,
        client.export_jobs.name_to_type,
        server.add_export_job_type,
        ExportJobType,
        'export job type'
    )


def test_suppressions() -> None:
    # Test that suppressions can be tested for whether or not they are "Do Not Call", "Do Not Email", or "Do Not Mail"
    do_not_call1 = Suppression('NC')
    do_not_call2 = Suppression('Do Not Call')
    do_not_email1 = Suppression('NE')
    do_not_email2 = Suppression('Do Not Email')
    do_not_mail1 = Suppression('NM')
    do_not_mail2 = Suppression('Do Not Mail')
    do_not_walk1 = Suppression('NW')
    do_not_walk2 = Suppression('Do Not Walk')

    assert do_not_call1.no_call
    assert do_not_call2.no_call
    assert Suppression.DO_NOT_CALL.no_call
    assert do_not_email1.no_email
    assert do_not_email2.no_email
    assert Suppression.DO_NOT_EMAIL.no_email
    assert do_not_mail1.no_mail
    assert do_not_mail2.no_mail
    assert Suppression.DO_NOT_MAIL.no_mail
    assert do_not_walk1.no_walk
    assert do_not_walk2.no_walk
    assert Suppression.DO_NOT_WALK.no_walk

    assert not do_not_call1.no_email
    assert not do_not_email2.no_mail
    assert not do_not_mail1.no_walk
    assert not do_not_walk2.no_call
