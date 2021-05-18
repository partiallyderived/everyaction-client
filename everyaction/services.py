"""
This module contains the objects that have methods corresponding to collections of API calls as they are grouped in the
`EveryAction 8 VAN API docs <https://docs.everyaction.com/reference>`__.
"""

from typing import Dict, Iterable, List, Optional, Union

from everyaction.core import ea_endpoint, E, EAMap, EAProperty, EAService, EAValue
from everyaction.exception import EAFindFailedException
from everyaction.objects import *

__all__ = [
    'ActivistCodes',
    'Ballots',
    'BargainingUnits',
    'BulkImport',
    'CanvassResponse',
    'ChangedEntities',
    'Codes',
    'Commitments',
    'Contributions',
    'CustomFields',
    'Departments',
    'Designations',
    'Disbursements',
    'DistrictFields',
    'EmailMessages',
    'Employers',
    'EventTypes',
    'Events',
    'ExportJobs',
    'ExtendedSourceCodes',
    'FileLoadingJobs',
    'FinancialBatches',
    'Folders',
    'JobClasses',
    'Locations',
    'MemberStatuses',
    'MiniVANExports',
    'Notes',
    'OnlineActionsForms',
    'Phones',
    'PrintedLists',
    'Relationships',
    'ReportedDemographics',
    'SavedLists',
    'ScheduleTypes',
    'ScoreUpdates',
    'Scores',
    'ShiftTypes',
    'Signups',
    'Stories',
    'SupporterGroups',
    'SurveyQuestions',
    'TargetExportJobs',
    'Targets',
    'Users',
    'VoterRegistrationBatches',
    'Worksites'
]


# The services are in the same order as they appear in the EveryAction documentation.


