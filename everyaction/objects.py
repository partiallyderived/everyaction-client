"""
This module contains EveryAction objects, such as :class:`.Person` or :class:`.CanvassResponse`, which represent
structured EveryAction data directly corresponding to objects in the
`EveryAction 8 VAN API docs <https://docs.everyaction.com/reference/api-overview>`__.
"""

from datetime import datetime
from typing import Any, ClassVar, Dict, Iterable, List, Optional, Union

from everyaction.core import EAObject, EAProperty, EAValue
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
    'BulkImportAction',
    'BulkImportField',
    'BulkImportJob',
    'BulkImportJobData',
    'Canvasser',
    'CanvassContext',
    'CanvassFileRequest',
    'CanvassResponse',
    'ChangedEntityBulkImportField',
    'ChangedEntityExportJob',
    'ChangedEntityExportRequest',
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
    'EmployerPhone',
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
    'MappingValue',
    'Membership',
    'MembershipSourceCode',
    'MemberStatus',
    'MiniVANExport',
    'Note',
    'NoteCategory',
    'OnlineActionsForm',
    'Person',
    'Phone',
    'PhonesFileAction',
    'Pledge',
    'PrintedList',
    'ProgramType',
    'Pronoun',
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
# properties at all and does not inherit except from EAObject.
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
    committeeId=EAProperty(),
    committeeName=EAProperty('committee'),
    commonName=EAProperty('common'),
    confidenceLevel=EAProperty('confidence'),
    contact=EAProperty(),
    contactMethodPreferenceCode=EAProperty('contact_preference_code', 'preference_code', 'contact_preference'),
    contactMode=EAProperty(),
    contactTypeId=EAProperty('contact_type'),
    contentId=EAProperty('content'),
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
    detailedCode=EAProperty(),
    description=EAProperty('desc'),
    designationId=EAProperty('designation'),
    dialingPrefix=EAProperty('prefix'),
    directMarketingCode=EAProperty('marketing_code'),
    disclosureFieldValue=EAProperty('field_value', 'disclosure_value', 'value'),
    displayMode=EAProperty(),
    displayName=EAProperty('display'),
    doorCount=EAProperty('door'),
    dotNetTimeZoneId=EAProperty('dot_net_time_zone', 'time_zone'),
    downloadUrl=EAProperty('download'),
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
    jobTitle=EAProperty(),
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
    maxLength=EAProperty(),
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
    officialName=EAProperty('official'),
    omitActivistCodeContactHistory=EAProperty('omit_contact_history', 'omit_history'),
    onlineReferenceNumber=EAProperty('reference_number', 'ref_number'),
    onlyMyBatches=EAProperty('only_mine'),
    openCount=EAProperty('opens'),
    optInStatus=EAProperty('opt_in'),
    orderby=EAProperty('order_by'),
    organizationContactCommonName=EAProperty('organization_contact', 'org_contact_common', 'org_common'),
    organizationContactOfficialName=EAProperty('organization_contact_official', 'org_contact_official', 'org_official'),
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
    parentOrganization=EAProperty('parent', factory=_employer_factory),
    parentValueId=EAProperty('parent_value'),
    party=EAProperty(),
    paymentType=EAProperty(),
    personIdColumn=EAProperty('id_column', 'id_col'),
    personIdType=EAProperty('person_type'),
    personType=EAProperty(),
    phone=EAProperty(),
    phoneId=EAProperty('phone'),
    phoneNumber=EAProperty('number'),
    phoneSourceId=EAProperty('phone_source', 'source'),
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
    requestedIds=EAProperty('ids', singular_alias='requested_id'),
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
    skipMatching=EAProperty(),
    smsOptInStatus=EAProperty('sms_opt_in'),
    source=EAProperty(),
    sourceUrl=EAProperty('source', 'url'),
    sourceValue=EAProperty('source'),
    startingAfter=EAProperty('after'),
    startingBefore=EAProperty('before'),
    startDate=EAProperty('start'),
    startTime=EAProperty('start'),
    startTimeOverride=EAProperty('start_override', 'start'),
    stateCode=EAProperty('state'),
    stateId=EAProperty('state'),
    stateOrProvince=EAProperty('state', 'province'),
    staticValue=EAProperty('static'),
    status=EAProperty(),
    statuses=EAProperty(),
    statusName=EAProperty('status'),
    streetAddress=EAProperty('address'),
    subject=EAProperty('subject'),
    subscriptionStatus=EAProperty('status'),
    supporterGroupId=EAProperty('supporter_group', 'group'),
    suffix=EAProperty(),
    surveyQuestionId=EAProperty('question'),
    surveyResponseId=EAProperty('response'),
    syncPeriodEnd=EAProperty('sync_end', 'end'),
    syncPeriodStart=EAProperty('sync_start', 'start'),
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
    webhookUrl=EAProperty('webhook'),
    website=EAProperty(),
    whatIf=EAProperty(),
    zipOrPostalCode=EAProperty('zip_code', 'zip', 'postal_code', 'postal'),
    Description=EAProperty('desc'),
    ID=EAProperty('id'),
    Phone=EAProperty('phone'),
    PreferredPhone=EAProperty('preferred'),
    SonarScore=EAProperty('sonar'),
    VANID=EAProperty('van_id', 'van')
)


class ActivistCode(
    EAObject,
    _id='id',
    _name='name',
    _prefix='activistCode',
    _shared={'description', 'isMultiAssign', 'mediumName', 'scriptQuestion', 'shortName', 'status', 'type'}
):
    """Represents an `Activist Code <https://docs.everyaction.com/reference/activistcodes-common-models>`__."""


class ActivistCodeData(
    EAObject,
    _id='id',
    _name='name',
    _prefix='activistCode',
    _prefixed={'name', 'typeAndName'},
    _shared={'canvassedBy', 'dateCanvassed', 'dateCreated'}
):
    """Represents the data associated with responses to `getting Activist Codes
    <https://docs.everyaction.com/reference/people-vanid-activistcodes>`__.
    """


class Adjustment(EAObject, _shared={'adjustmentType', 'amount', 'datePosted'}):
    """Represents the data associated with responses to `adjusting a Contribution
    <https://docs.everyaction.com/reference/contributions-contributionid-adjustments>`__.
    """


class AdjustmentResponse(EAObject, _shared={'contributionId', 'dateAdjusted', 'originalAmount', 'remainingAmount'}):
    """Represents the data associated with a response to a `Contribution adjustment
    <https://docs.everyaction.com/reference/contributions-contributionid-adjustments>`__.
    """


class APIKeyProfile(
    EAObject,
    _shared={
        'apiKeyTypeName',
        'committeeId',
        'committeeName',
        'databaseName',
        'hasMyCampaign',
        'hasMyVoters',
        'keyReference',
        'stateId',
        'username',
        'userFirstName',
        'userLastName'
    }
):
    """Represents an `API key profile <https://docs.everyaction.com/reference/introspection>`__."""


class Attribution(EAObject, _shared={'amountAttributed', 'attributionType', 'dateThanked', 'notes', 'vanId'}):
    """Represents an `Attribution object
    <https://docs.everyaction.com/reference/contribution-common-models#attributions>`__.
    """


