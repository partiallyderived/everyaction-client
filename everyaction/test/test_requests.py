import json as pyjson  # "json" conflicts with necessary keyword arguments.
from collections.abc import Sequence
from urllib.parse import parse_qs, urlparse

import pytest
from requests import HTTPError

import everyaction.core
from everyaction import EAException, EAHTTPException
from everyaction.core import ea_endpoint, EAObject, EAProperty, EAService
from everyaction.objects import Error


def structs_to_dicts(obj):
    # Convert EAObject objects to nested dicts for equality checking purposes.
    if isinstance(obj, EAObject):
        return {k: structs_to_dicts(v) for k, v in obj.items()}
    if isinstance(obj, Sequence) and not isinstance(obj, str):
        return [structs_to_dicts(x) for x in obj]
    return obj


class MockResponse:
    def __init__(self, data, code):
        self.data = data
        self.code = code

    def json(self):
        return self.data

    def raise_for_status(self):
        if not self:
            raise HTTPError(str(self.code))

    def __bool__(self):
        return self.code < 400


class MockEAClient:
    def __init__(self):
        self.req_type = None
        self.route = None
        self.query = None
        self.json = None
        self.paginated = False
        self.resp_json = {}
        self.default_limit = 0
        self.code = 200
        self.endpoint = 'http://example.com'

    def _received(self, req_type, route, query=None, data=None, json=None):
        if data and json:
            raise AssertionError(f'Only one of data={data} and json={json} should be specified.')

        if route.startswith(self.endpoint):
            route = route[len(self.endpoint):]
        self.req_type = req_type
        self.route = route
        self.query = query or {}
        self.json = pyjson.loads(data) if data else json if json else {}

        # Get any query args appearing in route and add to self.query.
        self.query.update({k: v[0] for k, v in parse_qs(urlparse(route).query).items()})

        if self.paginated:
            skip = int(self.query.get('$skip', 0))
            top = int(self.query.get('$top', everyaction.core._DEFAULT_MAX_TOP))
            count = len(self.resp_json)

            # Returned response json data will have at most top records, starting at skip.
            if skip + top >= count:
                # We're done paginating, send response with 0 count and None nextPageLink.
                page_json = {'items': self.resp_json[skip:], 'nextPageLink': None, 'count': 0}
            else:
                # New value for skip: skip top additional records.
                new_skip = skip + top

                # New value for top: the number of remaining records if less than top, otherwise keep same value.
                new_top = min(count - new_skip, top)
                page_json = {
                    'items': self.resp_json[skip:skip + top],
                    'nextPageLink': f'{self.endpoint}/{route}?$top={new_top}&$skip={new_skip}',
                    'count': count
                }
            response = MockResponse(page_json, self.code)
        else:
            response = MockResponse(self.resp_json, self.code)

        return response

    def delete(self, route, params=None, data=None, json=None, headers=None):
        return self._received('delete', route, params, data, json)

    def get(self, route, params=None, data=None, json=None, headers=None):
        return self._received('get', route, params, data, json)

    def patch(self, route, params=None, data=None, json=None, headers=None):
        return self._received('patch', route, params, data, json)

    def post(self, route, params=None, data=None, json=None, headers=None):
        return self._received('post', route, params, data, json)

    def put(self, route, params=None, data=None, json=None, headers=None):
        return self._received('put', route, params, data, json)


class Structure1(EAObject, a=EAProperty(), b=EAProperty(factory=int)):
    pass


class Structure2(EAObject, c=EAProperty(), d=EAProperty(factory=Structure1)):
    pass


class Structure3(
    EAObject,
    prop1=EAProperty('p1'),
    prop2=EAProperty('p2', factory=Structure1),
    array_prop1=EAProperty('ap1', singular_alias='single1', factory=int),
    array_prop2=EAProperty('ap2', singular_alias='single2', factory=Structure2)
):
    pass


@pytest.fixture
def client():
    return MockEAClient()


