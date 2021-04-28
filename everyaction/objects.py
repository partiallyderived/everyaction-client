"""
This module contains EveryAction objects, such as :class:`.Person` or :class:`.CanvassResponse`, which represent
structured EveryAction data directly corresponding to objects in the
`EveryAction 8 VAN API docs <https://developers.everyaction.com/van-api>`__.
"""

from typing import Any, Iterable, Optional, Union

from everyaction.core import EAObject, EAObjectWithID, EAObjectWithIDAndName, EAObjectWithName, EAProperty, EAValue
from everyaction.exception import EAException


__all__ = [
    'ActivistCode',
    'ActivistCodeData',
    'ActivistCodeResponse',
    'Address',
    'AddRegistrantsResponse',
    'Adjustment',
    'AdjustmentResponse',
    'Attribution',
    'AvailableValue',
    'APIKeyProfile',
    'AVEVDataFileAction',
    'BallotRequestType',
    'BallotReturnStatus',
    'BallotType',
    'BankAccount',
    'BargainingUnit',
    'BargainingUnitJobClass',
    'BatchForm',
    'BatchProgram',
    'BulkImportAction',
    'BulkImportField',
    'BulkImportJob',
    'BulkImportJobData',
    'Canvasser',
    'CanvassContext',
    'CanvassResponse',
    'ChangedEntityBulkImportField',
    'ChangedEntityExportJob',
    'ChangedEntityField',
    'ChangeType',
    'Code',
    'CodeResult',
    'Column',
    'Commitment',
    'ConfirmationEmailData',
    'Constraints',
    'ContactHistory',
    'ContactType',
    'Contribution',
    'Currency',
    'CustomField',
    'CustomFieldValue',
    'Department',
    'Designation',
    'DisclosureFieldValue',
    'Disbursement',
    'DistrictField',
    'DistrictFieldValue',
    'Email',
    'EmailMessage',
    'EmailMessageContent',
    'EmailMessageContentDistributions',
    'Employer',
    'EmployerBargainingUnit',
    'Error',
    'Event',
    'EventRole',
    'EventShift',
    'EventType',
    'ExportJob',
    'ExportJobType',
    'ExtendedSourceCode',
    'FieldValueMapping',
    'File',
    'FileLoadingJob',
    'FinancialBatch',
    'Folder',
    'GeoCoordinate',
    'Identifier',
    'InputType',
    'IsCellStatus',
    'JobActionType',
    'JobClass',
    'JobFile',
    'JobNotification',
    'KeyValuePair',
    'Listener',
    'ListLoadCallbackData',
    'Location',
    'MappingParent',
    'MappingType',
    'MappingTypeData',
    'Membership',
    'MembershipSourceCode',
    'MemberStatus',
    'MiniVANExport',
    'Note',
    'NoteCategory',
    'OnlineActionForm',
    'Organization',
    'OrganizationPhone',
    'Person',
    'Phone',
    'Pledge',
    'PreferredPronoun',
    'PrintedList',
    'ProgramType',
    'Registrant',
    'RegistrationForm',
    'RelationalMapping',
    'Relationship',
    'ReportedEthnicity',
    'ReportedGender',
    'ReportedLanguagePreference',
    'ReportedRace',
    'ReportedSexualOrientation',
    'ResultCode',
    'SavedList',
    'SavedListData',
    'SavedListLoadAction',
    'ScheduleType',
    'Score',
    'ScoreApprovalCriteria',
    'ScoreLoadAction',
    'ScoreUpdate',
    'ScriptResponse',
    'ShiftType',
    'Signup',
    'Status',
    'Story',
    'StoryStatus',
    'Subgroup',
    'SupportedEntity',
    'SupporterGroup',
    'SupportField',
    'Suppression',
    'SurveyQuestion',
    'SurveyCanvassResponse',
    'SurveyResponse',
    'Target',
    'TargetExportJob',
    'UpdateStatistics',
    'User',
    'ValueMapping',
    'ValueMappingData',
    'VolunteerActivityResponse',
    'VoterRegistrationBatch',
    'WorkArea',
    'Worksite'
]


# Class definitions and additions to shared properties are organized by their "orders".
# A property has order n > 1 when its factory depends on at least one class of order n - 1 and it depends on classes of
# no higher order than n - 1. A property has order 1 when its factory does not depend on an EAObject child definition.
# Similarly, a Class has order n > 1 when it has properties of order n or is a subclass of a class of order n - 1 and
# has no higher order properties/base classes. A Class has order 1 when it has only properties of order 1 or no
# properties at all and does not inherit except from EAObject, EAObjectWithID, or EAObjectWithIDAndName.
# The organization style is the following, with each component in alphabetical order: 1st order properties in, 1st order
# classes which may depend on 1st order properties, 2nd order properties whose factories depend on a 1st order class,
# 2nd order classes which may depend on 1st or 2nd order properties or a 1st order class, and so on. This organizational
# structure allows for a consistent way to specify entities after their dependencies and in alphabetical order
# independent from their dependencies are named.

# Expand is handled specially
def _expand_factory(arg: Union[str, Iterable[str]]) -> str:
    if not isinstance(arg, str):
        # comma-delimited str or Iterable[str] allowed for expand.
        # Note: str is Iterable, be careful when modifying this code.
        if isinstance(arg, Iterable):
            return ','.join(arg)
        else:
            raise TypeError(
                f'Expected str or Iterable for expand, found {type(arg).__name__}: {arg}'
            )
    return arg

# --- Circular Reference Factories ---
# The following functions are factories for objects which have circular references.
# For example, Organizations have a field which is another Organization, and Departments have employers and vice-versa.


def _employer_factory(*args: Any, **kwargs: Any) -> 'Employer':
    return Employer(*args, **kwargs)


def _organization_factory(*args: Any, **kwargs: Any) -> 'Organization':
    return Organization(*args, **kwargs)


