"""
This module contains the objects that have methods corresponding to collections of API calls as they are grouped in the
`EveryAction 8 VAN API docs <https://developers.everyaction.com/van-api>`__
"""

from typing import Dict, Iterable, List, Optional, Union

from everyaction.core import ea_endpoint, EAMap, EAProperty, EAService, EAValue
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
    'OnlineActionForms',
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
    `People <https://developers.everyaction.com/van-api#people>`__ service.
    """

    @ea_endpoint('people/{vanId}/activistCodes', 'get', paginated=True, result_factory=ActivistCodeData)
    def activist_codes(
        self, van_id: int, /, *, limit: Optional[int] = None, **kwargs: EAValue
    ) -> List[ActivistCodeData]:
        """See `GET /people/{vanId}/activistCodes
        <https://developers.everyaction.com/van-api#people-get-people--vanid--activistcodes>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ActivistCodeData` objects.
        """

    @ea_endpoint('people/{vanId}/canvassResponses', 'post', data_type=CanvassResponse, has_result=False)
    def add_canvass_responses(self, van_id: int, /, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/canvassResponses
        <https://developers.everyaction.com/van-api#people-post-people--vanid--canvassresponses>`__.

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
        <https://developers.everyaction.com/van-api#people-post-people--personidtype---personid--canvassresponses>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.CanvassResponse` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{vanId}/codes', 'post', data_type=Code, has_result=False)
    def add_code(self, van_id: int, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/codes
        <https://developers.everyaction.com/van-api#people-post-people--vanid--codes>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Code` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{personIdType}:{personId}/codes', 'post', data_type=Code, has_result=False)
    def add_code_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> None:
        """See `POST /people/{personIdType}:{personId}/codes
        <https://developers.everyaction.com/van-api#people-post-people--personidtype---personid--codes>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Code` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{vanId}/myActivistFlags', 'put', has_result=False)
    def add_my_activist_flag(self, van_id: int, /) -> None:
        """See `PUT /people/{vanId}/myActivistFlags
        <https://developers.everyaction.com/van-api#people-put-people--vanid--myactivistflags>`__.

        :param van_id: The :code:`vanId` path parameter.
        """

    @ea_endpoint('people/{vanId}/notes', 'post', data_type=Note, has_result=False)
    def add_notes(self, van_id: int, /, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/notes
        <https://developers.everyaction.com/van-api#people-post-people--vanid--notes>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Note` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{personIdType}:{personId}/notes', 'post', data_type=Note, has_result=False)
    def add_notes_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> None:
        """See `POST /people/{personIdType}:{personId}/notes
        <https://developers.everyaction.com/van-api#people-post-people--personidtype---personid--notes>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Note` is
            appropriate to unpack here.
        """

    @ea_endpoint('people/{vanId}/relationships', 'post', prop_keys={'relationshipId', 'vanId'}, has_result=False)
    def add_relationship(self, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/relationships
        <https://developers.everyaction.com/van-api#people-post-people--vanid--relationships>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        """

    @ea_endpoint('people/find', 'post', data_type=Person, result_factory=Person._find_factory)
    def find(self, **kwargs: EAValue) -> Optional[Person]:
        """See `POST /people/find
        <https://developers.everyaction.com/van-api#people-post-people-find>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Person` is
            appropriate to unpack here.
        :returns: The found :class:`.Person` object, or :code:`None` if no person could be found.
        """

    @ea_endpoint('people/findOrCreate', 'post', data_type=Person, result_factory=Person._find_factory)
    def find_or_create(self, **kwargs: EAValue) -> Person:
        """See `POST /people/findOrCreate
        <https://developers.everyaction.com/van-api#people-post-people-findorcreate>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Person` is
            appropriate to unpack here.
        :returns: The found or else created :class:`.Person` object.
        """

    @ea_endpoint('people/{vanId}', 'get', query_arg_keys={'$expand'}, result_factory=Person)
    def get(self, van_id: int, /, **kwargs: EAValue) -> Person:
        """See `GET /people/{vanId}
        <https://developers.everyaction.com/van-api#people-get-people--vanid>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.Person` object.
        """

    @ea_endpoint('people/{personIdType}:{personId}', 'get', query_arg_keys={'$expand'}, result_factory=Person)
    def get_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> Person:
        """See `GET /people/{personIdType}:{personId}
        <https://developers.everyaction.com/van-api#people-get-people--personidtype---personid>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.Person` object.
        """

    @ea_endpoint('people/{vanId}/membership', 'get', result_factory=Membership)
    def membership(self, van_id: int, /) -> Membership:
        """See `GET /people/{vanId}/membership
        <https://developers.everyaction.com/van-api#people-get-people--vanid--membership>`__.

        :param van_id: The :code:`vanId` path parameter.
        :returns: The resulting :class:`.Membership` object.
        """

    @ea_endpoint('people/{vanId}/notes', 'get', paginated=True, max_top=50, result_factory=Note)
    def notes(self, van_id: int, /, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Note]:
        """See `GET /people/{vanId}/notes
        <https://developers.everyaction.com/van-api#people-get-people--vanid--notes>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Note` objects.
        """

    @ea_endpoint('people/{vanId}/codes/{codeId}', 'delete', has_result=False)
    def remove_code(self, van_id: int, code_id: int, /) -> None:
        """See `DELETE /people/{vanId}/codes/{codeId}
        <https://developers.everyaction.com/van-api#people-delete-people--vanid--codes--codeid>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param code_id: The :code:`code_id` path parameter.
        """

    @ea_endpoint('people/{personIdType}:{personId}/codes/{codeId}', 'delete', has_result=False)
    def remove_code_(self, person_id_type: str, person_id: str, code_id: int, /) -> None:
        """See `DELETE /people/{personIdType}:{personId}/codes/{codeId}
        <https://developers.everyaction.com/van-api#people-delete-people--personidtype---personid--codes--codeid>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param code_id: The :code:`codeId` path parameter.
        """

    @ea_endpoint('people/{vanId}/myActivistFlags', 'delete', has_result=False)
    def remove_my_activist_flag(self, van_id: int, /) -> None:
        """See `DELETE /people/{vanId}myActivistFlags
        <https://developers.everyaction.com/van-api#people-delete-people--vanid--myactivistflags>`__.

        :param van_id: The :code:`vanId` path parameter.
        """

    @ea_endpoint('people/{vanId}/disclosureFieldValues', 'post', prop_keys={'disclosureFieldValues'}, has_result=False)
    def set_disclosures_fields(self, van_id: int, /, **kwargs: EAValue) -> None:
        """See `POST /people/{vanId}/disclosureFieldValues
        <https://developers.everyaction.com/van-api#people-post-people--vanid--disclosurefieldvalues>`__.

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
        <https://developers.everyaction.com/van-api#people-post-people--personidtype---personid--disclosurefieldvalues>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """

    @ea_endpoint('people/{vanId}', 'post', data_type=Person, result_factory=Person._find_factory)
    def update(self, van_id: int, /, **kwargs: EAValue) -> Optional[Person]:
        """See `POST /people/{vanId}
        <https://developers.everyaction.com/van-api#people-post-people--vanid>`__.

        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Person` is
            appropriate to unpack here.
        :returns: (van id, status) of the updated person.
        """

    @ea_endpoint('people/{personIdType}:{personId}', 'post', data_type=Person, result_factory=Person._find_factory)
    def update_(self, person_id_type: str, person_id: str, /, **kwargs: EAValue) -> Optional[Person]:
        """See `POST /people/{personIdType}:{personId}
        <https://developers.everyaction.com/van-api#people-post-people--personidtype---personid>`__.

        :param person_id_type: The :code:`personIdType` path parameter.
        :param person_id: The :code:`personId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Person` is
            appropriate to unpack here.
        :returns: (van id, status) of the resulting person.
        """

    @ea_endpoint('people/{vanId}/notes/{noteId}', 'put', data_type=Note, has_result=False)
    def update_note(self, van_id: int, note_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /people/{vanId}/notes/{noteId}
        <https://developers.everyaction.com/van-api#people-put-people--vanid--notes--noteid>`__.

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
        `POST /people/find <https://developers.everyaction.com/van-api#people-post-people-find>`__.
        Then, if a person was found, use their VAN ID to retrieve their stored :class:`.Person` record by invoking
        `GET /people/{vanId} <https://developers.everyaction.com/van-api#people-get-people--vanid>`__.

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
        `POST /people/find <https://developers.everyaction.com/van-api#people-post-people-find>`__ followed by
        `POST /people/{vanId} <https://developers.everyaction.com/van-api#people-post-people--vanid>`__ if the person
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
    `Activist Codes <https://developers.everyaction.com/van-api#activist-codes>`__ service.
    """

    @ea_endpoint('activistCodes/{activistCodeId}', 'get', result_factory=ActivistCode)
    def get(self, code_id: Union[int, str], /) -> ActivistCode:
        """See `GET /activistCodes/{activistCodeId}
        <https://developers.everyaction.com/van-api#activist-codes-get-activistcodes--activistcodeid>`__.

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
        <https://developers.everyaction.com/van-api#activist-codes-get-activistcodes>`__.

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
    `Ballots <https://developers.everyaction.com/van-api#ballots>`__ service.
    """

    @ea_endpoint('ballotRequestTypes/{ballotRequestTypeId}', 'get', result_factory=BallotRequestType)
    def request_type(self, type_id: str, /) -> BallotRequestType:
        """See `GET /ballotRequestTypes/{ballotRequestTypeId}
        <https://developers.everyaction.com/van-api#ballots-get-ballotrequesttypes--ballotrequesttypeid>`__.

        :returns: The resulting :class:`.BallotRequestType` object.
        """

    @ea_endpoint('ballotRequestTypes', 'get', paginated=True, result_factory=BallotRequestType)
    def request_types(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[BallotRequestType]:
        """See `GET /ballotRequestTypes
        <https://developers.everyaction.com/van-api#ballots-get-ballotrequesttypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.BallotRequestType` objects.
        """

    @ea_endpoint('ballotReturnStatuses/{ballotReturnStatusId}', 'get', result_factory=BallotReturnStatus)
    def return_status(self, status_id: int, /) -> BallotReturnStatus:
        """See `GET /ballotReturnStatuses/{ballotRequestTypeId}
        <https://developers.everyaction.com/van-api#ballots-get-ballotreturnstatuses--ballotreturnstatusid>`__.

        :param status_id: The :code:`ballotReturnStatusId` path parameter.
        :returns: The resulting :class:`.BallotReturnStatus` object.
        """

    @ea_endpoint('ballotReturnStatuses', 'get', paginated=True, result_factory=BallotReturnStatus)
    def return_statuses(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[BallotReturnStatus]:
        """See `GET /ballotReturnStatuses
        <https://developers.everyaction.com/van-api#ballots-get-ballotreturnstatuses>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.BallotReturnStatus` objects.
        """

    @ea_endpoint('ballotTypes/{ballotTypeId}', 'get', result_factory=BallotType)
    def type(self, type_id: int, /) -> BallotType:
        """See `GET /ballotTypes/{ballotTypeId}
        <https://developers.everyaction.com/van-api#ballots-get-ballottypes--ballottypeid>`__.

        :param type_id: The :code:`ballotTypeId` path parameter.
        :returns: The resulting :class:`.BallotType` object.
        """

    @ea_endpoint('ballotTypes', 'get', paginated=True, result_factory=BallotType)
    def types(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[BallotType]:
        """See `GET /ballotTypes
        <https://developers.everyaction.com/van-api#ballots-get-ballottypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.BallotType` objects.
        """


class BargainingUnits(EAService):
    """Represents the
    `BargainingUnits <https://developers.everyaction.com/van-api#bargaining-units>`__ service.
    """

    @ea_endpoint('bargainingUnits/{bargainingUnitId}', 'get', result_factory=BargainingUnit)
    def get(self, bargaining_unit: int, /) -> BargainingUnit:
        """See `GET /bargainingUnits/{bargainingUnitId}
        <https://developers.everyaction.com/van-api#bargaining-units-get-bargainingunits--bargainingunitid>`__.

        :param bargaining_unit: The :code:`bargainingUnitId` path parameter.
        :returns: The resulting :class:`.BargainingUnit` object.
        """

    @ea_endpoint('bargainingUnits', 'get', paginated=True, result_factory=BargainingUnit)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[BargainingUnit]:
        """See `GET /bargainingUnits
        <https://developers.everyaction.com/van-api#bargaining-units-get-bargainingunits>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.BargainingUnit` objects.
        """


class BulkImport(EAService):
    """Represents the
    `Bulk Import <https://developers.everyaction.com/van-api#bulk-import>`__ service.
    """

    @ea_endpoint('bulkImportJobs', 'post', data_type=BulkImportJob, result_factory=BulkImportJobData)
    def create(self, **kwargs: EAValue) -> BulkImportJobData:
        """See `POST /bulkImportJobs
        <https://developers.everyaction.com/van-api#bulk-import-post-bulkimportjobs>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.BulkImportJob` is
            appropriate to unpack here.
        :returns: The :class:`.BulkImportJobData` object for the created Bulk Import Job.
        """

    @ea_endpoint('bulkImportJobs/{jobId}', 'get', result_factory=BulkImportJobData)
    def get(self, job_id: int, /) -> BulkImportJobData:
        """See `GET /bulkImportJobs/{jobId}
        <https://developers.everyaction.com/van-api#bulk-import-get-bulkimportjobs--jobid>`__.

        :param job_id: The :code:`jobId` path parameter.
        :returns: The resulting :class:`.BulkImportJobData` object.
        """

    @ea_endpoint('bulkImportMappingTypes/{mappingTypeName}', 'get', result_factory=MappingTypeData)
    def mapping_type(self, name: str, /) -> MappingTypeData:
        """See `GET /bulkImportMappingTypes/{mappingTypeName}
        <https://developers.everyaction.com/van-api#bulk-import-get-bulkimportmappingtypes--mappingtypename>`__.

        :param name: The :code:`mappingTypeName` path parameter.
        :returns: The resulting :class:`.MappingTypeData` object.
        """

    @ea_endpoint('bulkImportMappingTypes', 'get', paginated=True, result_factory=MappingTypeData)
    def mapping_types(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[MappingTypeData]:
        """See `GET /bulkImportMappingTypes
        <https://developers.everyaction.com/van-api#bulk-import-get-bulkimportmappingtypes--mappingtypename---fieldname--values>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.MappingTypeData` objects.
        """

    @ea_endpoint('bulkImportJobs/resources', 'get')
    def resources(self) -> List[str]:
        """See `GET /bulkImportJobs/resources
        <https://developers.everyaction.com/van-api#bulk-import-get-bulkimportjobs-resources>`__.

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
        <https://developers.everyaction.com/van-api#bulk-import-get-bulkimportmappingtypes--mappingtypename---fieldname--values>`__.

        :param mapping_name: The :code:`mappingTypeName` path parameter.
        :param field_name: The :code:`fieldName` path parameter.
        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ValueMappingData` objects.
        """


class CanvassResponses(EAService):
    """Represents the
    `Canvass Responses <https://developers.everyaction.com/van-api#canvass-responses>`__ service.
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
        <https://developers.everyaction.com/van-api#canvass-responses-get-canvassresponses-contacttypes>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ContactType` objects.
        """

    @ea_endpoint('canvassResponses/inputTypes', 'get', result_array=True, result_factory=InputType)
    def input_types(self) -> List[InputType]:
        """See `GET /canvassResponses/inputTypes
        <https://developers.everyaction.com/van-api#canvass-responses-get-canvassresponses-inputtypes>`__.

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
        <https://developers.everyaction.com/van-api#canvass-responses-get-canvassresponses-resultcodes>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ResultCode` objects.
        """

    def find_result_code(self, name: str) -> ResultCode:
        """Finds the :class:`.ResultCode` which exactly matches the given name.

        :param name: Name of result code to find.
        :returns: The resulting :class:`.ResultCode`.
        :raises EAFindFailedException: If the result code could not be found.
        """
        lower = name.lower()
        codes = self.result_codes()
        for code in codes:
            if code.name.lower() == lower:
                return code
        raise EAFindFailedException(f'No such result code: "{name}"')


class ChangedEntities(EAService):
    """Represents the
    `Changed Entities <https://developers.everyaction.com/van-api#changed-entities>`__ service.
    """

    @ea_endpoint(
        'changedEntityExportJobs/changeTypes/{resourceType}',
        'get',
        result_array=True,
        result_factory=ChangeType
    )
    def change_types(self, resource: str, /) -> List[ChangeType]:
        """See `GET /changedEntityExportJobs/changeTypes/{resourceType}
        <https://developers.everyaction.com/van-api#changed-entities-get-changedentityexportjobs-changetypes--resourcetype>`__.

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
        <https://developers.everyaction.com/van-api#changed-entities-post-changedentityexportjobs>`__.

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
        <https://developers.everyaction.com/van-api#changed-entities-get-changedentityexportjobs-fields--resourcetype>`__.

        :param resource: The :code:`resourceType` path parameter.
        :returns: The resulting :class:`.ChangedEntityField` object.
        """

    @ea_endpoint('changedEntityExportJobs/{exportJobId}', 'get', result_factory=ChangedEntityExportJob)
    def get(self, job_id: int, /) -> ChangedEntityExportJob:
        """See `GET /changedEntityExportJobs/{exportJobId}
        <https://developers.everyaction.com/van-api#changed-entities-get-changedentityexportjobs--exportjobid>`__.

        :param job_id: The :code:`exportJobId` path parameter.
        :returns: The resulting :class:`.ChangedEntityExportJobData` object.
        """

    @ea_endpoint('changedEntityExportJobs/resources', 'get')
    def resources(self) -> List[str]:
        """See `GET /changedEntityExportJobs/resources
        <https://developers.everyaction.com/van-api#changed-entities-get-changedentityexportjobs-resources>`__.

        :returns: List of the resource type names.
        """


class Codes(EAService):
    """Represents the
    `Codes <https://developers.everyaction.com/van-api#codes>`__ service.
    """

    @ea_endpoint('codes', 'post', data_type=Code, result_factory=Code)
    def create(self, **kwargs: EAValue) -> Code:
        """See `POST /codes
        <https://developers.everyaction.com/van-api#codes-post-codes>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Code` is
            appropriate to unpack here.
        :returns: The created :class:`.Code` object.
        """

    @ea_endpoint('codes/batch', 'post', prop_keys={'codes'}, result_array=True, result_factory=CodeResult)
    def create_each(self, **kwargs: EAValue) -> List[CodeResult]:
        """See `POST /codes/batch
        <https://developers.everyaction.com/van-api#codes-post-codes-batch>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.CodeResult` objects for each code to be created.
        """

    @ea_endpoint('codes/{codeId}', 'delete', has_result=False)
    def delete(self, code_id: int, /) -> None:
        """See `DELETE /codes/{codeId}
        <https://developers.everyaction.com/van-api#codes-delete-codes--codeid>`__.

        :param code_id: The :code:`codeId` path parameter.
        """

    @ea_endpoint('codes', 'delete', result_array=True, result_factory=CodeResult)
    def delete_each(self, *, data: List[int]) -> List[CodeResult]:
        """See `DELETE /codes
        <https://developers.everyaction.com/van-api#codes-delete-codes>`__.

        :param data: The ids of the codes to delete.
        :returns: List of the resulting :class:`.CodeResult` objects for each code to be deleted.
        """

    @ea_endpoint('codes/{codeId}', 'get', result_factory=Code)
    def get(self, code_id: int, /) -> Code:
        """See `GET /codes/{codeId}
        <https://developers.everyaction.com/van-api#codes-get-codes--codeid>`__.

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
        <https://developers.everyaction.com/van-api#codes-get-codes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Code` objects.
        """

    @ea_endpoint('codes/supportedEntities', 'get', result_array=True)
    def supported_entities(self) -> List[str]:
        """See `GET /codes/supportedEntities
        <https://developers.everyaction.com/van-api#codes-get-codes-supportedentities>`__.

        :returns: List of the names of the supported entities.
        """

    @ea_endpoint('codeTypes', 'get', result_array=True)
    def types(self) -> List[str]:
        """See `GET /codeTypes
        <https://developers.everyaction.com/van-api#codes-get-codetypes>`__.

        :returns: List of the names of the code types.
        """

    @ea_endpoint('codes/{codeId}', 'put', data_type=Code, has_result=False)
    def update(self, code_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /codes/{codeId}
        <https://developers.everyaction.com/van-api#codes-put-codes--codeid>`__.

        :param code_id: The :code:`codeId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Code` is
            appropriate to unpack here.
        """

    @ea_endpoint('codes', 'put', prop_keys={'codes'}, result_array=True, result_factory=CodeResult)
    def update_each(self, **kwargs: EAValue) -> List[CodeResult]:
        """See `PUT /codes
        <https://developers.everyaction.com/van-api#codes-put-codes>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.CodeResult` objects for each code to be updated.
        """


class Commitments(EAService):
    """Represents the
    `Commitments <https://developers.everyaction.com/van-api#commitments>`__ service.
    """

    @ea_endpoint('commitments/{commitmentId}', 'patch', data_type=Commitment, result_factory=Commitment)
    def update(self, commitment_id: int, /, **kwargs: EAValue) -> Commitment:
        """See `PATCH /commitments/{commitmentId}
        <https://developers.everyaction.com/van-api#commitments-patch-commitments--commitmentid>`__.

        :param commitment_id: The :code:`commitmentId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Commitment` is
            appropriate to unpack here.
        :returns: The resulting :class:`.Commitment` object.
        """


class Contributions(EAService):
    """Represents the
    `Contributions <https://developers.everyaction.com/van-api#contributions>`__ service.
    """

    @ea_endpoint(
        'contributions/{contributionId}/adjustments',
        'post',
        data_type=Adjustment,
        result_factory=AdjustmentResponse
    )
    def adjust(self, contribution_id: int, /, **kwargs: EAValue) -> AdjustmentResponse:
        """See `POST /contributions/{contributionId}/adjustments
        <https://developers.everyaction.com/van-api#contributions-post-contributions--contributionid--adjustments>`__.

        :param contribution_id: The :code:`contributionId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Adjustment` is
            appropriate to unpack here.
        :returns: The resulting :class:`.AdjustmentResponse` object.
        """

    @ea_endpoint('contributions/attributionTypes', 'get', result_array=True)
    def attribution_types(self) -> List[str]:
        """See `GET /contributions/attributionTypes
        <https://developers.everyaction.com/van-api#contributions-get-contributions-attributiontypes>`__.

        :returns: List of the attribution types.
        """

    @ea_endpoint('contributions', 'post', data_type=Contribution, result_factory=Contribution)
    def create(self, **kwargs: EAValue) -> Contribution:
        """See `POST /contributions
        <https://developers.everyaction.com/van-api#contributions-post-contributions>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Contribution` is
            appropriate to unpack here.
        :returns: The created :class:`.Contribution` object.
        """

    @ea_endpoint('contributions/{contributionId}/attributions/{vanId}', 'put', data_type=Attribution, has_result=False)
    def create_or_update_attribution(self, contribution_id: int, van_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /contributions/{contributionId}/attributions/{vanId}
        <https://developers.everyaction.com/van-api#contributions-put-contributions--contributionid--attributions--vanid>`__.

        :param contribution_id: The :code:`contributionId` path parameter.
        :param van_id: The :code:`vanId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Attribution` is
            appropriate to unpack here.
        """

    @ea_endpoint('contributions/{contributionId}/attributions/{vanId}', 'delete', has_result=False)
    def delete_attribution(self, contribution_id: int, van_id: int, /) -> None:
        """See `DELETE /contributions/{contributionId}/attributions/{vanId}
        <https://developers.everyaction.com/van-api#contributions-delete-contributions--contributionid--attributions--vanid>`__.

        :param contribution_id: The :code:`contributionId` path parameter.
        :param van_id: The :code:`vanId` path parameter.
        """

    @ea_endpoint('contributions/{contributionId}', 'get', result_factory=Contribution)
    def get(self, contribution_id: int, /) -> Contribution:
        """See `GET /contributions/{contributionId}
        <https://developers.everyaction.com/van-api#contributions-get-contributions--contributionid>`__.

        :param contribution_id: The :code:`contributionId` path parameter.
        :returns: The resulting :class:`.Contribution` object.
        """

    @ea_endpoint('contributions/{alternateIdType}:{alternateId}', 'get', result_factory=Contribution)
    def get_(self, alternate_id_type: str, alternate_id: str, /) -> Contribution:
        """See `GET /contributions/{alternateIdType}:{alternateId}
        <https://developers.everyaction.com/van-api#contributions-get-contributions--alternateidtype---alternateid>`__.

        :param alternate_id_type: The :code:`alternateIdType` path parameter.
        :param alternate_id: The :code:`alternateId` path parameter.
        :returns: The resulting :class:`.Contribution` object.
        """


class CustomFields(EAService):
    """Represents the
    `Custom Fields <https://developers.everyaction.com/van-api#custom-fields>`__ service.
    """

    @ea_endpoint('customFields/{customFieldId}', 'get')
    def get(self, field_id: int, /) -> CustomField:
        """See `GET /customFields/customFieldId
        <https://developers.everyaction.com/van-api#custom-fields-get-customfields--customfieldid>`__.

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
        <https://developers.everyaction.com/van-api#custom-fields-get-customfields>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.CustomField` objects.
        """


class Departments(EAService):
    """Represents the
    `Departments <https://developers.everyaction.com/van-api#departments>`__ service.
    """

    @ea_endpoint('departments/{department_id}', 'get', result_factory=Department)
    def get(self, department_id: int, /) -> Department:
        """See `GET /departments/{departmentId}
        <https://developers.everyaction.com/van-api#departments-get-departments--departmentid>`__.

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
        <https://developers.everyaction.com/van-api#departments-get-departments>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The resulting :class:`.Department` objects.
        """


class Designations(EAService):
    """Represents the
    `Designations <https://developers.everyaction.com/van-api#designations>`__ service.
    """

    @ea_endpoint('designations', 'get', result_array_key='items', result_factory=Designation)
    def list(self) -> List[Designation]:
        """See `GET /designations
        <https://developers.everyaction.com/van-api#designations-get-designations>`__.

        :returns: List of the resulting :class:`.Designation` objects.
        """


class Disbursements(EAService):
    """Represents the
    `Disbursements <https://developers.everyaction.com/van-api#disbursements>`__ service.
    """

    @ea_endpoint('disbursements', 'post', data_type=Disbursement, has_result=False)
    def create_or_update(self, **kwargs: EAValue) -> None:
        """See `POST /disbursements
        <https://developers.everyaction.com/van-api#disbursements-post-disbursements>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Disbursement` is
            appropriate to unpack here.
        """

    @ea_endpoint('disbursements/{disbursementId}', 'get', result_factory=Disbursement)
    def get(self, disbursement_id: int, /) -> Disbursement:
        """See `GET /disbursements/{disbursementId}
        <https://developers.everyaction.com/van-api#disbursements-get-disbursements--disbursementid>`__.

        :param disbursement_id: The :code:`disbursementId` path parameter.
        :returns: The resulting :class:`.Disbursement` object.
        """


class DistrictFields(EAService):
    """Represents the
    `District Fields <https://developers.everyaction.com/van-api#districtfields>`__ service.
    """

    @ea_endpoint('districtFields/{districtFieldId}', 'get', result_factory=DistrictField)
    def get(self, field_id: int, /) -> DistrictField:
        """See `GET /districtFields/{districtFieldId}
        <https://developers.everyaction.com/van-api#district-fields-get-districtfields--districtfieldid>`__.

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
        <https://developers.everyaction.com/van-api#district-fields-get-districtfields>`__.

        :returns: List of the resulting :class:`.DistrictField` objects.
        """


class EmailMessages(EAService):
    """Represents the
    `Email <https://developers.everyaction.com/van-api#email>`__ service.
    """

    @ea_endpoint('email/messages/{emailId}', 'get', query_arg_keys={'$expand'}, result_factory=EmailMessage)
    def get(self, email_id: int, /, **kwargs: EAValue) -> EmailMessage:
        """See `GET /email/messages/{emailId}
        <https://developers.everyaction.com/van-api#email-get-email-message--emailid>`__.

        :param email_id: The :code:`emailId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.EmailMessage` object.
        """

    @ea_endpoint('email/messages', 'get', query_arg_keys={'$orderby'}, result_array=True, result_factory=EmailMessage)
    def list(self, **kwargs: EAValue) -> List[EmailMessage]:
        """See `GET /email/messages
        <https://developers.everyaction.com/van-api#email-get-email-messages>`__.

        :returns: List of the resulting :class:`.EmailMessage` objects.
        """


class Employers(EAService):
    """Represents the
    `Employers <https://developers.everyaction.com/van-api#employers>`__ service.
    """

    @ea_endpoint(
        'employers/{employer_id}/bargainingUnits/{bargaining_unit_id}',
        'post',
        result_factory=EmployerBargainingUnit
    )
    def add_bargaining_unit(self, employer_id: int, bargaining_unit_id: int, /) -> EmployerBargainingUnit:
        """See `POST /employers/{employerId}/bargainingUnits/{bargainingUnitId}
        <https://developers.everyaction.com/van-api#employers-post-employers--employerid--bargainingunits--bargainingunitid>`__.

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
        <https://developers.everyaction.com/van-api#employers-post-employers--employerid--bargainingunits--bargainingunitid--jobclasses--jobclassid>`__.

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
        <https://developers.everyaction.com/van-api#employers-post-employers--employerid--shifttypes--shifttypeid>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param shift_type_id: The :code:`shiftTypeId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.ShiftType` is
            appropriate to unpack here.
        :returns: The added :class:`.ShiftType` object.
        """

    @ea_endpoint('employers', 'post', data_type=Employer, result_factory=Employer)
    def create(self, **kwargs: EAValue) -> Employer:
        """See `POST /employers
        <https://developers.everyaction.com/van-api#employers-post-employers>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. An :class:`.Employer` is
            appropriate to unpack here.
        :returns: The created :class:`.Employer` object.
        """

    @ea_endpoint('employers/{employer_id}/departments', 'post', data_type=Department, result_factory=Department)
    def create_department(self, employer_id: int, /, **kwargs: EAValue) -> Department:
        """See `POST /employers/{employerId}/departments
        <https://developers.everyaction.com/van-api#employers-post-employers--employerid--departments>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Department` is
            appropriate to unpack here.
        :returns: The created :class:`.Department` object.
        """

    @ea_endpoint('employers/{employer_id}/worksites', 'post', data_type=Worksite, result_factory=Worksite)
    def create_worksite(self, employer_id: int, /, **kwargs: EAValue) -> Worksite:
        """See `POST /employers/{employer_id}/worksites
        <https://developers.everyaction.com/van-api#employers-post-employers--employerid--worksites>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Worksite` is
            appropriate to unpack here.
        :returns: The created :class:`.Worksite` object.
        """

    @ea_endpoint('employers/{employer_id}', 'get', query_arg_keys={'$expand'}, result_factory=Employer)
    def get(self, employer_id: int, /, **kwargs: EAValue) -> Employer:
        """See `GET /employers/{employerId}
        <https://developers.everyaction.com/van-api#employers-get-employers--employerid>`__.

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
        <https://developers.everyaction.com/van-api#employers-get-employers>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Employer` objects.
        """

    @ea_endpoint('employers/{employer_id}', 'patch', prop_keys={'isMyOrganization'}, result_factory=Employer)
    def update(self, employer_id: int, /, **kwargs: EAValue) -> Employer:
        """See `PATCH /employers/{employerId}
        <https://developers.everyaction.com/van-api#employers-patch-employers--employerid>`__.

        :param employer_id: The :code:`employerId` path parameter.
        :param kwargs: The applicable query and JSON arguments for the request.
        :returns: The updated :class:`.Employer` object.
        """


class EventTypes(EAService):
    """Represents the
    `Event Types <https://developers.everyaction.com/van-api#eventtypes>`__ service.
    """

    @ea_endpoint('events/types/{eventTypeId}', 'get', result_factory=EventType)
    def get(self, type_id: int, /) -> EventType:
        """See `GET /events/types/{eventTypeId}
        <https://developers.everyaction.com/van-api#event-types-get-events-types--eventtypeid>`__.

        :param type_id: The :code:`eventTypeId` path parameter.
        :returns: The resulting :class:`.EventType` object.
        """

    @ea_endpoint('events/types', 'get', result_array=True, result_factory=EventType)
    def list(self) -> List[EventType]:
        """See
        `GET /events/types <https://developers.everyaction.com/van-api#event-types-get-events-types>`__

        :returns: List of the resulting :class:`.EventType` objects.
        """


class Events(EAService):
    """Represents the
    `Events <https://developers.everyaction.com/van-api#events>`__ service.
    """

    @ea_endpoint('events/{eventId}/shifts', 'post', data_type=EventShift, result_factory=EventShift)
    def add_shift(self, event_id: int, /, **kwargs: EAValue) -> EventShift:
        """See `POST /events/{eventId}/shifts
        <https://developers.everyaction.com/van-api#events-post-events--eventid--shifts>`__.

        :param event_id: The :code:`eventId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.EventShift` is
            appropriate to unpack here.
        :returns: The resulting :class:`.EventShift` object.
        """

    @ea_endpoint('events', 'post', data_type=Event, result_factory=Event)
    def create(self, **kwargs: EAValue) -> Event:
        """See `POST /events
        <https://developers.everyaction.com/van-api#events-post-events>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Event` is appropriate to
            unpack here.
        :returns: The resulting :class:`.Event` object.
        """

    @ea_endpoint('events/{eventId}', 'delete')
    def delete(self, event_id: int, /) -> None:
        """See `DELETE /events/{eventId}
        <https://developers.everyaction.com/van-api#events-delete-events--eventid>`__.

        :param event_id: The :code:`eventId` path parameter.
        """

    @ea_endpoint('events/{eventId}', 'get', query_arg_keys={'$expand'}, result_factory=Event)
    def get(self, event_id: int, /, **kwargs: EAValue) -> Event:
        """See `GET /events/{eventId}
        <https://developers.everyaction.com/van-api#events-get-events--eventid>`__.

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
        <https://developers.everyaction.com/van-api#events-get-events>`__.

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
        <https://developers.everyaction.com/van-api#events-patch-events--eventid>`__. For
        convenience, the `eventId` parameter need only be specified as a positional/path parameter.

        :param event_id: The :code:`eventId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """

    @ea_endpoint('events/{eventId}', 'put', data_type=Event, has_result=False)
    def update(self, event_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /events/{eventId}
        <https://developers.everyaction.com/van-api#events-put-events--eventid>`__.

        :param event_id: The :code:`eventId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Event` is
            appropriate to unpack here.
        """


class ExportJobs(EAService):
    """Represents the
    `Export Jobs <https://developers.everyaction.com/van-api#exportjobs>`__ service.
    """

    @ea_endpoint('exportJobs', 'post', prop_keys={'savedListId', 'type', 'webhookUrl'}, result_factory=ExportJob)
    def create(self, **kwargs: EAValue) -> ExportJob:
        """See `POST /exportJobs
        <https://developers.everyaction.com/van-api#export-jobs-post-exportjobs>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.ExportJob` object.
        """

    @ea_endpoint('exportJobs/{exportJobId}', 'get', result_factory=ExportJob)
    def get(self, job_id: int, /) -> ExportJob:
        """See `GET /exportJobs/{exportJobId}
        <https://developers.everyaction.com/van-api#export-jobs-get-exportjobs--exportjobid>`__.

        :param job_id: The :code:`exportJobId` path parameter.
        :returns: The resulting :class:`.ExportJob` object.
        """

    @ea_endpoint('exportJobTypes', 'get', paginated=True, result_factory=ExportJobType)
    def types(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ExportJobType]:
        """See `GET /exportJobTypes
        <https://developers.everyaction.com/van-api#export-jobs-get-exportjobtypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ExportJobType` objects.
        """


class ExtendedSourceCodes(EAService):
    """Represents the
    `Extended Source Codes <https://developers.everyaction.com/van-api#extendedsourcecodes>`__ service.
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
        <https://developers.everyaction.com/van-api#extended-source-codes-get-codes-extendedsourcecodes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.ExtendedSourceCode` objects.
        """


class FileLoadingJobs(EAService):
    """Represents the
    `File Loading Jobs <https://developers.everyaction.com/van-api#fileloadingjobs>`__ service.
    """

    @ea_endpoint('fileLoadingJobs', 'post', data_type=FileLoadingJob, result_factory=FileLoadingJob)
    def create(self, **kwargs: EAValue) -> FileLoadingJob:
        """See `POST /fileLoadingJobs
        <https://developers.everyaction.com/van-api#file-loading-jobs-post-fileloadingjobs>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.FileLoadingJob` is
            appropriate to unpack here.
        :returns: The created :class:`.FileLoadingJob` object.
        """

    @ea_endpoint('fileLoadingJobs/{jobId}', 'get', result_factory=FileLoadingJob)
    def get(self, job_id: int, /) -> FileLoadingJob:
        """See `GET /fileLoadingJobs/{jobId}
        <https://developers.everyaction.com/van-api#file-loading-jobs-get-fileloadingjobs--jobid>`__.

        :param job_id: The :code:`jobId` path parameter.
        :returns: The resulting :class:`.FileLoadingJob` object.
        """


class FinancialBatches(EAService):
    """Represents the
    `Financial Batches <https://developers.everyaction.com/van-api#financialbatches>`__ service.
    """

    @ea_endpoint('financialBatches', 'post', data_type=FinancialBatch, result_factory=FinancialBatch)
    def create(self, **kwargs: EAValue) -> FinancialBatch:
        """See `POST /financialBatches
        <https://developers.everyaction.com/van-api#financial-batches-post-financialbatches>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.FinancialBatch` is
            appropriate to unpack here.
        :returns: The created :class:`.FinancialBatch` object.
        """

    @ea_endpoint('financialBatches/{financialBatchId}', 'get', result_factory=FinancialBatch)
    def get(self, batch_id: int, /) -> FinancialBatch:
        """See `GET /financialBatches/{financialBatchId}
        <https://developers.everyaction.com/van-api#financial-batches-get-financialbatches--financialbatchid>`__.

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
        <https://developers.everyaction.com/van-api#financial-batches-get-financialbatches>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.FinancialBatch` objects.
        """


class Folders(EAService):
    """Represents the
    `Folders <https://developers.everyaction.com/van-api#folders>`__ service.
    """

    # TODO: Documentation missing at https://developers.everyaction.com/van-api#folders-overview.

    @ea_endpoint('folders/{folderId}', 'get', result_factory=Folder)
    def get(self, folder_id: int, /) -> Folder:
        """See `GET /folders/{folderId}
        <https://developers.everyaction.com/van-api#folders-get-folders--folderid>`__.

        :param folder_id: The :code:`folderId` path parameter.
        """

    @ea_endpoint('folders', 'get', paginated=True, result_factory=Folder)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Folder]:
        """See `GET /folders
        <https://developers.everyaction.com/van-api#folders-get-folders>`__.
        
        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """


class JobClasses(EAService):
    """Represents the
    `JobClasses <https://developers.everyaction.com/van-api#job-classes>`__ service.
    """

    @ea_endpoint('jobClasses', 'post', data_type=JobClass, result_factory=JobClass)
    def create(self, **kwargs: EAValue) -> JobClass:
        """See `POST /jobClasses
        <https://developers.everyaction.com/van-api#job-classes-post-jobclasses>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.JobClass` is appropriate
            to unpack here.
        :returns: The created :class:`.JobClass` object.
        """

    @ea_endpoint('jobClasses/{job_class_id}', 'get', result_factory=JobClass)
    def get(self, job_class_id: int, /) -> JobClass:
        """See `GET /jobClasses/{jobClassId}
        <https://developers.everyaction.com/van-api#job-classes-get-jobclasses--jobclassid>`__.

        :param job_class_id: The :code:`jobClassId` path parameter.
        :returns: The resulting :class:`.JobClass`.
        """

    @ea_endpoint('/jobClasses', 'get', paginated=True, result_factory=JobClass)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[JobClass]:
        """See `GET /jobClasses
        <https://developers.everyaction.com/van-api#job-classes-get-jobclasses>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.JobClass` objects.
        """


class Locations(EAService):
    """Represents the
    `Locations <https://developers.everyaction.com/van-api#locations>`__ service.
    """

    @ea_endpoint('locations', 'post', data_type=Location, result_factory=Location)
    def create(self, **kwargs: EAValue) -> Location:
        """See `POST /locations
        <https://developers.everyaction.com/van-api#locations-post-locations>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Location` is
            appropriate to unpack here.
        :returns: The created :class:`.Location` object.
        """

    @ea_endpoint('locations/{locationId}', 'delete', has_result=False)
    def delete(self, location_id: int, /) -> None:
        """See `DELETE /locations/{locationId}
        <https://developers.everyaction.com/van-api#locations-delete-locations--locationid>`__.

        :param location_id: The :code:`locationId` path parameter.
        """

    @ea_endpoint('locations/findOrCreate', 'post', data_type=Location, result_factory=Location, exclude_keys={'id'})
    def find_or_create(self, **kwargs: EAValue) -> Location:
        """See `POST /locations/findOrCreate
        <https://developers.everyaction.com/van-api#locations-post-locations-findorcreate>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Location` is
            appropriate to unpack here.
        :returns: The resulting :class:`.Location` object.
        """

    @ea_endpoint('locations/{locationId}', 'get', result_factory=Location, exclude_keys={'id'})
    def get(self, location_id: int, /) -> Location:
        """See `GET /locations/{locationId}
        <https://developers.everyaction.com/van-api#locations-get-locations--locationid>`__.

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
        <https://developers.everyaction.com/van-api#locations-get-locations>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Location` objects.
        """


class MemberStatuses(EAService):
    """Represents the
    `Member Statuses <https://developers.everyaction.com/van-api#member-statuses>`__ service.
    """

    @ea_endpoint('memberStatuses', 'post', data_type=MemberStatus, result_factory=MemberStatus)
    def create(self, **kwargs: EAValue) -> MemberStatus:
        """See `POST /memberStatuses
        <https://developers.everyaction.com/van-api#member-statuses-post-memberstatuses>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.MemberStatus` is
            appropriate to unpack here.
        :returns: The created :class:`.MemberStatus` object.
        """

    @ea_endpoint('memberStatuses/{member_status_id}', 'get', result_factory=MemberStatus)
    def get(self, member_status_id: int, /) -> MemberStatus:
        """See `GET /memberStatuses/{memberStatusId}
        <https://developers.everyaction.com/van-api#member-statuses-get-memberstatuses--memberstatusid>`__.

        :param member_status_id: The :code:`member_status_id` path parameter.
        :returns: The resulting :class:`.MemberStatus` object.
        """

    @ea_endpoint('memberStatuses', 'get', paginated=True, result_factory=MemberStatus)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[MemberStatus]:
        """See `GET /memberStatuses
        <https://developers.everyaction.com/van-api#member-statuses-get-memberstatuses>`__.

        :param limit: Maximum number of records to get for the request.
        :param kwargs: The applicable query arguments and JSON data for the request.

        :returns: List of the resulting :class:`.MemberStatus` objects.
        """


class MiniVANExports(EAService):
    """Represents the
    `MiniVANExports <https://developers.everyaction.com/van-api#minivanexports>`__ service.
    """

    @ea_endpoint('minivanExports/{minivanExportId}', 'get', result_factory=MiniVANExport)
    def get(self, export_id: int, /) -> MiniVANExport:
        """See `GET /minivanExports/{minivanExportId}
        <https://developers.everyaction.com/van-api#minivan-exports-get-minivanexports--minivanexportid>`__.

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
        <https://developers.everyaction.com/van-api#minivan-exports-get-minivanexports>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.MiniVANExport` objects.
        """


class Notes(EAService):
    """Represents the
    `Notes <https://developers.everyaction.com/van-api#notes>`__ service.
    """

    @ea_endpoint('notes/categories', 'get', result_array=True, result_factory=NoteCategory)
    def categories(self) -> List[NoteCategory]:
        """See `GET /notes/categories/{noteCategoryId}
        <https://developers.everyaction.com/van-api#notes-get-notes-categories--notecategoryid>`__.

        :returns: List of the resulting :class:`.NoteCategory` objects.
        """

    @ea_endpoint('notes/categories/{noteCategoryId}', 'get', result_factory=NoteCategory)
    def category(self, category_id: int, /) -> NoteCategory:
        """See `GET /notes/categories
        <https://developers.everyaction.com/van-api#notes-get-notes-categories>`__.

        :param category_id: The :code:`noteCategoryId` path parameter.
        :returns: The resulting :class:`.NoteCategory` object.
        """

    @ea_endpoint('notes/categoryTypes', 'get', result_array=True)
    def category_types(self) -> List[str]:
        """See `GET /notes/categoryTypes
        <https://developers.everyaction.com/van-api#notes-get-notes-categorytypes>`__.

        :returns: List of the names of the category types.
        """


class OnlineActionForms(EAService):
    """Represents the
    `Online Action Forms <https://developers.everyaction.com/van-api#onlineactionforms>`__ service.
    """

    @ea_endpoint('onlineActionsForms/{formTrackingId}', 'get', result_factory=OnlineActionForm)
    def get(self, tracking_id: int, /):
        """See `GET /onlineActionsForms/{formTrackingId}
        <https://developers.everyaction.com/van-api#online-actions-forms-get-onlineactionsforms--formtrackingid>`__.

        :param tracking_id: The :code:`formTrackingId` path parameter.
        :returns: The resulting :class:`.OnlineActionForm` object.
        """

    @ea_endpoint('onlineActionsForms', 'get', paginated=True, result_factory=OnlineActionForm)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[OnlineActionForm]:
        """See `GET /onlineActionsForms
        <https://developers.everyaction.com/van-api#online-actions-forms-get-onlineactionsforms>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.OnlineActionForm` objects.
        """


class Phones(EAService):
    """Represents the
    `Phones <https://developers.everyaction.com/van-api#phones>`__ service.
    """

    @ea_endpoint('phones/isCellStatuses', 'get', paginated=True, result_factory=IsCellStatus)
    def is_cell_statuses(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[IsCellStatus]:
        """See `GET /phones/isCellStatuses
        <https://developers.everyaction.com/van-api#phones-get-phones-iscellstatuses>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.IsCellStatus` objects.
        """


class PrintedLists(EAService):
    """Represents the
    `Printed Lists <https://developers.everyaction.com/van-api#printedlists>`__ service.
    """

    @ea_endpoint('printedLists/{printedListNumber}', 'get', result_factory=PrintedList)
    def get(self, list_number: str, /) -> PrintedList:
        """See `GET /printedLists/{printedListNumber}
        <https://developers.everyaction.com/van-api#printed-lists-get-printedlists--printedlistnumber>`__.

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
        <https://developers.everyaction.com/van-api#printed-lists-get-printedlists>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.PrintedList` objects.
        """


class Relationships(EAService):
    """Represents the
    `Relationships <https://developers.everyaction.com/van-api#relationships>`__ service.
    """

    @ea_endpoint('relationships', 'get', paginated=True, result_factory=Relationship)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Relationship]:
        """See `GET /relationships
        <https://developers.everyaction.com/van-api#relationships-get-relationships>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Relationship` objects.
        """


class ReportedDemographics(EAService):
    """Represents the
    `Reported Demographics <https://developers.everyaction.com/van-api#reporteddemographics>`__ service.
    """

    @ea_endpoint('reportedEthnicities', 'get', paginated=True, result_factory=ReportedEthnicity)
    def ethnicities(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ReportedEthnicity]:
        """See `GET /reportedEthnicities
        <https://developers.everyaction.com/van-api#reported-demographics-get-reportedethnicities>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ReportedEthnicity` objects.
        """

    @ea_endpoint('reportedGenders', 'get', paginated=True, result_factory=ReportedGender)
    def genders(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ReportedGender]:
        """See `GET /reportedGenders
        <https://developers.everyaction.com/van-api#reported-demographics-get-reportedgenders>`__.

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
        <https://developers.everyaction.com/van-api#reported-demographics-get-reportedlanguagepreferences>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ReportedLanguagePreference` objects.
        """

    @ea_endpoint('pronouns', 'get', paginated=True, result_factory=PreferredPronoun)
    def pronouns(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[PreferredPronoun]:
        """See `GET /pronouns
        <https://developers.everyaction.com/van-api#reported-demographics-get-pronouns>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.PreferredPronoun` objects.
        """

    @ea_endpoint('reportedRaces', 'get', paginated=True, result_factory=ReportedRace)
    def races(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ReportedRace]:
        """See `GET /reportedRaces
        <https://developers.everyaction.com/van-api#reported-demographics-get-reportedraces>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ReportedRace` objects.
        """

    @ea_endpoint('reportedSexualOrientations', 'get', paginated=True, result_factory=ReportedSexualOrientation)
    def sexual_orientations(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ReportedSexualOrientation]:
        """See `GET /reportedSexualOrientations
        <https://developers.everyaction.com/van-api#reported-demographics-get-reportedsexualorientations>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ReportedSexualOrientation` objects.
        """


class SavedLists(EAService):
    """Represents the
    `Saved Lists <https://developers.everyaction.com/van-api#savedlists>`__ service.
    """

    @ea_endpoint('savedLists/{savedListId}', 'get', result_factory=SavedList)
    def get(self, list_id: int, /) -> SavedList:
        """See `GET /savedLists/{savedListId}
        <https://developers.everyaction.com/van-api#saved-lists-get-savedlists--savedlistid>`__.

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
        <https://developers.everyaction.com/van-api#saved-lists-get-savedlists>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.SavedList` objects.
        """


class ScheduleTypes(EAService):
    """Represents the
    `Schedule Types <https://developers.everyaction.com/van-api#schedule-types>`__ service.
    """

    @ea_endpoint('scheduleTypes', 'post', data_type=ScheduleType, result_factory=ScheduleType)
    def create(self, **kwargs: EAValue) -> ScheduleType:
        """See `POST /scheduleTypes
        <https://developers.everyaction.com/van-api#schedule-types-post-scheduletypes>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.ScheduleType` is
            appropriate to unpack here.
        :returns: The created :class:`.ScheduleType` object.
        """

    @ea_endpoint('scheduleTypes/{schedule_type_id}', 'get', result_factory=ScheduleType)
    def get(self, schedule_type_id: int, /) -> ScheduleType:
        """See `GET /scheduleTypes/{scheduleTypeId}
        <https://developers.everyaction.com/van-api#schedule-types-get-scheduletypes>`__.

        :param schedule_type_id: The :code:`scheduleTypeId` path parameter.
        :returns: The resulting :class:`.ScheduleType` object.
        """

    @ea_endpoint('scheduleTypes', 'get', paginated=True, result_factory=ScheduleType)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ScheduleType]:
        """See `GET /scheduleTypes
        <https://developers.everyaction.com/van-api#schedule-types-get-scheduletypes>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ScheduleType` objects.
        """


class ScoreUpdates(EAService):
    """Represents the
    `Score Updates <https://developers.everyaction.com/van-api#scoreupdates>`__ service.
    """

    @ea_endpoint('scoreUpdates/{scoreUpdateId}', 'get', result_factory=ScoreUpdate)
    def get(self, update_id: int, /) -> ScoreUpdate:
        """See `GET /scoreUpdates/{scoreUpdateId}
        <https://developers.everyaction.com/van-api#score-updates-get-scoreupdates--scoreupdateid>`__.

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
        <https://developers.everyaction.com/van-api#score-updates-get-scoreupdates>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ScoreUpdate` objects.
        """

    @ea_endpoint('scoreUpdates/{scoreUpdateId}', 'patch', prop_keys={'loadStatus'}, has_result=False)
    def patch(self, update_id: int, /, **kwargs: EAValue) -> None:
        """See `PATCH /scoreUpdates/{scoreUpdateId}
        <https://developers.everyaction.com/van-api#score-updates-patch-scoreupdates--scoreupdateid>`__.

        :param update_id: The :code:`scoreUpdateId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """


class Scores(EAService):
    """Represents the
    `Scores <https://developers.everyaction.com/van-api#scores>`__ service.
    """

    @ea_endpoint('scores/{scoreId}', 'get', result_factory=Score)
    def get(self, score_id: int, /) -> Score:
        """See `GET /scores/{scoreId}
        <https://developers.everyaction.com/van-api#scores-get-scores--scoreid>`__.

        :param score_id: The :code:`scoreId` path parameter.
        :returns: The resulting :class:`.Score` object.
        """

    @ea_endpoint('scores', 'get', paginated=True, result_factory=Score)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Score]:
        """See `GET /scores
        <https://developers.everyaction.com/van-api#scores-get-scores>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Score` objects.
        """


class Signups(EAService):
    """Represents the
    `Signups <https://developers.everyaction.com/van-api#signups>`__ service.
    """

    @ea_endpoint('signups', 'post', data_type=Signup, result_factory=Signup)
    def create_or_update(self, **kwargs: EAValue) -> Signup:
        """See `POST /signups
        <https://developers.everyaction.com/van-api#signups-post-signups>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Signup` is
            appropriate to unpack here.
        :returns: The created :class:`.Signup` object.
        """

    @ea_endpoint('signups/{eventSignupId}', 'delete', has_result=False)
    def delete(self, signup_id: int, /) -> None:
        """See `DELETE /signups/{eventSignupId}
        <https://developers.everyaction.com/van-api#signups-delete-signups--eventsignupid>`__.

        :param signup_id: The :code:`eventSignupId` path parameter.
        """

    @ea_endpoint('signups/{eventSignupId}', 'get', result_factory=Signup)
    def get(self, signup_id: int, /) -> Signup:
        """See `GET /signups/{eventSignupId}
        <https://developers.everyaction.com/van-api#signups-get-signups--eventsignupid>`__.

        :param signup_id: The :code:`eventSignupId` path parameter.
        :returns: The resulting :class:`.Signup` object.
        """

    @ea_endpoint('signups', 'get', query_arg_keys={'eventId', 'vanId'}, paginated=True, result_factory=Signup)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Signup]:
        """See `GET /signups
        <https://developers.everyaction.com/van-api#signups-get-signups>`__.

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
        <https://developers.everyaction.com/van-api#signups-get-signups-statuses>`__.

        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The resulting :class:`.Status` objects.
        """

    @ea_endpoint('signups/{eventSignupId}', 'put', data_type=Signup, has_result=False)
    def update(self, signup_id: int, /, **kwargs: EAValue) -> None:
        """See `PUT /signups/{eventSignupId}
        <https://developers.everyaction.com/van-api#signups-put-signups--eventsignupid>`__.

        :param signup_id: The :code:`eventSignupId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Signup` is
            appropriate to unpack here.
        """


class ShiftTypes(EAService):
    """Represents the
    `Shift Types <https://developers.everyaction.com/van-api#shift-types>`__ service.
    """

    @ea_endpoint('shiftTypes', 'post', data_type=ShiftType, result_factory=ShiftType)
    def create(self, **kwargs: EAValue) -> ShiftType:
        """See `POST /shiftTypes
        <https://developers.everyaction.com/van-api#shift-types-post-shifttypes>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.ShiftType` is
            appropriate to unpack here.
        :returns: The created :class:`.ShiftType` object.
        """

    @ea_endpoint('shiftTypes/{shift_type_id}', 'get', result_factory=ShiftType)
    def get(self, shift_type_id: int, /) -> ShiftType:
        """See `GET /shiftTypes/{shiftTypeId}
        <https://developers.everyaction.com/van-api#shift-types-get-shifttypes--shifttypeid>`__.

        :param shift_type_id: The :code:`shiftTypeId` path parameter.
        :returns: The resulting :class:`.ShiftType` object.
        """

    @ea_endpoint('shiftTypes', 'get', paginated=True, result_factory=ShiftType)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[ShiftType]:
        """See `GET /shiftTypes
        <https://developers.everyaction.com/van-api#shift-types>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.ShiftType` objects.
        """


class Stories(EAService):
    """Represents the
    `Stories <https://developers.everyaction.com/van-api#stories>`__ service.
    """

    @ea_endpoint('stories', 'post', data_type=Story, result_factory=Story)
    def create(self, **kwargs: EAValue) -> Story:
        """See `POST /stories
        <https://developers.everyaction.com/van-api#stories-post-stories>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.Story` is
            appropriate to unpack here.
        :returns: The resulting :class:`.Story` object.
        """

    @ea_endpoint('stories/{storyId}', 'get', result_factory=Story)
    def get(self, story_id: int, /) -> Story:
        """See `GET /stories/{storyId}
        <https://developers.everyaction.com/van-api#stories-get-stories--storyid>`__.

        :param story_id: The :code:`storyId` path parameter.
        :returns: The resulting :class:`.Story` object.
        """


class SupporterGroups(EAService):
    """Represents the
    `Supporter Groups <https://developers.everyaction.com/van-api#supportergroups>`__ service.
    """

    @ea_endpoint('supporterGroups/{supporterGroupId}/people/{vanId}', 'put', has_result=False)
    def add_person(self, group_id: int, van_id: int, /) -> None:
        """See `PUT /supporterGroups/{supporterGroupId}/people/{vanId}
        <https://developers.everyaction.com/van-api#supporter-groups-put-supportergroups--supportergroupid--people--vanid>`__.

        :param group_id: The :code:`groupId` path parameter.
        :param van_id: The :code:`vanId` path parameter.
        """

    @ea_endpoint('supporterGroups', 'post', data_type=SupporterGroup, result_factory=SupporterGroup)
    def create(self, **kwargs: EAValue) -> SupporterGroup:
        """See `POST /supporterGroups
        <https://developers.everyaction.com/van-api#supporter-groups-post-supportergroups>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.SupporterGroup` is
            appropriate to unpack here.
        :returns: The created :class:`.SupporterGroup` object.
        """

    @ea_endpoint('supporterGroups/{supporterGroupId}', 'delete', has_result=False)
    def delete(self, group_id: int, /) -> None:
        """See `DELETE /supporterGroups/{supporterGroupId}
        <https://developers.everyaction.com/van-api#supporter-groups-delete-supportergroups--supportergroupid>`__.

        :param group_id: The :code:`supporterGroupId` path parameter.
        """

    @ea_endpoint('supporterGroups/{supporterGroupId}', 'get', result_factory=SupporterGroup)
    def get(self, group_id: int, /) -> SupporterGroup:
        """See `GET /supporterGroups/{supporterGroupId}
        <https://developers.everyaction.com/van-api#supporter-groups-get-supportergroups--supportergroupid>`__.

        :param group_id: The :code:`supporterGroupId` path parameter.
        :returns: The resulting :class:`.SupporterGroup` object.
        """

    @ea_endpoint('supporterGroups', 'get', paginated=True, result_factory=SupporterGroup)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[SupporterGroup]:
        """See `GET /supporterGroups
        <https://developers.everyaction.com/van-api#supporter-groups-get-supportergroups>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.SupporterGroup` objects.
        """

    @ea_endpoint('supporterGroups/{supporterGroupId}/people/{vanId}', 'delete', has_result=False)
    def remove_person(self, group_id: int, van_id: int, /) -> None:
        """See `DELETE /supporterGroups/{supporterGroupId}/people/{vanId}
        <https://developers.everyaction.com/van-api#supporter-groups-delete-supportergroups--supportergroupid--people--vanid>`__.

        :param group_id: The :code:`groupId` path parameter.
        :param van_id: The :code:`vanId` path parameter.
        """


class SurveyQuestions(EAService):
    """Represents the
    `Survey Questions <https://developers.everyaction.com/van-api#surveyquestions>`__ service.
    """

    @ea_endpoint('surveyQuestions/{surveyQuestionId}', 'get', result_factory=SurveyQuestion)
    def get(self, question_id: Union[int, str], /) -> SurveyQuestion:
        """See `GET /surveyQuestions/{surveyQuestionId}
        <https://developers.everyaction.com/van-api#survey-questions-get-surveyquestions--surveyquestionid>`__.

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
        <https://developers.everyaction.com/van-api#survey-questions-get-surveyquestions>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.SurveyQuestion` objects.
        """


class TargetExportJobs(EAService):
    """Represents the
    `Target Export Jobs <https://developers.everyaction.com/van-api#targetexportjobs>`__ service.
    """

    @ea_endpoint('targetExportJobs', 'post', data_type=TargetExportJob, result_factory=TargetExportJob)
    def create(self, **kwargs: EAValue) -> TargetExportJob:
        """See `POST /targetExportJobs
        <https://developers.everyaction.com/van-api#target-export-jobs-post-targetexportjobs>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.TargetExportJob` is
            appropriate to unpack here.
        :returns: The created :class:`.TargetExportJob` object.
        """

    @ea_endpoint('targetExportJobs/{exportJobId}', 'get', result_factory=TargetExportJob)
    def get(self, job_id: int, /) -> TargetExportJob:
        """See `GET /targetExportJobs/{exportJobId}
        <https://developers.everyaction.com/van-api#target-export-jobs-get-targetexportjobs--exportjobid>`__.

        :param job_id: The :code:`exportJobId` path parameter.
        :returns: The resulting :class:`.TargetExportJob` object.
        """


class Targets(EAService):
    """Represents the
    `Targets <https://developers.everyaction.com/van-api#targets>`__ service.
    """

    @ea_endpoint('targets/{targetId}', 'get', result_factory=Target)
    def get(self, target_id: int, /) -> Target:
        """See `GET /targets/{targetId}
        <https://developers.everyaction.com/van-api#targets-get-targets--targetid>`__.

        :param target_id: The :code:`targetId` path parameter.
        :returns: The resulting :class:`.Target` object.
        """

    @ea_endpoint('targets', 'get', query_arg_keys={'status', 'type', '$expand'}, paginated=True, result_factory=Target)
    def list(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[Target]:
        """See `GET /targets
        <https://developers.everyaction.com/van-api#targets-get-targets>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Target` objects.
        """


class Users(EAService):
    """Represents the
    `Users <https://developers.everyaction.com/van-api#users>`__ service.
    """

    @ea_endpoint(
        'users/{userId}/districtFieldValues',
        'post',
        props={'districtFieldValues': EAProperty('field_values', 'values', singular_alias='value')},
        result_key='districtFieldValues'
    )
    def add_district_fields(self, user_id: int, /, **kwargs: EAValue) -> List[str]:
        """See `POST /users/{userId}/districtFieldValues
        <https://developers.everyaction.com/van-api#users-post-users--userid--districtfieldvalues>`__.

        :param user_id: The :code:`userId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The full set of names of the user's district field values.
        """

    @ea_endpoint('users/{userId}/districtFieldValues', 'get', result_key='districtFieldValues')
    def district_fields(self, user_id: int, /) -> List[str]:
        """See `GET /users/{userId}/districtFieldValues
        <https://developers.everyaction.com/van-api#users-get-users--userid--districtfieldvalues>`__.

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
        <https://developers.everyaction.com/van-api#users-put-users--userid--districtfieldvalues>`__.

        :param user_id: The :code:`userId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: The full set of names of the user's district field values.
        """


class VoterRegistrationBatches(EAService):
    """Represents the
    `Voter Registration Batches <https://developers.everyaction.com/van-api#voterregistrationbatches>`__ service.
    """

    @ea_endpoint(
        'voterRegistrationBatches/{batchId}/people',
        'post',
        result_array=True,
        result_factory=AddRegistrantsResponse
    )
    def add_registrants(self, batch_id: int, /, *, data: List[Registrant]) -> List[AddRegistrantsResponse]:
        """See `POST /voterRegistrationBatches/{batchId}/people
        <https://developers.everyaction.com/van-api#voter-registration-batches-post-voterregistrationbatches--batchid--people>`__.

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
        <https://developers.everyaction.com/van-api#voter-registration-batches-post-voterregistrationbatches>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.VoterRegistrationBatch`
            is appropriate to unpack here.
        :returns: The created :class:`.VoterRegistrationBatch`.
        """

    @ea_endpoint('voterRegistrationBatches/registrationForms', 'get', paginated=True, result_factory=RegistrationForm)
    def forms(self, *, limit: Optional[int] = None, **kwargs: EAValue) -> List[RegistrationForm]:
        """See `GET /voterRegistrationBatches/registrationForms
        <https://developers.everyaction.com/van-api#voter-registration-batches-get-voterregistrationbatches-registrationforms>`__.

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
        <https://developers.everyaction.com/van-api#voter-registration-batches-get-voterregistrationbatches>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.VoterRegistrationBatch` objects.
        """

    @ea_endpoint('voterRegistrationBatches/programTypes', 'get', paginated=True, result_factory=ProgramType)
    def programs(self, limit: Optional[int] = None, **kwargs: EAValue) -> List[ProgramType]:
        """See `GET /voterRegistrationBatches/programTypes
        <https://developers.everyaction.com/van-api#voter-registration-batches-get-voterregistrationbatches-programtypes>`__.

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
        <https://developers.everyaction.com/van-api#voter-registration-batches-get-voterregistrationbatches-states--state--supportedfields>`__.

        :param limit: Maximum number of records to get for this request.
        :param state: The :code:`state` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.SupportField` objects.
        """

    @ea_endpoint('voterRegistrationBatches/{batchId}', 'patch', prop_keys={'status'}, has_result=False)
    def update_status(self, batch_id: int, /, **kwargs: EAValue) -> None:
        """See `PATCH /voterRegistrationBatches/{batchId}
        <https://developers.everyaction.com/van-api#voter-registration-batches-patch-voterregistrationbatches--batchid>`__.

        :param batch_id: The :code:`batchId` path parameter.
        :param kwargs: The applicable query arguments and JSON data for the request.
        """


class Worksites(EAService):
    """Represents the
    `Worksites <https://developers.everyaction.com/van-api#worksites>`__ service.
    """

    @ea_endpoint('worksites/{worksite_id}/workAreas', 'post', data_type=WorkArea, result_factory=WorkArea)
    def create_work_area(self, **kwargs: EAValue) -> WorkArea:
        """See `POST /worksites/{worksiteId}/workAreas
        <https://developers.everyaction.com/van-api#worksites-post-worksites--worksiteid--workareas>`__.

        :param kwargs: The applicable query arguments and JSON data for the request. A :class:`.WorkArea` is appropriate
            to unpack here.
        :returns: The created :class:`.WorkArea`.
        """

    @ea_endpoint('worksites/{worksite_id}', 'get', result_factory=Worksite)
    def get(self, worksite_id: int) -> Worksite:
        """See `GET /worksites/{worksiteId}
        <https://developers.everyaction.com/van-api#worksites-get-worksites--worksiteid>`__.

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
        <https://developers.everyaction.com/van-api#worksites-get-worksites>`__.

        :param limit: Maximum number of records to get for this request.
        :param kwargs: Applicable query arguments and JSON data for the request.
        :returns: List of the resulting :class:`.Worksite` objects.
        """