def test_request_type(client):
    class BasicGroup(EAService):
        @ea_endpoint('basic/route', 'delete')
        def delete(self, **kwargs):
            pass

        @ea_endpoint('basic/route', 'get')
        def get(self, **kwargs):
            pass

        @ea_endpoint('basic/route', 'patch')
        def patch(self, **kwargs):
            pass

        @ea_endpoint('basic/route', 'post')
        def post(self, **kwargs):
            pass

        @ea_endpoint('basic/route', 'put')
        def put(self, **kwargs):
            pass

    group = BasicGroup(client)

    group.delete()
    assert client.req_type == 'delete'
    assert client.route == 'basic/route'

    group.get()
    assert client.req_type == 'get'

    group.patch()
    assert client.req_type == 'patch'

    group.post()
    assert client.req_type == 'post'

    group.put()
    assert client.req_type == 'put'

    with pytest.raises(EAException, match='Name or alias "arg" not recognized by BasicGroup.get'):
        group.get(arg=0)

    with pytest.raises(AssertionError, match='Got "fake" as a request type, expected one of'):
        class FakeGroup(EAService):
            @ea_endpoint('fake/route', 'fake')
            def fake(self):
                pass


def test_path_params(client):
    class PathParamsGroup(EAService):
        @ea_endpoint('first/second/third', 'get')
        def zero(self, **kwargs):
            pass

        @ea_endpoint('{param}/second/third', 'get')
        def one(self, param, /):
            pass

        @ea_endpoint('{param1}/second/{param2}', 'get')
        def two(self, param1, param2, /):
            pass

    group = PathParamsGroup(client)

    group.one('first')
    assert client.route == 'first/second/third'

    group.two('first', 'third')
    assert client.route == 'first/second/third'


def test_query_args(client):
    EAProperty.share(common_query=EAProperty('common'))

    class QueryArgsGroup(EAService):
        @ea_endpoint(
            'who/cares',
            'get',
            query_arg_keys={'arg1', '$arg2', 'arg3', 'common_query'},
            props={'arg1': EAProperty('a1'), 'arg2': EAProperty('a2'), 'arg3': EAProperty('a3', factory=Structure2)}
        )
        def get(self, **kwargs):
            pass

        @ea_endpoint('i/care', 'get', query_arg_keys={'common_query'}, props={'common_query': EAProperty()})
        def common_in_props(self, **kwargs):
            pass

        @ea_endpoint('you/care', 'get', query_arg_keys={'$expand'})
        def expand(self, **kwargs):
            pass

    group = QueryArgsGroup(client)

    # Specifying query arguments is optional.
    group.get()
    assert client.query == {}

    # Simple query arg.
    group.get(arg1=3)
    assert client.query == {'arg1': '3'}
    assert client.json == {}

    # Now with alias.
    group.get(a1=3)
    assert client.query == {'arg1': '3'}

    # Query arg prefixed with $.
    group.get(a2='4')
    assert client.query == {'$arg2': '4'}

    # Structured query arg.
    # Important to use strings for properties we do not explicitly load via json.loads, as everything received by
    # the client should be a string.
    # Normally, the EveryAction server would do this step or something similar.
    struct = Structure2(c='1', d=Structure1(a=2, b='3'))
    group.get(arg3=struct)
    client.query['arg3'] = pyjson.loads(client.query['arg3'])
    assert client.query == {'arg3': structs_to_dicts(struct)}

    # Test common arg.
    group.get(common=4)
    assert client.query == {'common_query': '4'}

    # All together.
    group.get(a1=1, a2=2, a3=struct, common_query=3)
    client.query['arg3'] = pyjson.loads(client.query['arg3'])
    assert client.query == {
        'arg1': '1',
        '$arg2': '2',
        'arg3': structs_to_dicts(struct),
        'common_query': '3'
    }

    # Test that $expand may be specified via str or Iterable.
    group.expand(expand='a,b')
    assert client.query == {'$expand': 'a,b'}
    group.expand(expand=['a', 'b'])
    assert client.query == {'$expand': 'a,b'}

    # Make sure $expand cannot be some other type.
    with pytest.raises(TypeError, match='Expected str or Iterable for expand'):
        group.expand(expand=1)

    # Test that keys in props take precedence over common properties.
    group.common_in_props(common_query='3')
    assert client.query == {'common_query': '3'}

    # Make sure "common" alias doesn't work for this method.
    with pytest.raises(EAException, match='Name or alias "common" not recognized'):
        group.common_in_props(common='3')

    # Make sure common_json cannot appear in both prop_keys and query_arg_keys.
    with pytest.raises(AssertionError, match='At least one key specified in more than one of'):
        class PropAndQueryKeysGroup(EAService):
            @ea_endpoint('asdf/fdsa', 'get', query_arg_keys={'common_json'}, prop_keys={'common_json'})
            def get(self, **kwargs):
                pass

    # Test that query arg key must be a shared property when not in props.
    with pytest.raises(AssertionError, match='test_arg is not a shared property'):
        class TestArgGroup(EAService):
            @ea_endpoint('asdf/fdsa', 'get', query_arg_keys={'test_arg'})
            def get(self, **kwargs):
                pass