class AvailableValue(EAObject, _id='id', _name='name', _shared={'parentValueId'}):
    """Represents
    `AvailableValues <https://docs.everyaction.com/reference/custom-fields-common-models#available-value>`__ for a
    Custom Field.
    """


class BallotRequestType(EAObject, _id='id', _name='name', _prefix='ballotRequestType'):
    """Represents a `Ballot Request Type
    <https://docs.everyaction.com/reference/ballots-common-models#ballot-request-type>`__.
    """


class BallotReturnStatus(EAObject, _id='id', _name='name', _prefix='ballotReturnStatus'):
    """Represents a `Ballot Return Status
    <https://docs.everyaction.com/reference/ballots-common-models#ballot-return-status>`__.
    """


class BallotType(EAObject, _id='id', _name='name', _prefix='ballotType'):
    """Represents a `Ballot Type <https://docs.everyaction.com/reference/ballots-common-models#ballot-type>`__."""


class BankAccount(EAObject, _id='id', _name='name', _prefix='bankAccount'):
    """Represents a `Contribution Bank Account object
    <https://docs.everyaction.com/reference/contribution-common-models#contribution-bank-account>`__.
    """


class BargainingUnit(
    EAObject, _id='id', _name='name', _prefix='bargainingUnit', _shared={'employerBargainingUnitId', 'shortName'}
):
    """Represents a `Bargaining Unit
    <https://docs.everyaction.com/reference/bargaining-units-common-models#bargaining-unit>`__.
    """


class Canvasser(EAObject, _id='id', _prefix='canvasser'):
    """Represents a `Canvasser <https://docs.everyaction.com/reference/common-models-25>`__."""


class CanvassFileRequest(
    EAObject,
    _id='id',
    _shared={'dateExpired', 'downloadUrl', 'errorCode', 'guid', 'savedListId', 'status', 'type', 'webhookUrl'},
):
    """Represents a `Canvass File Request <https://docs.everyaction.com/reference/canvassfilerequests>`__."""


class ChangedEntityExportRequest(
    EAObject,
    _id='id',
    _prefix='exportJob',
    _shared={
        'dateChangedFrom',
        'dateChangedTo',
        'excludeChangesFromSelf',
        'includeInactive',
        'requestedCustomFieldIds',
        'requestedFields',
        'requestedIds',
        'resourceType'
    }
):
    """Represents data associated with a request to `create a Changed Entity Export Job
    <https://docs.everyaction.com/reference/changedentityexportjobs>`__.
    """


class ChangeType(
    EAObject,
    _id='ID',
    _name='name',
    _prefix='changeType',
    _prefixed={'name'},
    _shared={'Description'},
    ID=EAProperty()
):
    """Represents a `changeType
    <https://docs.everyaction.com/reference/changedentityexportjobs-changetypes-resourcetype>`__.
    """
    # Note: According to the above link, the properties are all upper-cased, but in testing, it appears that actually
    # only Description is upper-cased and "ID" is used rather than "Id".


class CodeResult(EAObject, _id='id', _prefix='code', _shared={'message'}):
    """Represents the data associated with a response to a code batch request. See `POST /codes/batch
    <https://docs.everyaction.com/reference/codes-batch>`__ for an example.
    """


class Column(EAObject, _name='name'):
    """Represents a `Column <https://docs.everyaction.com/reference/bulkimportjobs#column>`__."""


