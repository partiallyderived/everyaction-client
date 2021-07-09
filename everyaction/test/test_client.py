import os
import unittest.mock as mock

import pytest

from everyaction import EAClient, EAException


@pytest.fixture(autouse=True)
def mock_session():
    # Just in case these were already set in the environment, delete them for a test and then add them back so as
    # not to interfere.
    app_name = os.environ.pop('EVERYACTION_APP_NAME', None)
    api_key = os.environ.pop('EVERYACTION_API_KEY', None)
    with mock.patch('everyaction.client.Session') as session:
        yield session
    if app_name is not None:
        os.environ['EVERYACTION_APP_NAME'] = app_name
    if api_key is not None:
        os.environ['EVERYACTION_API_KEY'] = api_key


def test_init():
    # Test implicit from_env, asserting that exceptions are raised if the app/key env vars are not both specified.
    with pytest.raises(EAException, match='Environment variable EVERYACTION_APP_NAME is missing or empty.'):
        EAClient()

    os.environ['EVERYACTION_APP_NAME'] = 'my_app'
    with pytest.raises(EAException, match='Environment variable EVERYACTION_API_KEY is missing or empty.'):
        EAClient()

    del os.environ['EVERYACTION_APP_NAME']
    os.environ['EVERYACTION_API_KEY'] = 'key'
    with pytest.raises(EAException, match='Environment variable EVERYACTION_APP_NAME is missing or empty.'):
        EAClient()

    os.environ['EVERYACTION_APP_NAME'] = 'my_app'
    with pytest.raises(EAException, match='mode must either be specified or be implicit'):
        # Mode not implicit in api key (since it doesn't end with |0 or |1) so this should still raise an exception.
        EAClient()

    client = EAClient(mode=0)
    assert client.app_name == 'my_app'
    assert client._session.auth[1] == 'key|0'

    # Check default endpoint is US endpoint.
    assert client.endpoint == 'https://api.securevan.com/v4'

    # Check mode is VoterFile (0).
    assert client.mode == 'VoterFile'

    # Check that we can give the mode name instead of 0.
    client = EAClient(mode='VoterFile')

    # Check that API key correctly created in this case.
    assert client._session.auth[1] == 'key|0'

    # Same checks for MyCampaign (1).
    client = EAClient(mode=1)
    assert client._session.auth[1] == 'key|1'
    assert client.mode == 'MyCampaign'

    # Check case insensitivity.
    client = EAClient(mode='mycampaign')
    assert client._session.auth[1] == 'key|1'

    with pytest.raises(EAException, match=r'Mode number \(2\) is too high \(expected at most 1\)'):
        # Mode number too high.
        EAClient(mode=2)

    with pytest.raises(EAException, match=r'Mode number \(-1\) is negative'):
        # Mode number negative.
        EAClient(mode=-1)

    with pytest.raises(EAException, match='Unrecognized mode "SomethingElse"'):
        # Unrecognized mode.
        EAClient(mode='SomethingElse')

    with pytest.raises(
        EAException,
        match='Neither of app_name=SomeApp or api_key should be specified when from_env is True'
    ):
        EAClient('SomeApp', from_env=True)

    with pytest.raises(
        EAException,
        match='Neither of app_name=None or api_key should be specified when from_env is True'
    ):
        EAClient(api_key='key', from_env=True)

    with pytest.raises(
        EAException,
        match='Neither of app_name=SomeApp or api_key should be specified when from_env is True'
    ):
        EAClient('SomeApp', 'key', from_env=True)

    # Make sure explicitly setting from_env=True is allowed.
    EAClient(mode=1, from_env=True)

    # Clean environment before testing non-env constructions.
    del os.environ['EVERYACTION_APP_NAME']
    del os.environ['EVERYACTION_API_KEY']

    with pytest.raises(EAException, match='api_key must be given'):
        # Need API key.
        EAClient('my_app')

    with pytest.raises(EAException, match='app_name must be given'):
        # Need app name.
        EAClient(api_key='key|0')

    with pytest.raises(EAException, match='mode must either be specified or be implicit'):
        # Need mode.
        EAClient('my_app', 'key')

    # Explicitly specifying from_env=False is OK.
    EAClient('my_app', 'key|0', from_env=False)

    # Constructor fine, mode implicit in API key.
    client = EAClient('my_app', 'key|0')
    assert client.app_name == 'my_app'
    assert client._session.auth[1] == 'key|0'

    with pytest.raises(EAException, match='mode specified but mode already indicated in API key'):
        # Can't specify mode when it is implicit in API key.
        EAClient('my_app', 'key|0', mode=0)

    client = EAClient('my_app', 'key', mode='MyCampaign')
    assert client._session.auth[1] == 'key|1'

    # Make sure a literal endpoint can be given, even if it is not the US or INTL endpoint.
    client = EAClient('my_app', 'key|0', endpoint='http://example.com')
    assert client.mode == 'VoterFile'
    assert client.endpoint == 'http://example.com'

    with pytest.raises(EAException, match='Unrecognized endpoint alias example.com'):
        # Endpoint must start with http to be given literally.
        EAClient('my_app', 'key|0', endpoint='example.com')

    # Test US alias.
    client = EAClient('my_app', 'key|0', endpoint='US')
    assert client.endpoint == 'https://api.securevan.com/v4'

    # Check case insensitivity.
    client = EAClient('my_app', 'key|0', endpoint='uS')
    assert client.endpoint == 'https://api.securevan.com/v4'

    # Test INTL alias.
    client = EAClient('my_app', 'key|0', endpoint='INTL')
    assert client.endpoint == 'https://intlapi.securevan.com/v4'

    with pytest.raises(EAException, match=r'Mode number \(3\) is too high \(expected at most 1\)'):
        # Mode implicit in API key must still be valid
        EAClient('my_app', 'key|3')


def test_instance():
    client = EAClient('my_app', 'key|0')

    # Test default_limit getter/setter
    client.default_limit = 200
    assert client.default_limit == 200

    client.default_limit = 0
    assert client.default_limit == 0

    with pytest.raises(ValueError, match='default_limit must be at least 0, not -1'):
        client.default_limit = -1

    # Test that repr is what is expected. Note that api_key is intentionally absent.
    assert (
        str(client) ==
        'EAClient(app_name=my_app, endpoint=https://api.securevan.com/v4, mode=VoterFile, default_limit=0)'
    )


def test_requests(mock_session):
    # Test that arguments are passed to a requests Session object as expected.
    # Nothing complicated to test here, just ensure that arguments are passed and that route is prepended with the
    # correct endpoint.
    client = EAClient('my_app', 'key|0')

    client.delete('some/route', json={'my': 'data'})
    client.get('some/route', json={'my': 'data'})
    client.patch('some/route', json={'my': 'data'})
    client.post('some/route', json={'my': 'data'})
    client.put('some/route', json={'my': 'data'})

    mock_session().delete.assert_called_with('https://api.securevan.com/v4/some/route', json={'my': 'data'})
    mock_session().get.assert_called_with('https://api.securevan.com/v4/some/route', json={'my': 'data'})
    mock_session().patch.assert_called_with('https://api.securevan.com/v4/some/route', json={'my': 'data'})
    mock_session().post.assert_called_with('https://api.securevan.com/v4/some/route', json={'my': 'data'})
    mock_session().put.assert_called_with('https://api.securevan.com/v4/some/route', json={'my': 'data'})