# --- First Order Properties and Objects ---
EAProperty.share(
    acceptedOneTimeAmount=EAProperty('accepted_one_time'),
    acceptedRecurringAmount=EAProperty('accepted_recurring', 'recurring'),
    action=EAProperty(),
    actionType=EAProperty('type'),
    added=EAProperty(),
    additionalEnvelopeName=EAProperty('additional_envelope'),
    additionalSalutation=EAProperty(),
    adjustmentType=EAProperty('type'),
    allowMultipleMode=EAProperty('multiple_mode', 'mode'),
    alternateId=EAProperty('alternate', 'alt'),
    amount=EAProperty(),
    amountAttributed=EAProperty('amount'),
    apiKeyTypeName=EAProperty('type_name', 'type'),
    areSubgroupsSticky=EAProperty('sticky_subgroups', 'sticky_groups'),
    assignableTypes=EAProperty(singular_alias='assignable_type'),
    assignedValue=EAProperty('value'),
    attributionType=EAProperty('type'),
    average=EAProperty(),
    averageValue=EAProperty('average'),
    badValues=EAProperty('bad'),
    bankAccount=EAProperty('account'),
    bankAccountId=EAProperty('bank_account', 'account'),
    batchCode=EAProperty('batch'),
    biographyImageUrl=EAProperty('biography_image', 'bio_image_url', 'bio_image'),
    bounceCount=EAProperty('bounces'),
    campaignId=EAProperty('campaign'),
    canBeMappedToColumn=EAProperty('column_mappable', 'mappable'),
    canBeRepeatable=EAProperty('allows_repeats'),
    canHaveGoals=EAProperty('allows_goals'),
    canHaveMultipleLocations=EAProperty('allows_multiple_locations'),
    canHaveMultipleShifts=EAProperty('allows_multiple_shifts'),
    canHaveRoleMaximums=EAProperty('allows_role_maximums'),
    canHaveRoleMinimums=EAProperty('allows_role_minimums'),
    canvassedBy=EAProperty('canvasser'),
    canvassFileRequestId=EAProperty('canvass_id'),
    canvassFileRequestGuid=EAProperty('canvass_guid'),
    caseworkCases=EAProperty('cases', singular_alias='case'),
    caseworkIssues=EAProperty('issues', singular_alias='issue'),
    caseworkStories=EAProperty('stories', singular_alias='story'),
    ccExpirationMonth=EAProperty('cc_exp_month'),
    ccExpirationYear=EAProperty('cc_exp_year'),
    changeTypeName=EAProperty('change_type', 'change'),
    channelTypeName=EAProperty('channel_type', 'channel'),
    checkDate=EAProperty(),
    checkNumber=EAProperty(),
    city=EAProperty(),
    code=EAProperty(),
    codeId=EAProperty('code'),
    codeIds=EAProperty('codes'),
    collectedLocationId=EAProperty('collected_location', 'location'),
    color=EAProperty(),
    columnDelimiter=EAProperty('delimiter'),
    columnName=EAProperty('column'),
    committeeName=EAProperty('committee'),
    confidenceLevel=EAProperty('confidence'),
    contact=EAProperty(),
    contactMethodPreferenceCode=EAProperty('contact_preference_code', 'preference_code', 'contact_preference'),
    contactMode=EAProperty(),
    contactModeId=EAProperty('contact_mode'),
    contactTypeId=EAProperty('contact_type'),
    contributionCount=EAProperty('contributions'),
    contributionId=EAProperty('contribution'),
    contributionSummary=EAProperty(),
    contributionTotal=EAProperty(),
    copyToEmails=EAProperty('copy_to', is_array=True),
    countryCode=EAProperty('country'),
    coverCostsAmount=EAProperty('cover_costs'),
    createdAfter=EAProperty('after'),
    createdBefore=EAProperty('before'),
    createdBy=EAProperty('creator'),
    createdByCommitteeId=EAProperty('committee'),
    createdByEmail=EAProperty('created_by', 'creator_email', 'creator'),
    createdDate=EAProperty('created'),
    creditCardLast4=EAProperty('cc_last4', 'last4'),
    currency=EAProperty(),
    currencyType=EAProperty('type'),
    custom=EAProperty(),
    customFieldGroupId=EAProperty('group'),
    customFieldId=EAProperty('field'),
    customFieldsGroupType=EAProperty('group_type', 'type'),
    customPropertyKey=EAProperty('property_key', 'custom_key', 'key'),
    cycle=EAProperty(),
    databaseMode=EAProperty('mode'),
    databaseName=EAProperty(),
    dateAdjusted=EAProperty('adjusted', 'date'),
    dateCanvassed=EAProperty('canvassed'),
    dateCardsSent=EAProperty('cards_sent'),
    dateChangedFrom=EAProperty('changed_from'),
    dateChangedTo=EAProperty('changed_to'),
    dateClosed=EAProperty('closed'),
    dateCreated=EAProperty('created'),
    dateDeposited=EAProperty('deposited'),
    dateExpired=EAProperty('expired'),
    dateExpireMembership=EAProperty('expiration_date', 'expiration', 'expires'),
    dateIssued=EAProperty('issued'),
    dateLastRenewed=EAProperty('last_renewed', 'renewed'),
    dateModified=EAProperty('modified'),
    dateOfBirth=EAProperty('birthday'),
    dateOpened=EAProperty('opened'),
    datePosted=EAProperty('posted'),
    dateProcessed=EAProperty('processed'),
    dateReceived=EAProperty('received'),
    dateScheduled=EAProperty('scheduled'),
    dateSent=EAProperty('sent'),
    dateStartMembership=EAProperty('start_date', 'started'),
    dateThanked=EAProperty('thanked'),
    decreasedBy=EAProperty('decrease'),
    defaultEndTime=EAProperty('default_end'),
    defaultStartTime=EAProperty('default_start'),
    depositDate=EAProperty(),
    depositNumber=EAProperty(),
    detailedCode=EAProperty('code'),
    description=EAProperty('desc'),
    designationId=EAProperty('designation'),
    dialingPrefix=EAProperty('prefix'),
    directMarketingCode=EAProperty('marketing_code'),
    disclosureFieldValue=EAProperty('field_value', 'disclosure_value', 'value'),
    displayMode=EAProperty(),
    displayName=EAProperty('display'),
    doorCount=EAProperty('door'),
    dotNetTimeZoneId=EAProperty('dot_net_time_zone', 'time_zone'),
    downloadUrl=EAProperty('url'),
    duesAttributionTypeName=EAProperty('dues_attribution_type', 'dues_attribution'),
    duesEntityTypeName=EAProperty('dues_entity_type', 'dues_entity'),
    duplicateRows=EAProperty('duplicates'),
    electionRecords=EAProperty(singular_alias='election_record'),
    electionType=EAProperty(),
    email=EAProperty(),
    employer=EAProperty(factory=_employer_factory),
    employerBargainingUnitId=EAProperty('employer_bargaining_unit'),
    employerId=EAProperty('employer'),
    endDate=EAProperty('end'),
    endTime=EAProperty('end'),
    endTimeOverride=EAProperty('end_override', 'end'),
    enrollmentTypeName=EAProperty('enrollment_type', 'enrollment'),
    envelopeName=EAProperty('envelope'),
    errorCode=EAProperty('error'),
    eventId=EAProperty('event'),
    eventTypeId=EAProperty('event_type', 'type'),
    eventTypeIds=EAProperty('event_types'),
    excludeChangesFromSelf=EAProperty('exclude_self'),
    expand=EAProperty(factory=_expand_factory),
    expectedContributionCount=EAProperty('expected_count'),
    expectedContributionTotalAmount=EAProperty('expected_total', 'expected_amount'),
    exportedRecordCount=EAProperty('exported_records', 'record_count', 'records', 'count'),
    ext=EAProperty(),
    externalId=EAProperty('external'),
    fieldName=EAProperty('field'),
    fieldType=EAProperty('field', 'type'),
    fileSizeKbLimit=EAProperty('size_kb_limit', 'kb_limit'),
    financialBatchId=EAProperty('financial_batch'),
    finderNumber=EAProperty('finder'),
    firstName=EAProperty('first'),
    folderId=EAProperty('folder'),
    folderName=EAProperty('folder'),
    formalEnvelopeName=EAProperty('formal_envelope'),
    formalSalutation=EAProperty(),
    formSubmissionCount=EAProperty('form_submissions', 'forms', 'submissions'),
    frequency=EAProperty(),
    fromEmail=EAProperty(),
    fromName=EAProperty('sender'),
    fromSubject=EAProperty('subject'),
    fullName=EAProperty(),
    generatedAfter=EAProperty('after'),
    generatedBefore=EAProperty('before'),
    goal=EAProperty(),
    groupId=EAProperty(),
    groupName=EAProperty(),
    groupType=EAProperty(),
    guid=EAProperty(),
    hasHeader=EAProperty(),
    hasMyCampaign=EAProperty('my_campaign'),
    hasMyVoters=EAProperty('my_voters'),
    hasPredefinedValues=EAProperty('has_predefined'),
    hasQuotes=EAProperty(),
    hint=EAProperty(),
    increasedBy=EAProperty('increase'),
    includeAllAutoGenerated=EAProperty('include_auto_generated', 'include_generated'),
    includeAllStatuses=EAProperty('include_statuses', 'include_closed'),
    includeInactive=EAProperty(),
    includeUnassigned=EAProperty(),
    inputTypeId=EAProperty('input_type'),
    interventionCallbackUrl=EAProperty('intervention_url', 'callback_url'),
    invalidCharacters=EAProperty('invalid_chars'),
    invalidRowsFileUrl=EAProperty('invalid_rows_url', 'invalid_url'),
    inRepetitionWithEventId=EAProperty('repeat_of'),
    isActive=EAProperty('active'),
    isApplicable=EAProperty('applicable'),
    isAssociatedWithBadges=EAProperty('associated_with_badges'),
    isAtLeastOneLocationRequired=EAProperty('needs_location', 'location_required', 'requires_location'),
    isAutoGenerated=EAProperty('auto_generated', 'generated'),
    isConfirmationEmailEnabled=EAProperty('confirmation_email_enabled', 'confirmation_enabled', 'confirmation'),
    isConfirmedOptInEnabled=EAProperty('confirmed_opt_in_enabled', 'opt_in_enabled', 'opt_in'),
    isCoreField=EAProperty('is_core', 'core_field', 'core'),
    isCustomDistrict=EAProperty('custom_district', 'is_custom', 'custom'),
    isEditable=EAProperty('editable'),
    isEventLead=EAProperty('event_lead', 'lead'),
    isExportable=EAProperty('exportable'),
    isMember=EAProperty('member'),
    isMultiAssign=EAProperty('multi_assign'),
    isMyOrganization=EAProperty('my_organization', 'my_org'),
    isOfflineSignup=EAProperty('offline_property', 'offline'),
    isOnlineActionsAvailable=EAProperty('online_actions_available', 'actions_available'),
    isOnlyEditableByCreatingUser=EAProperty(
        'only_editable_by_creating_user',
        'only_editable_by_creator',
        'only_creator_may_edit'
    ),
    isOpen=EAProperty('open'),
    isPreferred=EAProperty('preferred'),
    isPubliclyViewable=EAProperty('publicly_viewable', 'public'),
    isRecurringEmailEnabled=EAProperty('recurring_email_enabled', 'recurring_enabled', 'recurring'),
    isRequired=EAProperty('required'),
    isSearchable=EAProperty('searchable'),
    isSharedWithChildCommitteesByDefault=EAProperty('default_share_child'),
    isSharedWithMasterCommitteeByDefault=EAProperty('default_share_master'),
    isSubscribed=EAProperty('subscribed'),
    isUpsellAccepted=EAProperty('upsell_accepted'),
    isUpsellShown=EAProperty('upsell_shown'),
    isViewRestricted=EAProperty('view_restricted'),
    jobStatus=EAProperty('status'),
    key=EAProperty(),
    keyReference=EAProperty('reference'),
    lastName=EAProperty('last'),
    lat=EAProperty(),
    levelId=EAProperty(),
    levelName=EAProperty(),
    line1=EAProperty(),
    line2=EAProperty(),
    line3=EAProperty(),
    linkedCreditCardPaymentDisbursementId=EAProperty('credit_card_payment'),
    linkedJointFundraisingContributionId=EAProperty(
        'joint_fundraising_contribution', 'fundraising_contribution', 'fundraising'
    ),
    linkedPartnershipContributionId=EAProperty('partnership_contribution', 'partnership'),
    linkedReimbursementDisbursementId=EAProperty('reimbursement'),
    linksClickedCount=EAProperty('links_clicked'),
    listCount=EAProperty('list'),
    listDescription=EAProperty('description', 'desc'),
    listName=EAProperty('list', 'name'),
    loadStatus=EAProperty('status'),
    lon=EAProperty(),
    mappingTypeName=EAProperty('mapping_type', 'mapping'),
    matchedRows=EAProperty('matched'),
    matchedRowsCount=EAProperty('matched_count', 'matched'),
    matchPercent=EAProperty('match', 'percent'),
    max=EAProperty(),
    maxDoorCount=EAProperty('max_door'),
    maxFieldLength=EAProperty('max_length', 'max_len'),
    maxPeopleCount=EAProperty('max_people'),
    maxTextboxCharacters=EAProperty('max_box_chars'),
    maxValue=EAProperty('max'),
    medianValue=EAProperty('median'),
    mediumName=EAProperty('medium'),
    message=EAProperty(),
    middleName=EAProperty('middle'),
    min=EAProperty(),
    minValue=EAProperty('min'),
    modifiedBy=EAProperty('modifier'),
    modifiedByEmail=EAProperty('modified_by', 'modifier_email', 'modifier'),
    nextTransactionDate=EAProperty('next_transaction', 'next'),
    nickname=EAProperty(),
    notes=EAProperty(),
    nulledOut=EAProperty('nulled'),
    number=EAProperty(),
    numberOfCards=EAProperty('num_cards', 'cards'),
    numberTimesRenewed=EAProperty('times_renewed', 'renewals'),
    occupation=EAProperty(),
    onlineReferenceNumber=EAProperty('reference_number', 'ref_number'),
    onlyMyBatches=EAProperty('only_mine'),
    openCount=EAProperty('opens'),
    optInStatus=EAProperty('opt_in'),
    orderby=EAProperty('order_by'),
    organizationContactName=EAProperty('organization_contact', 'org_contact'),
    organizationContactOfficialName=EAProperty('organization_contact_official', 'org_contact_official'),
    organizationId=EAProperty('organization', 'org'),
    organizationRoles=EAProperty('org_roles', singular_alias='org_role'),
    organizeAt=EAProperty(),
    originalAmount=EAProperty('original'),
    originalRowCount=EAProperty('original_count', 'original'),
    outOfRange=EAProperty('OOR'),
    overwriteExistingListId=EAProperty('overwrite_existing_id', 'overwrite_id', 'overwrite'),
    parentCodeId=EAProperty('parent_code'),
    parentDepartmentId=EAProperty('parent_department', 'parent'),
    parentFieldId=EAProperty('parent_field', 'parent'),
    parentFieldName=EAProperty('parent_field', 'parent'),
    parentId=EAProperty('parent'),
    parentOrganization=EAProperty('parent', factory=_organization_factory),
    parentValueId=EAProperty('parent_value'),
    party=EAProperty(),
    paymentType=EAProperty(),
    personIdColumn=EAProperty('id_column', 'id_col'),
    personIdType=EAProperty('person_type'),
    personType=EAProperty(),
    phone=EAProperty(),
    phoneId=EAProperty('phone'),
    points=EAProperty(),
    preview=EAProperty(),
    primaryContact=EAProperty(),
    primaryCustomField=EAProperty('primary_custom'),
    processedAmount=EAProperty(),
    processedCurrency=EAProperty(),
    professionalSuffix=EAProperty(),
    properties=EAProperty(singular_alias='property'),
    question=EAProperty(),
    questionId=EAProperty('question'),
    recipientCount=EAProperty('recipients'),
    recordCount=EAProperty('records'),
    recurrenceType=EAProperty('recurrence'),
    referenceCode=EAProperty('reference'),
    relationshipId=EAProperty('relationship'),
    remainingAmount=EAProperty('remaining'),
    replyToEmail=EAProperty('reply_to'),
    requestedCustomFieldIds=EAProperty('custom_field_ids', 'custom_fields', singular_alias='custom_field'),
    requestedFields=EAProperty('fields', singular_alias='field'),
    requestedIds=EAProperty('ids', singular_alias='id'),
    resourceType=EAProperty('resource'),
    resourceTypes=EAProperty('resources', singular_alias='resource'),
    resourceUrl=EAProperty('url'),
    responseId=EAProperty('response'),
    result=EAProperty(),
    resultCodeId=EAProperty('result_code'),
    resultFileColumnName=EAProperty('result_column_name', 'result_column', 'column_name', 'column'),
    resultFileSizeKbLimit=EAProperty('size_kb_limit', 'kb_limit'),
    resultFileSizeLimitKb=EAProperty('size_kb_limit', 'kb_limit'),
    resultOutcomeGroup=EAProperty('outcome_group'),
    salutation=EAProperty(),
    savedListId=EAProperty('saved_list', 'list'),
    scoreColumn=EAProperty('score_col'),
    scoreId=EAProperty('score'),
    scriptQuestion=EAProperty('question'),
    searchKeyword=EAProperty('search', 'keyword'),
    selectedOneTimeAmount=EAProperty('selected_one_time'),
    selfReportedEthnicities=EAProperty('ethnicities', is_array=True),
    selfReportedEthnicity=EAProperty('ethnicity'),
    selfReportedGenders=EAProperty('genders', singular_alias='gender'),
    selfReportedLanguagePreference=EAProperty('language_preference', 'language'),
    selfReportedRace=EAProperty('race'),
    selfReportedRaces=EAProperty('races', is_array=True),
    selfReportedSexualOrientations=EAProperty('sexual_orientations', singular_alias='sexual_orientation'),
    senderDisplayName=EAProperty('sender_display', 'sender_name'),
    senderEmailAddress=EAProperty('sender_email'),
    sex=EAProperty(),
    shortName=EAProperty('short'),
    smsOptInStatus=EAProperty('sms_opt_in'),
    sourceUrl=EAProperty('source', 'url'),
    sourceValue=EAProperty('source'),
    startingAfter=EAProperty('after'),
    startingBefore=EAProperty('before'),
    startDate=EAProperty('start'),
    startTime=EAProperty('start'),
    startTimeOverride=EAProperty('start_override', 'start'),
    stateCode=EAProperty('state'),
    stateOrProvince=EAProperty('state', 'province'),
    staticValue=EAProperty('static'),
    status=EAProperty(),
    statuses=EAProperty(),
    statusName=EAProperty('status'),
    subscriptionStatus=EAProperty('status'),
    supporterGroupId=EAProperty('supporter_group', 'group'),
    suffix=EAProperty(),
    surveyQuestionId=EAProperty('question'),
    surveyResponseId=EAProperty('response'),
    targetId=EAProperty('target'),
    targetValue=EAProperty('target'),
    text=EAProperty(),
    title=EAProperty(),
    tolerance=EAProperty('tolerance'),
    totalDuesPaid=EAProperty('total_paid'),
    totalRows=EAProperty('total'),
    turfName=EAProperty('turf'),
    type=EAProperty(),
    typeAndName=EAProperty(),
    typeId=EAProperty('type'),
    unitNo=EAProperty('unit'),
    unmatchedRowsCount=EAProperty('unmatched_count', 'unmatched'),
    unsubscribeCount=EAProperty('unsubscribes'),
    upsellType=EAProperty('upsell'),
    url=EAProperty(),
    username=EAProperty('user'),
    userFirstName=EAProperty('first_name', 'first'),
    userLastName=EAProperty('last_name', 'last'),
    value=EAProperty(),
    vanId=EAProperty('van'),
    webhookUrl=EAProperty('webhook', 'hook'),
    website=EAProperty(),
    zipOrPostalCode=EAProperty('zip_code', 'zip', 'postal_code', 'postal'),
    ID=EAProperty()
)


