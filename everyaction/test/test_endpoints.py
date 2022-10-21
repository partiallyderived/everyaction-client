import json
import os.path

from makefun import wraps

import pytest

import everyaction.core
from everyaction import EAClient, EAHTTPException

DATA_FILE = 'test_data.json'
pytestmark = pytest.mark.skipif(
    not all(x in os.environ for x in [EAClient._APP_NAME_ENV, EAClient._API_KEY_ENV]),
    reason=f'Need environment variables {EAClient._APP_NAME_ENV} and {EAClient._API_KEY_ENV}'
)


def _check_get_list(resource_name, service=None, get_method=None, list_method=None, list_args=None):
    list_args = list_args or {}
    # This method checks that we can list records for a resource and then "get" the first element in the listed
    # records without error.

    # Service can be specified to infer get/list methods, otherwise they should be explicitly given.
    get_method = get_method or getattr(service, 'get')
    list_method = list_method or getattr(service, 'list')
    record = _skip_if_empty_else_first(resource_name, list_method(**list_args))
    get_method(record.id)


def _skip_if_absent(key, data):
    value = data.get(key)
    if value is None:
        pytest.skip(f'{key} must be specified in {DATA_FILE} to test this.')
    return value


def _skip_if_empty_else_first(resource_name, records):
    if not records:
        pytest.skip(f'No {resource_name} found.')
    return records[0]


@pytest.fixture(autouse=True)
def setup():
    everyaction.core._fail_on_unrecognized = True
    try:
        yield
    finally:
        everyaction.core._fail_on_unrecognized = False


def skip_if_403(func):
    @wraps(func)
    def wrapper(**kwargs):
        try:
            func(**kwargs)
        except EAHTTPException as e:
            if e.response.status_code == 403:
                # If we got a 403 error, we did not fail to find the endpoint, but could not verify that we could parse
                # the response data into the expected structures.
                pytest.skip('API key not authorized for this action (got 403)')
            raise
    return wrapper


@pytest.fixture(scope='module')
def client():
    client = EAClient()
    # Only need one result for paginated methods.
    client.default_limit = 1
    yield client
    client.close()


@pytest.fixture(scope='module')
def data():
    # Some tests need data from EveryAction in order to proceed (usually because they need an ID to pass to a get method
    # when a listing version of that method is lacking).
    with open(DATA_FILE) as f:
        return json.load(f)


@pytest.fixture
def bulk_import_job(data):
    return _skip_if_absent('bulk_import_job', data)


@pytest.fixture
def canvass_file_request(data):
    return _skip_if_absent('canvass_file_request', data)


@pytest.fixture
def changed_entity_export_job(data):
    return _skip_if_absent('changed_entity_export_job', data)


@pytest.fixture
def contribution(data):
    return _skip_if_absent('contribution', data)


@pytest.fixture
def disbursement(data):
    return _skip_if_absent('disbursement', data)


@pytest.fixture
def event(data):
    return _skip_if_absent('event', data)


@pytest.fixture
def export_job(data):
    return _skip_if_absent('export_job', data)


@pytest.fixture
def file_loading_job(data):
    return _skip_if_absent('file_loading_job', data)


@pytest.fixture(scope='module')
def person(client, data):
    van_id = _skip_if_absent('person', data)
    return client.people.get(van_id, expand='emails')


@pytest.fixture
def state(data):
    return _skip_if_absent('state', data)


@pytest.fixture
def story(data):
    return _skip_if_absent('story', data)


@pytest.fixture
def user(data):
    return _skip_if_absent('user', data)


# The purposes of these tests are the following:
# 1. Verify that various read-only endpoints exist. For list endpoints, this is verified simply by calling the
#    endpoint. For get endpoints that get a particular resource, this is verified by invoking the get endpoint
#    with the data for a single object returned by the list endpoint. When no list endpoint is available, DATA_FILE
#    is searched for a particular key to run the test with. Otherwise, the test is skipped.
# 2. Verify that we can parse the response data from the various endpoints into the expected structures without
#    error.
# Endpoints that can modify EA data, such as People.find_or_create, are not tested in order to ensure that these
# tests do not modify data in the given EA database.


@skip_if_403
def test_api_key_profile(client):
    client.api_key_profile()


@skip_if_403
def test_activist_codes(client):
    _check_get_list('activist codes', client.activist_codes)


@skip_if_403
def test_ballot_request_types(client):
    request_type_id, request_type_name = _skip_if_empty_else_first(
        'ballot request types',
        client.ballots.request_types()
    )
    assert client.ballots.request_type(request_type_id) == request_type_name


@skip_if_403
def test_ballot_return_statuses(client):
    return_status_id, return_status_name = _skip_if_empty_else_first(
        'ballot return statuses',
        client.ballots.return_statuses()
    )
    assert client.ballots.request_type(return_status_id) == return_status_name