def test_json(client):
    EAProperty.share(common_json=EAProperty('common'))

    class JsonGroup(EAService):
        @ea_endpoint(
            'asdf/fdsa',
            'get',
            prop_keys={'common_json'},
            props={
                'arg1': EAProperty('a1'),
                'arg2': EAProperty('a2'),
                'arg3': EAProperty('a3', factory=Structure2)
            },
            data_type=Structure3
        )
        def get(self, **kwargs):
            pass

    group = JsonGroup(client)

    # JSON data is optional.
    group.get()
    assert client.json == {}

    # Simple use case.
    group.get(arg1=1)
    assert client.json == {'arg1': 1}
    assert client.query == {}

    # Try with alias.
    group.get(a2=2)
    assert client.json == {'arg2': 2}

    # Try with structured data.
    struct = Structure2(c=3, d=Structure1(a=1, b='2'))
    group.get(a3=struct)

    # Note of course that the json will have a dict, *not* a Structure2 instance.
    assert client.json == {'arg3': structs_to_dicts(struct)}

    # Try with common key.
    group.get(common=1)
    assert client.json == {'common_json': 1}

    complicated_struct = Structure3(
        prop1=1,
        prop2=Structure1(a=2, b=3),
        array_prop1=['4'],
        array_prop2=[Structure2(c=5, d=Structure1(a=6, b=7)), Structure2(c=8, d=Structure1(a=9, b=10))]
    )

    # Try with properties from Structure3. Mix dicts with EAObjects.
    group.get(prop1=1, p2=Structure1(a=2, b=3), single1='4', ap2=[
        Structure2(c=5, d={'a': 6, 'b': 7}),
        {
            'c': 8,
            'd': Structure1(a=9, b=10)
        }
    ])
    assert client.json == structs_to_dicts(complicated_struct)

    # All together.
    group.get(a1=1, a2=2, a3=struct, common_json=4, **complicated_struct)
    assert client.json == {
        'arg1': 1,
        'arg2': 2,
        'arg3': {'c': 3, 'd': {'a': 1, 'b': 2}},
        'common_json': 4,
        **structs_to_dicts(complicated_struct)
    }

    # Test that prop_keys and props may not have the duplicate keys.
    with pytest.raises(AssertionError, match='At least one key specified in both'):
        class PropKeysPropsDupGroup(EAService):
            @ea_endpoint('prop/keys', 'get', prop_keys={'common_json'}, props={'common_json': EAProperty()})
            def get(self, **kwargs):
                pass


def test_path_params_to_data(client):
    class ParamsToDataGroup(EAService):
        @ea_endpoint(
            'first/{param}/third',
            'get',
            path_params_to_data={'param'},
            props={'param': EAProperty('p'), 'other': EAProperty()}
        )
        def one(self, param, /, **kwargs):
            pass

        @ea_endpoint(
            '{param1}/{param2}/third',
            'get',
            path_params_to_data={'param1', 'param2'},
            props={'param1': EAProperty('p1'), 'param2': EAProperty('p2'), 'other': EAProperty()}
        )
        def two(self, param1, param2, /, **kwargs):
            pass

        @ea_endpoint(
            '{param1}/{param2}/third',
            'get',
            path_params_to_data={'param2'},
            props={'param2': EAProperty('p2'), 'other': EAProperty()}
        )
        def mixed(self, param1, param2, /, **kwargs):
            pass

    group = ParamsToDataGroup(client)

    # Test that the path param appears in JSON data along with other data.
    group.one('value', other='thing')
    assert client.route == 'first/value/third'
    assert client.json == {'param': 'value', 'other': 'thing'}

    # Test that specifying a value using keyword alias is OK.
    group.one(1, p=2, other=3)
    assert client.route == 'first/1/third'
    assert client.json == {'param': 2, 'other': 3}

    # Try with two params to be copied to data.
    group.two(1, 2, other=3)
    assert client.route == '1/2/third'
    assert client.json == {'param1': 1, 'param2': 2, 'other': 3}

    # Try with one of the two params specified via keyword alias.
    group.two(1, 2, p2=3, other=4)
    assert client.route == '1/2/third'
    assert client.json == {'param1': 1, 'param2': 3, 'other': 4}

    # Test that only parameters appearing in path_params_to_data are copied.
    group.mixed(1, 2, other=3)
    assert client.json == {'param2': 2, 'other': 3}

    # Test that keys in path_params_to_data must actually correspond to path parameters.
    with pytest.raises(AssertionError, match='contains keys not in path_params'):
        class MissingParamToData(EAService):
            @ea_endpoint('missing/param', 'get', path_params_to_data={'param'})
            def missing(self, **kwargs):
                pass

    # Test that keys in path_params_to_data must be a recognized property.
    with pytest.raises(AssertionError, match='fake_param is not a shared property'):
        class NonPropParamToData(EAService):
            @ea_endpoint('{fake_param}/route', 'get', path_params_to_data={'fake_param'})
            def fake(self, **kwargs):
                pass