class ActivistCode(
    EAObjectWithIDAndName,
    _prefix='activistCode',
    _keys={'description', 'isMultiAssign', 'mediumName', 'scriptQuestion', 'shortName', 'status', 'type'}
):
    """Represents an `Activist Code
    <https://developers.everyaction.com/van-api#activist-codes-common-models>`__.
    """


class ActivistCodeData(
    EAObjectWithIDAndName,
    _prefix='activistCode',
    _prefixed={'name', 'typeAndName'},
    _keys={'canvassedBy', 'dateCanvassed', 'dateCreated'}
):
    """Represents the data associated with responses to `getting Activist Codes
    <https://developers.everyaction.com/van-api#people-get-people--vanid--activistcodes>`__.
    """


class Adjustment(EAObject, _keys={'adjustmentType', 'amount', 'datePosted'}):
    """Represents the data associated with responses to `adjusting a Contribution
    <https://developers.everyaction.com/van-api#contributions-post-contributions--contributionid--adjustments>`__.
    """


class AdjustmentResponse(EAObject, _keys={'contributionId', 'dateAdjusted', 'originalAmount', 'remainingAmount'}):
    """Represents the data associated with a response to a `Contribution adjustment
    <https://developers.everyaction.com/van-api#contributions-post-contributions--contributionid--adjustments>`__.
    """


class APIKeyProfile(
    EAObject,
    _keys={
        'apiKeyTypeName',
        'committeeName',
        'databaseName',
        'hasMyCampaign',
        'hasMyVoters',
        'keyReference',
        'username',
        'userFirstName',
        'userLastName'
    }
):
    """Represents an `API key profile
    <https://developers.everyaction.com/van-api#everyaction-8-introspection>`__.
    """


class Attribution(EAObject, _keys={'amountAttributed', 'attributionType', 'dateThanked', 'notes', 'vanId'}):
    """Represents an `Attribution object
    <https://developers.everyaction.com/van-api#contributions-common-models>`__.
    """


class AvailableValue(EAObjectWithIDAndName, _keys={'parentValueId'}):
    """Represents
    `AvailableValues <https://developers.everyaction.com/van-api#custom-fields-common-models>`__.
    for a Custom Field.
    """


class BallotRequestType(EAObjectWithIDAndName, _prefix='ballotRequestType'):
    """Represents a `Ballot Request Type
    <https://developers.everyaction.com/van-api#ballots-common-models>`__.
    """


class BallotReturnStatus(EAObjectWithIDAndName, _prefix='ballotReturnStatus'):
    """Represents a `Ballot Return Status
    <https://developers.everyaction.com/van-api#ballots-common-models>`__.
    """


class BallotType(EAObjectWithIDAndName, _prefix='ballotType'):
    """Represents a `Ballot Type
    <https://developers.everyaction.com/van-api#ballots-common-models>`__.
    """


class BankAccount(EAObjectWithIDAndName, _prefix='bankAccount'):
    """Represents a `Bank Account object
    <https://developers.everyaction.com/van-api#contributions-common-models>`__.
    """


class BargainingUnit(EAObjectWithIDAndName, _prefix='bargainingUnit', _keys={'employerBargainingUnitId', 'shortName'}):
    """Represents a `Bargaining Unit
    <https://developers.everyaction.com/van-api#bargaining-units>`__.
    """


class BatchForm(EAObjectWithIDAndName, _prefix='form'):
    """Represents a form for `Voter Registration Batches
    <https://developers.everyaction.com/van-api#voter-registration-batches-common-models>`__.
    """


class BatchProgram(EAObjectWithID, _prefix='programType'):
    """Represents a program for `Voter Registration Batches
    <https://developers.everyaction.com/van-api#voter-registration-batches-common-models>`__.
    """


class Canvasser(EAObjectWithID, _prefix='canvasser'):
    """Represents a `Canvasser
    <https://developers.everyaction.com/van-api#minivan-exports-common-models>`__.
    """


class CanvassContext(EAObject, _keys={'contactTypeId', 'dateCanvassed', 'inputTypeId', 'phoneId'}):
    """Represents a `Canvass Context
    <https://developers.everyaction.com/van-api#people-post-people--vanid--canvassresponses>`__.
    """