class People(EAService):
    """Represents the
    `People <https://docs.everyaction.com/reference/people>`__ service.
    """

    @ea_endpoint('people/{vanId}/activistCodes', 'get', paginated=True, result_factory=ActivistCodeData)
    def activist_codes(
        self, van_id: int, /, *, limit: Optional[int] = None, **kwargs: EAValue
    ) -> List[ActivistCodeData]:
        """See `GET /people/{vanId}/activistCodes
        <https://docs.everyaction.com/reference/people#peoplevanidactivistcodes>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ActivistCodeData` objects.
        """

    @ea_endpoint('people/{vanId}/canvassResponses', 'post', data_type=CanvassResponse, has_result=False)
    def add_canvass_responses(self, van_id: int, /, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/canvassResponses
        <https://docs.everyaction.com/reference/people#peoplevanidcanvassresponses>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.CanvassResponse` is
            appropriate to unpack here.
        """

    @ea_endpoint(
        'people/{personIdType}:{personId}/canvassResponses',
        'post',
        data_type=CanvassResponse,
        has_result=False
    )
    def add_canvass_responses_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> None:
        """See `POST /people/{personIdType}:{personId}/canvassResponses
        <https://docs.everyaction.com/reference/people#peoplepersonidtypepersonidcanvassresponses>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.CanvassResponse` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{vanId}/codes', 'post', data_type=Code, has_result=False)
    def add_code(self, van_id: int, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/codes
        <https://docs.everyaction.com/reference/people#peoplevanidcodes>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Code` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{personIdType}:{personId}/codes', 'post', data_type=Code, has_result=False)
    def add_code_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> None:
        """See `POST /people/{personIdType}:{personId}/codes
        <https://docs.everyaction.com/reference/people#peoplepersonidtypepersonidcodes>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Code` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{vanId}/myActivistFlags', 'put', has_result=False)
    def add_my_activist_flag(self, van_id: int, /) -> None:
        """See `PUT /people/{vanId}/myActivistFlags
        <https://docs.everyaction.com/reference/people#peoplevanidmyactivistflags>`__.

        :param van_id: The :code:`vanId` path parameter.
        """

    @ea_endpoint('people/{vanId}/notes', 'post', data_type=Note, has_result=False)
    def add_notes(self, van_id: int, /, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/notes
        <https://docs.everyaction.com/reference/people#peoplevanidnotes-1>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Note` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{personIdType}:{personId}/notes', 'post', data_type=Note, has_result=False)
    def add_notes_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> None:
        """See `POST /people/{personIdType}:{personId}/notes
        <https://docs.everyaction.com/reference/people#peoplepersonidtypepersonidnotes>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Note` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{vanId}/relationships', 'post', prop_keys={'relationshipId', 'vanId'}, has_result=False)
    def add_relationship(self, van_id: int, /, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/relationships
        <https://docs.everyaction.com/reference/people#peoplevanidrelationships>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """

    @ea_endpoint('people/find', 'post', data_type=Person, result_factory=Person._find_factory)
    def find(self, **kwargs: EAValue) -> Optional[Person]:
        """See `POST /people/find
        <https://docs.everyaction.com/reference/people#peoplefind>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Person` is
            appropriate to unpack here.
        :returns: The found :class:`.Person` object, or :code:`None` if no person could be found.
        """

    @ea_endpoint('people/findByPhone', 'post', prop_keys={'phoneNumber'}, result_factory=Person)
    def find_by_phone(self, **kwargs: EAValue) -> Person:
        """See `POST /people/findByPhone
        <https://docs.everyaction.com/reference/people#peoplefindbyphone>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.Person` object.
        """

    @ea_endpoint('people/findOrCreate', 'post', data_type=Person, result_factory=Person._find_factory)
    def find_or_create(self, **kwargs: EAValue) -> Person:
        """See `POST /people/findOrCreate
        <https://docs.everyaction.com/reference/people#peoplefindorcreate>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Person` is
            appropriate to unpack here.
        :returns: The found or else created :class:`.Person` object.
        """

    @ea_endpoint('people/{vanId}', 'get', query_arg_keys={'$expand'}, result_factory=Person)
    def get(self, van_id: int, /, **kwargs: EAValue) -> Person:
        """See `GET /people/{vanId}
        <https://docs.everyaction.com/reference/people#peoplevanid-1>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.Person` object.
        """

    @ea_endpoint('people/{personIdType}:{personId}', 'get', query_arg_keys={'$expand'}, result_factory=Person)
    def get_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> Person:
        """See `GET /people/{personIdType}:{personId}
        <https://docs.everyaction.com/reference/people#peoplepersonidtypepersonid-1>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.Person` object.
        """

    @ea_endpoint('people/{vanId}/membership', 'get', result_factory=Membership)
    def membership(self, van_id: int, /) -> Membership:
        """See `GET /people/{vanId}/membership
        <https://docs.everyaction.com/reference/people#peoplevanidmembership>`__.

        :param van_id: The :code:`vanId` path parameter.
        :returns: The resulting :class:`.Membership` object.
        """

    @ea_endpoint('people/{vanId}/notes', 'get', paginated=True, max_top=50, result_factory=Note)
    def notes(self, van_id: int, /, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Note]:
        """See `GET /people/{vanId}/notes
        <https://docs.everyaction.com/reference/people#peoplevanidnotes>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Note` objects.
        """

    @ea_endpoint('people/{vanId}/codes/{codeId}', 'delete', has_result=False)
    def remove_code(self, van_id: int, code_id: int, /) -> None:
        """See `DELETE /people/{vanId}/codes/{codeId}
        <https://docs.everyaction.com/reference/people#peoplevanidcodescodeid>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param code_id: The :code:`code_id` path parameter.
        """

    @ea_endpoint('people/{personIdType}:{personId}/codes/{codeId}', 'delete', has_result=False)
    def remove_code_(self, person_id_type: str, person_id: str, code_id: int, /) -> None:
        """See `DELETE /people/{personIdType}:{personId}/codes/{codeId}
        <https://docs.everyaction.com/reference/people#peoplepersonidtypepersonidcodescodeid>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param code_id: The :code:`codeId` path parameter.
        """

    @ea_endpoint('people/{vanId}/myActivistFlags', 'delete', has_result=False)
    def remove_my_activist_flag(self, van_id: int, /) -> None:
        """See `DELETE /people/{vanId}/myActivistFlags
        <https://docs.everyaction.com/reference/people#peoplevanidmyactivistflags-1>`__.

        :param van_id: The :code:`vanId` path parameter.
        """

    @ea_endpoint('people/{vanId}/disclosureFieldValues', 'post', prop_keys={'disclosureFieldValues'}, has_result=False)
    def set_disclosures_fields(self, van_id: int, /, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/disclosureFieldValues
        <https://docs.everyaction.com/reference/people#peoplevaniddisclosurefieldvalues>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """

    @ea_endpoint(
        'people/{personIdType}:{personId}/disclosureFieldValues',
        'post',
        prop_keys={'disclosureFieldValues'},
        has_result=False,
    )
    def set_disclosures_fields_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> None:
        """See `POST /people/{personIdType}:{personId}/disclosureFieldValues
        <https://docs.everyaction.com/reference/people#peoplepersonidtypepersoniddisclosurefieldvalues>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """

    @ea_endpoint('people/{vanId}', 'post', data_type=Person, result_factory=Person._find_factory)
    def update(self, van_id: int, /, **kwargs: EAValue) -> Optional[Person]:
        """See `POST /people/{vanId}
        <https://docs.everyaction.com/reference/people#peoplevanid>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Person` is
            appropriate to unpack here.
        :returns: (van id, status) of the updated person.
        """

    @ea_endpoint('people/{personIdType}:{personId}', 'post', data_type=Person, result_factory=Person._find_factory)
    def update_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> Optional[Person]:
        """See `POST /people/{personIdType}:{personId}
        <https://docs.everyaction.com/reference/people#peoplepersonidtypepersonid>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Person` is
            appropriate to unpack here.
        :returns: (van id, status) of the resulting person.
        """

    @ea_endpoint('people/{vanId}/notes/{noteId}', 'put', data_type=Note, has_result=False)
    def update_note(self, van_id: int, note_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /people/{vanId}/notes/{noteId}
        <https://docs.everyaction.com/reference/people#peoplevanidnotesnoteid>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param note_id: The :code:`noteId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Note` is
            appropriate to unpack here.
        """

    def _get_van_id(self, **kwargs: EAValue) -> Optional[int]:
        # If kwargs contains vanId or an alias, return that. Otherwise, get the van_id via People.find.
        van_id = EAProperty.shared('vanId').find('vanId', kwargs)
        if not van_id:
            person = self.find(**kwargs)
            if person:
                return person.id
            return None
        return van_id

    def _get_van_id_or_raise(self, **kwargs) -> int:
        # Like _get_van_id, but raises an exception when a person can't be found.
        van_id = self._get_van_id(**kwargs)
        if not van_id:
            raise EAFindFailedException(f'Could not find {Person(**kwargs)}')
        return van_id

    def _update_activist_code(self, activist_code: Union[int, str], action: str, **kwargs: EAValue) -> None:
        # When a string is given for an activist code, get the int ID for it, otherwise just return the int.
        if isinstance(activist_code, str):
            activist_code = self.ea.activist_codes.find(activist_code).id
        van_id = self._get_van_id_or_raise(**kwargs)
        self.add_canvass_responses(van_id, response=ActivistCodeResponse(activist_code, action=action))

    def apply_activist_code(self, activist_code: Union[int, str], **kwargs: EAValue) -> None:
        """Apply the given activist code to the person distinguished by the specified data.

        :param activist_code: The activist code name or ID.
        :param kwargs: The JSON data to lookup the person with. A :class:`.Person` is appropriate to unpack here.
        :raises EAFindFailedException: If either the given activist code or a person could not be found.
        """
        self._update_activist_code(activist_code, 'Apply', **kwargs)

    def apply_notes(self, notes: Note, **kwargs: EAValue) -> None:
        """Apply the given notes to the person distinguished by the specified data.

        :param notes: The notes to add.
        :param kwargs: The JSON data to lookup the person with. A :class:`.Person` is appropriate to unpack here.
        :raises EAFindFailedException: If a person could not be found.
        """
        self.add_notes(self._get_van_id_or_raise(**kwargs), **notes)

    def apply_result_code(self, result_code: Union[int, str], **kwargs: EAValue) -> None:
        """Apply the given result code to the person distinguished by the given data.

        :param result_code: The ID or name of the result code to apply.
        :param kwargs: The JSON data to lookup the person with. A :class:`.Person` is appropriate to unpack here.
        :raises EAFindFailedException: If either the given result code or a person could not be found.
        """
        # When a string is given for a result code, get the int ID for it.
        if isinstance(result_code, str):
            result_code = self.ea.canvass_responses.find_result_code(result_code).id
        van_id = self._get_van_id_or_raise(**kwargs)
        self.add_canvass_responses(van_id, result_code=result_code)

    def lookup(self, *, expand: Union[str, Iterable[str]] = '', **kwargs: EAValue) -> Optional[Person]:
        """Attempt to find a person using the data in `kwargs` by invoking
        `POST /people/find <https://docs.everyaction.com/reference/people#peoplefind>`__.
        Then, if a person was found, use their VAN ID to retrieve their stored :class:`.Person` record by invoking
        `GET /people/{vanId} <https://docs.everyaction.com/reference/people#peoplevanid-1>`__.

        :param expand: List or comma-separated string of names of properties to get for the person.
        :param kwargs: The JSON data to lookup the person with. A :class:`.Person` is appropriate to unpack here.
        :returns: The resulting :class:`.Person` object if found, otherwise `None`.
        """
        van_id = self._get_van_id(**kwargs)
        if not van_id:
            return None
        return self.get(van_id, expand=expand)

    def remove_activist_code(self, activist_code: Union[int, str], **kwargs: EAValue) -> None:
        """Remove the given activist code from the person distinguished by the specified data.

        :param activist_code: The activist code name or ID.
        :param kwargs: The JSON data to lookup the person with. A :class:`.Person` is appropriate to unpack here.
        :raises EAFindFailedException: If either the given activist code or a person could not be found.
        """
        self._update_activist_code(activist_code, 'Remove', **kwargs)

    def update_if_exists(self, lookup_args: EAMap, update_args: EAMap) -> Optional[int]:
        """Update a person with the given properties if they already exist as a record. Works by invoking
        `POST /people/find <https://docs.everyaction.com/reference/people#peoplefind>`__ followed by>`__.
        `POST /people/{vanId} <https://docs.everyaction.com/reference/people#peoplevanid>`__ if the person>`__.
        exists.

        :param lookup_args: The JSON data to lookup the person with. A :class:`.Person` is appropriate to unpack here.
        :param update_args: The JSON data to update the person with. A :class:`.Person` is appropriate to unpack here.
        :returns: The VAN ID of the person, or `None` is no such record was found.
        """
        van_id = self._get_van_id(**lookup_args)
        if not van_id:
            return None
        self.update(van_id, **update_args)
        return van_id


class ActivistCodes(EAService):
    """Represents the
    `Activist Codes <https://docs.everyaction.com/reference/activist-codes>`__ service.
    """

    @ea_endpoint('activistCodes/{activistCodeId}', 'get', result_factory=ActivistCode)
    def get(self, code_id: Union[int, str], /) -> ActivistCode:
        """See `GET /activistCodes/{activistCodeId}
        <https://docs.everyaction.com/reference/activist-codes#activistcodesactivistcodeid>`__.

        :param code_id: The :code:`activistCodeId` path parameter.
        :returns: The resulting :class:`.ActivistCode` object.
        """

    @ea_endpoint(
        'activistCodes',
        'get',
        query_arg_keys={'name', 'statuses', 'type'},
        paginated=True,
        result_factory=ActivistCode
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ActivistCode]:
        """See `GET /activistCodes
        <https://docs.everyaction.com/reference/activist-codes#activistcodes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ActivistCode` objects.
        """

    def find(self, name: str) -> ActivistCode:
        """Find an activist code with exactly the given name. If multiple activists codes have this name, the first will
        be returned.

        :param name: Name of activist code to find.
        :return: The resulting :class:`.ActivistCode`.
        :raises EAException: If the activist code could not be found or if multiple activist codes exist with that name.
        """
        code_in_list = [c for c in self.list(limit=0, name=name) if c.name == name]
        if len(code_in_list) > 1:
            # Multiple activist codes can have the same name (confirmed via experiment).
            raise EAFindFailedException(f'Multiple activist codes named "{name}"')
        if not code_in_list:
            raise EAFindFailedException(f'No activist codes named "{name}"')
        return code_in_list[0]

    def find_each(self, names: Iterable[str]) -> Dict[str, ActivistCode]:
        """Find each activist code for each of the given names.

        :param names: Names of activist codes to find.
        :return: {Name: :class:`.ActivistCode`} for each activist code found.
        :raises EAException: If any activist code could not be found or if multiple activist codes exist with the name
            of any requested activist code.
        """
        names = set(names)
        all_codes = self.list(limit=0)
        result = {}
        for code in all_codes:
            if code.name in names:
                if code.name in result:
                    raise EAFindFailedException(f'Multiple activist codes named "{code.name}"')
                result[code.name] = code
        missing = names - set(result)
        if missing:
            raise EAFindFailedException(f'The following activist codes could not be found: {", ".join(missing)}')
        return result


class Ballots(EAService):
    """Represents the
    `Ballots <https://docs.everyaction.com/reference/ballots>`__ service.
    """

    @ea_endpoint('ballotRequestTypes/{ballotRequestTypeId}', 'get', result_factory=BallotRequestType)
    def request_type(self, type_id: str, /) -> BallotRequestType:
        """See `GET /ballotRequestTypes/{ballotRequestTypeId}
        <https://docs.everyaction.com/reference/ballot-request-types#ballotrequesttypesballotrequesttypeid>`__.

        :returns: The resulting :class:`.BallotRequestType` object.
        """

    @ea_endpoint('ballotRequestTypes', 'get', paginated=True, result_factory=BallotRequestType)
    def request_types(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[BallotRequestType]:
        """See `GET /ballotRequestTypes
        <https://docs.everyaction.com/reference/ballot-request-types#ballotrequesttypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.BallotRequestType` objects.
        """

    @ea_endpoint('ballotReturnStatuses/{ballotReturnStatusId}', 'get', result_factory=BallotReturnStatus)
    def return_status(self, status_id: int, /) -> BallotReturnStatus:
        """See `GET /ballotReturnStatuses/{ballotRequestTypeId}
        <https://docs.everyaction.com/reference/ballot-return-statuses#ballotreturnstatusesballotrequesttypeid>`__.

        :param status_id: The :code:`ballotReturnStatusId` path parameter.
        :returns: The resulting :class:`.BallotReturnStatus` object.
        """

    @ea_endpoint('ballotReturnStatuses', 'get', paginated=True, result_factory=BallotReturnStatus)
    def return_statuses(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[BallotReturnStatus]:
        """See `GET /ballotReturnStatuses
        <https://docs.everyaction.com/reference/ballot-return-statuses#ballotreturnstatuses>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.BallotReturnStatus` objects.
        """

    @ea_endpoint('ballotTypes/{ballotTypeId}', 'get', result_factory=BallotType)
    def type(self, type_id: int, /) -> BallotType:
        """See `GET /ballotTypes/{ballotTypeId}
        <https://docs.everyaction.com/reference/ballot-types#ballottypesballottypeid>`__.

        :param type_id: The :code:`ballotTypeId` path parameter.
        :returns: The resulting :class:`.BallotType` object.
        """

    @ea_endpoint('ballotTypes', 'get', paginated=True, result_factory=BallotType)
    def types(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[BallotType]:
        """See `GET /ballotTypes
        <https://docs.everyaction.com/reference/ballot-types#ballottypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.BallotType` objects.
        """


class BargainingUnits(EAService):
    """Represents the
    `BargainingUnits <https://docs.everyaction.com/reference/bargaining-units>`__ service.
    """

    @ea_endpoint('bargainingUnits/{bargainingUnitId}', 'get', result_factory=BargainingUnit)
    def get(self, bargaining_unit: int, /) -> BargainingUnit:
        """See `GET /bargainingUnits/{bargainingUnitId}
        <https://docs.everyaction.com/reference/bargaining-units#bargainingunitsbargainingunitid>`__.

        :param bargaining_unit: The :code:`bargainingUnitId` path parameter.
        :returns: The resulting :class:`.BargainingUnit` object.
        """

    @ea_endpoint('bargainingUnits', 'get', paginated=True, result_factory=BargainingUnit)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[BargainingUnit]:
        """See `GET /bargainingUnits
        <https://docs.everyaction.com/reference/bargaining-units#bargainingunits>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.BargainingUnit` objects.
        """


class BulkImport(EAService):
    """Represents the
    `Bulk Import <https://docs.everyaction.com/reference/bulk-import>`__ service.
    """

    @ea_endpoint('bulkImportJobs', 'post', data_type=BulkImportJob, result_factory=BulkImportJobData)
    def create(self, **kwargs: EAValue) -> BulkImportJobData:
        """See `POST /bulkImportJobs
        <https://docs.everyaction.com/reference/bulk-import-jobs#bulkimportjobs>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.BulkImportJob` is
            appropriate to unpack here.
        :returns: The :class:`.BulkImportJobData` object for the created Bulk Import Job.
        """

    @ea_endpoint('bulkImportJobs/{jobId}', 'get', result_factory=BulkImportJobData)
    def get(self, job_id: int, /) -> BulkImportJobData:
        """See `GET /bulkImportJobs/{jobId}
        <https://docs.everyaction.com/reference/bulk-import-jobs#bulkimportjobsjobid>`__.

        :param job_id: The :code:`jobId` path parameter.
        :returns: The resulting :class:`.BulkImportJobData` object.
        """

    @ea_endpoint('bulkImportMappingTypes/{mappingTypeName}', 'get', result_factory=MappingTypeData)
    def mapping_type(self, name: str, /) -> MappingTypeData:
        """See `GET /bulkImportMappingTypes/{mappingTypeName}
        <https://docs.everyaction.com/reference/bulk-import-mapping-types#bulkimportmappingtypesmappingtypename>`__.

        :param name: The :code:`mappingTypeName` path parameter.
        :returns: The resulting :class:`.MappingTypeData` object.
        """

    @ea_endpoint('bulkImportMappingTypes', 'get', paginated=True, result_factory=MappingTypeData)
    def mapping_types(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[MappingTypeData]:
        """See `GET /bulkImportMappingTypes
        <https://docs.everyaction.com/reference/bulk-import-mapping-types#bulkimportmappingtypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.MappingTypeData` objects.
        """

    @ea_endpoint('bulkImportJobs/resources', 'get')
    def resources(self) -> List[str]:
        """See `GET /bulkImportJobs/resources
        <https://docs.everyaction.com/reference/bulk-import-jobs#bulkimportjobsresources>`__.

        :returns: List of resource type names.
        """

    @ea_endpoint(
        'bulkImportMappingTypes/{mappingTypeName}/{fieldName}/values',
        'get',
        paginated=True,
        result_factory=ValueMappingData
    )
    def values(
        self,
        mapping_name: str,
        field_name: str,
        /,
        *,
        limit: Optional[int] = None,
        **kwargs: EAValue
    ) -> List[ValueMappingData]:
        """See `GET /bulkImportMappingTypes/{mappingTypeName}/{fieldName}/values
        <https://docs.everyaction.com/reference/bulk-import-mapping-types#bulkimportmappingtypesmappingtypenamefieldnamevalues>`__.

        :param mapping_name: The :code:`mappingTypeName` path parameter.
        :param field_name: The :code:`fieldName` path parameter.
        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ValueMappingData` objects.
        """


class CanvassResponses(EAService):
    """Represents the
    `Canvass Responses <https://docs.everyaction.com/reference/canvass-responses>`__ service.
    """

    @ea_endpoint(
        'canvassResponses/contactTypes',
        'get',
        query_arg_keys={'inputTypeId'},
        result_array=True,
        result_factory=ContactType
    )
    def contact_types(self, **kwargs: EAValue) -> List[ContactType]:
        """See `GET /canvassResponses/contactTypes
        <https://docs.everyaction.com/reference/canvass-responses#canvassresponsescontacttypes>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ContactType` objects.
        """

    @ea_endpoint('canvassResponses/inputTypes', 'get', result_array=True, result_factory=InputType)
    def input_types(self) -> List[InputType]:
        """See `GET /canvassResponses/inputTypes
        <https://docs.everyaction.com/reference/canvass-responses#canvassresponsesinputtypes>`__.

        :returns: List of the resulting :class:`.InputType` objects.
        """

    @ea_endpoint(
        'canvassResponses/resultCodes',
        'get',
        query_arg_keys={'contactTypeId', 'inputTypeId'},
        result_array=True,
        result_factory=ResultCode
    )
    def result_codes(self, **kwargs: EAValue) -> List[ResultCode]:
        """See `GET /canvassResponses/resultCodes
        <https://docs.everyaction.com/reference/canvass-responses#canvassresponsesresultcodes>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ResultCode` objects.
        """

    @staticmethod
    def _find(name: str, all_objects: List[E], obj_name: str) -> E:
        # Finds a contact type, input type, or result code.
        lower = name.lower()
        for obj in all_objects:
            if obj.name.lower() == lower:
                return obj
        raise EAFindFailedException(f'No such {obj_name}: "{name}"')

    def find_contact_type(self, name: str) -> ContactType:
        """Finds the :class:`.ContactType` which exactly matches the given name.

        :param name: Name of contact type to find.
        :returns: The resulting :class:`.ContactType` object..
        :raises EAFindFailedException: If the contact type could not be found.
        """
        return self._find(name, self.contact_types(), 'contact type')

    def find_input_type(self, name: str) -> InputType:
        """Finds the :class:`.InputType` which exactly matches the given name.

        :param name: Name of input type to find.
        :returns: The resulting :class:`.InputType` object.
        :raises EAFindFailedException: If the input type could not be found.
        """
        return self._find(name, self.input_types(), 'input type')

    def find_result_code(self, name: str) -> ResultCode:
        """Finds the :class:`.ResultCode` which exactly matches the given name.

        :param name: Name of result code to find.
        :returns: The resulting :class:`.ResultCode` object..
        :raises EAFindFailedException: If the result code could not be found.
        """
        return self._find(name, self.result_codes(), 'result code')


class ChangedEntities(EAService):
    """Represents the
    `Changed Entities <https://docs.everyaction.com/reference/changed-entities>`__ service.
    """

    @ea_endpoint(
        'changedEntityExportJobs/changeTypes/{resourceType}',
        'get',
        result_array=True,
        result_factory=ChangeType
    )
    def change_types(self, resource: str, /) -> List[ChangeType]:
        """See `GET /changedEntityExportJobs/changeTypes/{resourceType}
        <https://docs.everyaction.com/reference/changed-entity-export-jobs#changedentityexportjobschangetypesresourcetype>`__.

        :param resource: The :code:`resourceType` path parameter.
        :returns: List of the resulting :class:`.ChangeType` objects.
        """

    @ea_endpoint(
        'changedEntityExportJobs',
        'post',
        data_type=ChangedEntityExportJob,
        result_factory=ChangedEntityExportJob
    )
    def create(self, **kwargs: EAValue) -> ChangedEntityExportJob:
        """See `POST /changedEntityExportJobs
        <https://docs.everyaction.com/reference/changed-entity-export-jobs#changedentityexportjobs>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.ChangedEntityExportJob`
            is appropriate to unpack here.
        :returns: The resulting :class:`.ChangedEntityExportJob` object.
        """

    @ea_endpoint(
        'changedEntityExportJobs/fields/{resourceType}',
        'get',
        result_array=True,
        result_factory=ChangedEntityField
    )
    def fields(self, resource: str, /) -> List[ChangedEntityField]:
        """See `GET /changedEntityExportJobs/fields/{resourceType}
        <https://docs.everyaction.com/reference/changed-entity-export-jobs#changedentityexportjobsfieldsresourcetype>`__.

        :param resource: The :code:`resourceType` path parameter.
        :returns: The resulting :class:`.ChangedEntityField` object.
        """

    @ea_endpoint('changedEntityExportJobs/{exportJobId}', 'get', result_factory=ChangedEntityExportJob)
    def get(self, job_id: int, /) -> ChangedEntityExportJob:
        """See `GET /changedEntityExportJobs/{exportJobId}
        <https://docs.everyaction.com/reference/changed-entity-export-jobs#changedentityexportjobsexportjobid>`__.

        :param job_id: The :code:`exportJobId` path parameter.
        :returns: The resulting :class:`.ChangedEntityExportJobData` object.
        """

    @ea_endpoint('changedEntityExportJobs/resources', 'get')
    def resources(self) -> List[str]:
        """See `GET /changedEntityExportJobs/resources
        <https://docs.everyaction.com/reference/changed-entity-export-jobs#changedentityexportjobsresources>`__.

        :returns: List of the resource type names.
        """


class Codes(EAService):
    """Represents the
    `Codes <https://docs.everyaction.com/reference/codes>`__ service.
    """

    @ea_endpoint('codes', 'post', data_type=Code, result_factory=Code)
    def create(self, **kwargs: EAValue) -> Code:
        """See `POST /codes
        <https://docs.everyaction.com/reference/codes#codes-2>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Code` is
            appropriate to unpack here.
        :returns: The created :class:`.Code` object.
        """

    @ea_endpoint('codes/batch', 'post', prop_keys={'codes'}, result_array=True, result_factory=CodeResult)
    def create_each(self, **kwargs: EAValue) -> List[CodeResult]:
        """See `POST /codes/batch
        <https://docs.everyaction.com/reference/codes#codesbatch>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.CodeResult` objects for each code to be created.
        """

    @ea_endpoint('codes/{codeId}', 'delete', has_result=False)
    def delete(self, code_id: int, /) -> None:
        """See `DELETE /codes/{codeId}
        <https://docs.everyaction.com/reference/codes#codescodeid-2>`__.

        :param code_id: The :code:`codeId` path parameter.
        """

    @ea_endpoint('codes', 'delete', result_array=True, result_factory=CodeResult)
    def delete_each(self, *, data: List[int]) -> List[CodeResult]:
        """See `DELETE /codes
        <https://docs.everyaction.com/reference/codes#codes-4>`__.

        :param data: The ids of the codes to delete.
        :returns: List of the resulting :class:`.CodeResult` objects for each code to be deleted.
        """

    @ea_endpoint('codes/{codeId}', 'get', result_factory=Code)
    def get(self, code_id: int, /) -> Code:
        """See `GET /codes/{codeId}
        <https://docs.everyaction.com/reference/codes#codescodeid>`__.

        :param code_id: The :code:`codeId` path parameter.
        :returns: The resulting :class:`.Code` object.
        """

    @ea_endpoint(
        'codes',
        'get',
        query_arg_keys={'codeType', 'name', 'parentCodeId', 'supportedEntities', '$expand', '$orderby'},
        paginated=True,
        props={'codeType': EAProperty('type')},
        result_factory=Code
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Code]:
        """See `GET /codes
        <https://docs.everyaction.com/reference/codes#codes-1>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Code` objects.
        """

    @ea_endpoint('codes/supportedEntities', 'get', result_array=True)
    def supported_entities(self) -> List[str]:
        """See `GET /codes/supportedEntities
        <https://docs.everyaction.com/reference/codes#codessupportedentities>`__.

        :returns: List of the names of the supported entities.
        """

    @ea_endpoint('codeTypes', 'get', result_array=True)
    def types(self) -> List[str]:
        """See `GET /codeTypes
        <https://docs.everyaction.com/reference/code-types#codetypes>`__.

        :returns: List of the names of the code types.
        """

    @ea_endpoint('codes/{codeId}', 'put', data_type=Code, has_result=False)
    def update(self, code_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /codes/{codeId}
        <https://docs.everyaction.com/reference/codes#codescodeid-1>`__.

        :param code_id: The :code:`codeId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Code` is
            appropriate to unpack here.
        """

    @ea_endpoint('codes', 'put', prop_keys={'codes'}, result_array=True, result_factory=CodeResult)
    def update_each(self, **kwargs: EAValue) -> List[CodeResult]:
        """See `PUT /codes
        <https://docs.everyaction.com/reference/codes#codes-3>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.CodeResult` objects for each code to be updated.
        """


class Commitments(EAService):
    """Represents the
    `Commitments <https://docs.everyaction.com/reference/commitments>`__ service.
    """

    @ea_endpoint('commitments/{commitmentId}', 'patch', data_type=Commitment, result_factory=Commitment)
    def update(self, commitment_id: int, /, **kwargs: EAValue) -> Commitment:
        """See `PATCH /commitments/{commitmentId}
        <https://docs.everyaction.com/reference/commitments#commitmentscommitmentid>`__.

        :param commitment_id: The :code:`commitmentId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Commitment` is
            appropriate to unpack here.
        :returns: The resulting :class:`.Commitment` object.
        """


class Contributions(EAService):
    """Represents the
    `Contributions <https://docs.everyaction.com/reference/contributions>`__ service.
    """

    @ea_endpoint(
        'contributions/{contributionId}/adjustments',
        'post',
        data_type=Adjustment,
        result_factory=AdjustmentResponse
    )
    def adjust(self, contribution_id: int, /, **kwargs: EAValue) -> AdjustmentResponse:
        """See `POST /contributions/{contributionId}/adjustments
        <https://docs.everyaction.com/reference/contributions#contributionscontributionidadjustments>`__.

        :param contribution_id: The :code:`contributionId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Adjustment` is
            appropriate to unpack here.
        :returns: The resulting :class:`.AdjustmentResponse` object.
        """

    @ea_endpoint('contributions/attributionTypes', 'get', result_array=True)
    def attribution_types(self) -> List[str]:
        """See `GET /contributions/attributionTypes
        <https://docs.everyaction.com/reference/contributions#contributionsattributiontypes>`__.

        :returns: List of the attribution types.
        """

    @ea_endpoint('contributions', 'post', data_type=Contribution, result_factory=Contribution)
    def create(self, **kwargs: EAValue) -> Contribution:
        """See `POST /contributions
        <https://docs.everyaction.com/reference/contributions#contributions-1>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Contribution` is
            appropriate to unpack here.
        :returns: The created :class:`.Contribution` object.
        """

    @ea_endpoint('contributions/{contributionId}/attributions/{vanId}', 'put', data_type=Attribution, has_result=False)
    def create_or_update_attribution(self, contribution_id: int, van_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /contributions/{contributionId}/attributions/{vanId}
        <https://docs.everyaction.com/reference/contributions#contributionscontributionidattributionsvanid>`__.

        :param contribution_id: The :code:`contributionId` path parameter.
        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Attribution` is
            appropriate to unpack here.
        """

    @ea_endpoint('contributions/{contributionId}/attributions/{vanId}', 'delete', has_result=False)
    def delete_attribution(self, contribution_id: int, van_id: int, /) -> None:
        """See `DELETE /contributions/{contributionId}/attributions/{vanId}
        <https://docs.everyaction.com/reference/contributions#contributionscontributionidattributionsvanid-1>`__.

        :param contribution_id: The :code:`contributionId` path parameter.
        :param van_id: The :code:`vanId` path parameter.
        """

    @ea_endpoint('contributions/{contributionId}', 'get', result_factory=Contribution)
    def get(self, contribution_id: int, /) -> Contribution:
        """See `GET /contributions/{contributionId}
        <https://docs.everyaction.com/reference/contributions#contributionscontributionid>`__.

        :param contribution_id: The :code:`contributionId` path parameter.
        :returns: The resulting :class:`.Contribution` object.
        """

    @ea_endpoint('contributions/{alternateIdType}:{alternateId}', 'get', result_factory=Contribution)
    def get_(self, alternate_id_type: str, alternate_id: str, /) -> Contribution:
        """See `GET /contributions/{alternateIdType}:{alternateId}
        <https://docs.everyaction.com/reference/contributions#contributionsalternateidtypealternateid>`__.

        :param alternate_id_type: The :code:`alternateIdType` path parameter.
        :param alternate_id: The :code:`alternateId` path parameter.
        :returns: The resulting :class:`.Contribution` object.
        """


class CustomFields(EAService):
    """Represents the
    `Custom Fields <https://docs.everyaction.com/reference/custom-fields>`__ service.
    """

    @ea_endpoint('customFields/{customFieldId}', 'get')
    def get(self, field_id: int, /) -> CustomField:
        """See `GET /customFields/customFieldId
        <https://docs.everyaction.com/reference/custom-fields#customfieldscustomfieldid>`__.

        :param field_id: The :code:`customFieldId` path parameter.
        :returns: The resulting :class:`.CustomField` object.
        """

    @ea_endpoint(
        'customFields',
        'get',
        query_arg_keys={'customFieldsGroupType'},
        result_array=True,
        result_factory=CustomField
    )
    def list(self, **kwargs: EAValue) -> List[CustomField]:
        """See `GET /customFields
        <https://docs.everyaction.com/reference/custom-fields#customfields>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.CustomField` objects.
        """


class Departments(EAService):
    """Represents the
    `Departments <https://docs.everyaction.com/reference/departments>`__ service.
    """

    @ea_endpoint('departments/{department_id}', 'get', result_factory=Department)
    def get(self, department_id: int, /) -> Department:
        """See `GET /departments/{departmentId}
        <https://docs.everyaction.com/reference/departments#departmentsdepartmentid>`__.

        :param department_id: The :code:`departmentId` path parameter.
        :returns: The resulting :class:`.Department` object.
        """

    @ea_endpoint(
        'departments',
        'get',
        query_arg_keys={'employerId', 'isMyOrganization'},
        paginated=True,
        result_factory=Department
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Department]:
        """See `GET /departments
        <https://docs.everyaction.com/reference/departments#departments>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The resulting :class:`.Department` objects.
        """


class Designations(EAService):
    """Represents the
    `Designations <https://docs.everyaction.com/reference/designations>`__ service.
    """

    @ea_endpoint('designations', 'get', result_array_key='items', result_factory=Designation)
    def list(self) -> List[Designation]:
        """See `GET /designations
        <https://docs.everyaction.com/reference/designations#designations>`__.

        :returns: List of the resulting :class:`.Designation` objects.
        """


class Disbursements(EAService):
    """Represents the
    `Disbursements <https://docs.everyaction.com/reference/disbursements>`__ service.
    """

    @ea_endpoint('disbursements', 'post', data_type=Disbursement, has_result=False)
    def create_or_update(self, **kwargs: EAValue) -> None:
        """See `POST /disbursements
        <https://docs.everyaction.com/reference/disbursements#disbursements>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Disbursement` is
            appropriate to unpack here.
        """

    @ea_endpoint('disbursements/{disbursementId}', 'get', result_factory=Disbursement)
    def get(self, disbursement_id: int, /) -> Disbursement:
        """See `GET /disbursements/{disbursementId}
        <https://docs.everyaction.com/reference/disbursements#disbursementsdisbursementid>`__.

        :param disbursement_id: The :code:`disbursementId` path parameter.
        :returns: The resulting :class:`.Disbursement` object.
        """


class DistrictFields(EAService):
    """Represents the
    `District Fields <https://docs.everyaction.com/reference/district-fields>`__ service.
    """

    @ea_endpoint('districtFields/{districtFieldId}', 'get', result_factory=DistrictField)
    def get(self, field_id: int, /) -> DistrictField:
        """See `GET /districtFields/{districtFieldId}
        <https://docs.everyaction.com/reference/district-fields#districtfieldsdistrictfieldid>`__.

        :param field_id: The :code:`districtFieldId` path parameter.
        :returns: The resulting :class:`.DistrictField` object.
        """

    @ea_endpoint(
        'districtFields',
        'get',
        query_arg_keys={'custom', 'organizeAt'},
        result_array=True,
        result_factory=DistrictField
    )
    def list(self) -> List[DistrictField]:
        """See `GET /districtFields
        <https://docs.everyaction.com/reference/district-fields#districtfields>`__.

        :returns: List of the resulting :class:`.DistrictField` objects.
        """


class EmailMessages(EAService):
    """Represents the
    `Email <https://docs.everyaction.com/reference/email>`__ service.
    """

    @ea_endpoint('email/messages/{emailId}', 'get', query_arg_keys={'$expand'}, result_factory=EmailMessage)
    def get(self, email_id: int, /, **kwargs: EAValue) -> EmailMessage:
        """See `GET /email/messages/{emailId}
        <https://docs.everyaction.com/reference/email#emailmessagesemailid>`__.

        :param email_id: The :code:`emailId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.EmailMessage` object.
        """

    @ea_endpoint('email/messages', 'get', query_arg_keys={'$orderby'}, result_array=True, result_factory=EmailMessage)
    def list(self, **kwargs: EAValue) -> List[EmailMessage]:
        """See `GET /email/messages
        <https://docs.everyaction.com/reference/email#emailmessages>`__.

        :returns: List of the resulting :class:`.EmailMessage` objects.
        """


class Employers(EAService):
    """Represents the
    `Employers <https://docs.everyaction.com/reference/employers>`__ service.
    """

    @ea_endpoint(
        'employers/{employer_id}/bargainingUnits/{bargaining_unit_id}',
        'post',
        result_factory=EmployerBargainingUnit
    )
    def add_bargaining_unit(self, employer_id: int, bargaining_unit_id: int, /) -> EmployerBargainingUnit:
        """See `POST /employers/{employerId}/bargainingUnits/{bargainingUnitId}
        <https://docs.everyaction.com/reference/employers#employersemployeridbargainingunitsbargainingunitid>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param bargaining_unit_id: The :code:`bargainingUnitId` path parameter.
        :returns: The resulting :class`.EmployerBargainingUnit` object.
        """

    @ea_endpoint(
        'employers/{employer_id}/bargainingUnits/{bargaining_unit_id}/jobClasses/{job_class_id}',
        'post',
        result_factory=EmployerBargainingUnit
    )
    def add_job_class(self, employer_id: int, bargaining_unit_id: int, job_class_id: int, /) -> BargainingUnitJobClass:
        """See `POST /employers/{employerId}/bargainingUnits/{bargainingUnitId}/jobClasses/{jobClassId}
        <https://docs.everyaction.com/reference/employers#employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param bargaining_unit_id: The :code:`bargainingUnitId` path parameter.
        :param job_class_id: The :code:`jobClassId` path parameter.
        :returns: The added :class:`.BargainingUnitJobClass` object.
        """

    @ea_endpoint(
        'employers/{employer_id}/shiftTypes/{shiftTypeId}',
        'post',
        data_type=ShiftType,
        result_factory=ShiftType
    )
    def add_shift_type(self, employer_id: int, shift_type_id: int, /, **kwargs) -> ShiftType:
        """See `POST /employers/{employerId}/shiftTypes/{shiftTypeId}
        <https://docs.everyaction.com/reference/employers#employersemployeridshifttypesshifttypeid>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param shift_type_id: The :code:`shiftTypeId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.ShiftType` is
            appropriate to unpack here.
        :returns: The added :class:`.ShiftType` object.
        """

    @ea_endpoint('employers', 'post', data_type=Employer, result_factory=Employer)
    def create(self, **kwargs: EAValue) -> Employer:
        """See `POST /employers
        <https://docs.everyaction.com/reference/employers#employers-2>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. An :class:`.Employer` is
            appropriate to unpack here.
        :returns: The created :class:`.Employer` object.
        """

    @ea_endpoint('employers/{employer_id}/departments', 'post', data_type=Department, result_factory=Department)
    def create_department(self, employer_id: int, /, **kwargs: EAValue) -> Department:
        """See `POST /employers/{employerId}/departments
        <https://docs.everyaction.com/reference/employers#employersemployeriddepartments>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Department` is
            appropriate to unpack here.
        :returns: The created :class:`.Department` object.
        """

    @ea_endpoint('employers/{employer_id}/worksites', 'post', data_type=Worksite, result_factory=Worksite)
    def create_worksite(self, employer_id: int, /, **kwargs: EAValue) -> Worksite:
        """See `POST /employers/{employer_id}/worksites
        <https://docs.everyaction.com/reference/employers#employersemployer_idworksites>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Worksite` is
            appropriate to unpack here.
        :returns: The created :class:`.Worksite` object.
        """

    @ea_endpoint('employers/{employer_id}', 'get', query_arg_keys={'$expand'}, result_factory=Employer)
    def get(self, employer_id: int, /, **kwargs: EAValue) -> Employer:
        """See `GET /employers/{employerId}
        <https://docs.everyaction.com/reference/employers#employersemployerid>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.Employer` object.
        """

    @ea_endpoint(
        'employers',
        'get',
        query_arg_keys={'isMyOrganization', '$expand'},
        paginated=True,
        max_top=500,
        result_factory=Employer
    )
    def list(self, *, limit: Optional[int] = None, **kwargs) -> List[Employer]:
        """See `GET /employers
        <https://docs.everyaction.com/reference/employers#employers-1>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Employer` objects.
        """

    @ea_endpoint('employers/{employer_id}', 'patch', prop_keys={'isMyOrganization'}, result_factory=Employer)
    def update(self, employer_id: int, /, **kwargs: EAValue) -> Employer:
        """See `PATCH /employers/{employerId}
        <https://docs.everyaction.com/reference/employers#employersemployerid-1>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param kwargs: The applicable query and JSON arguments for the request.
        :returns: The updated :class:`.Employer` object.
        """


class EventTypes(EAService):
    """Represents the
    `Event Types <https://docs.everyaction.com/reference/event-types>`__ service.
    """

    @ea_endpoint('events/types/{eventTypeId}', 'get', result_factory=EventType)
    def get(self, type_id: int, /) -> EventType:
        """See `GET /events/types/{eventTypeId}
        <https://docs.everyaction.com/reference/events#eventstypeseventtypeid>`__.

        :param type_id: The :code:`eventTypeId` path parameter.
        :returns: The resulting :class:`.EventType` object.
        """

    @ea_endpoint('events/types', 'get', result_array=True, result_factory=EventType)
    def list(self) -> List[EventType]:
        """See `GET /events/types
        <https://docs.everyaction.com/reference/events#eventstypes>`__.

        :returns: List of the resulting :class:`.EventType` objects.
        """


class Events(EAService):
    """Represents the
    `Events <https://docs.everyaction.com/reference/events>`__ service.
    """

    @ea_endpoint('events/{eventId}/shifts', 'post', data_type=EventShift, result_factory=EventShift)
    def add_shift(self, event_id: int, /, **kwargs: EAValue) -> EventShift:
        """See `POST /events/{eventId}/shifts
        <https://docs.everyaction.com/reference/events#eventseventidshifts>`__.

        :param event_id: The :code:`eventId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.EventShift` is
            appropriate to unpack here.
        :returns: The resulting :class:`.EventShift` object.
        """

    @ea_endpoint('events', 'post', data_type=Event, result_factory=Event)
    def create(self, **kwargs: EAValue) -> Event:
        """See `POST /events
        <https://docs.everyaction.com/reference/events#events-2>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Event` is appropriate to
            unpack here.
        :returns: The resulting :class:`.Event` object.
        """

    @ea_endpoint('events/{eventId}', 'delete')
    def delete(self, event_id: int, /) -> None:
        """See `DELETE /events/{eventId}
        <https://docs.everyaction.com/reference/events#eventseventid-2>`__.

        :param event_id: The :code:`eventId` path parameter.
        """

    @ea_endpoint('events/{eventId}', 'get', query_arg_keys={'$expand'}, result_factory=Event)
    def get(self, event_id: int, /, **kwargs: EAValue) -> Event:
        """See `GET /events/{eventId}
        <https://docs.everyaction.com/reference/events#eventseventid>`__.

        :param event_id: The :code:`eventId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.Event` object.
        """

    @ea_endpoint(
        'events',
        'get',
        query_arg_keys={
            'codeIds',
            'createdByCommitteeId',
            'districtFieldValue',
            'eventTypeIds',
            'inRepetitionWithEventId',
            'startingAfter',
            'startingBefore',
            '$expand'
        },
        paginated=True,
        max_top=50,
        props={'districtFieldValue': EAProperty()},
        result_factory=Event
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Event]:
        """See `GET /events
        <https://docs.everyaction.com/reference/events#events-1>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Event` objects.
        """

    @ea_endpoint(
        'events/{eventId}',
        'patch',
        query_arg_keys={'recurrenceType'},
        path_params_to_data={'eventId'},
        prop_keys={'isActive'},
        has_result=False
    )
    def patch(self, event_id: int, /, **kwargs: EAValue) -> None:
        """See `PATCH /events/{eventId}
        <https://docs.everyaction.com/reference/events#eventseventid-1>`__.
        convenience, the `eventId` parameter need only be specified as a positional/path parameter.

        :param event_id: The :code:`eventId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """

    @ea_endpoint('events/{eventId}', 'put', data_type=Event, has_result=False)
    def update(self, event_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /events/{eventId}
        <https://docs.everyaction.com/reference/events#eventseventid-3>`__.

        :param event_id: The :code:`eventId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Event` is
            appropriate to unpack here.
        """


class ExportJobs(EAService):
    """Represents the
    `Export Jobs <https://docs.everyaction.com/reference/export-jobs>`__ service.
    """

    @ea_endpoint('exportJobs', 'post', prop_keys={'savedListId', 'type', 'webhookUrl'}, result_factory=ExportJob)
    def create(self, **kwargs: EAValue) -> ExportJob:
        """See `POST /exportJobs
        <https://docs.everyaction.com/reference/export-jobs#exportjobs>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.ExportJob` object.
        """

    @ea_endpoint('exportJobs/{exportJobId}', 'get', result_factory=ExportJob)
    def get(self, job_id: int, /) -> ExportJob:
        """See `GET /exportJobs/{exportJobId}
        <https://docs.everyaction.com/reference/export-jobs#exportjobsexportjobid>`__.

        :param job_id: The :code:`exportJobId` path parameter.
        :returns: The resulting :class:`.ExportJob` object.
        """

    @ea_endpoint('exportJobTypes', 'get', paginated=True, result_factory=ExportJobType)
    def types(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ExportJobType]:
        """See `GET /exportJobTypes
        <https://docs.everyaction.com/reference/export-job-types#exportjobtypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ExportJobType` objects.
        """


class ExtendedSourceCodes(EAService):
    """Represents the
    `Extended Source Codes <https://docs.everyaction.com/reference/extended-source-codes>`__ service.
    """

    @ea_endpoint(
        'codes/extendedSourceCodes',
        'get',
        query_arg_keys={'vanId', 'extendedSourceCodeName'},
        paginated=True,
        props={'extendedSourceCodeName': EAProperty('name')},
        result_factory=ExtendedSourceCode
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ExtendedSourceCode]:
        """See `GET /codes/extendedSourceCodes
        <https://docs.everyaction.com/reference/codes#codesextendedsourcecodes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.ExtendedSourceCode` objects.
        """


class FileLoadingJobs(EAService):
    """Represents the
    `File Loading Jobs <https://docs.everyaction.com/reference/file-loading-jobs>`__ service.
    """

    @ea_endpoint('fileLoadingJobs', 'post', data_type=FileLoadingJob, result_factory=FileLoadingJob)
    def create(self, **kwargs: EAValue) -> FileLoadingJob:
        """See `POST /fileLoadingJobs
        <https://docs.everyaction.com/reference/file-loading-jobs#fileloadingjobs>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.FileLoadingJob` is
            appropriate to unpack here.
        :returns: The created :class:`.FileLoadingJob` object.
        """

    @ea_endpoint('fileLoadingJobs/{jobId}', 'get', result_factory=FileLoadingJob)
    def get(self, job_id: int, /) -> FileLoadingJob:
        """See `GET /fileLoadingJobs/{jobId}
        <https://docs.everyaction.com/reference/file-loading-jobs#fileloadingjobsjobid>`__.

        :param job_id: The :code:`jobId` path parameter.
        :returns: The resulting :class:`.FileLoadingJob` object.
        """


class FinancialBatches(EAService):
    """Represents the
    `Financial Batches <https://docs.everyaction.com/reference/financial-batches>`__ service.
    """

    @ea_endpoint('financialBatches', 'post', data_type=FinancialBatch, result_factory=FinancialBatch)
    def create(self, **kwargs: EAValue) -> FinancialBatch:
        """See `POST /financialBatches
        <https://docs.everyaction.com/reference/financial-batches#financialbatches-1>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.FinancialBatch` is
            appropriate to unpack here.
        :returns: The created :class:`.FinancialBatch` object.
        """

    @ea_endpoint('financialBatches/{financialBatchId}', 'get', result_factory=FinancialBatch)
    def get(self, batch_id: int, /) -> FinancialBatch:
        """See `GET /financialBatches/{financialBatchId}
        <https://docs.everyaction.com/reference/financial-batches#financialbatchesfinancialbatchid>`__.

        :param batch_id: The :code:`financialBatchId` path parameter.
        :returns: The resulting :class:`.FinancialBatch` object.
        """

    @ea_endpoint(
        'financialBatches',
        'get',
        query_arg_keys={'includeAllAutoGenerated', 'includeAllStatuses', 'includeUnassigned', 'searchKeyword'},
        result_array_key='items',
        result_factory=FinancialBatch
    )
    def list(self, **kwargs: EAValue) -> List[FinancialBatch]:
        """See `GET /financialBatches
        <https://docs.everyaction.com/reference/financial-batches#financialbatches>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.FinancialBatch` objects.
        """


class Folders(EAService):
    """Represents the
    `Folders <https://docs.everyaction.com/reference/folders>`__ service.
    """

    @ea_endpoint('folders/{folderId}', 'get', result_factory=Folder)
    def get(self, folder_id: int, /) -> Folder:
        """See `GET /folders/{folderId}
        <https://docs.everyaction.com/reference/folders#foldersfolderid>`__.

        :param folder_id: The :code:`folderId` path parameter.
        """

    @ea_endpoint('folders', 'get', paginated=True, result_factory=Folder)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Folder]:
        """See `GET /folders
        <https://docs.everyaction.com/reference/folders#folders>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """


class JobClasses(EAService):
    """Represents the
    `JobClasses <https://docs.everyaction.com/reference/job-classes>`__ service.
    """

    @ea_endpoint('jobClasses', 'post', data_type=JobClass, result_factory=JobClass)
    def create(self, **kwargs: EAValue) -> JobClass:
        """See `POST /jobClasses
        <https://docs.everyaction.com/reference/job-classes#jobclasses-1>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.JobClass` is appropriate
            to unpack here.
        :returns: The created :class:`.JobClass` object.
        """

    @ea_endpoint('jobClasses/{job_class_id}', 'get', result_factory=JobClass)
    def get(self, job_class_id: int, /) -> JobClass:
        """See `GET /jobClasses/{jobClassId}
        <https://docs.everyaction.com/reference/job-classes#jobclassesjobclassid>`__.

        :param job_class_id: The :code:`jobClassId` path parameter.
        :returns: The resulting :class:`.JobClass`.
        """

    @ea_endpoint('/jobClasses', 'get', paginated=True, result_factory=JobClass)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[JobClass]:
        """See `GET /jobClasses
        <https://docs.everyaction.com/reference/job-classes#jobclasses>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.JobClass` objects.
        """


class Locations(EAService):
    """Represents the
    `Locations <https://docs.everyaction.com/reference/locations>`__ service.
    """

    @ea_endpoint('locations', 'post', data_type=Location, result_factory=Location)
    def create(self, **kwargs: EAValue) -> Location:
        """See `POST /locations
        <https://docs.everyaction.com/reference/locations#locations-2>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Location` is
            appropriate to unpack here.
        :returns: The created :class:`.Location` object.
        """

    @ea_endpoint('locations/{locationId}', 'delete', has_result=False)
    def delete(self, location_id: int, /) -> None:
        """See `DELETE /locations/{locationId}
        <https://docs.everyaction.com/reference/locations#locationslocationid-1>`__.

        :param location_id: The :code:`locationId` path parameter.
        """

    @ea_endpoint('locations/findOrCreate', 'post', data_type=Location, result_factory=Location, exclude_keys={'id'})
    def find_or_create(self, **kwargs: EAValue) -> Location:
        """See `POST /locations/findOrCreate
        <https://docs.everyaction.com/reference/locations#locationsfindorcreate>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Location` is
            appropriate to unpack here.
        :returns: The resulting :class:`.Location` object.
        """

    @ea_endpoint('locations/{locationId}', 'get', result_factory=Location, exclude_keys={'id'})
    def get(self, location_id: int, /) -> Location:
        """See `GET /locations/{locationId}
        <https://docs.everyaction.com/reference/locations#locationslocationid>`__.

        :param location_id: The :code:`locationId` path parameter.
        :returns: The resulting :class:`.Location` object.
        """

    @ea_endpoint(
        'locations',
        'get',
        query_arg_keys={'name'},
        paginated=True,
        result_factory=Location,
        exclude_keys={'id'}
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Location]:
        """See `GET /locations
        <https://docs.everyaction.com/reference/locations#locations-1>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Location` objects.
        """


class MemberStatuses(EAService):
    """Represents the
    `Member Statuses <https://docs.everyaction.com/reference/member-statuses>`__ service.
    """

    @ea_endpoint('memberStatuses', 'post', data_type=MemberStatus, result_factory=MemberStatus)
    def create(self, **kwargs: EAValue) -> MemberStatus:
        """See `POST /memberStatuses
        <https://docs.everyaction.com/reference/member-statuses#memberstatuses-1>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.MemberStatus` is
            appropriate to unpack here.
        :returns: The created :class:`.MemberStatus` object.
        """

    @ea_endpoint('memberStatuses/{member_status_id}', 'get', result_factory=MemberStatus)
    def get(self, member_status_id: int, /) -> MemberStatus:
        """See `GET /memberStatuses/{memberStatusId}
        <https://docs.everyaction.com/reference/member-statuses#memberstatusesmemberstatusid>`__.

        :param member_status_id: The :code:`member_status_id` path parameter.
        :returns: The resulting :class:`.MemberStatus` object.
        """

    @ea_endpoint('memberStatuses', 'get', paginated=True, result_factory=MemberStatus)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[MemberStatus]:
        """See `GET /memberStatuses
        <https://docs.everyaction.com/reference/member-statuses#memberstatuses>`__.

        :param limit: Maximum number of records to get for the request.
        :param kwargs: The applicable query arguments and JSON data for the request.

        :returns: List of the resulting :class:`.MemberStatus` objects.
        """


class MiniVANExports(EAService):
    """Represents the
    `MiniVANExports <https://docs.everyaction.com/reference/minivan-exports>`__ service.
    """

    @ea_endpoint('minivanExports/{minivanExportId}', 'get', result_factory=MiniVANExport)
    def get(self, export_id: int, /) -> MiniVANExport:
        """See `GET /minivanExports/{minivanExportId}
        <https://docs.everyaction.com/reference/minivan-exports#minivanexportsminivanexportid>`__.

        :param export_id: The :code:`minivanExportId` path parameter.
        :returns: The resulting :class:`.MiniVANExport` object.
        """

    @ea_endpoint(
        'minivanExports',
        'get',
        query_arg_keys={'createdBy', 'generatedAfter', 'generatedBefore', 'name', '$expand'},
        paginated=True,
        max_top=50,
        result_factory=MiniVANExport
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[MiniVANExport]:
        """See `GET /minivanExports
        <https://docs.everyaction.com/reference/minivan-exports#minivanexports>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.MiniVANExport` objects.
        """


class Notes(EAService):
    """Represents the
    `Notes <https://docs.everyaction.com/reference/notes>`__ service.
    """

    @ea_endpoint('notes/categories', 'get', result_array=True, result_factory=NoteCategory)
    def categories(self) -> List[NoteCategory]:
        """See `GET /notes/categories/{noteCategoryId}
        <https://docs.everyaction.com/reference/notes#notescategoriesnotecategoryid>`__.

        :returns: List of the resulting :class:`.NoteCategory` objects.
        """

    @ea_endpoint('notes/categories/{noteCategoryId}', 'get', result_factory=NoteCategory)
    def category(self, category_id: int, /) -> NoteCategory:
        """See `GET /notes/categories
        <https://docs.everyaction.com/reference/notes#notescategories>`__.

        :param category_id: The :code:`noteCategoryId` path parameter.
        :returns: The resulting :class:`.NoteCategory` object.
        """

    @ea_endpoint('notes/categoryTypes', 'get', result_array=True)
    def category_types(self) -> List[str]:
        """See `GET /notes/categoryTypes
        <https://docs.everyaction.com/reference/notes#notescategorytypes>`__.

        :returns: List of the names of the category types.
        """


class OnlineActionsForms(EAService):
    """Represents the
    `Online Action Forms <https://docs.everyaction.com/reference/online-actions-forms>`__ service.
    """

    @ea_endpoint('onlineActionsForms/{formTrackingId}', 'get', result_factory=OnlineActionsForm)
    def get(self, tracking_id: int, /):
        """See `GET /onlineActionsForms/{formTrackingId}
        <https://docs.everyaction.com/reference/online-actions-forms#onlineactionsformsformtrackingid>`__.

        :param tracking_id: The :code:`formTrackingId` path parameter.
        :returns: The resulting :class:`.OnlineActionForm` object.
        """

    @ea_endpoint('onlineActionsForms', 'get', paginated=True, result_factory=OnlineActionsForm)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[OnlineActionsForm]:
        """See `GET /onlineActionsForms
        <https://docs.everyaction.com/reference/online-actions-forms#onlineactionsforms>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.OnlineActionForm` objects.
        """


class Phones(EAService):
    """Represents the
    `Phones <https://docs.everyaction.com/reference/phones>`__ service.
    """

    @ea_endpoint('phones/isCellStatuses', 'get', paginated=True, result_factory=IsCellStatus)
    def is_cell_statuses(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[IsCellStatus]:
        """See `GET /phones/isCellStatuses
        <https://docs.everyaction.com/reference/phones#phonesiscellstatuses>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.IsCellStatus` objects.
        """


class PrintedLists(EAService):
    """Represents the
    `Printed Lists <https://docs.everyaction.com/reference/printed-lists>`__ service.
    """

    @ea_endpoint('printedLists/{printedListNumber}', 'get', result_factory=PrintedList)
    def get(self, list_number: str, /) -> PrintedList:
        """See `GET /printedLists/{printedListNumber}
        <https://docs.everyaction.com/reference/printed-lists#printedlistsprintedlistnumber>`__.

        :param list_number: The :code:`printedListNumber` path parameter.
        :returns: The resulting :class:`.PrintedList` object.
        """

    @ea_endpoint(
        'printedLists',
        'get',
        query_arg_keys={'createdBy', 'folderName', 'generatedAfter', 'generatedBefore', 'turfName'},
        result_factory=PrintedList
    )
    def list(self, **kwargs: EAValue) -> List[PrintedList]:
        """See `GET /printedLists
        <https://docs.everyaction.com/reference/printed-lists#printedlists>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.PrintedList` objects.
        """


class Relationships(EAService):
    """Represents the
    `Relationships <https://docs.everyaction.com/reference/relationships>`__ service.
    """

    @ea_endpoint('relationships', 'get', paginated=True, result_factory=Relationship)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Relationship]:
        """See `GET /relationships
        <https://docs.everyaction.com/reference/relationships#relationships>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Relationship` objects.
        """


class ReportedDemographics(EAService):
    """Represents the
    `Reported Demographics <https://docs.everyaction.com/reference/reported-demographics>`__ service.
    """

    @ea_endpoint('reportedEthnicities', 'get', paginated=True, result_factory=ReportedEthnicity)
    def ethnicities(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ReportedEthnicity]:
        """See `GET /reportedEthnicities
        <https://docs.everyaction.com/reference/reported-ethnicities#reportedethnicities>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ReportedEthnicity` objects.
        """

    @ea_endpoint('reportedGenders', 'get', paginated=True, result_factory=ReportedGender)
    def genders(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ReportedGender]:
        """See `GET /reportedGenders
        <https://docs.everyaction.com/reference/reported-genders#reportedgenders>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ReportedGender` objects.
        """

    @ea_endpoint('reportedLanguagePreferences', 'get', paginated=True, result_factory=ReportedLanguagePreference)
    def language_preferences(
        self,
        *,
        limit: Optional[int] = None,
        **kwargs: EAValue
    ) -> List[ReportedLanguagePreference]:
        """See `GET /reportedLanguagePreferences
        <https://docs.everyaction.com/reference/reported-language-preferences#reportedlanguagepreferences>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ReportedLanguagePreference` objects.
        """

    @ea_endpoint('pronouns', 'get', paginated=True, result_factory=PreferredPronoun)
    def pronouns(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[PreferredPronoun]:
        """See `GET /pronouns
        <https://docs.everyaction.com/reference/pronouns#pronouns>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.PreferredPronoun` objects.
        """

    @ea_endpoint('reportedRaces', 'get', paginated=True, result_factory=ReportedRace)
    def races(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ReportedRace]:
        """See `GET /reportedRaces
        <https://docs.everyaction.com/reference/reported-races#reportedraces>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ReportedRace` objects.
        """

    @ea_endpoint('reportedSexualOrientations', 'get', paginated=True, result_factory=ReportedSexualOrientation)
    def sexual_orientations(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ReportedSexualOrientation]:
        """See `GET /reportedSexualOrientations
        <https://docs.everyaction.com/reference/reported-sexual-orientations#reportedsexualorientations>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ReportedSexualOrientation` objects.
        """


class SavedLists(EAService):
    """Represents the
    `Saved Lists <https://docs.everyaction.com/reference/saved-lists>`__ service.
    """

    @ea_endpoint('savedLists/{savedListId}', 'get', result_factory=SavedList)
    def get(self, list_id: int, /) -> SavedList:
        """See `GET /savedLists/{savedListId}
        <https://docs.everyaction.com/reference/saved-lists#savedlistssavedlistid>`__.

        :param list_id: The :code:`savedListId` path parameter.
        :returns: The resulting :class:`.SavedList` object.
        """

    @ea_endpoint(
        'savedLists',
        'get',
        query_arg_keys={'folderId', 'maxDoorCount', 'maxPeopleCount'},
        paginated=True,
        result_factory=SavedList
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[SavedList]:
        """See `GET /savedLists
        <https://docs.everyaction.com/reference/saved-lists#savedlists>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.SavedList` objects.
        """

    @ea_endpoint('savedLists/smsSync', 'post', prop_keys={'syncPeriodEnd', 'syncPeriodStart'}, result_factory=SavedList)
    def sms_sync(self, **kwargs: EAValue) -> SavedList:
        """See `POST /savedLists/smsSync
        <https://docs.everyaction.com/reference/saved-lists#smssync>`__>`__.

        """


class ScheduleTypes(EAService):
    """Represents the
    `Schedule Types <https://docs.everyaction.com/reference/schedule-types>`__ service.
    """

    @ea_endpoint('scheduleTypes', 'post', data_type=ScheduleType, result_factory=ScheduleType)
    def create(self, **kwargs: EAValue) -> ScheduleType:
        """See `POST /scheduleTypes
        <https://docs.everyaction.com/reference/schedule-types#scheduletypes-1>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.ScheduleType` is
            appropriate to unpack here.
        :returns: The created :class:`.ScheduleType` object.
        """

    @ea_endpoint('scheduleTypes/{schedule_type_id}', 'get', result_factory=ScheduleType)
    def get(self, schedule_type_id: int, /) -> ScheduleType:
        """See `GET /scheduleTypes/{scheduleTypeId}
        <https://docs.everyaction.com/reference/schedule-types#scheduletypesscheduletypeid>`__.

        :param schedule_type_id: The :code:`scheduleTypeId` path parameter.
        :returns: The resulting :class:`.ScheduleType` object.
        """

    @ea_endpoint('scheduleTypes', 'get', paginated=True, result_factory=ScheduleType)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ScheduleType]:
        """See `GET /scheduleTypes
        <https://docs.everyaction.com/reference/schedule-types#scheduletypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ScheduleType` objects.
        """


class ScoreUpdates(EAService):
    """Represents the
    `Score Updates <https://docs.everyaction.com/reference/score-updates>`__ service.
    """

    @ea_endpoint('scoreUpdates/{scoreUpdateId}', 'get', result_factory=ScoreUpdate)
    def get(self, update_id: int, /) -> ScoreUpdate:
        """See `GET /scoreUpdates/{scoreUpdateId}
        <https://docs.everyaction.com/reference/score-updates#scoreupdatesscoreupdateid>`__.

        :param update_id: The :code:`scoreUpdateId` path parameter.
        :returns: The resulting :class:`.ScoreUpdate` object.
        """

    @ea_endpoint(
        'scoreUpdates',
        'get',
        query_arg_keys={'createdAfter', 'createdBefore', 'scoreId'},
        paginated=True,
        result_factory=ScoreUpdate
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ScoreUpdate]:
        """See `GET /scoreUpdates
        <https://docs.everyaction.com/reference/score-updates#scoreupdates>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ScoreUpdate` objects.
        """

    @ea_endpoint('scoreUpdates/{scoreUpdateId}', 'patch', prop_keys={'loadStatus'}, has_result=False)
    def patch(self, update_id: int, /, **kwargs: EAValue) -> None:
        """See `PATCH /scoreUpdates/{scoreUpdateId}
        <https://docs.everyaction.com/reference/score-updates#scoreupdatesscoreupdateid-1>`__.

        :param update_id: The :code:`scoreUpdateId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """


class Scores(EAService):
    """Represents the
    `Scores <https://docs.everyaction.com/reference/scores>`__ service.
    """

    @ea_endpoint('scores/{scoreId}', 'get', result_factory=Score)
    def get(self, score_id: int, /) -> Score:
        """See `GET /scores/{scoreId}
        <https://docs.everyaction.com/reference/scores#scoresscoreid>`__.

        :param score_id: The :code:`scoreId` path parameter.
        :returns: The resulting :class:`.Score` object.
        """

    @ea_endpoint('scores', 'get', paginated=True, result_factory=Score)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Score]:
        """See `GET /scores
        <https://docs.everyaction.com/reference/scores#scores>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Score` objects.
        """


class ShiftTypes(EAService):
    """Represents the
    `Shift Types <https://docs.everyaction.com/reference/shift-types>`__ service.
    """

    @ea_endpoint('shiftTypes', 'post', data_type=ShiftType, result_factory=ShiftType)
    def create(self, **kwargs: EAValue) -> ShiftType:
        """See `POST /shiftTypes
        <https://docs.everyaction.com/reference/shift-types#shifttypes-1>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.ShiftType` is
            appropriate to unpack here.
        :returns: The created :class:`.ShiftType` object.
        """

    @ea_endpoint('shiftTypes/{shift_type_id}', 'get', result_factory=ShiftType)
    def get(self, shift_type_id: int, /) -> ShiftType:
        """See `GET /shiftTypes/{shiftTypeId}
        <https://docs.everyaction.com/reference/shift-types#shifttypesshifttypeid>`__.

        :param shift_type_id: The :code:`shiftTypeId` path parameter.
        :returns: The resulting :class:`.ShiftType` object.
        """

    @ea_endpoint('shiftTypes', 'get', paginated=True, result_factory=ShiftType)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ShiftType]:
        """See `GET /shiftTypes
        <https://docs.everyaction.com/reference/shift-types#shifttypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ShiftType` objects.
        """


class Signups(EAService):
    """Represents the
    `Signups <https://docs.everyaction.com/reference/signups>`__ service.
    """

    @ea_endpoint('signups', 'post', data_type=Signup, result_factory=Signup)
    def create_or_update(self, **kwargs: EAValue) -> Signup:
        """See `POST /signups
        <https://docs.everyaction.com/reference/signups#signups-2>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Signup` is
            appropriate to unpack here.
        :returns: The created :class:`.Signup` object.
        """

    @ea_endpoint('signups/{eventSignupId}', 'delete', has_result=False)
    def delete(self, signup_id: int, /) -> None:
        """See `DELETE /signups/{eventSignupId}
        <https://docs.everyaction.com/reference/signups#signupseventsignupid-2>`__.

        :param signup_id: The :code:`eventSignupId` path parameter.
        """

    @ea_endpoint('signups/{eventSignupId}', 'get', result_factory=Signup)
    def get(self, signup_id: int, /) -> Signup:
        """See `GET /signups/{eventSignupId}
        <https://docs.everyaction.com/reference/signups#signupseventsignupid-1>`__.

        :param signup_id: The :code:`eventSignupId` path parameter.
        :returns: The resulting :class:`.Signup` object.
        """

    @ea_endpoint('signups', 'get', query_arg_keys={'eventId', 'vanId'}, paginated=True, result_factory=Signup)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Signup]:
        """See `GET /signups
        <https://docs.everyaction.com/reference/signups#signups-1>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Signup` objects.
        """

    @ea_endpoint(
        'signups/statuses',
        'get',
        query_arg_keys={'eventId', 'eventTypeId'},
        result_array=True,
        result_factory=Status
    )
    def statuses(self, **kwargs: EAValue) -> List[Status]:
        """See `GET /signups/statuses
        <https://docs.everyaction.com/reference/signups#signupsstatuses>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.Status` objects.
        """

    @ea_endpoint('signups/{eventSignupId}', 'put', data_type=Signup, has_result=False)
    def update(self, signup_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /signups/{eventSignupId}
        <https://docs.everyaction.com/reference/signups#signupseventsignupid>`__.

        :param signup_id: The :code:`eventSignupId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Signup` is
            appropriate to unpack here.
        """


class Stories(EAService):
    """Represents the
    `Stories <https://docs.everyaction.com/reference/stories>`__ service.
    """

    @ea_endpoint('stories', 'post', data_type=Story, result_factory=Story)
    def create(self, **kwargs: EAValue) -> Story:
        """See `POST /stories
        <https://docs.everyaction.com/reference/stories#stories>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Story` is
            appropriate to unpack here.
        :returns: The resulting :class:`.Story` object.
        """

    @ea_endpoint('stories/{storyId}', 'get', result_factory=Story)
    def get(self, story_id: int, /) -> Story:
        """See `GET /stories/{storyId}
        <https://docs.everyaction.com/reference/stories#storiesstoryid>`__.

        :param story_id: The :code:`storyId` path parameter.
        :returns: The resulting :class:`.Story` object.
        """


class SupporterGroups(EAService):
    """Represents the
    `Supporter Groups <https://docs.everyaction.com/reference/supporter-groups>`__ service.
    """

    @ea_endpoint('supporterGroups/{supporterGroupId}/people/{vanId}', 'put', has_result=False)
    def add_person(self, group_id: int, van_id: int, /) -> None:
        """See `PUT /supporterGroups/{supporterGroupId}/people/{vanId}
        <https://docs.everyaction.com/reference/supporter-groups#supportergroupssupportergroupidpeoplevanid>`__.

        :param group_id: The :code:`groupId` path parameter.
        :param van_id: The :code:`vanId` path parameter.
        """

    @ea_endpoint('supporterGroups', 'post', data_type=SupporterGroup, result_factory=SupporterGroup)
    def create(self, **kwargs: EAValue) -> SupporterGroup:
        """See `POST /supporterGroups
        <https://docs.everyaction.com/reference/supporter-groups#supportergroups-1>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.SupporterGroup` is
            appropriate to unpack here.
        :returns: The created :class:`.SupporterGroup` object.
        """

    @ea_endpoint('supporterGroups/{supporterGroupId}', 'delete', has_result=False)
    def delete(self, group_id: int, /) -> None:
        """See `DELETE /supporterGroups/{supporterGroupId}
        <https://docs.everyaction.com/reference/supporter-groups#supportergroupssupportergroupid-1>`__.

        :param group_id: The :code:`supporterGroupId` path parameter.
        """

    @ea_endpoint('supporterGroups/{supporterGroupId}', 'get', result_factory=SupporterGroup)
    def get(self, group_id: int, /) -> SupporterGroup:
        """See `GET /supporterGroups/{supporterGroupId}
        <https://docs.everyaction.com/reference/supporter-groups#supportergroupssupportergroupid-1>`__.

        :param group_id: The :code:`supporterGroupId` path parameter.
        :returns: The resulting :class:`.SupporterGroup` object.
        """

    @ea_endpoint('supporterGroups', 'get', paginated=True, result_factory=SupporterGroup)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[SupporterGroup]:
        """See `GET /supporterGroups
        <https://docs.everyaction.com/reference/supporter-groups#supportergroups>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.SupporterGroup` objects.
        """

    @ea_endpoint('supporterGroups/{supporterGroupId}/people/{vanId}', 'delete', has_result=False)
    def remove_person(self, group_id: int, van_id: int, /) -> None:
        """See `DELETE /supporterGroups/{supporterGroupId}/people/{vanId}
        <https://docs.everyaction.com/reference/supporter-groups#supportergroupssupportergroupidpeoplevanid>`__.

        :param group_id: The :code:`groupId` path parameter.
        :param van_id: The :code:`vanId` path parameter.
        """


class SurveyQuestions(EAService):
    """Represents the
    `Survey Questions <https://docs.everyaction.com/reference/survey-questions>`__ service.
    """

    @ea_endpoint('surveyQuestions/{surveyQuestionId}', 'get', result_factory=SurveyQuestion)
    def get(self, question_id: Union[int, str], /) -> SurveyQuestion:
        """See `GET /surveyQuestions/{surveyQuestionId}
        <https://docs.everyaction.com/reference/survey-questions#surveyquestionssurveyquestionid>`__.

        :param question_id: The :code:`surveyQuestionId` path parameter.
        :returns: The resulting :class:`.SurveyQuestion` object.
        """

    @ea_endpoint(
        'surveyQuestions',
        'get',
        query_arg_keys={'cycle', 'name', 'question', 'statuses', 'type'},
        paginated=True,
        result_factory=SurveyQuestion
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[SurveyQuestion]:
        """See `GET /surveyQuestions
        <https://docs.everyaction.com/reference/survey-questions#surveyquestions>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.SurveyQuestion` objects.
        """


class TargetExportJobs(EAService):
    """Represents the
    `Target Export Jobs <https://docs.everyaction.com/reference/target-export-jobs>`__ service.
    """

    @ea_endpoint('targetExportJobs', 'post', data_type=TargetExportJob, result_factory=TargetExportJob)
    def create(self, **kwargs: EAValue) -> TargetExportJob:
        """See `POST /targetExportJobs
        <https://docs.everyaction.com/reference/target-export-jobs#targetexportjobs>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.TargetExportJob` is
            appropriate to unpack here.
        :returns: The created :class:`.TargetExportJob` object.
        """

    @ea_endpoint('targetExportJobs/{exportJobId}', 'get', result_factory=TargetExportJob)
    def get(self, job_id: int, /) -> TargetExportJob:
        """See `GET /targetExportJobs/{exportJobId}
        <https://docs.everyaction.com/reference/target-export-jobs#targetexportjobsexportjobid>`__.

        :param job_id: The :code:`exportJobId` path parameter.
        :returns: The resulting :class:`.TargetExportJob` object.
        """


class Targets(EAService):
    """Represents the
    `Targets <https://docs.everyaction.com/reference/targets>`__ service.
    """

    @ea_endpoint('targets/{targetId}', 'get', result_factory=Target)
    def get(self, target_id: int, /) -> Target:
        """See `GET /targets/{targetId}
        <https://docs.everyaction.com/reference/targets#targetstargetid>`__.

        :param target_id: The :code:`targetId` path parameter.
        :returns: The resulting :class:`.Target` object.
        """

    @ea_endpoint('targets', 'get', query_arg_keys={'status', 'type', '$expand'}, paginated=True, result_factory=Target)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Target]:
        """See `GET /targets
        <https://docs.everyaction.com/reference/targets#targets>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Target` objects.
        """


class Users(EAService):
    """Represents the
    `Users <https://docs.everyaction.com/reference/users>`__ service.
    """

    @ea_endpoint(
        'users/{userId}/districtFieldValues',
        'post',
        props={'districtFieldValues': EAProperty('field_values', 'values', singular_alias='value')},
        result_key='districtFieldValues'
    )
    def add_district_fields(self, user_id: int, /, **kwargs: EAValue) -> List[str]:
        """See `POST /users/{userId}/districtFieldValues
        <https://docs.everyaction.com/reference/users#usersuseriddistrictfieldvalues-1>`__.

        :param user_id: The :code:`userId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The full set of names of the user's district field values.
        """

    @ea_endpoint('users/{userId}/districtFieldValues', 'get', result_key='districtFieldValues')
    def district_fields(self, user_id: int, /) -> List[str]:
        """See `GET /users/{userId}/districtFieldValues
        <https://docs.everyaction.com/reference/users#usersuseriddistrictfieldvalues>`__.

        :param user_id: The :code:`userId` path parameter.
        :returns: The names of the resulting district field values.
        """

    @ea_endpoint(
        'users/{userId}/districtFieldValues',
        'put',
        props={'districtFieldValues': EAProperty('field_values', 'values', singular_alias='value')},
        result_key='districtFieldValues'
    )
    def set_district_fields(self, user_id: int, /, **kwargs: EAValue) -> List[str]:
        """See `PUT /users/{userId}/districtFieldValues
        <https://docs.everyaction.com/reference/users#usersuseriddistrictfieldvalues-2>`__.

        :param user_id: The :code:`userId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The full set of names of the user's district field values.
        """


class VoterRegistrationBatches(EAService):
    """Represents the
    `Voter Registration Batches <https://docs.everyaction.com/reference/voter-registration-batches>`__ service.
    """

    @ea_endpoint(
        'voterRegistrationBatches/{batchId}/people',
        'post',
        result_array=True,
        result_factory=AddRegistrantsResponse
    )
    def add_registrants(self, batch_id: int, /, *, data: List[Registrant]) -> List[AddRegistrantsResponse]:
        """See `POST /voterRegistrationBatches/{batchId}/people
        <https://docs.everyaction.com/reference/voter-registration-batches#voterregistrationbatchesbatchidpeople>`__.

        :param batch_id: The :code:`batchId` path parameter.
        :param data: List of the :class:`.Registrant` objects to add.
        :returns: The resulting :class:`.AddRegistrantsResponse` objects.
        """

    @ea_endpoint(
        'voterRegistrationBatches',
        'post',
        data_type=VoterRegistrationBatch,
        result_factory=VoterRegistrationBatch
    )
    def create(self, **kwargs: EAValue) -> VoterRegistrationBatch:
        """See `POST /voterRegistrationBatches
        <https://docs.everyaction.com/reference/voter-registration-batches#voterregistrationbatches-1>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.VoterRegistrationBatch`
            is appropriate to unpack here.
        :returns: The created :class:`.VoterRegistrationBatch`.
        """

    @ea_endpoint('voterRegistrationBatches/registrationForms', 'get', paginated=True, result_factory=RegistrationForm)
    def forms(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[RegistrationForm]:
        """See `GET /voterRegistrationBatches/registrationForms
        <https://docs.everyaction.com/reference/voter-registration-batches#voterregistrationbatchesregistrationforms>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.RegistrationForm` objects.
        """

    @ea_endpoint(
        'voterRegistrationBatches',
        'get',
        query_arg_keys={
            'createdAfter',
            'createdBefore',
            'onlyMyBatches',
            'personType',
            'programType',
            'stateCode',
            'status',
            '$orderby'
        },
        paginated=True,
        result_factory=VoterRegistrationBatch
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[VoterRegistrationBatch]:
        """See `GET /voterRegistrationBatches
        <https://docs.everyaction.com/reference/voter-registration-batches#voterregistrationbatches>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.VoterRegistrationBatch` objects.
        """

    @ea_endpoint('voterRegistrationBatches/programTypes', 'get', paginated=True, result_factory=ProgramType)
    def programs(self, limit: Optional[int] = None, **kwargs: EAValue) -> List[ProgramType]:
        """See `GET /voterRegistrationBatches/programTypes
        <https://docs.everyaction.com/reference/voter-registration-batches#voterregistrationbatchesprogramtypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ProgramType` objects.
        """

    @ea_endpoint(
        'voterRegistrationBatches/states/{state}/supportedFields',
        'get',
        paginated=True,
        result_factory=SupportField
    )
    def support_fields(
        self,
        state: str,
        /,
        *,
        limit: Optional[int] = None,
        **kwargs: EAValue
    ) -> List[SupportField]:
        """See `GET /voterRegistrationBatches/states/{state}/supportedFields
        <https://docs.everyaction.com/reference/voter-registration-batches#voterregistrationbatchesstatesstatesupportedfields>`__.

        :param limit: Maximum number of records to get for this request.
        :param state: The :code:`state` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.SupportField` objects.
        """

    @ea_endpoint('voterRegistrationBatches/{batchId}', 'patch', prop_keys={'status'}, has_result=False)
    def update_status(self, batch_id: int, /, **kwargs: EAValue) -> None:
        """See `PATCH /voterRegistrationBatches/{batchId}
        <https://docs.everyaction.com/reference/voter-registration-batches#voterregistrationbatchesbatchid>`__.

        :param batch_id: The :code:`batchId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """


class Worksites(EAService):
    """Represents the
    `Worksites <https://docs.everyaction.com/reference/worksites>`__ service.
    """

    @ea_endpoint('worksites/{worksite_id}/workAreas', 'post', data_type=WorkArea, result_factory=WorkArea)
    def create_work_area(self, **kwargs: EAValue) -> WorkArea:
        """See `POST /worksites/{worksiteId}/workAreas
        <https://docs.everyaction.com/reference/worksites#worksitesworksiteidworkareas>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.WorkArea` is appropriate
            to unpack here.
        :returns: The created :class:`.WorkArea`.
        """

    @ea_endpoint('worksites/{worksite_id}', 'get', result_factory=Worksite)
    def get(self, worksite_id: int) -> Worksite:
        """See `GET /worksites/{worksiteId}
        <https://docs.everyaction.com/reference/worksites#worksitesworksiteid>`__.

        :param worksite_id: The :code:`worksiteId` path parameter.
        :returns: The resulting :class:`.Worksite` object.
        """

    @ea_endpoint(
        'worksites',
        'get',
        query_arg_keys={'employerId', 'isMyOrganization', '$expand'},
        paginated=True,
        result_factory=Worksite
    )
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Worksite]:
        """See `GET /worksites
        <https://docs.everyaction.com/reference/worksites#worksites>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: Applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Worksite` objects.
        """