@skip_if_403
def test_ballot_types(client):
    ballot_type_id, ballot_type_name = _skip_if_empty_else_first('ballot types', client.ballots.types())
    assert client.ballots.request_type(ballot_type_id) == ballot_type_name


@skip_if_403
def test_bargaining_units(client):
    _check_get_list('bargaining units', client.bargaining_units)


@skip_if_403
def test_bulk_import(client, bulk_import_job):
    client.bulk_import.get(bulk_import_job)


@skip_if_403
def test_bulk_mapping_types(client):
    mapping_type = _skip_if_empty_else_first('bulk import mapping types', client.bulk_import.mapping_types())
    assert client.bulk_import.mapping_type(mapping_type.name).name == mapping_type.name


@skip_if_403
def test_bulk_resources(client):
    _skip_if_empty_else_first('bulk import resources', client.bulk_import.resources())


@skip_if_403
def test_campaigns(client):
    _skip_if_empty_else_first('campaigns', client.campaigns.list())


@skip_if_403
def test_canvass_file_requests(client, canvass_file_request):
    client.canvass_file_requests.get(canvass_file_request)


@skip_if_403
def test_canvass_response_contact_types(client):
    _skip_if_empty_else_first('canvass response contact types', client.canvass_responses.contact_types())


@skip_if_403
def test_canvass_response_input_types(client):
    _skip_if_empty_else_first('canvass response input types', client.canvass_responses.input_types())


@skip_if_403
def test_canvass_response_result_codes(client):
    _skip_if_empty_else_first('canvass response result codes', client.canvass_responses.result_codes())


@skip_if_403
def test_changed_entities(client, changed_entity_export_job):
    client.changed_entities.job(changed_entity_export_job)


@skip_if_403
def test_changed_entity_change_types(client):
    resources = client.changed_entities.resources()
    if resources:
        _skip_if_empty_else_first('changed entity change types', client.changed_entities.change_types(resources[0]))
    else:
        pytest.skip('No changed entity resource found to search change types for.')


@skip_if_403
def test_changed_entity_fields(client):
    resources = client.changed_entities.resources()
    if resources:
        _skip_if_empty_else_first('changed entity fields', client.changed_entities.fields(resources[0]))
    else:
        pytest.skip('No changed entity resource found to search for fields for.')


@skip_if_403
def test_changed_entity_resources(client):
    _skip_if_empty_else_first('changed entity resource', client.changed_entities.resources())


@skip_if_403
def test_codes(client):
    _check_get_list('codes', client.codes)


@skip_if_403
def test_code_supported_entities(client):
    _skip_if_empty_else_first('code supported entities', client.codes.supported_entities())


@skip_if_403
def test_code_types(client):
    _skip_if_empty_else_first('code types', client.codes.types())


@skip_if_403
def test_contributions(client, contribution):
    contribution_object = client.contributions.get(contribution)
    assert contribution_object.id == contribution
    assert client.contributions.get_('onlineReferenceNumber', contribution_object.reference_number).id == contribution


@skip_if_403
def test_contribution_attribution_types(client):
    _skip_if_empty_else_first('contribution attribution types', client.contributions.attribution_types())


@skip_if_403
def test_custom_fields(client):
    _check_get_list('custom fields', client.custom_fields)


@skip_if_403
def test_demographics_ethnicities(client):
    _skip_if_empty_else_first('reported ethnicities', client.demographics.ethnicities())


@skip_if_403
def test_demographics_gender(client):
    _skip_if_empty_else_first('reported genders', client.demographics.genders())


@skip_if_403
def test_demographics_language_preferences(client):
    _skip_if_empty_else_first('reported language preferences', client.demographics.language_preferences())


@skip_if_403
def test_demographics_pronouns(client):
    _skip_if_empty_else_first('reported pronouns', client.demographics.pronouns())


@skip_if_403
def test_demographics_races(client):
    _skip_if_empty_else_first('reported races', client.demographics.races())


@skip_if_403
def test_demographics_sexual_orientations(client):
    _skip_if_empty_else_first('sexual orientations', client.demographics.sexual_orientations())


@skip_if_403
def test_departments(client):
    _check_get_list('departments', client.departments)


@skip_if_403
def test_designations(client):
    _check_get_list('designations', client.designations)


@skip_if_403
def test_disbursement(client, disbursement):
    assert client.disbursements.get(disbursement).id == disbursement


@skip_if_403
def test_district_fields(client):
    _check_get_list('district fields', client.district_fields)


@skip_if_403
def test_email_messages(client):
    _check_get_list('email messages', client.email)


@skip_if_403
def test_employers(client):
    _check_get_list('employers', client.employers)


@skip_if_403
def test_event_types(client):
    _check_get_list('event types', client.event_types)


@skip_if_403
def test_events(client):
    _check_get_list('events', client.events)


@skip_if_403
def test_export_jobs(client, export_job):
    assert client.export_jobs.get(export_job).id == export_job