class ChangeType(EAObject, _prefix='changeType', _prefixed={'name'}, _keys={'description'}):
    """Represents a `changeType
    <https://developers.everyaction.com/van-api#changed-entities-get-changedentityexportjobs-changetypes--resourcetype>`__.
    """

    @classmethod
    def _id_key(cls) -> Optional[str]:
        return 'ID'


class CodeResult(EAObjectWithID, _prefix='code', _keys={'message'}):
    """Represents the data associated with a response to a code batch request. See `POST /codes/batch
    <https://developers.everyaction.com/van-api#codes-post-codes-batch>`__
    for an example.
    """


class Column(EAObjectWithName):
    """Represents a `Column
    <https://developers.everyaction.com/van-api#column-bi-anchor>`__.
    """


class Commitment(
    EAObjectWithID,
    _prefix='commitment',
    _keys={
        'amount',
        'ccExpirationMonth',
        'ccExpirationYear',
        'creditCardLast4',
        'currency',
        'designationId',
        'endDate',
        'frequency',
        'nextTransactionDate',
        'paymentType',
        'startDate',
        'status'
    }
):
    """Represents a `Commitment
    <https://developers.everyaction.com/van-api#commitments-common-models>`__.
    """


class ConfirmationEmailData(
    EAObject,
    _keys={
        'copyToEmails',
        'fromEmail',
        'fromName',
        'fromSubject',
        'isConfirmationEmailEnabled',
        'isRecurringEmailEnabled',
        'replyToEmail'
    }
):
    """Represents `Confirmation Email Data
    <https://developers.everyaction.com/van-api#online-actions-forms-confirmation-email-data>`__.
    """


class ContactType(EAObjectWithIDAndName, _prefix='contactType', _keys={'channelTypeName'}):
    """Represents a `Contact Type
    <https://developers.everyaction.com/van-api#canvass-responses-get-canvassresponses-contacttypes>`__.
    """


class Constraints(EAObject, _keys={'invalidCharacters'}):
    """Represents a description of the violated constraints for :class:`.Error` objects."""


class ContactHistory(EAObject, _keys={'contactTypeId', 'dateCanvassed', 'inputTypeId', 'resultCodeId'}):
    """Represents a `Contact History object
    <https://developers.everyaction.com/van-api#contact-notes-contact-history>`__.
    """


class Currency(EAObject, _keys={'amount', 'currencyType'}):
    """Represents the type and the amount of a currency. Found, for instance, in the response of
    `GET /people/{vanId}/membership
    <https://developers.everyaction.com/van-api#people-get-people--vanid--membership>`__.
    """


class CustomFieldValue(EAObject, _keys={'assignedValue', 'customFieldGroupId', 'customFieldId'}):
    """Represents a `CustomFieldValue
    <https://developers.everyaction.com/van-api#people-common-models>`__.
    """

    def __init__(
        self,
        customFieldId: Optional[int] = None,
        customFieldGroupId: Optional[int] = None,
        assignedValue: Optional[str] = None,
        **kwargs: EAValue
    ) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param customFieldId: ID of the custom field.
        :param customFieldGroupId: ID of the group of the custom field.
        :param assignedValue: Value assigned to the custom field.
        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(
            customFieldId=customFieldId,
            customFieldGroupId=customFieldGroupId,
            assignedValue=assignedValue,
            **kwargs
        )


class Department(EAObjectWithIDAndName, _prefix='department', _keys={'employer', 'parentDepartmentId'}):
    """Represents a `Department
    <https://developers.everyaction.com/van-api#departments-common-models>`__.
    """


class Designation(EAObjectWithIDAndName, _prefix='designation'):
    """Represents a `Designation
    <https://developers.everyaction.com/van-api#designations-get-designations>`__.
    """


class DisclosureFieldValue(EAObjectWithID, _prefix='disclosureField', _prefixed={'value'}, _keys={'designationId'}):
    """Represents a `Disclosure Field Value
    <https://developers.everyaction.com/van-api#people-common-models>`__.
    """

    def __init__(
        self,
        disclosureFieldId: Optional[int] = None,
        disclosureFieldValue: Optional[str] = None,
        designationId: Optional[int] = None,
        **kwargs: EAValue
    ) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param disclosureFieldId: ID of the disclosure field.
        :param disclosureFieldValue: Value for the disclosure field.
        :param designationId: ID of designation.
        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(
            disclosureFieldId=disclosureFieldId,
            disclosureFieldValue=disclosureFieldValue,
            designationId=designationId,
            **kwargs
        )


class DistrictFieldValue(EAObjectWithIDAndName, _keys={'parentId'}):
    """Represents a `District Field Value
    <https://developers.everyaction.com/van-api#district-fields-get-districtfields>`__.
    """