def test_response_data(client):
    class ResponseDataGroup(EAService):
        @ea_endpoint('response/no-result', 'get', has_result=False)
        def no_result(self, **kwargs):
            pass

        @ea_endpoint('response/no-factory', 'get')
        def no_factory(self, **kwargs):
            pass

        @ea_endpoint('response/with-factory', 'get', result_factory=Structure2)
        def with_factory(self, **kwargs):
            pass

        @ea_endpoint('response/result-key', 'get', result_key='a')
        def result_key(self, **kwargs):
            pass

        @ea_endpoint('response/result-array', 'get', result_array=True, result_factory=int)
        def result_array(self, **kwargs):
            pass

        @ea_endpoint('response/result-array-key', 'get', result_array_key='objects', result_factory=Structure2)
        def result_array_key(self, **kwargs):
            pass

        @ea_endpoint('response/result-array-and-key', 'get', result_array=True, result_key='a')
        def result_array_and_key(self, **kwargs):
            pass

    group = ResponseDataGroup(client)

    assert group.no_result() is None

    # Test that methods with/without factory will produce different results, depending on whether or not the raw
    # dict data is converted into an EAObject.
    data = {'c': 3, 'd': {'a': 1, 'b': '2'}}
    client.resp_json = data
    assert group.no_factory() == data
    assert group.with_factory() != data
    assert group.with_factory() == Structure2(**data)

    # Test that result_key and result_keys correctly extract values from specified keys.
    data = {'a': 1, 'b': 2}
    client.resp_json = data
    assert group.result_key() == 1

    # Test that a given factory is applied to all response data items in an array.
    data = ['1', '2', '3', '4']
    client.resp_json = data
    assert group.result_array() == [1, 2, 3, 4]

    # Similar test, but the array of items is behind a key in a mapping.
    data = {'objects': [{'c': 3, 'd': {'a': 1, 'b': '2'}}, {'c': 4, 'd': {'a': 5, 'b': '6'}}]}
    client.resp_json = data
    assert group.result_array_key() == [Structure2(**data['objects'][0]), Structure2(**data['objects'][1])]

    # Test that we can extract an array of simple values by combining result_array and result_key.
    data = [{'a': 1}, {'a': 2}, {'a': 3}]
    client.resp_json = data
    assert group.result_array_and_key() == [1, 2, 3]

    # Test that has_result=False is incompatible with keys that process the result.
    for param, value in [
        ('result_array', True),
        ('result_array_key', 'key'),
        ('result_key', 'key'),
        ('result_factory', Structure1),
    ]:
        with pytest.raises(AssertionError, match='has_result should be True when any of'):
            keyword_args = {param: value}

            class HasResultFalseGroup(EAService):
                @ea_endpoint('result/false', 'get', has_result=False, **keyword_args)
                def get(self, **kwargs):
                    pass

    # Test that result_array and result_array_key may not both be specified.
    with pytest.raises(AssertionError, match='At most one of'):
        class ResultArrayAndResultArrayKey(EAService):
            @ea_endpoint('fake/route', 'get', result_array=True, result_array_key='key')
            def get(self, **kwargs):
                pass

    # Test that a key found in data_type may not be specified in props.
    with pytest.raises(AssertionError, match='has at least one property in'):
        class DataAndPropsGroup(EAService):
            @ea_endpoint('data/props', 'get', data_type=Structure1, props={'a': EAProperty()})
            def get(self, **kwargs):
                pass


