Naming Conventions
==================

This page procedurally documents the naming conventions for methods, objects, and parameters in this package. Refer
to this section if you are having difficulty finding a particular service or method corresponding to an HTTP endpoint,
though that will hopefully rarely be the case. This section will commonly reference camelCase, CapWords, and snake_case
naming schemes.

* :doc:`EveryAction Objects <objects>` are usually named to exactly match a corresponding object referenced in the
  EveryAction documentation, but with the CapWords convention if that was not already the case (though it usually is).
  When in doubt, check the documentation for the ``kwargs`` parameter of the method you want to call to check the
  type of object for the JSON data for that method, and the documented return values of a method to determine the type
  of the returned value.
* :doc:`Service Classes <services>` usually have names that match the corresponding groups in the EveryAction
  documentation but with spaces removed, resulting in a CapWords convention. There are some exceptions: for example, the
  service `Email <https://docs.everyaction.com/reference/email>`__ in the EveryAction documentation is called
  :class:`.EmailMessages` in this package since "Email" conflicts with an :class:`Email object .Email`.
* Instance attributes corresponding to services in :class:`.EAClient` usually have names which are snake_cased
  versions of the service they are an instance of. There are some exceptions for brevity:
  :class:`.ReportedDemographics` is shortened to ``demographics`` for example.
* Path parameters are positional only and thus their names are irrelevant from the user's perspective. In this package's
  documentation, they are named the snake_cased version of the camelCased parameter that appears in the EveryAction
  documentation.
* Query Arguments and JSON data keys have multiple names, but their original camelCased name as given in the EveryAction
  documentation is always acceptable. However, users may find it more convenient to use their shortened and snake_cased
  `aliases`.
* All methods follow the snake_case conventions. Additional conventions are followed according to what the method does,
  as described below.
* Methods which retrieve a specific piece of data that corresponds to the type of data for which the enclosing service
  the method is named, such as for
  `GET /people/{vanId} <https://docs.everyaction.com/reference/people-vanid>`__ (since it gets a
  :class:`.Person` under the service :class:`.People`), are called ``get`` as in :meth:`.People.get`.
* Methods which retrieve a specific piece of data which *does not* correspond to the type of data for which the
  enclosing service is named, such as for
  `GET /people/{vanId}/membership <https://docs.everyaction.com/reference/people-vanid-membership>`__
  are named according to the type of data being retrieved, in this case "membership" as in :meth:`.People.membership`.
* Methods which retrieve multiple pieces of data that correspond to the type of data for which the enclosing service
  is named, such as for
  `GET /activistCodes <https://docs.everyaction.com/reference/activistcodes>`__, are called
  ``list`` as in :meth:`.ActivistCodes.list`.
* Methods which retrieve multiple pieces of data that *do not* correspond to the type of data for which the enclosing
  service is named, such as for
  `GET /people/{vanId}/activistCodes <https://docs.everyaction.com/reference/people-vanid-activistcodes>`__,
  are named according to the pluralized version of the data being retrieved, such as ``activist_codes`` as in
  :meth:`.People.activist_codes`.
* Methods which create new data, such as for
  `POST /codes <https://docs.everyaction.com/reference/post-codes>`__, are called ``create`` as in
  :meth:`.Codes.create`.
* Methods which update a specific piece of data, such as for
  `POST /people/{vanId} <https://docs.everyaction.com/reference/people-vanid>`__, are called
  ``update`` when the data being updated corresponds to the type of data for which the enclosing service is named
  (as in :meth:`.People.update`), and ``update_X`` where ``X`` is the type of data being updated when it does
  not correspond to the enclosing service (as in :meth:`.VoterRegistrationBatches.update_status`).
* Methods which delete a piece of data, such as for
  `DELETE /codes/{codeId} <https://docs.everyaction.com/reference/delete-codes-codeid>`__, are called
  ``delete`` when the data being deleted corresponds to the type of data for which the enclosing service is named
  (as in :meth:`.Codes.delete`), and ``delete_X`` where ``X`` is the type of data being deleted when it does not
  correspond to the enclosing service (as in :meth:`.Contributions.delete_attribution`).
* Methods which modify an existing piece of data by adding a property to it, such as for
  `POST /people/{vanId}/codes <https://docs.everyaction.com/reference/people-vanid-codes>`__, are named
  ``add_X`` (as in :meth:`.People.add_code`), where ``X`` is the type of data being added. When such a method
  may add multiple pieces of data, such as for
  `POST /people/{vanId}/canvassResponses <https://docs.everyaction.com/reference/people-vanid-canvassresponses>`__,
  the name is pluralized as in :meth:`.People.add_canvass_responses`.
* Methods which modify an existing piece of data by removing a property from it, such as for
  `DELETE /people/{vanId}/codes/{codeId} <https://docs.everyaction.com/reference/people-vanid-codes-codeid>`__,
  are named ``remove_X`` (as in :meth:`.People.remove_code`), where ``X`` is the type of data being removed. No
  methods of this kind currently remove multiple pieces of data, though in principle the name would then be pluralized.
* Methods which modify an existing piece of data by setting a property to a value, such as for
  `POST /people/{vanId}/disclosureFieldValues <https://docs.everyaction.com/reference/people-vanid-disclosurefieldvalues>`__,
  are called ``set_X`` (as in :meth:`.People.set_disclosure_fields`), where ``X`` is the type of data being set.
  All methods of this type currently operate on multiple pieces of data and are thus pluralized.
* Except for cases previously described, methods which perform an action for multiple pieces of data, such as for
  `POST /codes/batch <https://docs.everyaction.com/reference/codes-batch>`__ to create multiple codes, are
  name ``X_each`` (as in :meth:`.Codes.create_each`), where ``X`` is the action being performed.
* Many methods are shortened for brevity when their intent is obvious in the context. For example, to get a particular
  ballot return status, the method is named :meth:`return_status <.Ballots.return_status>` instead of
  ``ballot_return_status``, and other methods under :class:`.Ballots` have similar shortenings.