class Commitment(
    EAObject,
    _id='id',
    _prefix='commitment',
    _shared={
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
    """Represents a `Commitment <https://docs.everyaction.com/reference/commitments-common-models#commitment>`__."""


class ConfirmationEmailData(
    EAObject,
    _shared={
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
    <https://docs.everyaction.com/reference/oa-common-models#confirmation-email-data>`__.
    """


class ContactType(EAObject, _id='id', _name='name', _prefix='contactType', _shared={'channelTypeName'}):
    """Represents a `Contact Type <https://docs.everyaction.com/reference/canvassresponses-contacttypes>`__."""


class Constraints(EAObject, _shared={'invalidCharacters', 'maxLength'}):
    """Represents a description of the violated constraints for :class:`.Error` objects."""


class ContactHistory(EAObject, _shared={'contactTypeId', 'dateCanvassed', 'inputTypeId', 'resultCodeId'}):
    """Represents a `Contact History object <https://docs.everyaction.com/reference/post-people-vanid-notes>`__."""


class Currency(EAObject, _shared={'amount', 'currencyType'}):
    """Represents the type and the amount of a currency. Found, for instance, in the response of
    `GET /people/{vanId}/membership <https://docs.everyaction.com/reference/people-vanid-membership>`__.
    """


class CustomFieldValue(EAObject, _shared={'assignedValue', 'customFieldGroupId', 'customFieldId'}):
    """Represents a `CustomFieldValue <https://docs.everyaction.com/reference/common-models#custom-field-value>`__."""

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


class Department(EAObject, _id='id', _name='name', _prefix='department', _shared={'employer', 'parentDepartmentId'}):
    """Represents a `Department <https://docs.everyaction.com/reference/departments-common-models#department>`__."""


class Designation(EAObject, _id='id', _name='name', _prefix='designation'):
    """Represents a `Designation <https://docs.everyaction.com/reference/designations-common-models#designation>`__."""


class DisclosureFieldValue(
    EAObject, _id='id', _prefix='disclosureField', _prefixed={'value'}, _shared={'designationId'}
):
    """Represents a `Disclosure Field Value
    <https://docs.everyaction.com/reference/common-models#disclosure-field-value>`__.
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


class DistrictFieldValue(EAObject, _id='id', _name='name', _shared={'parentId'}):
    """Represents a `District Field Value
    <https://docs.everyaction.com/reference/common-models-13#district-field-value>`__.
    """


class Email(EAObject, _shared={'dateCreated', 'email', 'isPreferred', 'isSubscribed', 'subscriptionStatus', 'type'}):
    """Represents an `Email <https://docs.everyaction.com/reference/common-models#email>`__."""

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
    _shared={
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
    <https://docs.everyaction.com/reference/common-models-14>`__.
    """


class EmployerPhone(
    EAObject,
    _id='id',
    _prefix='organizationPhone',
    _shared={
        'confidenceLevel',
        'countryCode',
        'dialingPrefix',
        'organizationId',
        'phone',
        'phoneSourceId'
    },
    phoneType=EAProperty('type')
):
    """Represents a `Phone for an employer <https://docs.everyaction.com/reference/common-models-15>`__."""


class EventRole(EAObject, _id='id', _name='name', _prefix='role', _shared={'goal', 'isEventLead', 'max', 'min'}):
    """Represents a `Role <https://docs.everyaction.com/reference/common-models-18#role>`__ for an Event Type."""


class EventShift(EAObject, _id='id', _name='name', _prefix='eventShift', _shared={'endTime', 'startTime'}):
    """Represents a `Shift <https://docs.everyaction.com/reference/common-models-18#shift>`__."""


class ExportJobType(EAObject, _id='id', _name='name', _prefix='exportJobType'):
    """Represents an `Export Job Type <https://docs.everyaction.com/reference/exportjobtypes>`__."""


class File(EAObject, _shared={'dateExpired', 'downloadUrl', 'recordCount'}):
    """Represents a `File object <https://docs.everyaction.com/reference/targetexportjobsexportjobid#file>`__ in
    EveryAction. Used in many contexts.
    """


class FinancialBatch(
    EAObject,
    _id='id',
    _name='name',
    _prefix='financialBatch',
    _prefixed={'name', 'number'},
    _shared={
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
    """Represents a `Financial Batch <https://docs.everyaction.com/reference/common-models-21#financial-batch>`__."""


class Folder(EAObject, _id='id', _name='name', _prefix='folder'):
    """Represents a `folder <https://docs.everyaction.com/reference/common-models-31#folder>`__."""


class GeoCoordinate(EAObject, _shared={'lat', 'lon'}):
    """Represents a `Geographic Coordinate
    <https://docs.everyaction.com/reference/common-models-23#geographic-coordinate>`__.
    """


class Identifier(EAObject, _shared={'externalId', 'type'}):
    """Represents an `Identifier <https://docs.everyaction.com/reference/common-models#identifier>`__."""


class IsCellStatus(EAObject, _id='id', _name='name', _prefix='status', _prefixed={'name'}):
    """Represents an `Phone Is a Cell Status <https://docs.everyaction.com/reference/phonesiscellstatuses>`__."""


class JobActionType(EAObject, _shared={'actionType'}):
    """Represents a `Job Action Type <https://docs.everyaction.com/reference/fileloadingjobs#action>`__."""

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


class JobClass(EAObject, _id='id', _name='name', _prefix='jobClass', _shared={'shortName'}):
    """Represents a `Job Class <https://docs.everyaction.com/reference/common-models-22#job-class>`__."""


class JobNotification(EAObject, _shared={'description', 'message', 'status'}):
    """Represents a `Notification <https://docs.everyaction.com/reference/fileloadingjobs#notification>`__ for File
    Loading Jobs.
    """


class InputType(EAObject, _id='id', _name='name', _prefix='inputType'):
    """Represents an `Input Type <https://docs.everyaction.com/reference/canvassresponses-inputtypes>`__."""


class KeyValuePair(EAObject, _shared={'key', 'value'}):
    """Represents a key value pair for possible values of a `Support Field
    <https://docs.everyaction.com/reference/voterregistrationbatchesstatesstatesupportedfields>`__.
    """


class Listener(EAObject, _shared={'type', 'value'}):
    """Represents a `Listener <https://docs.everyaction.com/reference/fileloadingjobs>`__ for a file-loading job."""


class MappingValue(EAObject, _id='id', _name='name', _shared={'parentId', 'sourceValue', 'targetValue'}):
    """Represents a `value <https://docs.everyaction.com/reference/bulkimportjobs#mapping-types>`__ in the context of
    bulk import jobs.
    """


class MembershipSourceCode(EAObject, _id='id', _name='name', _prefix='code', _prefixed={'name'}):
    """Represents a `Membership Source Code <https://docs.everyaction.com/reference/people-vanid-membership>`__."""


class MemberStatus(EAObject, _id='id', _name='name', _prefix='memberStatus', _shared={'isMember'}):
    """Represents a `Member Status <https://docs.everyaction.com/reference/common-models-24#member-status>`__."""


class NoteCategory(EAObject, _id='id', _name='name', _prefix='noteCategory', _shared={'assignableTypes'}):
    """Represents a `Note Category <https://docs.everyaction.com/reference/common-models-26#note-category>`__."""


class Pledge(EAObject, _id='id', _prefix='pledge'):
    """Represents a `Pledge object <https://docs.everyaction.com/reference/contribution-common-models#pledge>`__."""


class PrintedList(EAObject, _name='name', _shared={'number'}):
    """Represents a `Printed List <https://docs.everyaction.com/reference/common-models-28#printed-list>`__."""


class ProgramType(EAObject, _id='id', _name='name', _prefix='programType'):
    """Represents a `Program Type <https://docs.everyaction.com/reference/common-models-39#program-type>`__."""


class Pronoun(
    EAObject,
    _id='id',
    _name='name',
    _prefix='pronoun',
    _prefixed={'name'},
    id=EAProperty('preferredPronounId', 'preferred_pronoun_id'),
    name=EAProperty('preferredPronounName', 'preferred_pronoun_name')
):
    """Represents a `pronoun <https://docs.everyaction.com/reference/pronouns>`__."""


class RegistrationForm(EAObject, _id='id', _name='name', _prefix='form'):
    """Represents a `Registration Form <https://docs.everyaction.com/reference/common-models-39#form>`__."""


class RelationalMapping(EAObject, _shared={'fieldName', 'value'}):
    """Represents a `Relational Mapping
    <https://docs.everyaction.com/reference/changedentityexportjobs-fields-resourcetype>`__.
    """


class Relationship(EAObject, _id='id', _name='name'):
    """Represents a `Relationship <https://docs.everyaction.com/reference/relationships-1>`__."""


class ReportedEthnicity(EAObject, _id='id', _name='name', _prefix='reportedEthnicity', _prefixed={'name'}):
    """Represents a `Reported Ethnicity <https://docs.everyaction.com/reference/reportedethnicities>`__."""


class ReportedGender(EAObject, _id='id', _name='name', _prefix='reportedGender', _prefixed={'name'}):
    """Represents a `Reported Gender <https://docs.everyaction.com/reference/reportedgenders>`__."""


class ReportedLanguagePreference(
    EAObject, _id='id', _name='name', _prefix='reportedLanguagePreference', _prefixed={'name'}
):
    """Represents a `Reported Language Preference
    <https://docs.everyaction.com/reference/reportedlanguagepreferences>`__.
    """


class ReportedRace(EAObject, _id='id', _name='name', _prefix='reportedRace', _prefixed={'name'}):
    """Represents a `Reported Race <https://docs.everyaction.com/reference/reportedraces>`__."""


class ReportedSexualOrientation(
    EAObject, _id='id', _name='name', _prefix='reportedSexualOrientation', _prefixed={'name'}
):
    """Represents a `Reported Sexual Orientation
    <https://docs.everyaction.com/reference/reportedsexualorientations>`__.
    """


class ResultCode(
    EAObject, _id='id', _name='name', _prefix='resultCode', _shared={'mediumName', 'resultOutcomeGroup', 'shortName'}
):
    """Represents a `Result Code <https://docs.everyaction.com/reference/canvassresponses-resultcodes>`__."""


class SavedList(
    EAObject, _id='id', _name='name', _prefix='savedList', _shared={'description', 'doorCount', 'listCount'}
):
    """Represents a `Saved List <https://docs.everyaction.com/reference/common-models-29#saved-list>`__."""


class SavedListData(
    EAObject,
    _id='id',
    _prefix='savedList',
    _shared={'matchedRowsCount', 'originalRowCount', 'unmatchedRowsCount'}
):
    """Represents `Saved List Data <https://docs.everyaction.com/reference/fileloadingjobs#saved-list-load>`__ for Saved
    List Load actions.
    """


class ScheduleType(EAObject, _id='id', _name='name', _prefix='scheduleType'):
    """Represents a `Schedule Type <https://docs.everyaction.com/reference/common-models-30#schedule-type>`__."""


class Score(
    EAObject, _id='id', _name='name', _prefix='score', _shared={'description', 'maxValue', 'minValue', 'shortName'}
):
    """Represents a `Score <https://docs.everyaction.com/reference/scores-overview>`__."""


class ScoreApprovalCriteria(EAObject, _shared={'average', 'tolerance'}):
    """Represents `Score Approval Criteria <https://docs.everyaction.com/reference/fileloadingjobs#score-load-action>`__
    for Score Load actions.
    """


class ScriptResponse(EAObject, _shared={'type'}):
    """Represents a `Script Response <https://docs.everyaction.com/reference/people-vanid-canvassresponses>`__."""

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


class ShiftType(EAObject, _id='id', _name='name', _prefix='shiftType', _shared={'defaultEndTime', 'defaultStartTime'}):
    """Represents a `Shift Type <https://docs.everyaction.com/reference/common-models-15>`__."""


class Status(EAObject, _id='id', _name='name', _prefix='status'):
    """Represents a `Status <https://docs.everyaction.com/reference/common-models-17>`__ in EveryAction. Used in
    multiple contexts.
    """


class StoryStatus(EAObject, _id='id', _name='statusName', _prefix='storyStatus'):
    """Represents a `StoryStatus <https://docs.everyaction.com/reference/common-models-34#story-status>`__."""


class Subgroup(EAObject, _id='id', _name='name', _prefix='subgroup', _shared={'fullName', 'isAssociatedWithBadges'}):
    """Represents a `Subgroup <https://docs.everyaction.com/reference/common-models-37#subgroup>`__ for a Target."""


class SupportedEntity(EAObject, _name='name', _shared={'isApplicable', 'isSearchable'}):
    """Represents a `Supported Entity <https://docs.everyaction.com/reference/codes-common-models#supported-entity>`__
    in the context of codes.
    """


class SupporterGroup(EAObject, _id='id', _name='name', _shared={'description'}):
    """Represents a `Supporter Group <https://docs.everyaction.com/reference/common-models-35#supporter-group>`__."""


class Suppression(EAObject, _name='name', _prefix='suppression', _prefixed={'code', 'name'}):
    """Represents a `Suppression <https://docs.everyaction.com/reference/common-models#suppression>`__."""
    _CODE_TO_NAME: ClassVar[Dict[str, str]] = {
        'NC': 'do not call',
        'NE': 'do not email',
        'NM': 'do not mail',
        'NW': 'do not walk'
    }
    _NAME_TO_CODE: ClassVar[Dict[str, str]] = {n: c for c, n in _CODE_TO_NAME.items()}

    DO_NOT_CALL: ClassVar['Suppression'] = None
    DO_NOT_EMAIL: ClassVar['Suppression'] = None
    DO_NOT_MAIL: ClassVar['Suppression'] = None
    DO_NOT_WALK: ClassVar['Suppression'] = None

    def __init__(
        self,
        code_or_name: Optional[str] = None,
        **kwargs: EAValue
    ) -> None:
        """Initialize by setting the specified property names and aliases. Note that values will automatically be
        converted to API objects when appropriate. When the positional argument `code_or_name` is given, it is assumed
        to be a code (e.g., "NC" for "Do not call") when it has length at most 2, and otherwise it is assumed to be a
        name.

        :param code_or_name: When the given, it is assumed to be a code (e.g., "NC" for "Do not call") when it has
            length at most 2, and otherwise it is assumed to be a name.
        :param kwargs: Mapping of (alias or name) -> value.
        """
        code = None
        name = None
        if code_or_name:
            # Infer from str length whether it is a name or a code.
            if len(code_or_name) > 2:
                super().__init__(suppressionName=code_or_name, **kwargs)
            else:
                super().__init__(suppressionCode=code_or_name, **kwargs)
        # Continue trying to infer the name or code if they are not yet determined.
        code = code or self._NAME_TO_CODE.get((name or '').lower())
        name = name or self._CODE_TO_NAME.get((code or '').upper())
        super().__init__(suppressionCode=code, suppressionName=name, **kwargs)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Suppression):
            return False
        if self.code and other.code:
            return self.code.upper() == other.code.upper()
        if self.name and other.name:
            return self.name.lower() == other.name.lower()
        # "Null" suppressions where name and code are both None are equal to each other.
        return not (self.name or other.name or self.code or other.code)

    @property
    def no_call(self) -> bool:
        """Indicates whether this is a "Do Not Call" suppression.

        :return: ``True`` if this is a "Do Not Call" suppression, ``False`` otherwise.
        """
        return (self.code or '').upper() == 'NC' or (self.name or '').lower() == 'do not call'

    @property
    def no_email(self) -> bool:
        """Indicates whether this is a "Do Not Email" suppression.

        :return: ``True`` if this is a "Do Not Email" suppression, ``False`` otherwise.
        """
        return (self.code or '').upper() == 'NE' or (self.name or '').lower() == 'do not email'

    @property
    def no_mail(self) -> bool:
        """Indicates whether this is a "Do Not Mail" suppression.

        :return: ``True`` if this is a "Do Not Mail" suppression, ``False`` otherwise.
        """
        return (self.code or '').upper() == 'NM' or (self.name or '').lower() == 'do not mail'

    @property
    def no_walk(self) -> bool:
        """Indicate whether this is a "Do Not Walk" suppression.

        :return: ``True`` if this is a "Do Not Walk" suppression, ``False`` otherwise.
        """
        return (self.code or '').upper() == 'NW' or (self.name or '').lower() == 'do not walk'


Suppression.DO_NOT_CALL = Suppression('NC')
Suppression.DO_NOT_EMAIL = Suppression('NE')
Suppression.DO_NOT_MAIL = Suppression('NM')
Suppression.DO_NOT_WALK = Suppression('NW')


class SurveyResponse(EAObject, _id='id', _name='name', _prefix='surveyResponse', _shared={'mediumName', 'shortName'}):
    """Represents a `Survey Response <https://docs.everyaction.com/reference/common-models-36#survey-response>`__."""


class UpdateStatistics(EAObject):
    """Represents an `Update Statistics <https://docs.everyaction.com/reference/score-updates>`__ object."""


class User(EAObject, _id='id', _prefix='user', _shared={'firstName', 'lastName'}):
    """Represents a `VAN User <https://docs.everyaction.com/reference/common-models-20>`__."""


class WorkArea(EAObject, _id='id', _name='name', _prefix='workArea'):
    """Represents a `Work Area <https://docs.everyaction.com/reference/common-models-16#worksite>`__."""


# --- Second Order Properties and Objects ---
EAProperty.share(
    activistCodes=EAProperty(singular_alias='activist_code', factory=ActivistCode),
    approvalCriteria=EAProperty('criteria', factory=ScoreApprovalCriteria),
    availableValues=EAProperty('available', 'values', singular_alias='value', factory=AvailableValue),
    bargainingUnit=EAProperty(factory=BargainingUnit),
    bargainingUnits=EAProperty(singular_alias='bargaining_unit', factory=BargainingUnit),
    canvassers=EAProperty(singular_alias='canvasser', factory=Canvasser),
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
    form=EAProperty(factory=RegistrationForm),
    geoLocation=EAProperty('geo',  'location', factory=GeoCoordinate),
    identifiers=EAProperty(singular_alias='identifier', factory=Identifier),
    isCellStatus=EAProperty('cell_status', 'is_cell', factory=IsCellStatus),
    jobClass=EAProperty(factory=JobClass),
    limitedToParentValues=EAProperty('limited_to', is_array=True, factory=AvailableValue),
    listeners=EAProperty(singular_alias='listener', factory=Listener),
    pledge=EAProperty(factory=Pledge),
    possibleValues=EAProperty('possible', singular_alias='possible_value', factory=KeyValuePair),
    programType=EAProperty('program', factory=ProgramType),
    pronouns=EAProperty('pronoun', 'preferredPronoun', factory=Pronoun),
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
    values=EAProperty(singular_alias='value', factory=MappingValue)
)


class ActivistCodeResponse(ScriptResponse, EAObject, _id='id', _prefix='activistCode', _shared={'action'}):
    """Represents an `Activist Code Response
    <https://docs.everyaction.com/reference/people-vanid-canvassresponses>`__.
    """

    def __init__(self, id: Optional[int] = None, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param id: ID to initialize with. When given alone, a simple object results (see
            `A Note About Simple Objects <https://docs.everyaction.com/reference/events-overview>`__).
        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(type='ActivistCode', activistCodeId=id, **kwargs)


class Address(
    EAObject,
    _id='id',
    _prefix='address',
    _prefixed={'line1', 'line2', 'line3'},
    _shared={
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
    """Represents an `Address <https://docs.everyaction.com/reference/common-models#address>`__."""


class AVEVDataFileAction(JobActionType):
    """Represents an `AVEV Data File Action
    <https://docs.everyaction.com/reference/fileloadingjobs#avev-data-file>`__.
    """

    def __init__(self, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(actionType='AVEVDataFile', **kwargs)


class BargainingUnitJobClass(
    EAObject,
    _id='id',
    _prefix='employerBargainingUnitJobClass',
    _shared={'bargainingUnit', 'employerBargainingUnitId', 'jobClass'}
):
    """Represents an `Employer Bargaining Unit Job Class
    <https://docs.everyaction.com/reference/common-models-15>`__.
    """


class ChangedEntityBulkImportField(EAObject, _shared={'fieldName', 'mappingTypeName', 'relationalMappings'}):
    """Represents a `bulk import field
    <https://docs.everyaction.com/reference/changedentityexportjobs-fields-resourcetype>`__
    in the context of changed entities.
    """


class ChangedEntityExportJob(
    EAObject,
    _id='id',
    _prefix='exportJob',
    _shared={
        'dateChangedFrom',
        'dateChangedTo',
        'exportedRecordCount',
        'files',
        'jobStatus',
        'message'
    }
):
    """Represents data for an existing `ChangedEntityExportJob
    <https://docs.everyaction.com/reference/changed-entities-common-models>`__.
    """


class Code(
    EAObject,
    _id='id',
    _name='name',
    _prefix='code',
    _prefixed={'type'},
    _shared={'dateCreated', 'dateModified', 'description', 'parentCodeId', 'supportedEntities'}
):
    """Represents a `Code object <https://docs.everyaction.com/reference/codes-common-models#code>`__."""


class CustomField(
    EAObject,
    _id='id',
    _name='name',
    _prefix='customField',
    _prefixed={'groupId', 'groupName', 'groupType', 'name', 'parentId', 'typeId'},
    _shared={'availableValues', 'isEditable', 'isExportable', 'maxTextboxCharacters'}
):
    """Represents a `Custom Field <https://docs.everyaction.com/reference/custom-fields-common-models>`__."""


class DistrictField(
    EAObject,
    _id='id',
    _name='name',
    _prefix='districtField',
    _prefixed={'values'},
    _shared={'isCustomDistrict', 'parentFieldId'}
):
    """Represents a `District Field <https://docs.everyaction.com/reference/common-models-13#district-field>`__."""


class EmailMessageContent(
    EAObject,
    _shared={
        'createdBy',
        'dateCreated',
        'emailMessageContentDistributions',
        'name',
        'senderDisplayName',
        'senderEmailAddress',
        'subject'
    }
):
    """Represents an `email message content object <https://docs.everyaction.com/reference/common-models-14>`__."""


class EmployerBargainingUnit(EAObject, _id='id', _prefix='employerBargainingUnit', _shared={'bargainingUnit'}):
    """Represents an `Employer Bargaining Unit
    <https://docs.everyaction.com/reference/employersemployeridbargainingunitsbargainingunitid>`__.
    """


class Error(
    EAObject,
    _shared={
        'code', 'detailedConstraints', 'detailedCode', 'hint', 'properties', 'referenceCode', 'resourceUrl', 'text'
    }
):
    """Represents an `Error object <https://docs.everyaction.com/reference/errors>`__."""


class ExtendedSourceCode(
    EAObject,
    _id='id',
    _name='name',
    _prefix='extendedSourceCode',
    _prefixed={'name'},
    _shared={'dateCreated', 'dateModified', 'modifiedBy'},
    createdBy=EAProperty('creator', factory=User)
):
    """Represents an `Extended Source Code
    <https://docs.everyaction.com/reference/common-models-20#extended-source-code>`__.
    """


class FieldValueMapping(EAObject, _shared={'columnName', 'fieldName', 'staticValue', 'values'}):
    """Represents a `fieldValueMapping <https://docs.everyaction.com/reference/bulkimportjobs#mapping-types>`__."""


class JobFile(
    EAObject,
    _prefix='file',
    _prefixed={'name'},
    _shared={'columns', 'columnDelimiter', 'hasHeader', 'hasQuotes', 'sourceUrl'}
):
    """Represents a `file object for a job <https://docs.everyaction.com/reference/bulkimportjobs#file>`__."""


class ListLoadCallbackData(JobNotification, _shared={'description', 'message', 'savedList', 'status'}):
    """Represents `Callback Data <https://docs.everyaction.com/reference/fileloadingjobs#callback-data>`__ for a Saved
    List Load action.
    """


class MappingParent(EAObject, _shared={'limitedToParentValues', 'parentFieldName'}):
    """Represents prerequisites for mapping a field as described `here
    <https://docs.everyaction.com/reference/bulkimportmappingtypes>`__.
    """


class Membership(
    EAObject,
    _shared={
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
    """Contains `membership information <https://docs.everyaction.com/reference/people-vanid-membership>`__ for a
    person.
    """


class MiniVANExport(
    EAObject,
    _id='id',
    _name='name',
    _prefix='minivanExport',
    _shared={
        'canvassers',
        'databaseMode',
        'dateCreated'
    },
    createdBy=EAProperty('creator', factory=User)
):
    """Represents a `MiniVAN Export <https://docs.everyaction.com/reference/common-models-25#minivan-export>`__."""


class Note(
    EAObject,
    _id='id',
    _prefix='note',
    _shared={'category', 'contactHistory', 'createdDate', 'isViewRestricted', 'text'}
):
    """Represents a `Note <https://docs.everyaction.com/reference/people-vanid-notes>`__."""


class OnlineActionsForm(
    EAObject,
    _id='id',
    _name='formName',
    _prefix='formTracking',
    _shared={
        'activistCodes',
        'campaignId',
        'codeId',
        'confirmationEmailData',
        'createdByEmail',
        'dateCreated',
        'dateModified',
        'designation',
        'eventId',
        'isActive',
        'isConfirmedOptInEnabled',
        'modifiedByEmail'
    },
    formName=EAProperty('name'),
    formType=EAProperty('type'),
    formTypeId=EAProperty('type_id')
):
    """Represents an `Online Actions Form
    <https://docs.everyaction.com/reference/oa-common-models#online-actions-form>`__.
    """


class Phone(
    EAObject,
    _id='id',
    _prefix='phone',
    _prefixed={'number', 'optInStatus', 'type'},
    _shared={'countryCode', 'dateCreated', 'dialingPrefix', 'ext', 'isCellStatus', 'isPreferred', 'smsOptInStatus'}
):
    """Represents a `Phone <https://docs.everyaction.com/reference/common-models#phone>`__."""

    def __init__(self, id_or_number: Optional[Union[int, str]] = None, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param id_or_number: Either the phone ID (if an integer), or the phone number (if a string). A simple object
            will result when an integer is given for the `id_or_number` positional parameter
            (see `A Note About Simple Objects <https://docs.everyaction.com/reference/overview-19>`__).
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


class PhonesFileAction(
    JobActionType,
    _shared={'Phone', 'PreferredPhone', 'SonarScore', 'VANID'},
    _prefix='Phone',
    _prefixed={'ext', 'optInStatus', 'source', 'type'}
):
    """Represents a `Phones File Action <https://docs.everyaction.com/reference/fileloadingjobs#phones-file>`__."""

    def __init__(self, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(actionType='phonesFile', **kwargs)


class SavedListLoadAction(
    JobActionType,
    _shared={'folderId', 'listDescription', 'listName', 'overwriteExistingListId', 'personIdColumn', 'personIdType'}
):
    """Represents a `Saved List Load action
    <https://docs.everyaction.com/reference/fileloadingjobs#saved-list-load>`__.
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
    _shared={'approvalCriteria', 'personIdColumn', 'personIdType', 'scoreColumn', 'scoreId'}
):
    """Represents a `Score Load Action <https://docs.everyaction.com/reference/fileloadingjobs#score-load-action>`__."""

    def __init__(self, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(actionType='Score', **kwargs)


class ScoreUpdate(
    EAObject,
    _id='id',
    _prefix='scoreUpdate',
    _shared={'dateProcessed', 'loadStatus', 'score', 'updateStatistics'}
):
    """Represents a `Score Update <https://docs.everyaction.com/reference/scoreupdatesscoreupdateid>`__."""


class SupportField(
    EAObject,
    _shared={'customPropertyKey', 'displayName', 'fieldType', 'maxFieldLength', 'possibleValues'}
):
    """Represents a `Support Field
    <https://docs.everyaction.com/reference/voterregistrationbatchesstatesstatesupportedfields>`__ for a Voter
    Registration Batch.
    """


class SurveyCanvassResponse(
    ScriptResponse,
    _shared={'mediumName', 'name', 'shortName', 'surveyQuestionId', 'surveyResponseId'}
):
    """Represents a `Survey Response <https://docs.everyaction.com/reference/people-vanid-canvassresponses>`__ in the
    context of a canvass response.
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
    EAObject,
    _id='id',
    _name='name',
    _prefix='target',
    _shared={'areSubgroupsSticky', 'description', 'points', 'status', 'subgroups', 'type'}
):
    """Represents a `Target <https://docs.everyaction.com/reference/common-models-37#target>`__."""


class TargetExportJob(
    EAObject,
    _id='id',
    _prefix='exportJob',
    _shared={'file', 'jobStatus', 'targetId', 'webhookUrl'},
):
    """Represents a `Target Export Job
    <https://docs.everyaction.com/reference/targetexportjobsexportjobid#target-export-job-result>`__.
    """


class VolunteerActivityResponse(ScriptResponse, _prefix='volunteerActivity', _shared={'action'}):
    """Represents a `Volunteer Activity <https://docs.everyaction.com/reference/people-vanid-canvassresponses>`__."""

    def __init__(self, id: Optional[int] = None, **kwargs: EAValue) -> None:
        """
        Initialize by setting the specified property names and aliases. Note that values will automatically be converted
        to API objects when appropriate.

        :param id: ID to initialize with. When given alone, a simple object results (see
            `A Note About Simple Objects <https://docs.everyaction.com/reference/events-overview>`__).
        :param kwargs: Mapping of (alias or name) -> value.
        """
        super().__init__(type='VolunteerActivity', volunteerActivityId=id, **kwargs)


class VoterRegistrationBatch(
    EAObject,
    _id='id',
    _name='name',
    _prefix='voterRegistrationBatch',
    _shared={'dateCreated', 'description', 'form', 'personType', 'programType', 'stateCode', 'status'}
):
    """Represents a `Voter Registration Batch
    <https://docs.everyaction.com/reference/common-models-39#voter-registration-batch>`__.
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


class AddRegistrantsResponse(EAObject, _shared={'alternateId', 'errors', 'result', 'vanId'}):
    """Represents the data associated with a response to `adding registrants
    <https://docs.everyaction.com/reference/voterregistrationbatchesbatchidpeople>`__ to a Voter Registration Batch.
    """


class BulkImportField(
    EAObject,
    _name='name',
    _shared={'canBeMappedToColumn', 'description', 'hasPredefinedValues', 'isRequired', 'parents'}
):
    """Represents a `mapping type field <https://docs.everyaction.com/reference/bulkimportmappingtypes>`__."""


class BulkImportJobData(
    EAObject,
    _id='id',
    _prefix='job',
    _shared={'errors', 'resourceType', 'resultFileSizeLimitKb', 'resultFiles', 'status'}
):
    """Represents data for an existing `Bulk Import Job
    <https://docs.everyaction.com/reference/bulk-import-common-models>`__.
    """


class CanvassContext(
    EAObject,
    _shared={
        'campaignId',
        'contactTypeId',
        'contentId',
        'dateCanvassed',
        'inputTypeId',
        'omitActivistCodeContactHistory',
        'phoneId',
        'skipMatching'
    },
    phone=EAProperty(factory=Phone)
):
    """Represents a `Canvass Context <https://docs.everyaction.com/reference/people-vanid-canvassresponses>`__."""


class ChangedEntityField(
    EAObject,
    _name='name',
    _shared={'availableValues', 'bulkImportFields', 'isCoreField', 'maxTextboxCharacters'},
    _prefix='field',
    _prefixed={'name', 'type'},
):
    """Represents a `changed entity field
    <https://docs.everyaction.com/reference/changedentityexportjobs-fields-resourcetype>`__.
    """

    _TYPE_TO_FACTORY = {}

    ValueType = Union[bool, int, str, datetime]

    @staticmethod
    def _parse_bool(s: str) -> bool:
        if s.lower() == 'true':
            return True
        if s.lower() == 'false':
            return False
        raise ValueError(f'Could not parse "{s}" to a boolean.')

    def parse(self, value: str) -> ValueType:
        """Parse the raw string value of a field into a typed result.
        The below table gives the behavior of this function for each `field type
        <https://docs.everyaction.com/reference/changedentityexportjobs-fields-resourcetype>`__.

        +------------+--------------------------------------------------------------------------------------------+
        | Field Type | Behavior                                                                                   |
        +============+============================================================================================+
        | B          | Parses "true" to ``True`` and "false" to ``False``.                                        |
        +------------+--------------------------------------------------------------------------------------------+
        | D          | Parses into a naive `datetime object <https://docs.python.org/3/library/datetime.html>`__. |
        +------------+--------------------------------------------------------------------------------------------+
        | M          | Keeps the original string value.                                                           |
        +------------+--------------------------------------------------------------------------------------------+
        | N          | Parses into an ``int``.                                                                    |
        +------------+--------------------------------------------------------------------------------------------+
        | T          | Keeps the original string value.                                                           |
        +------------+--------------------------------------------------------------------------------------------+


        :param value: The value to parse.
        :return: The parsed value.
        """
        return self._TYPE_TO_FACTORY[self.type](value) if value else None


# References inner staticmethod so needs to be defined here.
ChangedEntityField._TYPE_TO_FACTORY = {
    'B': ChangedEntityField._parse_bool,
    'D': datetime.fromisoformat,
    'M': lambda s: s,
    'N': int,
    'T': lambda s: s,
}


class Contribution(
    EAObject,
    _shared={
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
    <https://docs.everyaction.com/reference/contribution-common-models#contribution>`__.
    """


class Disbursement(
    EAObject,
    _id='id',
    _prefix='disbursement',
    _shared={
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
    """Represents a `Disbursement <https://docs.everyaction.com/reference/disbursements-common-models>`__."""


class EmailMessage(
    EAObject,
    _id='id',
    _name='name',
    _prefix='foreignMessage',
    _shared={'createdBy', 'dateCreated', 'dateModified', 'dateScheduled', 'emailMessageContent'},
    campaignID=EAProperty('campaign')
):
    """Represents an `email message <https://docs.everyaction.com/reference/common-models-14>`__."""

    # TODO: Is emailMessageContent really an array? If so, can it actually contain multiple entities?


class FileLoadingJob(
    EAObject,
    _id='id',
    _prefix='job',
    _shared={'description', 'interventionCallbackUrl', 'invalidRowsFileUrl', 'listeners'},
    actions=EAProperty(singular_alias='action', factory=JobActionType.make),
    file=EAProperty(factory=JobFile)
):
    """Represents a `File Loading Job <https://docs.everyaction.com/reference/fileloadingjobs>`__."""


class Location(EAObject, _id='id', _name='name', _prefix='location', _shared={'address', 'displayName'}):
    """Represents a `Location <https://docs.everyaction.com/reference/common-models-23#location>`__."""


class MappingType(EAObject, _name='name', _shared={'fieldValueMappings', 'resultFileColumnName'}):
    """Represents a `bulk import mapping type
    <https://docs.everyaction.com/reference/bulkimportjobs#mapping-types>`__.
    """


class Person(
    EAObject,
    _id='id',
    _prefix='van',
    _shared={
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
        'jobTitle',
        'lastName',
        'middleName',
        'nickname',
        'occupation',
        'organizationContactCommonName',
        'organizationContactOfficialName',
        'organizationRoles',
        'party',
        'phones',
        'pronouns',
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
    """Represents a `Person <https://docs.everyaction.com/reference/common-models#match-candidate>`__."""

    @staticmethod
    def _find_factory(**kwargs: EAValue) -> Optional['Person']:
        status = kwargs.get('status')
        if status is not None:
            if status != 'Unmatched':
                raise AssertionError(f'Only expected Unmatched status, found "{status}"')
            return None
        return Person(**kwargs)

    @staticmethod
    def _get_preferred(of: List[Any], attr: Optional[str] = None) -> Optional[Any]:
        # Get a preferred entity from a list of entities by checking the "preferred" attribute.
        if of:
            result_list = [o for o in of if o.preferred]
            if result_list:
                # Multiple preferred entities should be impossible without bad modifications.
                assert len(result_list) == 1
                if attr:
                    return getattr(result_list[0], attr)
                return result_list[0]
        return None

    def add_suppression(self, suppression: Suppression) -> bool:
        """Adds the given suppression to this person if it is not already present.

        :param suppression: The suppression to add.
        :return: ``True`` if the suppression was added, ``False`` if it was already present.
        """
        # noinspection PyAttributeOutsideInit
        self.suppressions = self.suppressions or []
        if suppression not in self.suppressions:
            self.suppressions.append(suppression)
            return True
        return False

    def has_suppression(self, suppression: Suppression) -> Optional[bool]:
        """Determines whether this contact has the given suppression.

        :param suppression: The suppression to check for.
        :return: ``True`` if this contact has the suppression, ``False`` if suppression information is available (when
            *suppressions* attribute is not ``None``) and the suppression was not found, or ``None`` if no suppression
            information is available.
        """
        if self.suppressions is not None:
            return suppression in self.suppressions
        return None

    def remove_suppression(self, suppression: Suppression) -> bool:
        """Removes the given suppression from this person if it is present.

        :param suppression: The suppression to remove.
        :return: ``True`` if the suppression was removed, ``False`` if the suppression was not found.
        """
        if self.suppressions:
            try:
                self.suppressions.remove(suppression)
                return True
            except ValueError:
                return False
        return False

    def set_suppression(self, suppression: Suppression, value: bool) -> bool:
        """Add or remove the given suppression.

        :param suppression: Suppression to add or remove.
        :param value: ``True`` to add the suppression, ``False`` to remove it.
        :return: ``True`` if suppressions were changed, ``False`` otherwise.
        """
        if value:
            return self.add_suppression(suppression)
        else:
            return self.remove_suppression(suppression)

    @property
    def do_not_call(self) -> Optional[bool]:
        """Determine if this contact is marked as "Do Not Call".

        :return: ``True`` is this contact is marked as "Do Not Call", ``False`` is suppressions are present and do not
            contain "Do Not Call", or ``None`` if no suppression information is available.
        """
        return self.has_suppression(Suppression.DO_NOT_CALL)

    @do_not_call.setter
    def do_not_call(self, value: bool) -> None:
        """Sets the "Do Not Call" status of this contact.

        :param value: Value to set to.
        """
        self.set_suppression(Suppression.DO_NOT_CALL, value)

    @property
    def do_not_email(self) -> Optional[bool]:
        """Determine if this contact is marked as "Do Not Email".

        :return: ``True`` is this contact is marked as "Do Not Email", ``False`` is suppressions are present and do not
            contain "Do Not Email", or ``None`` if no suppression information is available.
        """
        return self.has_suppression(Suppression.DO_NOT_EMAIL)

    @do_not_email.setter
    def do_not_email(self, value: bool) -> None:
        """Sets the "Do Not Call" status of this contact.

        :param value: Value to set to.
        """
        self.set_suppression(Suppression.DO_NOT_EMAIL, value)

    @property
    def do_not_mail(self) -> Optional[bool]:
        """Determine if this contact is marked as "Do Not Mail".

        :return: ``True`` is this contact is marked as "Do Not Mail", ``False`` is suppressions are present and do not
            contain "Do Not Mail", or ``None`` if no suppression information is available.
        """
        return self.has_suppression(Suppression.DO_NOT_MAIL)

    @do_not_mail.setter
    def do_not_mail(self, value: bool) -> None:
        """Sets the "Do Not Call" status of this contact.

        :param value: Value to set to.
        """
        self.set_suppression(Suppression.DO_NOT_MAIL, value)

    @property
    def do_not_walk(self) -> Optional[bool]:
        """Determine if this contact is marked as "Do Not Mail".

        :return: ``True`` is this contact is marked as "Do Not Walk", ``False`` is suppressions are present and do not
            contain "Do Not Walk", or ``None`` if no suppression information is available.
        """
        return self.has_suppression(Suppression.DO_NOT_WALK)

    @do_not_walk.setter
    def do_not_walk(self, value: bool) -> None:
        """Sets the "Do Not Call" status of this contact.

        :param value: Value to set to.
        """
        self.set_suppression(Suppression.DO_NOT_WALK, value)

    @property
    def preferred_address(self) -> Optional[Address]:
        """Get this contact's preferred mailing address as an :class:`.Address` object if it exists, or ``None`` if this
        contact has no addresses or if information on what address is preferred is unavailable.

        :return: The preferred mailing address object, or ``None`` if no preferred mailing address could be determined.
        """
        return self._get_preferred(self.addresses)

    @property
    def preferred_email(self) -> Optional[str]:
        """Get the address of this contact's preferred email if it exists, or ``None`` if this contact has no email
        addresses or if information on what address is preferred is unavailable.

        :return: The preferred email address, or code:`None` if no preferred email address could be determined.
        """
        return self._get_preferred(self.emails, "email")

    @property
    def preferred_phone(self) -> Optional[str]:
        """Get the number of this contact's preferred phone if it exists, or ``None`` if this contact has no phone
        numbers or if information on what number is preferred is unavailable.

        :return: The preferred phone number, or code:`None` if no preferred phone number could be determined.
        """
        return self._get_preferred(self.phones, "number")


class Story(
    EAObject,
    _id='id',
    _prefix='story',
    _prefixed={'text'},
    _shared={'campaignId', 'storyStatus', 'tags', 'title', 'vanId'}
):
    """Represents a `Story <https://docs.everyaction.com/reference/common-models-34#story>`__."""


class SurveyQuestion(
    EAObject,
    _id='id',
    _name='name',
    _prefix='surveyQuestion',
    _shared={'cycle', 'mediumName', 'scriptQuestion', 'shortName', 'status', 'type'},
    responses=EAProperty(singular_alias='response', factory=SurveyCanvassResponse)
):
    """Represents a `Survey Question <https://docs.everyaction.com/reference/common-models-36#survey-question>`__."""


class ValueMappingData(EAObject, _id='id', _name='name', _shared={'parents'}):
    """Represents data for an existing `value mapping
    <https://docs.everyaction.com/reference/bulkimportmappingtypes-mappingtypename-fieldname-values>`__ in the context
    of bulk import jobs.
    """


class Worksite(
    EAObject, _id='id', _name='name', _prefix='worksite', _shared={'address', 'employer', 'isPreferred', 'workAreas'}
):
    """Represents a `Worksite <https://docs.everyaction.com/reference/common-models-16#worksite>`__."""


# --- Fourth Order Properties and Objects ---
EAProperty.share(
    canvassContext=EAProperty('context', factory=CanvassContext),
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
    _shared={'actionType', 'columnsToIncludeInResultsFile', 'mappingTypes', 'resultFileSizeKbLimit', 'resourceType'}
):
    """Represents a `bulk import action <https://docs.everyaction.com/reference/bulkimportjobs#action>`__."""


class CanvassResponse(EAObject, _shared={'canvassContext', 'responses', 'resultCodeId'}):
    """Represents a `Canvass Response <https://docs.everyaction.com/reference/people-vanid-canvassresponses>`__."""


class Employer(
    EAObject,
    _id='id',
    _name='name',
    _prefix='employer',
    _shared={
        'bargainingUnits',
        'departments',
        'isMyOrganization',
        'jobClasses',
        'parentOrganization',
        'shortName',
        'website',
        'worksites'
    },
    phones=EAProperty(singular_alias='phone', factory=EmployerPhone),
    shifts=EAProperty(singular_alias='shift', factory=ShiftType)
):
    """Represents an `Employer <https://docs.everyaction.com/reference/common-models-15#employer>`__."""


class EventType(
    EAObject,
    _id='id',
    _name='name',
    _prefix='eventType',
    _shared={
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
    """Represents an `Event Type <https://docs.everyaction.com/reference/common-models-17#event-type>`__."""


class ExportJob(
    EAObject,
    _id='id',
    _prefix='exportJob',
    _prefixed={'guid'},
    _shared={
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
    """Represents an `Export Job <https://docs.everyaction.com/reference/common-models-19#export-job>`__."""


class MappingTypeData(EAObject, _name='name', _shared={'allowMultipleMode', 'displayName', 'fields', 'resourceTypes'}):
    """Represents data for an existing `bulk import mapping type
    <https://docs.everyaction.com/reference/bulkimportmappingtypes>`__.
    """


class Registrant(EAObject, _shared={'alternateId', 'customProperties', 'person'}):
    """Represents a `Registrant <https://docs.everyaction.com/reference/voterregistrationbatchesbatchidpeople>`__ for a
    Voter Registration Batch.
    """


# --- Fifth Order Properties and Objects ---
EAProperty.share(
    actions=EAProperty(singular_alias='action', factory=BulkImportAction),
    eventType=EAProperty('type', factory=EventType)
)


class BulkImportJob(EAObject, _shared={'actions', 'description'}, file=EAProperty(factory=JobFile)):
    """Represents a `Bulk Import Job <https://docs.everyaction.com/reference/bulkimportjobs#bulk-import-job>`__."""


class Event(
    EAObject,
    _id='id',
    _name='name',
    _prefix='event',
    _shared={
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
    """Represents an `Event <https://docs.everyaction.com/reference/common-models-18#event>`__."""


# --- Sixth Order Properties and Objects ---
EAProperty.share(
    event=EAProperty(factory=Event)
)


class Signup(
    EAObject,
    _id='id',
    _prefix='eventSignup',
    _shared={
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
    """Represents a `Signup <https://docs.everyaction.com/reference/common-models-33#signup>`__."""