def test_pagination(client):
    class PaginationGroup(EAService):
        @ea_endpoint('paginated/request', 'get', paginated=True, max_top=3, result_factory=Structure1)
        def paginated(self, **kwargs):
            pass

        @ea_endpoint('not/paginated', 'get')
        def not_paginated(self, **kwargs):
            pass

    group = PaginationGroup(client)
    client.paginated = True

    # Count (number of records) = 1, top = 3, limit = 5: Should return a single record.
    data = [{'a': 1, 'b': '2'}]
    client.resp_json = data
    assert group.paginated(limit=5) == [Structure1(**data[0])]

    # Count = 2, top = 3, limit = 5: Should return both records.
    data.append({'a': 3, 'b': '4'})
    assert group.paginated(limit=5) == [Structure1(**data[0]), Structure1(**data[1])]

    # Count = 3, top = 3, limit = 1: Should return 1 record.
    data.append({'a': 5, 'b': '6'})
    assert group.paginated(limit=1) == [Structure1(**data[0])]

    # Try with skip = 2 to check third record is returned instead.
    assert group.paginated(limit=1, skip=2) == [Structure1(**data[2])]

    # Try with limit=2, skip=1 and check for last two records.
    assert group.paginated(limit=2, skip=1) == [Structure1(**data[1]), Structure1(**data[2])]

    # Count = 4, top = 3, limit = 5: Should return all records.
    data.append({'a': 7, 'b': '8'})
    assert group.paginated(limit=5) == (
        [Structure1(**data[0]), Structure1(**data[1]), Structure1(**data[2]), Structure1(**data[3])]
    )

    # Count = 5, top = 3, limit = 4: Should return 4 records.
    data.append({'a': 9, 'b': '10'})
    assert group.paginated(limit=4) == [
        Structure1(**data[0]), Structure1(**data[1]), Structure1(**data[2]), Structure1(**data[3])
    ]

    # Set default_limit to 2 and verify that first two records are returned when limit not specified.
    client.default_limit = 2
    assert group.paginated() == [Structure1(**data[0]), Structure1(**data[1])]

    # Use limit = 0 to verify that all records are returned.
    assert group.paginated(limit=0) == [
        Structure1(**data[0]),
        Structure1(**data[1]),
        Structure1(**data[2]),
        Structure1(**data[3]),
        Structure1(**data[4])
    ]

    # Test that paginated and result_array cannot simultaneously be specified.
    with pytest.raises(AssertionError, match='At most one of'):
        class PaginatedAndArray(EAService):
            @ea_endpoint('page/array', 'get', paginated=True, result_array=True)
            def get(self, **kwargs):
                pass

    # Test that top may not be specified for this library.
    with pytest.raises(EAException, match=r'\$top is not supported'):
        group.paginated(top=50)

    # Test that pagination arguments may not be specified for non-paginated requests.
    with pytest.raises(EAException, match='top=5 given for PaginationGroup.not_paginated, which is not paginated'):
        group.not_paginated(top=5)
    with pytest.raises(EAException, match='skip=5 given for PaginationGroup.not_paginated, which is not paginated'):
        group.not_paginated(skip=5)
    with pytest.raises(
        EAException, match='limit=5 given for PaginationGroup.not_paginated, which is not paginated'
    ):
        group.not_paginated(limit=5)


def test_error_response(client):
    class ErrorGroup(EAService):
        @ea_endpoint('error/route', 'get')
        def get(self, **kwargs):
            pass

    group = ErrorGroup(client)

    # Test with one error first, since exception message is different between 1 and multiple errors.
    errors = [Error(text='I AM ERROR')]
    client.code = 400
    client.resp_json = {'errors': errors}
    with pytest.raises(EAHTTPException, match='Reason: I AM ERROR') as exc_info:
        group.get()

    exc = exc_info.value
    assert exc.errors == errors
    assert isinstance(exc.http_error, HTTPError)
    assert exc.response.json() == {'errors': errors}

    # Now try with multiple errors.
    errors.append(Error(text='Another error'))
    with pytest.raises(EAHTTPException, match='Reasons:\n\\* I AM ERROR\n\\* Another error') as exc_info:
        group.get()

    exc = exc_info.value
    assert exc.errors == errors
    assert exc.response.json() == {'errors': errors}
