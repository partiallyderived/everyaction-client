Naming Conventions
==================

This page procedurally documents the naming conventions for methods, objects, and parameters in this package. Refer
to this section if you are having difficulty finding a particular service or method corresponding to an HTTP endpoint,
though that will hopefully rarely be the case. This section will commonly reference camelCase, CapWords, and snake_case
naming schemes.

* :doc:`EveryAction Objects <objects>` are usually named to exactly match a corresponding object referenced in the
  EveryAction documentation, but with the CapWords convention if that was not already the case (though it usually is).
  When in doubt, check the documentation for the :code:`kwargs` parameter of the method you want to call to check the
  type of object for the JSON data for that method, and the documented return values of a method to determine the type
  of the returned value.
* :doc:`Service Classes <services>` usually have names that match the corresponding groups in the EveryAction
  documentation but with spaces removed, resulting in a CapWords convention. There are some exceptions: for example, the
  service `Email <https://docs.everyaction.com/reference/email>`__ in the EveryAction documentation is called
  :class:`.EmailMessages` in this package since "Email" conflicts with an :class:`Email object .Email`.
* Instance attributes corresponding to services in :class:`.EAClient` usually have names which are snake_cased
  versions of the service they are an instance of. There are some exceptions for brevity:
  :class:`.ReportedDemographics` is shortened to :code:`demographics` for example.
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
  `GET /people/{vanId} <https://docs.everyaction.com/reference/people#peoplevanid>`__ (since it gets a
  :class:`.Person` under the service :class:`.People`), are called :code:`get` as in :meth:`.People.get`.
* Methods which retrieve a specific piece of data which *does not* correspond to the type of data for which the
  enclosing service is named, such as for
  `GET /people/{vanId}/membership <https://docs.everyaction.com/reference/people#peoplevanidmembership>`__
  are named according to the type of data being retrieved, in this case "membership" as in :meth:`.People.membership`.
* Methods which retrieve multiple pieces of data that correspond to the type of data for which the enclosing service
  is named, such as for
  `GET /activistCodes <https://docs.everyaction.com/reference/activist-codes#activistcodes>`__, are called
  :code:`list` as in :meth:`.ActivistCodes.list`.
* Methods which retrieve multiple pieces of data that *do not* correspond to the type of data for which the enclosing
  service is named, such as for
  `GET /people/{vanId}/activistCodes <https://docs.everyaction.com/reference/people#peoplevanidactivistcodes>`__,
  are named according to the pluralized version of the data being retrieved, such as :code:`activist_codes` as in
  :meth:`.People.activist_codes`.
* Methods which create new data, such as for
  `POST /codes <https://docs.everyaction.com/reference/codes#codes>`__, are called :code:`create` as in
  :meth:`.Codes.create`.
* Methods which update a specific piece of data, such as for
  `POST /people/{vanId} <https://docs.everyaction.com/reference/people#peoplevanid>`__, are called
  :code:`update` when the data being updated corresponds to the type of data for which the enclosing service is named
  (as in :meth:`.People.update`), and :code:`update_X` where :code:`X` is the type of data being updated when it does
  not correspond to the enclosing service (as in :meth:`.VoterRegistrationBatches.update_status`).
* Methods which delete a piece of data, such as for
  `DELETE /codes/{codeId} <https://docs.everyaction.com/reference/codes#codescodeid-2>`__, are called
  :code:`delete` when the data being deleted corresponds to the type of data for which the enclosing service is named
  (as in :meth:`.Codes.delete`), and :code:`delete_X` where :code:`X` is the type of data being deleted when it does not
  correspond to the enclosing service (as in :meth:`.Contributions.delete_attribution`).
* Methods which modify an existing piece of data by adding a property to it, such as for
  `POST /people/{vanId}/codes <https://docs.everyaction.com/reference/people#peoplevanidcodes>`__, are named
  :code:`add_X` (as in :meth:`.People.add_code`), where :code:`X` is the type of data being added. When such a method
  may add multiple pieces of data, such as for
  `POST /people/{vanId}/canvassResponses <https://docs.everyaction.com/reference/people#peoplevanidcanvassresponses>`__,
  the name is pluralized as in :meth:`.People.add_canvass_responses`.
* Methods which modify an existing piece of data by removing a property from it, such as for
  `DELETE /people/{vanId}/codes/{codeId} <https://docs.everyaction.com/reference/people#peoplevanidcodescodeid>`__,
  are named :code:`remove_X` (as in :meth:`.People.remove_code`), where :code:`X` is the type of data being removed. No
  methods of this kind currently remove multiple pieces of data, though in principle the name would then be pluralized.
* Methods which modify an existing piece of data by setting a property to a value, such as for
  `POST /people/{vanId}/disclosureFieldValues <https://docs.everyaction.com/reference/people#peoplevaniddisclosurefieldvalues>`__,
  are called :code:`set_X` (as in :meth:`.People.set_disclosure_fields`), where :code:`X` is the type of data being set.
  All methods of this type currently operate on multiple pieces of data and are thus pluralized.
* Except for cases previously described, methods which perform an action for multiple pieces of data, such as for
  `POST /codes/batch <https://docs.everyaction.com/reference/codes#codesbatch>`__ to create multiple codes, are
  name :code:`X_each` (as in :meth:`.Codes.create_each`), where :code:`X` is the action being performed.
* Many methods are shortened for brevity when their intent is obvious in the context. For example, to get a particular
  ballot return status, the method is named :meth:`return_status <.Ballots.return_status>` instead of
  :code:`ballot_return_status`, and other methods under :class:`.Ballots` have similar shortenings.