class Email(EAObject, _keys={'dateCreated', 'email', 'isPreferred', 'isSubscribed', 'subscriptionStatus', 'type'}):
    """Represents an `Email
    <https://developers.everyaction.com/van-api#people-common-models>`__.
    """

    def __init__(self, email: Optional[str] = None, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param email: The email address.
        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(email=email, **kwargs)


class EmailMessageContentDistributions(
    EAObject,
    _keys={
        'bounceCount',
        'contributionCount',
        'contributionTotal',
        'dateSent',
        'formSubmissionCount',
        'linksClickedCount',
        'openCount',
        'recipientCount',
        'unsubscribeCount'
    }
):
    """Represents an `Email Message Content Distributions object
    <https://developers.everyaction.com/van-api#email-common-models>`__.
    """


class EventRole(EAObjectWithIDAndName, _prefix='role', _keys={'goal', 'isEventLead', 'max', 'min'}):
    """Represents a `Role
    <https://developers.everyaction.com/van-api#events-common-models>`__
    for an Event Type.
    """


class EventShift(EAObjectWithIDAndName, _prefix='eventShift', _keys={'endTime', 'startTime'}):
    """Represents a `Shift
    <https://developers.everyaction.com/van-api#events-common-models>`__.
    """


class ExportJobType(EAObjectWithIDAndName, _prefix='exportJobType'):
    """Represents an `Export Job Type
    <https://developers.everyaction.com/van-api#export-jobs-get-exportjobtypes>`__.
    """


class File(EAObject, _keys={'dateExpired', 'downloadUrl', 'recordCount'}):
    """Represents a `File object
    <https://developers.everyaction.com/van-api#bulk-import-common-models>`__
    in EveryAction. Used in many contexts.
    """


class FinancialBatch(
    EAObjectWithIDAndName,
    _prefix='financialBatch',
    _prefixed={'name', 'number'},
    _keys={
        'bankAccountId',
        'checkDate',
        'checkNumber',
        'dateClosed',
        'dateDeposited',
        'dateOpened',
        'depositNumber',
        'designationId',
        'expectedContributionCount',
        'expectedContributionTotalAmount',
        'isAutoGenerated',
        'isOpen'
    }
):
    """Represents a `Financial Batch
    <https://developers.everyaction.com/van-api#financial-batches-common-models>`__.
    """


class Folder(EAObjectWithIDAndName, _prefix='folder'):
    """Represents a `folder
    <https://developers.everyaction.com/van-api#folders>`__.
    """


class GeoCoordinate(EAObject, _keys={'lat', 'lon'}):
    """Represents a `Geographic Coordinate
    <https://developers.everyaction.com/van-api#locations>`__.
    """


class Identifier(EAObject, _keys={'externalId', 'type'}):
    """Represents an `Identifier
    <https://developers.everyaction.com/van-api#people-common-models>`__.
    """


class IsCellStatus(EAObjectWithIDAndName, _prefix='status', _prefixed={'name'}):
    """Represents an `Phone Is a Cell Status
    <https://developers.everyaction.com/van-api#phones-get-phones-iscellstatuses>`__.
    """


class JobActionType(EAObject, _keys={'actionType'}):
    """Represents a `Job Action Type
    <https://developers.everyaction.com/van-api#job-action-anchor>`__.
    """

    @staticmethod
    def make(**kwargs: EAValue) -> 'JobActionType':
        action_type = EAProperty.shared('actionType').find('actionType', kwargs, pop=True)
        if not action_type:
            raise EAException('Expected actionType property or alias to be specified for JobActionType')
        lower = action_type.lower()

        if lower == 'score':
            return ScoreLoadAction(**kwargs)
        if lower == 'avevdatafile':
            return AVEVDataFileAction(**kwargs)
        if lower == 'loadsavedlistfile':
            return SavedListLoadAction(**kwargs)
        raise EAException(f'Unrecognized Job Action Type {action_type}')


class JobClass(EAObjectWithIDAndName, _prefix='jobClass', _keys={'shortName'}):
    """Represents a `Job Class
    <https://developers.everyaction.com/van-api#job-classes-common-models>`__.
    """


class JobNotification(EAObject, _keys={'description', 'message', 'status'}):
    """Represents a `Notification
    <https://developers.everyaction.com/van-api#notification-anchor>`__
    for File Loading Jobs.
    """


class InputType(EAObjectWithIDAndName, _prefix='inputType'):
    """Represents an `Input Type
    <https://developers.everyaction.com/van-api#canvass-responses-get-canvassresponses-inputtypes>`__.
    """


class KeyValuePair(EAObject, _keys={'key', 'value'}):
    """Represents a key value pair for possible values of a `Support Field
    <https://developers.everyaction.com/van-api#voter-registration-batches-get-voterregistrationbatches-states--state--supportedfields>`__.
    """


class Listener(EAObject, _keys={'type', 'value'}):
    """Represents a `Listener
    <https://developers.everyaction.com/van-api#file-loading-jobs-overview>`__.
    """


class MembershipSourceCode(EAObjectWithIDAndName, _prefix='code', _prefixed={'name'}):
    """Represents a `Membership Source Code
    <https://developers.everyaction.com/van-api#people-get-people--vanid--membership>`__.
    """


class MemberStatus(EAObjectWithIDAndName, _prefix='memberStatus', _keys={'isMember'}):
    """Represents a `Member Status
    <https://developers.everyaction.com/van-api#member-statuses-common-models>`__.
    """


class NoteCategory(EAObjectWithIDAndName, _prefix='noteCategory', _keys={'assignableTypes'}):
    """Represents a `Note Category
    <https://developers.everyaction.com/van-api#notes-common-models>`__.
    """


class Organization(
    EAObjectWithIDAndName,
    _prefix='organization',
    _prefixed={'type'},
    _keys={'parentOrganization', 'shortName', 'website'},
):
    """Represents an `Organization
    <https://developers.everyaction.com/van-api#employers-common-models>`__.
    """


class OrganizationPhone(
    EAObjectWithID,
    _prefix='organizationPhone',
    _keys={
        'confidenceLevel',
        'countryCode',
        'dialingPrefix',
        'organizationId',
        'phone',
    },
    phoneType=EAProperty('type')
):
    """Represents a `Phone for an organization
    <https://developers.everyaction.com/van-api#employers-common-models>`__.
    """


class Pledge(EAObjectWithID, _prefix='pledge'):
    """Represents a `Pledge object
    <https://developers.everyaction.com/van-api#contributions-common-models>`__.
    """


class PreferredPronoun(EAObjectWithIDAndName, _prefix='preferredPronoun', _prefixed={'name'}):
    """Represents a `preferred pronoun
    <https://developers.everyaction.com/van-api#reported-demographics-get-pronouns>`__.
    """


class PrintedList(EAObjectWithName, _keys={'number'}):
    """Represents a `Printed List
    <https://developers.everyaction.com/van-api#printed-lists-common-models>`__.
    """


class ProgramType(EAObjectWithIDAndName, _prefix='programType'):
    """Represents a `Program Type
    <https://developers.everyaction.com/van-api#voter-registration-batches-get-voterregistrationbatches-programtypes>`__.
    """


class RegistrationForm(EAObjectWithIDAndName, _prefix='form'):
    """Represents a `Registration Form
    <https://developers.everyaction.com/van-api#voter-registration-batches-get-voterregistrationbatches-registrationforms>`__.
    """


class RelationalMapping(EAObject, _keys={'fieldName', 'value'}):
    """Represents a `Relational Mapping
    <https://developers.everyaction.com/van-api#changed-entities-get-changedentityexportjobs-fields--resourcetype>`__.
    """


class Relationship(EAObjectWithIDAndName):
    """Represents a `Relationship
    <https://developers.everyaction.com/van-api#relationships-get-relationships>`__.
    """


class ReportedEthnicity(EAObjectWithIDAndName, _prefix='reportedEthnicity', _prefixed={'name'}):
    """Represents a `Reported Ethnicity
    <https://developers.everyaction.com/van-api#reported-demographics-get-reportedethnicities>`__.
    """


class ReportedGender(EAObjectWithIDAndName, _prefix='reportedGender', _prefixed={'name'}):
    """Represents a `Reported Gender
    <https://developers.everyaction.com/van-api#reported-demographics-get-reportedgenders>`__.
    """


class ReportedLanguagePreference(EAObjectWithIDAndName, _prefix='reportedLanguagePreference', _prefixed={'name'}):
    """Represents a `Reported Language Preference
    <https://developers.everyaction.com/van-api#reported-demographics-get-reportedlanguagepreferences>`__.
    """


class ReportedRace(EAObjectWithIDAndName, _prefix='reportedRace', _prefixed={'name'}):
    """Represents a `Reported Race
    <https://developers.everyaction.com/van-api#reported-demographics-get-reportedraces>`__.
    """


class ReportedSexualOrientation(EAObjectWithIDAndName, _prefix='reportedSexualOrientation', _prefixed={'name'}):
    """Represents a `Reported Sexual Orientation
    <https://developers.everyaction.com/van-api#reported-demographics-get-reportedsexualorientations>`__.
    """


class ResultCode(EAObjectWithIDAndName, _prefix='resultCode', _keys={'mediumName', 'resultOutcomeGroup', 'shortName'}):
    """Represents a `Result Code
    <https://developers.everyaction.com/van-api#canvass-responses-get-canvassresponses-resultcodes>`__.
    """


class SavedList(EAObjectWithIDAndName, _prefix='savedList', _keys={'description', 'doorCount', 'listCount'}):
    """Represents a `Saved List
    <https://developers.everyaction.com/van-api#saved-lists-common-models>`__.
    """


class SavedListData(
    EAObjectWithID,
    _prefix='savedList',
    _keys={'matchedRowsCount', 'originalRowCount', 'unmatchedRowsCount'}
):
    """Represents `Saved List Data
    <https://developers.everyaction.com/van-api#saved-list-load-anchor>`__
    for Saved List Load actions.
    """


class ScheduleType(EAObjectWithIDAndName, _prefix='scheduleType'):
    """Represents a `Schedule Type
    <https://developers.everyaction.com/van-api#schedule-types>`__.
    """


class Score(EAObjectWithIDAndName, _prefix='score', _keys={'description', 'maxValue', 'minValue', 'shortName'}):
    """Represents a `Score
    <https://developers.everyaction.com/van-api#scores-overview>`__.
    """


class ScoreApprovalCriteria(EAObject, _keys={'average', 'tolerance'}):
    """Represents `Score Approval Criteria
    <https://developers.everyaction.com/van-api#score-load-action-anchor>`__
    """


class ScriptResponse(EAObject, _keys={'type'}):
    """Represents a `Script Response
    <https://developers.everyaction.com/van-api#people-post-people--vanid--canvassresponses>`__.
    """

    _PROPERTIES = {
        'type': EAProperty()
    }

    @staticmethod
    def make(**kwargs: EAValue) -> 'ScriptResponse':
        typ = kwargs.pop('type', None)
        if typ is None:
            raise EAException('Expected type for ScriptResponse')
        lower = typ.lower()

        if lower == 'activistcode':
            return ActivistCodeResponse(**kwargs)
        if lower == 'surveyresponse':
            return SurveyCanvassResponse(**kwargs)
        if lower == 'volunteeractivity':
            return VolunteerActivityResponse(**kwargs)
        raise EAException(f'Unrecognized Script Response type: {typ}')


class ShiftType(EAObjectWithIDAndName, _prefix='shiftType', _keys={'defaultEndTime', 'defaultStartTime'}):
    """Represents a `Shift Type
    <https://developers.everyaction.com/van-api#employers-common-models>`__.
    """


class Status(EAObjectWithIDAndName, _prefix='status'):
    """Represents a `Status
    <https://developers.everyaction.com/van-api#event-types>`__
    in EveryAction. Used in multiple contexts.
    """


class StoryStatus(EAObjectWithIDAndName, _prefix='storyStatus'):
    """Represents a `StoryStatus
    <https://developers.everyaction.com/van-api#stories-common-models>`__.
    """

    @classmethod
    def _name_key(cls) -> Optional[str]:
        return 'statusName'


class Subgroup(EAObjectWithIDAndName, _prefix='subgroup', _keys={'fullName', 'isAssociatedWithBadges'}):
    """Represents a `Subgroup
    <https://developers.everyaction.com/van-api#targets-common-models>`__
    for a Target.
    """


class SupportedEntity(EAObjectWithName, _keys={'isApplicable', 'isSearchable'}):
    """Represents a `Supported Entity
    <https://developers.everyaction.com/van-api#codes-common-models>`__
    in the context of codes.
    """


class SupporterGroup(EAObjectWithIDAndName, _keys={'description'}):
    """Represents a `Supporter Group
    <https://developers.everyaction.com/van-api#supporter-groups-common-models>`__.
    """


class Suppression(EAObjectWithName, _prefix='suppression', _prefixed={'code', 'name'}):
    """Represents a `Suppression
    <https://developers.everyaction.com/van-api#people-common-models>`__.
    """

    def __init__(
        self,
        code_or_name: Optional[str] = None,
        **kwargs: EAValue
    ) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate. When the positional argument `code_or_name` is given, it is assumed to be a
        code (e.g., "NC" for "Do not call") when it has length at most 2, and otherwise it is assumed to be a name.

        :param code_or_name: When the given, it is assumed to be a code (e.g., "NC" for "Do not call") when it has
            length at most 2, and otherwise it is assumed to be a name.
        :param kwargs: Mapping of (alias or name) -> value.
        """
        if code_or_name:
            # Infer from str length whether it is a name or a code.
            if len(code_or_name) >= 2:
                super().__init__(suppressionName=code_or_name, **kwargs)
            else:
                super().__init__(suppressionCode=code_or_name, **kwargs)
        else:
            super().__init__(**kwargs)


class SurveyResponse(EAObjectWithIDAndName, _prefix='surveyResponse', _keys={'mediumName', 'shortName'}):
    """
    Represents a `Survey Response
    <https://developers.everyaction.com/van-api#survey-questions-common-models>`__.
    """


class UpdateStatistics(
    EAObject
):
    """Represents an `Update Statistics
    <https://developers.everyaction.com/van-api#score-updates>`__.
    """


class User(EAObjectWithID, _prefix='user', _keys={'firstName', 'lastName'}):
    """Represents a `VAN User
    <https://developers.everyaction.com/van-api#extended-source-codes>`__.
    """


class ValueMapping(EAObjectWithIDAndName, _keys={'parentId', 'sourceValue', 'targetValue'}):
    """Represents a `value
    <https://developers.everyaction.com/van-api#bulk-import-post-bulkimportjobs>`__
    in the context of bulk import jobs.
    """


class WorkArea(EAObjectWithIDAndName, _prefix='workArea'):
    """Represents a `Work Area
    <https://developers.everyaction.com/van-api#worksites-common-models>`__.
    """


# --- Second Order Properties and Objects ---
EAProperty.share(
    activistCodes=EAProperty(singular_alias='activist_code', factory=ActivistCode),
    approvalCriteria=EAProperty('criteria', factory=ScoreApprovalCriteria),
    availableValues=EAProperty('available', 'values', singular_alias='value', factory=AvailableValue),
    bargainingUnit=EAProperty(factory=BargainingUnit),
    bargainingUnits=EAProperty(singular_alias='bargaining_unit', factory=BargainingUnit),
    canvassers=EAProperty(singular_alias='canvasser', factory=Canvasser),
    canvassContext=EAProperty('context', factory=CanvassContext),
    category=EAProperty(factory=NoteCategory),
    columns=EAProperty(singular_alias='column', factory=Column),
    columnsToIncludeInResultsFile=EAProperty(
        'include_columns',
        'include',
        singular_alias='include_column',
        factory=Column
    ),
    confirmationEmailData=EAProperty(
        'confirmation_email',
        'confirmation_data',
        'confirmation',
        factory=ConfirmationEmailData
    ),
    contactAttributions=EAProperty('attributions', factory=Attribution),
    contactHistory=EAProperty('history', factory=ContactHistory),
    contributionBankAccount=EAProperty('contribution_account', 'account_obj', factory=BankAccount),
    customFieldValues=EAProperty('custom_values', singular_alias='custom_value', factory=CustomFieldValue),
    customProperties=EAProperty('properties', singular_alias='property', factory=KeyValuePair),
    departments=EAProperty(singular_alias='department', factory=Department),
    designation=EAProperty(factory=Designation),
    detailedConstraints=EAProperty('constraints', factory=Constraints),
    disclosureFieldValues=EAProperty(
        'disclosures',
        'field_values',
        'values',
        singular_alias='disclosure',
        factory=DisclosureFieldValue
    ),
    districtFieldValue=EAProperty(factory=DistrictFieldValue),
    districtFieldValues=EAProperty('values', singular_alias='value', factory=DistrictFieldValue),
    duesPaid=EAProperty(factory=Currency),
    emailMessageContentDistributions=EAProperty('distributions', factory=EmailMessageContentDistributions),
    file=EAProperty(factory=File),
    files=EAProperty(singular_alias='file', factory=File),
    firstMembershipSourceCode=EAProperty('first_source_code', 'source_code', factory=MembershipSourceCode),
    form=EAProperty(factory=BatchForm),
    geoLocation=EAProperty('geo',  'location', factory=GeoCoordinate),
    identifiers=EAProperty(singular_alias='identifier', factory=Identifier),
    isCellStatus=EAProperty('cell_status', 'is_cell', factory=IsCellStatus),
    jobClass=EAProperty(factory=JobClass),
    limitedToParentValues=EAProperty('limited_to', is_array=True, factory=AvailableValue),
    listeners=EAProperty(singular_alias='listener', factory=Listener),
    pledge=EAProperty(factory=Pledge),
    possibleValues=EAProperty('possible', singular_alias='possible_value', factory=KeyValuePair),
    preferredPronoun=EAProperty(factory=PreferredPronoun),
    programType=EAProperty('program', factory=BatchProgram),
    relationalMappings=EAProperty('relations', singular_alias='relation', factory=RelationalMapping),
    resultFiles=EAProperty('files', singular_alias='file', factory=File),
    role=EAProperty(factory=EventRole),
    roles=EAProperty(singular_alias='role', factory=EventRole),
    savedList=EAProperty('list', factory=SavedListData),
    score=EAProperty(factory=Score),
    scores=EAProperty(singular_alias='score', factory=Score),
    shift=EAProperty(factory=EventShift),
    shifts=EAProperty(singular_alias='shift', factory=EventShift),
    storyStatus=EAProperty('status', factory=StoryStatus),
    subgroups=EAProperty(singular_alias='subgroup', factory=Subgroup),
    suppressions=EAProperty(singular_alias='suppression', factory=Suppression),
    supportedEntities=EAProperty('entities', singular_alias='entity', factory=SupportedEntity),
    updateStatistics=EAProperty('update_stats', 'statistics', 'stats', factory=UpdateStatistics),
    values=EAProperty(singular_alias='value', factory=ValueMapping)
)


class ActivistCodeResponse(ScriptResponse, EAObjectWithID, _prefix='activistCode', _keys={'action'}):
    """Represents an `Activist Code Response
    <https://developers.everyaction.com/van-api#people-post-people--vanid--canvassresponses>`__.
    """

    def __init__(self, id: Optional[int] = None, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param id: ID to initialize with. When given alone, a simple object results (see
            `A Note About Simple Objects <https://developers.everyaction.com/van-api#events-overview>`__).
        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(type='ActivistCode', activistCodeId=id, **kwargs)


class Address(
    EAObjectWithID,
    _prefix='address',
    _prefixed={'line1', 'line2', 'line3'},
    _keys={
        'city',
        'countryCode',
        'displayMode',
        'geoLocation',
        'isPreferred',
        'preview',
        'stateOrProvince',
        'type',
        'zipOrPostalCode'
    }
):
    """Represents an `Address
    <https://developers.everyaction.com/van-api#people-common-models>`__.
    """


class AVEVDataFileAction(JobActionType):
    """Represents an `AVEV Data File Action
    <https://developers.everyaction.com/van-api#AVEVDataFile-anchor>`__.
    """

    def __init__(self, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(actionType='AVEVDataFile', **kwargs)


class BargainingUnitJobClass(
    EAObjectWithID,
    _prefix='employerBargainingUnitJobClass',
    _keys={'bargainingUnit', 'employerBargainingUnitId', 'jobClass'}
):
    """Represents an `Employer Bargaining Unit Job Class
    <https://developers.everyaction.com/van-api#employers-common-models>`__.
    """


class ChangedEntityBulkImportField(EAObject, _keys={'fieldName', 'mappingTypeName', 'relationalMappings'}):
    """Represents a `bulk import field
    <https://developers.everyaction.com/van-api#changed-entities-get-changedentityexportjobs-fields--resourcetype>`__
    in the context of changed entities.
    """


class ChangedEntityExportJob(
    EAObjectWithID,
    _prefix='exportJob',
    _keys={
        'code',
        'dateChangedFrom',
        'dateChangedTo',
        'excludeChangesFromSelf',
        'exportedRecordCount',
        'files',
        'fileSizeKbLimit',
        'includeInactive',
        'jobStatus',
        'message',
        'requestedCustomFieldIds',
        'requestedFields',
        'requestedIds',
        'resourceType'
    }
):
    """Represents data for an existing `ChangedEntityExportJob
    <https://developers.everyaction.com/van-api#changed-entities-common-models>`__.
    """


class Code(
    EAObjectWithIDAndName,
    _prefix='code',
    _prefixed={'type'},
    _keys={'dateCreated', 'dateModified', 'description', 'parentCodeId', 'supportedEntities'}
):
    """Represents a `Code object
    <https://developers.everyaction.com/van-api#codes-common-models>`__.
    """


class CustomField(
    EAObjectWithIDAndName,
    _prefix='customField',
    _prefixed={'groupId', 'groupName', 'groupType', 'name', 'parentId', 'typeId'},
    _keys={'availableValues', 'isEditable', 'isExportable', 'maxTextboxCharacters'}
):
    """Represents a `Custom Field
    <https://developers.everyaction.com/van-api#custom-fields-common-models>`__.
    """


class DistrictField(
    EAObjectWithIDAndName,
    _prefix='districtField',
    _prefixed={'values'},
    _keys={'isCustomDistrict', 'parentFieldId'}
):
    """Represents a `District Field
    <https://developers.everyaction.com/van-api#district-fields-get-districtfields>`__.
    """


class EmailMessageContent(
    EAObject,
    _keys={'createdBy', 'dateCreated', 'emailMessageContentDistributions', 'senderDisplayName', 'senderEmailAddress'}
):
    """Represents an `email message content object
    <https://developers.everyaction.com/van-api#email-common-models>`__.
    """


class EmployerBargainingUnit(EAObjectWithID, _prefix='employerBargainingUnit', _keys={'bargainingUnit'}):
    """Represents an `Employer Bargaining Unit
    <https://developers.everyaction.com/van-api#employers-post-employers--employerid--bargainingunits--bargainingunitid>`__.
    """


class Error(
    EAObject,
    _keys={'code', 'detailedConstraints', 'detailedCode', 'hint', 'properties', 'referenceCode', 'resourceUrl', 'text'}
):
    """Represents an `Error object
    <https://developers.everyaction.com/van-api#bulk-import-common-models>`__.
    """


class ExtendedSourceCode(
    EAObjectWithIDAndName,
    _prefix='extendedSourceCode',
    _prefixed={'name'},
    _keys={'dateCreated', 'dateModified', 'modifiedBy'},
    createdBy=EAProperty('creator', factory=User)
):
    """Represents an `Extended Source Code
    <https://developers.everyaction.com/van-api#extended-source-codes>`__.
    """


class FieldValueMapping(EAObject, _keys={'columnName', 'fieldName', 'staticValue', 'values'}):
    """Represents a `fieldValueMapping
    <https://developers.everyaction.com/van-api#bulk-import-post-bulkimportjobs>`__.
    """


class JobFile(
    EAObject,
    _prefix='file',
    _prefixed={'name'},
    _keys={'columns', 'columnDelimiter', 'hasHeader', 'hasQuotes', 'sourceUrl'}
):
    """Represents a `file object for a job
    <https://developers.everyaction.com/van-api#file-bi-anchor>`__.
    """


class ListLoadCallbackData(JobNotification, _keys={'description', 'message', 'savedList', 'status'}):
    """Represents `Callback Data
    <https://developers.everyaction.com/van-api#saved-list-load-anchor>`__
    for a Saved List Load action.
    """


class MappingParent(EAObject, _keys={'limitedToParentValues', 'parentFieldName'}):
    """Represents prerequisites for mapping a field as described `here
    <https://developers.everyaction.com/van-api#bulk-import-get-bulkimportmappingtypes>`__.
    """


class Membership(
    EAObject,
    _keys={
        'changeTypeName',
        'dateCardsSent',
        'dateExpireMembership',
        'dateLastRenewed',
        'dateStartMembership',
        'duesAttributionTypeName',
        'duesEntityTypeName',
        'duesPaid',
        'enrollmentTypeName',
        'firstMembershipSourceCode',
        'levelId',
        'levelName',
        'numberOfCards',
        'numberTimesRenewed',
        'statusName',
        'totalDuesPaid'
    }
):
    """Contains `membership information
    <https://developers.everyaction.com/van-api#people-get-people--vanid--membership>`__
    for a person.
    """


class MiniVANExport(
    EAObjectWithIDAndName,
    _prefix='minivanExport',
    _keys={
        'canvassers',
        'databaseMode',
        'dateCreated'
    },
    createdBy=EAProperty('creator', factory=User)
):
    """Represents a `MiniVAN Export
    <https://developers.everyaction.com/van-api#minivan-exports-common-models>`__.
    """


class Note(
    EAObjectWithID,
    _prefix='note',
    _keys={'category', 'contactHistory', 'createdDate', 'isViewRestricted', 'text'}
):
    """Represents a `Note
    <https://developers.everyaction.com/van-api#people-get-people--vanid--notes>`__.
    """


class OnlineActionForm(
    EAObjectWithIDAndName,
    _prefix='formTracking',
    _keys={
        'activistCodes',
        'campaignId',
        'codeId',
        'confirmationEmailData',
        'createdByEmail',
        'dateCreated',
        'designation',
        'eventId',
        'isActive',
        'isConfirmedOptInEnabled',
        'modifiedByEmail'
    },
    formType=EAProperty('type'),
    formTypeId=EAProperty()
):
    """Represents an `Online Action Form
    <https://developers.everyaction.com/van-api#online-actions-forms-common-models>`__.
    """

    @classmethod
    def _name_key(cls) -> Optional[str]:
        return 'formName'


class Phone(
    EAObjectWithID,
    _prefix='phone',
    _prefixed={'number', 'optInStatus', 'type'},
    _keys={'countryCode', 'dateCreated', 'dialingPrefix', 'ext', 'isCellStatus', 'isPreferred', 'smsOptInStatus'}
):
    """Represents a `Phone
    <https://developers.everyaction.com/van-api#people-common-models>`__.
    """

    def __init__(self, id_or_number: Optional[Union[int, str]] = None, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param id_or_number: Either the phone ID (if an integer), or the phone number (if a string). A simple object
            will result when an integer is given for the `id_or_number` positional parameter
            (see `A Note About Simple Objects <https://developers.everyaction.com/van-api#events-overview)>`__.
            When a string is given instead, it is assumed to correspond to the phone number, accessible via
            instance.number.
        :param kwargs: Mapping of (alias or name) -> value.
        """

        if id_or_number is not None:
            if isinstance(id_or_number, int):
                # Assume id for int.
                super().__init__(id=id_or_number, **kwargs)
            elif isinstance(id_or_number, str):
                # Assume phone number for str.
                super().__init__(number=id_or_number, **kwargs)
            else:
                raise ValueError(f'Expected int or str for id_or_number, got {type(id_or_number)}: {id_or_number}')
        else:
            super().__init__(**kwargs)


class SavedListLoadAction(
    JobActionType,
    _keys={'folderId', 'listDescription', 'listName', 'overwriteExistingListId', 'personIdColumn', 'personIdType'}
):
    """Represents a `Saved List Load action
    <https://developers.everyaction.com/van-api#saved-list-load-anchor>`__.
    """

    def __init__(self, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(actionType='LoadSavedListFile', **kwargs)


class ScoreLoadAction(
    JobActionType,
    _keys={'approvalCriteria', 'personIdColumn', 'personIdType', 'scoreColumn', 'scoreId'}
):
    """Represents a `Score Load Action
    <https://developers.everyaction.com/van-api#score-load-action-anchor>`__.
    """

    def __init__(self, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(actionType='Score', **kwargs)


class ScoreUpdate(
    EAObjectWithID,
    _prefix='scoreUpdate',
    _keys={'dateProcessed', 'loadStatus', 'score', 'updateStatistics'}
):
    """Represents a `Score Update
    <https://developers.everyaction.com/van-api#score-updates-get-scoreupdates--scoreupdateid>`__.
    """


class SupportField(
    EAObject,
    _keys={'customPropertyKey', 'displayName', 'fieldType', 'maxFieldLength', 'possibleValues'}
):
    """Represents a `Support Field
    <https://developers.everyaction.com/van-api#voter-registration-batches-get-voterregistrationbatches-registrationforms>`__
    for a Voter Registration Batch.
    """


class SurveyCanvassResponse(
    ScriptResponse,
    _keys={'mediumName', 'name', 'shortName', 'surveyQuestionId', 'surveyResponseId'}
):
    """Represents a `Survey Response
    <https://developers.everyaction.com/van-api#people-post-people--vanid--canvassresponses>`__
    in the context of a canvass response.
    """

    def __init__(
        self,
        surveyQuestionId: Optional[int] = None,
        surveyResponseId: Optional[int] = None,
        **kwargs: EAValue
    ) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param surveyQuestionId: ID of the survey question.
        :param surveyResponseId: ID of the survey response.
        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(
            type='SurveyResponse',
            surveyQuestionId=surveyQuestionId,
            surveyResponseId=surveyResponseId,
            **kwargs
        )


class Target(
    EAObjectWithIDAndName,
    _prefix='target',
    _keys={'areSubgroupsSticky', 'description', 'points', 'status', 'subgroups', 'type'}
):
    """Represents a `Target
    <https://developers.everyaction.com/van-api#targets-common-models>`__.
    """


class TargetExportJob(
    EAObjectWithID,
    _prefix='exportJob',
    _keys={'file', 'jobStatus', 'targetId', 'webhookUrl'},
):
    """Represents a `Target Export Job
    <https://developers.everyaction.com/van-api#target-export-jobs-get-targetexportjobs--exportjobid>`__.
    """


class VolunteerActivityResponse(ScriptResponse, _prefix='volunteerActivity', _keys={'action'}):
    """Represents a `Volunteer Activity
    <https://developers.everyaction.com/van-api#people-post-people--vanid--canvassresponses>`__.
    """

    def __init__(self, id: Optional[int] = None, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param id: ID to initialize with. When given alone, a simple object results (see
            `A Note About Simple Objects <https://developers.everyaction.com/van-api#events-overview>`__).
        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(type='VolunteerActivity', volunteerActivityId=id, **kwargs)


class VoterRegistrationBatch(
    EAObjectWithIDAndName,
    _prefix='voterRegistrationBatch',
    _keys={'dateCreated', 'description', 'form', 'personType', 'programType', 'stateCode', 'status'}
):
    """Represents a `Voter Registration Batch
    <https://developers.everyaction.com/van-api#voter-registration-batches-common-models>`__.
    """


# --- Third Order Properties and Objects ---
EAProperty.share(
    address=EAProperty(factory=Address),
    addresses=EAProperty(singular_alias='address', factory=Address),
    bulkImportFields=EAProperty(singular_alias='bulk_import_field', factory=ChangedEntityBulkImportField),
    codes=EAProperty(singular_alias='code', factory=Code),
    customFields=EAProperty(singular_alias='custom_field', factory=CustomField),
    districts=EAProperty(singular_alias='district', factory=DistrictField),
    districtFields=EAProperty(singular_alias='district_field', factory=DistrictField),
    emails=EAProperty(singular_alias='email', factory=Email),
    emailMessageContent=EAProperty(singular_alias='content', factory=EmailMessageContent),
    errors=EAProperty(singular_alias='error', factory=Error),
    extendedSourceCode=EAProperty('extended_source', factory=ExtendedSourceCode),
    fieldValueMappings=EAProperty(
        'field_mappings',
        'value_mappings',
        'mappings',
        singular_alias='mapping',
        factory=FieldValueMapping
    ),
    jobClasses=EAProperty(singular_alias='job_class', factory=BargainingUnitJobClass),
    parents=EAProperty(singular_alias='parent', factory=MappingParent),
    phones=EAProperty(singular_alias='phone', factory=Phone),
    recordedAddresses=EAProperty(singular_alias='recorded_address', factory=Address),
    responses=EAProperty(singular_alias='response', factory=ScriptResponse.make),
    surveyQuestionResponses=EAProperty('responses', singular_alias='response', factory=SurveyResponse),
    tags=EAProperty(singular_alias='tag', factory=Code),
    voterRegistrationBatches=EAProperty(
        'registration_batches',
        'batches',
        singular_alias='batch',
        factory=VoterRegistrationBatch
    ),
    workAreas=EAProperty(singular_alias='work_area')
)


class AddRegistrantsResponse(EAObject, _keys={'alternateId', 'errors', 'result', 'vanId'}):
    """Represents the data associated with a response to `adding registrants
    <https://developers.everyaction.com/van-api#voter-registration-batches-post-voterregistrationbatches--batchid--people>`__
    to a Voter Registration Batch.
    """


class BulkImportField(
    EAObjectWithName,
    _keys={'canBeMappedToColumn', 'description', 'hasPredefinedValues', 'isRequired', 'parents'}
):
    """Represents a `mapping type field
    <https://developers.everyaction.com/van-api#bulk-import-get-bulkimportmappingtypes>`__.
    """


class BulkImportJobData(
    EAObjectWithID,
    _prefix='job',
    _keys={'errors', 'resourceType', 'resultFileSizeLimitKb', 'resultFiles', 'status'}
):
    """Represents data for an existing `Bulk Import Job
    <https://developers.everyaction.com/van-api#bulk-import-common-models>`__.
    """


class CanvassResponse(EAObject, _keys={'canvassContext', 'responses', 'resultCodeId'}):
    """Represents a `Canvass Response
    <https://developers.everyaction.com/van-api#people-post-people--vanid--canvassresponses>`__.
    """


class ChangedEntityField(
    EAObjectWithName,
    _keys={'availableValues', 'bulkImportFields', 'isCoreField', 'maxTextboxCharacters'},
    fieldType=EAProperty('type')
):
    """Represents a `changed entity field
    <https://developers.everyaction.com/van-api#changed-entities-get-changedentityexportjobs-fields--resourcetype>`__.
    """
    @classmethod
    def _name_key(cls) -> Optional[str]:
        return 'fieldName'


class Contribution(
    EAObject,
    _keys={
        'acceptedOneTimeAmount',
        'acceptedRecurringAmount',
        'amount',
        'bankAccount',
        'checkDate',
        'checkNumber',
        'codes',
        'contact',
        'contactAttributions',
        'contributionBankAccount',
        'contributionId',
        'coverCostsAmount',
        'dateReceived',
        'dateThanked',
        'depositDate',
        'depositNumber',
        'designation',
        'directMarketingCode',
        'disclosureFieldValues',
        'extendedSourceCode',
        'identifiers',
        'isUpsellAccepted',
        'isUpsellShown',
        'linkedJointFundraisingContributionId',
        'linkedPartnershipContributionId',
        'notes',
        'onlineReferenceNumber',
        'paymentType',
        'pledge',
        'processedAmount',
        'processedCurrency',
        'selectedOneTimeAmount',
        'status',
        'upsellType'
    }
):
    """Represents a `Contribution
    <https://developers.everyaction.com/van-api#contributions-common-models>`__.
    """


class Disbursement(
    EAObjectWithID,
    _prefix='disbursement',
    _keys={
        'amount',
        'batchCode',
        'checkDate',
        'checkNumber',
        'codes',
        'contact',
        'dateIssued',
        'designation',
        'disclosureFieldValues',
        'linkedCreditCardPaymentDisbursementId',
        'linkedReimbursementDisbursementId',
        'notes'
    }
):
    """Represents a `Disbursement
    <https://developers.everyaction.com/van-api#disbursements-common-models>`__.
    """


class EmailMessage(
    EAObjectWithIDAndName,
    _prefix='foreignMessage',
    _keys={'createdBy', 'dateCreated', 'dateModified', 'dateScheduled', 'emailMessageContent'},
    campaignID=EAProperty('campaign')
):
    """Represents an `email message
    <https://developers.everyaction.com/van-api#email-common-models>`__.
    """

    # TODO: Is emailMessageContent really an array? If so, can it actually contain multiple entities?


class FileLoadingJob(
    EAObjectWithID,
    _prefix='job',
    _keys={'description', 'interventionCallbackUrl', 'invalidRowsFileUrl', 'listeners'},
    actions=EAProperty(singular_alias='action', factory=JobActionType.make),
    file=EAProperty(factory=JobFile)
):
    """Represents a `File Loading Job
    <https://developers.everyaction.com/van-api#file-loading-jobs-overview>`__.
    """


class Location(EAObjectWithIDAndName, _prefix='location', _keys={'address', 'displayName'}):
    """Represents a `Location
    <https://developers.everyaction.com/van-api#locations>`__.
    """


class MappingType(EAObjectWithName, _keys={'fieldValueMappings', 'resultFileColumnName'}):
    """Represents a `bulk import mapping type
    <https://developers.everyaction.com/van-api#mapping-bi-anchor>`__.
    """


class Person(
    EAObjectWithID,
    _prefix='van',
    _keys={
        'additionalEnvelopeName',
        'additionalSalutation',
        'addresses',
        'biographyImageUrl',
        'caseworkCases',
        'caseworkIssues',
        'caseworkStories',
        'collectedLocationId',
        'contactMethodPreferenceCode',
        'contactMode',
        'contactModeId',
        'customFieldValues',
        'customProperties',
        'cycle',
        'dateOfBirth',
        'disclosureFieldValues',
        'districts',
        'electionRecords',
        'electionType',
        'emails',
        'envelopeName',
        'finderNumber',
        'firstName',
        'formalEnvelopeName',
        'formalSalutation',
        'identifiers',
        'lastName',
        'middleName',
        'nickname',
        'occupation',
        'organizationContactOfficialName',
        'organizationRoles',
        'party',
        'phones',
        'preferredPronoun',
        'primaryContact',
        'recordedAddresses',
        'salutation',
        'scores',
        'selfReportedEthnicities',
        'selfReportedEthnicity',
        'selfReportedGenders',
        'selfReportedLanguagePreference',
        'selfReportedRace',
        'selfReportedRaces',
        'selfReportedSexualOrientations',
        'sex',
        'suppressions',
        'surveyQuestionResponses',
        'suffix',
        'title',
        'website'
    },
    employer=EAProperty()
):
    """Represents a `Person
    <https://developers.everyaction.com/van-api#people-common-models>`__.
    """

    @staticmethod
    def _find_factory(**kwargs: EAValue) -> Optional['Person']:
        status = kwargs.get('status')
        if status is not None:
            if status != 'Unmatched':
                raise AssertionError(f'Only expected Unmatched status, found "{status}"')
            return None
        return Person(**kwargs)


class Story(
    EAObjectWithID,
    _prefix='story',
    _prefixed={'text'},
    _keys={'campaignId', 'storyStatus', 'tags', 'title', 'vanId'}
):
    """Represents a `Story
    <https://developers.everyaction.com/van-api#stories-common-models>`__.
    """


class SurveyQuestion(
    EAObjectWithIDAndName,
    _prefix='surveyQuestion',
    _keys={'cycle', 'mediumName', 'scriptQuestion', 'shortName', 'status', 'type'},
    responses=EAProperty(singular_alias='response', factory=SurveyCanvassResponse)
):
    """Represents a `Survey Question
    <https://developers.everyaction.com/van-api#survey-questions-common-models>`__.
    """


class ValueMappingData(EAObjectWithIDAndName, _keys={'parents'}):
    """Represents data for an existing `value mapping
    <https://developers.everyaction.com/van-api#bulk-import-get-bulkimportmappingtypes--mappingtypename---fieldname--values>`__
    in the context of bulk import jobs.
    """


class Worksite(EAObjectWithIDAndName, _prefix='worksite', _keys={'address', 'employer', 'isPreferred', 'workAreas'}):
    """Represents a `Worksite
    <https://developers.everyaction.com/van-api#worksites-common-models>`__.
    """


# --- Fourth Order Properties and Objects ---
EAProperty.share(
    defaultLocation=EAProperty(factory=Location),
    fields=EAProperty(singular_alias='field', factory=BulkImportField),
    location=EAProperty(factory=Location),
    locations=EAProperty(singular_alias='location', factory=Location),
    mappingTypes=EAProperty('mappings', singular_alias='mapping', factory=MappingType),
    person=EAProperty(factory=Person),
    surveyQuestions=EAProperty('questions', singular_alias='question', factory=SurveyQuestion),
    worksites=EAProperty(singular_alias='worksite', factory=Worksite)
)


class BulkImportAction(
    EAObject,
    _keys={'actionType', 'columnsToIncludeInResultsFile', 'mappingTypes', 'resultFileSizeKbLimit', 'resourceType'}
):
    """Represents a `bulk import action
    <https://developers.everyaction.com/van-api#action-bi-anchor>`__.
    """


class Employer(
    EAObjectWithIDAndName,
    _prefix='employer',
    _keys={
        'bargainingUnits',
        'departments',
        'isMyOrganization',
        'jobClasses',
        'parentOrganization',
        'shortName',
        'website',
        'worksites'
    },
    phones=EAProperty(singular_alias='phone', factory=OrganizationPhone),
    shifts=EAProperty(singular_alias='shift', factory=ShiftType)
):
    """Represents an `Employer
    <https://developers.everyaction.com/van-api#employers-common-models>`__.
    """


class EventType(
    EAObjectWithIDAndName,
    _prefix='eventType',
    _keys={
        'canBeRepeatable',
        'canHaveGoals',
        'canHaveMultipleLocations',
        'canHaveMultipleShifts',
        'canHaveRoleMaximums',
        'canHaveRoleMinimums',
        'color',
        'defaultLocation',
        'isAtLeastOneLocationRequired',
        'isOnlineActionsAvailable',
        'isSharedWithChildCommitteesByDefault',
        'isSharedWithMasterCommitteeByDefault',
        'roles',
    },
    statuses=EAProperty(is_array=True, factory=Status)
):
    """Represents an `Event Type
    <https://developers.everyaction.com/van-api#event-types-common-models>`__.
    """


class ExportJob(
    EAObjectWithID,
    _prefix='exportJob',
    _prefixed={'guid'},
    _keys={
        'activistCodes',
        'canvassFileRequestId',
        'canvassFileRequestGuid',
        'customFields',
        'dateExpired',
        'districtFields',
        'downloadUrl',
        'errorCode',
        'savedListId',
        'status',
        'surveyQuestions',
        'type',
        'webhookUrl'
    }
):
    """Represents an `Export Job
    <https://developers.everyaction.com/van-api#export-jobs-common-models>`__.
    """


class MappingTypeData(EAObjectWithName, _keys={'allowMultipleMode', 'displayName', 'fields', 'resourceTypes'}):
    """Represents data for an existing `bulk import mapping type
    <https://developers.everyaction.com/van-api#bulk-import-get-bulkimportmappingtypes>`__.
    """


class Registrant(EAObject, _keys={'alternateId', 'customProperties', 'person'}):
    """Represents a `Registrant
    <https://developers.everyaction.com/van-api#voter-registration-batches-post-voterregistrationbatches--batchid--people>`__
    for a Voter Registration Batch.
    """


# --- Fifth Order Properties and Objects ---
EAProperty.share(
    actions=EAProperty(singular_alias='action', factory=BulkImportAction),
    eventType=EAProperty('type', factory=EventType)
)


class BulkImportJob(EAObject, _keys={'actions', 'description'}, file=EAProperty(factory=JobFile)):
    """Represents a `Bulk Import Job
    <https://developers.everyaction.com/van-api#bulk-import-post-bulkimportjobs>`__.
    """


class Event(
    EAObjectWithIDAndName,
    _prefix='event',
    _keys={
        'codes',
        'createdDate',
        'description',
        'districtFieldValue',
        'dotNetTimeZoneId',
        'endDate',
        'eventType',
        'isActive',
        'isOnlyEditableByCreatingUser',
        'isPubliclyViewable',
        'locations',
        'roles',
        'shifts',
        'shortName',
        'startDate',
        'voterRegistrationBatches'
    },
    notes=EAProperty(singular_alias='note', factory=Note)
):
    """Represents an `Event
    <https://developers.everyaction.com/van-api#events-common-models>`__.
    """


# --- Sixth Order Properties and Objects ---
EAProperty.share(
    event=EAProperty(factory=Event)
)


class Signup(
    EAObjectWithID,
    _prefix='eventSignup',
    _keys={
        'dateModified',
        'endTimeOverride',
        'event',
        'isOfflineSignup',
        'location',
        'modifiedBy',
        'notes',
        'person',
        'shift',
        'startTimeOverride',
        'supporterGroupId',
        'role'
    },
    status=EAProperty(factory=Status)
):
    """Represents a `Signup
    <https://developers.everyaction.com/van-api#signups-common-models>`__.
    """