@skip_if_403
def test_export_job_types(client):
    _skip_if_empty_else_first('export job types', client.export_jobs.types())


@skip_if_403
def test_extended_source_codes(client):
    _skip_if_empty_else_first('extended source codes', client.extended_source_codes.list())


@skip_if_403
def test_file_loading_jobs(client, file_loading_job):
    assert client.file_loading_jobs.get(file_loading_job).id == file_loading_job


@skip_if_403
def test_financial_batches(client):
    _check_get_list('financial batches', client.financial_batches)


@skip_if_403
def test_folders(client):
    _check_get_list('folders', client.folders)


@skip_if_403
def test_job_classes(client):
    _check_get_list('job classes', client.job_classes)


@skip_if_403
def test_locations(client):
    _check_get_list('locations', client.locations)


@skip_if_403
def test_member_statuses(client):
    _check_get_list('member statuses', client.member_statuses)


@skip_if_403
def test_minivan_exports(client):
    _check_get_list('MiniVAN exports', client.minivan_exports)


@skip_if_403
def test_note_categories(client):
    _check_get_list('note categories', get_method=client.notes.category, list_method=client.notes.categories)


@skip_if_403
def test_note_category_types(client):
    _skip_if_empty_else_first('note category types', client.notes.category_types())


@skip_if_403
def test_online_action_forms(client):
    _check_get_list('online action forms', client.forms)


@skip_if_403
def test_people(client, person):
    _check_get_list('people', client.people, list_args={'email': person.emails[0].email})


@skip_if_403
def test_person_activist_codes(client, person):
    _skip_if_empty_else_first('activist codes for given person', client.people.activist_codes(person.id))


@skip_if_403
def test_person_get(client, person):
    assert client.people.get(person.id).id == person.id
    assert client.people.get_('VANID', person.id).id == person.id


@skip_if_403
def test_person_find(client, person):
    if person.emails:
        email = person.emails[0]['email']
        result = client.people.find(email=email)
        assert result is not None
        assert result.id == person.id
    else:
        pytest.skip('Person record must have an email address to test person find.')


@skip_if_403
def test_person_membership(client, person):
    try:
        client.people.membership(person.id)
    except EAHTTPException as e:
        if e.response.status_code == 500:
            pytest.skip('Server error when accessing person membership')
        raise


@skip_if_403
def test_person_notes(client, person):
    _skip_if_empty_else_first('notes for given person', client.people.notes(person.id))
    client.people.notes(person.id)


@skip_if_403
def test_phone_is_cell_statuses(client):
    _skip_if_empty_else_first('is cell statuses', client.phones.is_cell_statuses())


@skip_if_403
def test_printed_lists(client):
    _check_get_list('printed lists', client.printed_lists)


@skip_if_403
def test_registration_batches(client):
    _skip_if_empty_else_first('voter registration batches', client.registration_batches.list())


@skip_if_403
def test_registration_batch_forms(client):
    _skip_if_empty_else_first('voter registration forms', client.registration_batches.forms())


@skip_if_403
def test_registration_batch_programs(client):
    _skip_if_empty_else_first('voter registration programs', client.registration_batches.programs())


@skip_if_403
def test_registration_batch_support_fields(client, state):
    pytest.skip('This endpoint currently always results in 404.')
    _skip_if_empty_else_first(
        f'registration batch support fields for state {state}',
        client.registration_batches.support_fields(state)
    )


@skip_if_403
def test_relationships(client):
    _skip_if_empty_else_first('relationships', client.relationships.list())


@skip_if_403
def test_saved_lists(client):
    _check_get_list('saved lists', client.saved_lists)


@skip_if_403
def test_schedule_types(client):
    _check_get_list('schedule types', client.schedule_types)


@skip_if_403
def test_score_updates(client):
    _check_get_list('score updates', client.score_updates)


@skip_if_403
def test_scores(client):
    _check_get_list('scores', client.scores)


@skip_if_403
def test_shift_types(client):
    _check_get_list('shift types', client.shift_types)


@skip_if_403
def test_signups(client, person):
    _check_get_list('signups', client.signups, list_args={'van': person.id})


@skip_if_403
def test_signup_statuses(client, event):
    _skip_if_empty_else_first('signup statuses', client.signups.statuses(event=event))


@skip_if_403
def test_stories(client, story):
    assert client.stories.get(story).id == story


@skip_if_403
def test_supporter_groups(client):
    _check_get_list('supporter groups', client.supporter_groups)


@skip_if_403
def test_survey_questions(client):
    _check_get_list('survey questions', client.questions, list_args={'statuses': 'Active'})


@skip_if_403
def test_targets(client):
    _check_get_list('targets', client.targets)


@skip_if_403
def test_user_district_fields(client, user):
    client.users.district_fields(user)


@skip_if_403
def test_worksites(client):
    _check_get_list('worksites', client.worksites)
