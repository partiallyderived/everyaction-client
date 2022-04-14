"""
This module contains :class:`EAClient`, the entrypoint for users to make requests following the
`EveryAction 8 VAN API <https://docs.everyaction.com/reference>`__.
"""

import os
from typing import Any, Dict, List, Optional, Union

from requests import Response, Session

from everyaction.core import ea_endpoint, EAService
from everyaction.exception import EAException
from everyaction.objects import APIKeyProfile
from everyaction.services import *


class EAClient(EAService):
    # Environment variable for EveryAction API key when from_env is True.
    _API_KEY_ENV: str = 'EVERYACTION_API_KEY'

    # Environment variable for EveryAction app name when from_env is True.
    _APP_NAME_ENV: str = 'EVERYACTION_APP_NAME'

    # The default value to use as the default value for the limit.
    _DEFAULT_DEFAULT_LIMIT: str = 50

    # Endpoint for most non-US clients.
    _INTL_ENDPOINT: str = 'https://intlapi.securevan.com/v4'

    # Everyaction database modes. The index of the mode is the number to be appended to the API key.
    _MODES: List[str] = [
        'VoterFile',
        'MyCampaign'
    ]

    # Mapping from short endpoint names to their corresponding endpoints.
    # Initialized by EAClient._resolve_endpoint(short_name).
    _SHORT_NAME_TO_ENDPOINT: Dict[str, str] = {}

    # Endpoint for most US-based clients.
    _US_ENDPOINT: str = 'https://api.securevan.com/v4'

    #: Application name for this client.
    app_name: str

    #: Default limit on the number of records a request may get for a paginated response. Set to 0 for no limit.
    default_limit: int

    #: Endpoint to send EveryAction requests to.
    endpoint: str

    #: Database mode used by the client (VoterFile or MyCampaign).
    mode: str

    #: `People <https://docs.everyaction.com/reference/people>`__ service.
    people: People

    #: `Activist Codes <https://docs.everyaction.com/reference/activist-codes>`__ service.
    activist_codes: ActivistCodes

    #: `Ballots <https://docs.everyaction.com/reference/ballots>`__ service.
    ballots: Ballots

    #: `Bargaining Units <https://docs.everyaction.com/reference/bargaining-units>`__ service.
    bargaining_units: BargainingUnits

    #: `Bulk Import <https://docs.everyaction.com/reference/bulk-import>`__ service.
    bulk_import: BulkImport

    #: `Canvass File Requests <https://docs.everyaction.com/reference/canvass-file-requests>`__ service.
    canvass_file_requests: CanvassFileRequests

    #: `Canvass Responses <https://docs.everyaction.com/reference/canvass-responses>`__ service.
    canvass_responses: CanvassResponses

    #: `Changed Entities <https://docs.everyaction.com/reference/changed-entities>`__ service.
    changed_entities: ChangedEntities

    #: `Codes <https://docs.everyaction.com/reference/codes>`__ service.
    codes: Codes

    #: `Commitments <https://docs.everyaction.com/reference/commitments>`__ service.
    commitments: Commitments

    #: `Contributions <https://docs.everyaction.com/reference/contributions>`__ service.
    contributions: Contributions

    #: `Custom Fields <https://docs.everyaction.com/reference/custom-fields>`__ service.
    custom_fields: CustomFields

    #: `Departments <https://docs.everyaction.com/reference/departments>`__ service.
    departments: Departments

    #: `Designations <https://docs.everyaction.com/reference/designations>`__ service.
    designations: Designations

    #: `Disbursements <https://docs.everyaction.com/reference/disbursements>`__ service.
    disbursements: Disbursements

    #: `District Fields <https://docs.everyaction.com/reference/district-fields>`__ service.
    district_fields: DistrictFields

    #: `Email <https://docs.everyaction.com/reference/email>`__ service.
    email: EmailMessages

    #: `Employers <https://docs.everyaction.com/reference/employers>`__ service.
    employers: Employers

    #: `Event Types <https://docs.everyaction.com/reference/event-types>`__ service.
    event_types: EventTypes

    #: `Events <https://docs.everyaction.com/reference/events>`__ service.
    events: Events

    #: `Export Jobs <https://docs.everyaction.com/reference/export-jobs>`__ service.
    export_jobs: ExportJobs

    #: `Extended Source Codes <https://docs.everyaction.com/reference/extended-source-codes>`__ service.
    extended_source_codes: ExtendedSourceCodes

    #: `File-Loading Jobs <https://docs.everyaction.com/reference/file-loading-jobs>`__ service.
    file_loading_jobs: FileLoadingJobs

    #: `Financial Batches <https://docs.everyaction.com/reference/financial-batches>`__ service.
    financial_batches: FinancialBatches

    #: `Folders <https://docs.everyaction.com/reference/folders>`__ service.
    folders: Folders

    #: `Job Classes <https://docs.everyaction.com/reference/job-classes>`__ service.
    job_classes: JobClasses

    #: `Locations <https://docs.everyaction.com/reference/locations>`__ service.
    locations: Locations

    #: `Member Statuses <https://docs.everyaction.com/reference/member-statuses>`__ service.
    member_statuses: MemberStatuses

    #: `MiniVAN Exports <https://docs.everyaction.com/reference/minivan-exports>`__ service.
    minivan_exports: MiniVANExports

    #: `Notes <https://docs.everyaction.com/reference/notes>`__ service.
    notes: Notes

    #: `Online Actions Forms <https://docs.everyaction.com/reference/online-actions-forms>`__ service.
    forms: OnlineActionsForms

    #: `Phones <https://docs.everyaction.com/reference/phones>`__ service.
    phones: Phones

    #: `Printed Lists <https://docs.everyaction.com/reference/printed-lists>`__ service.
    printed_lists: PrintedLists

    #: `Relationships <https://docs.everyaction.com/reference/relationships>`__ service.
    relationships: Relationships

    #: `Reported Demographics <https://docs.everyaction.com/reference/reported-demographics>`__ service.
    demographics: ReportedDemographics

    #: `Saved Lists <https://docs.everyaction.com/reference/saved-lists>`__ service.
    saved_lists: SavedLists

    #: `Schedule Types <https://docs.everyaction.com/reference/schedule-types>`__ service.
    schedule_types: ScheduleTypes

    #: `Score Updates <https://docs.everyaction.com/reference/score-updates>`__ service.
    score_updates: ScoreUpdates

    #: `Scores <https://docs.everyaction.com/reference/scores>`__ service.
    scores: Scores

    #: `Shift Types <https://docs.everyaction.com/reference/shift-types>`__ service.
    shift_types: ShiftTypes

    #: `Signups <https://docs.everyaction.com/reference/signups>`__ service.
    signups: Signups

    #: `Stories <https://docs.everyaction.com/reference/stories>`__ service.
    stories: Stories

    #: `Supporter Groups <https://docs.everyaction.com/reference/supporter-groups>`__ service.
    supporter_groups: SupporterGroups

    #: `Survey Questions <https://docs.everyaction.com/reference/survey-questions>`__ service.
    questions: SurveyQuestions

    #: `Target Export Jobs <https://docs.everyaction.com/reference/target-export-jobs>`__ service.
    target_export_jobs: TargetExportJobs

    #: `Targets <https://docs.everyaction.com/reference/targets>`__ service.
    targets: Targets

    #: `Users <https://docs.everyaction.com/reference/users>`__ service.
    users: Users

    #: `Voter Registration Batches <https://docs.everyaction.com/reference/voter-registration-batches>`__ service.
    registration_batches: VoterRegistrationBatches

    #: `Worksites <https://docs.everyaction.com/reference/worksites>`__ service.
    worksites: Worksites

    @ea_endpoint('/apiKeyProfiles', 'get', paginated=True, result_factory=APIKeyProfile)
    def _api_key_profile(self) -> List[APIKeyProfile]:
        # Odd request in that it is paginated but supposedly only ever has 1 element, corresponding to API key currently
        # being used. This private method gets the paginated result, and then the public api_key_profile method unpacks
        # it.
        pass

    @staticmethod
    def _check_mode_number(num: int) -> None:
        # Make sure mode number is not out of range of database modes.
        num_modes = len(EAClient._MODE_TO_NUM)
        if num >= num_modes:
            raise EAException(f'Mode number ({num}) is too high (expected at most {num_modes - 1})')
        elif num < 0:
            raise EAException(f'Mode number ({num}) is negative')

    @staticmethod
    def _resolve_endpoint(name: str) -> str:
        # Using an endpoint or alias of an endpoint supplied by a user, get the actual endpoint URL.
        if name.startswith('http'):
            # Assume full endpoint specified.
            return name
        lower = name.lower()
        endpoint = EAClient._SHORT_NAME_TO_ENDPOINT.get(lower)
        if not endpoint:
            supported_str = ', '.join(f'{k} -> {v}' for k, v in EAClient._SHORT_NAME_TO_ENDPOINT.items())
            raise EAException(
                f'Unrecognized endpoint alias {name} (did you forget "https://"?).'
                f'Supported aliases are:\n{supported_str}'
            )
        return endpoint

    @staticmethod
    def _resolve_mode(name_or_num: Union[str, int]) -> int:
        # Get the mode number corresponding to the given argument.
        if isinstance(name_or_num, str):
            lower = name_or_num.lower()
            result = EAClient._MODE_TO_NUM.get(lower)
            if result is None:
                raise EAException(
                    f'Unrecognized mode "{name_or_num}". Supported modes are: {", ".join(EAClient._MODE_TO_NUM.keys())}'
                )
            return result
        elif isinstance(name_or_num, int):
            EAClient._check_mode_number(name_or_num)
            return name_or_num
        else:
            raise EAException(f'Expected str or int for mode, got {type(name_or_num)}: {name_or_num}')

    def _add_base(self, route: str) -> str:
        # Sometimes, a route passed to the client will be the full URL.
        # If this is the case, just return that URL. Otherwise, prepend with the EveryAction endpoint.
        if route.startswith(self.endpoint):
            return route
        return f'{self.endpoint}/{route}'

    def _mode_num(self) -> int:
        # Get the mode number using the API key.
        return int(self._session.auth[1][-1])

    def __init__(
        self,
        app_name: Optional[str] = None,
        api_key: Optional[str] = None,
        *,
        endpoint: Optional[str] = None,
        mode: Optional[Union[int, str]] = None,
        from_env: Optional[bool] = None
    ) -> None:
        """Use the given arguments and environment variables to initialize the client.

        :param app_name: The API key's application name. See
            `EveryAction Authentication <https://docs.everyaction.com/reference/authentication>`__
            for more information.
        :param api_key: The API key for the client to use. If the database `mode` is not specified, the last two
            characters of the key should be the "pipe" (|) character followed by a digit indicating the database mode.
            Conversely, this should not be the case when `mode` is specified. See
            `EveryAction Authentication <https://docs.everyaction.com/reference/authentication>`__
            for more information.
        :param endpoint: The endpoint to use. Supports the aliases "US" for the endpoint for US-based clients and "INTL"
            for internationally-based clients.
        :param mode: The database mode to use. Supports the case-insensitive names "VoterFile" and "MyCampaign", as well
            as the digit to be appended to the API key. The mode should be explicitly specified if and only if it is not
            implicitly specified in the API key (see `api_key` above). See
            `EveryAction Authentication <https://docs.everyaction.com/reference/authentication>`__
            for more information.
        :param from_env: When `True`, retrieve the application name from the EVERYACTION_APP_NAME environment variable
            and the api key from the EVERYACTION_API_KEY environment variable. `from_env` should be `False` or
            unspecified when either of `app_name` or `api_key` is specified. `mode` may either be explicitly specified,
            or implicit in the api key environment variable (but not both). When none of `app_name`, `api_key`, or
            `from_env` is specified, the default behavior is to proceed as if `from_env=True`.
        """
        super().__init__(self)
        self._endpoint = self._resolve_endpoint(endpoint or 'US')
        self.default_limit = EAClient._DEFAULT_DEFAULT_LIMIT
        explicit_args = any([app_name, api_key])
        from_env = from_env or not explicit_args

        if from_env:
            if explicit_args:
                raise EAException(
                    f'Neither of app_name={app_name} or api_key should be specified when from_env is True'
                )

            app_name = os.environ.get(self._APP_NAME_ENV)
            if not app_name:
                raise EAException(f'Environment variable {self._APP_NAME_ENV} is missing or empty.')

            api_key = os.environ.get(self._API_KEY_ENV)
            if not api_key:
                raise EAException(f'Environment variable {self._API_KEY_ENV} is missing or empty.')
        else:
            if not app_name:
                raise EAException('app_name must be given when from_env is not specified.')
            if not api_key:
                raise EAException('api_key must be given when from_env is not specified.')
        if '|' in api_key:
            pipes = api_key.count('|')
            if pipes > 1:
                raise EAException(f'Expected at most 1 "|" character in API key, found {pipes}.')

            if len(api_key) < 2 or api_key[-2] != '|':
                raise EAException(f'Expected "|" character to be second-to-last character in API key.')
            if mode is not None:
                raise EAException(
                    'mode specified but mode already indicated in API key, which contains the "|" character.'
                )
        elif mode is not None:
            num = self._resolve_mode(mode)
            api_key += f'|{num}'
        else:
            raise EAException('mode must either be specified or be implicit in the given API key.')

        self._session = Session()
        self._session.auth = (app_name, api_key)

        # Mode number not verified yet if mode implicit in api key.
        self._check_mode_number(self._mode_num())

        import everyaction.services as services
        self.people = services.People(self)
        self.activist_codes = services.ActivistCodes(self)
        self.ballots = services.Ballots(self)
        self.bargaining_units = services.BargainingUnits(self)
        self.bulk_import = services.BulkImport(self)
        self.canvass_file_requests = services.CanvassFileRequests(self)
        self.canvass_responses = services.CanvassResponses(self)
        self.changed_entities = services.ChangedEntities(self)
        self.codes = services.Codes(self)
        self.commitments = services.Commitments(self)
        self.contributions = services.Contributions(self)
        self.custom_fields = services.CustomFields(self)
        self.departments = services.Departments(self)
        self.designations = services.Designations(self)
        self.disbursements = services.Disbursements(self)
        self.district_fields = services.DistrictFields(self)
        self.email = services.EmailMessages(self)
        self.employers = services.Employers(self)
        self.event_types = services.EventTypes(self)
        self.events = services.Events(self)
        self.export_jobs = services.ExportJobs(self)
        self.extended_source_codes = services.ExtendedSourceCodes(self)
        self.file_loading_jobs = services.FileLoadingJobs(self)
        self.financial_batches = services.FinancialBatches(self)
        self.folders = services.Folders(self)
        self.job_classes = services.JobClasses(self)
        self.locations = services.Locations(self)
        self.member_statuses = services.MemberStatuses(self)
        self.minivan_exports = services.MiniVANExports(self)
        self.notes = services.Notes(self)
        self.forms = services.OnlineActionsForms(self)
        self.phones = services.Phones(self)
        self.printed_lists = services.PrintedLists(self)
        self.relationships = services.Relationships(self)
        self.demographics = services.ReportedDemographics(self)
        self.saved_lists = services.SavedLists(self)
        self.schedule_types = services.ScheduleTypes(self)
        self.score_updates = services.ScoreUpdates(self)
        self.scores = services.Scores(self)
        self.shift_types = services.ShiftTypes(self)
        self.signups = services.Signups(self)
        self.stories = services.Stories(self)
        self.supporter_groups = services.SupporterGroups(self)
        self.questions = services.SurveyQuestions(self)
        self.target_export_jobs = services.TargetExportJobs(self)
        self.targets = services.Targets(self)
        self.users = services.Users(self)
        self.worksites = services.Worksites(self)
        self.registration_batches = services.VoterRegistrationBatches(self)

    def __repr__(self) -> str:
        # Just list the attributes in a readable fashion.
        return (
            f'EAClient(app_name={self.app_name}, endpoint={self.endpoint}, mode={self.mode}, '
            f'default_limit={self.default_limit})'
        )

    @property
    def app_name(self) -> str:
        return self._session.auth[0]

    @property
    def default_limit(self) -> int:
        return self._default_limit

    @default_limit.setter
    def default_limit(self, new_value: int) -> None:
        if new_value < 0:
            raise ValueError(
                f'default_limit must be at least 0, not {new_value}.\n'
                f'Note: setting default_limit as 0 allows for unlimited results.'
            )
        self._default_limit = new_value

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @property
    def mode(self) -> str:
        return self._MODES[self._mode_num()]

    def api_key_profile(self) -> APIKeyProfile:
        """Retrieves the `profile <https://docs.everyaction.com/reference/introspection>`__
        associated with the API key this client is using.

        :return: The resulting :class:`APIKeyProfile` object.
        """
        return self._api_key_profile()[0]

    def close(self) -> None:
        """Close the session associated with this client. Note that you will not be able to send requests after calling
        this method.
        """
        self._session.close()

    def delete(self, route: str, **kwargs: Any) -> Response:
        """Send a DELETE request to the configured EveryAction endpoint with the given path and arguments.

        :param route: Path to send request to.
        :param kwargs: Additional arguments to pass to the request.
        :return: The :class:`Response` to the request.
        """
        return self._session.delete(self._add_base(f'{self.endpoint}/{route}'), **kwargs)

    def get(self, route: str, **kwargs: Any) -> Response:
        """Send a GET request to the configured EveryAction endpoint with the given path and arguments.

        :param route: Path to send request to.
        :param kwargs: Additional arguments to pass to the request.
        :return: The :class:`Response` to the request.
        """
        return self._session.get(self._add_base(f'{self.endpoint}/{route}'), **kwargs)

    def patch(self, route: str, **kwargs: Any) -> Response:
        """Send a PATCH request to the configured EveryAction endpoint with the given path and arguments.

        :param route: Path to send request to.
        :param kwargs: Additional arguments to pass to the request.
        :return: The :class:`Response` to the request.
        """
        return self._session.patch(self._add_base(f'{self.endpoint}/{route}'), **kwargs)

    def post(self, route: str, **kwargs: Any) -> Response:
        """Send a POST request to the configured EveryAction endpoint with the given path and arguments.

        :param route: Path to send request to.
        :param kwargs: Additional arguments to pass to the request.
        :return: The :class:`Response` to the request.
        """
        return self._session.post(self._add_base(f'{self.endpoint}/{route}'), **kwargs)

    def put(self, route: str, **kwargs: Any) -> Response:
        """Send a PUT request to the configured EveryAction endpoint with the given path and arguments.

        :param route: Path to send request to.
        :param kwargs: Additional arguments to pass to the request.
        :return: The :class:`Response` to the request.
        """
        return self._session.put(self._add_base(f'{self.endpoint}/{route}'), **kwargs)


# Initialize class vars that depend on other class vars.

EAClient._SHORT_NAME_TO_ENDPOINT = {
    'intl': EAClient._INTL_ENDPOINT,
    'us': EAClient._US_ENDPOINT
}

EAClient._MODE_TO_NUM = {name.lower(): num for num, name in enumerate(EAClient._MODES)}
