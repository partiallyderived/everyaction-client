Python Client for EveryAction
=============================

The Python client for EveryAction is a client for the
`EveryAction 8 Developer API <https://docs.everyaction.com/reference>`__ written in Python. The goal of this library is
to organize the various endpoints listed in the API into methods and make the construction of JSON data and query
arguments for the requests more convenient.

Quick Reference
===============

.. toctree::
    :maxdepth: 2

    services
    client
    exceptions
    objects
    naming

Using the Client
================

To make requests, you must first create an :class:`.EAClient` object:

.. code-block:: python

    from everyaction import EAClient
    client = EAClient(mode=1)

In this example, it is assumed that the environment variables ``EVERYACTION_APP_NAME`` and ``EVERYACTION_API_KEY`` are
defined as your application name and EveryAction API key respectively, and ``mode=1`` specifies that we are working in
MyCampaign mode instead of VoterFile mode. See :meth:`EAClient.__init__ <.EAClient.__init__>` for more information and
initialization options.

Once the client is created, requests may be made by calling methods of :doc:`EAService <services>` objects, which are
objects that organize methods in the same way that the
`EveryAction 8 developer documentation <https://docs.everyaction.com/reference>`__ organizes HTTP endpoints. For
example, the following code uses the :class:`.People` service to send a ``POST`` request to
`/people/find <https://docs.everyaction.com/reference/people-find>`__ to find a person with the phone number
555-555-5555 and the email 123@fakeemail.com:

.. code-block:: python

    data = client.people.find(phone='5555555555', email='123@fakeemail.com')

Each service appears as an instance attribute of :class:`.EAClient`. Check out its documentation to see a list of the
service attributes and to which part of the documented HTTP endpoints each object corresponds to. Furthermore, check
out the :doc:`services documentation <services>` to see a list of the services as well as what their methods are, and to
which HTTP endpoint they correspond to. Some methods, such as :meth:`.People.lookup`, are implemented for user
convenience and do not directly correspond to an HTTP endpoint.

Service Methods
=================

This section will document how a user may use an :class:`.EAClient` to call a method corresponding to an HTTP endpoint
in the `EveryAction 8 developer documentation <https://docs.everyaction.com/reference>`__.

User Workflow
-------------

The design of this package comes with the expectation that the user is at least vaguely familiar with the EveryAction 8
developer documentation and wants to leverage this package with the goal of invoking the available documented endpoints
in a way which is more convenient than using a more direct mechanism such as ``cURL`` or directly using
`The Python Requests Library <https://realpython.com/python-requests/>`__. With that in mind, here is an outline of the
recommended workflow for users seeking to develop using this package:

1. Use EveryAction's documentation to determine the endpoint you want to invoke and the service associated with that
   endpoint.
2. Lookup the documentation for the :doc:`service object <services>` corresponding to that group to find the method
   associated with that endpoint. When necessary (though hopefully the design is intuitive enough for this to seldom be
   the case), refer to the :doc:`naming` if you are having troubling locating a particular group or method.
3. With an `instantiated client <Using the Client>`_, call the appropriate methods using the path parameters as
   positional arguments and the desired query arguments and JSON data as keyword arguments. When doing so proves
   verbose, as is often the case with the long property names in the EveryAction API, consider using `Aliases`_ to
   decrease the amount of typing you have to do. Additionally, if you have many JSON data keys you want to specify,
   consider organizing them in an `EveryAction object <EveryAction Objects>`_ and then unpacking them.

More details about how methods may be called and what return values may be expected are given in the sections below.

Path Parameters, Query Arguments, and JSON Data
-----------------------------------------------

When specifying arguments for methods corresponding to HTTP endpoints, path parameters (those that appear in the URL)
must be specified positionally. For example, the following code will invoke
`GET /people/{vanId} <https://docs.everyaction.com/reference/get-people-vanid>`__ using :meth:`.People.get` to get the
person with the VAN ID ``1234``:

.. code-block:: python

    person = client.people.get(1234)

In contrast, all query and JSON data arguments must be specified as keyword arguments. For example, the following code
will add view restricted notes to the person with the VAN ID ``5555`` with the text "Wears funny hats" by invoking
`POST /people/{vanId}/notes <https://docs.everyaction.com/reference/post-people-vanid-notes>`__ using
:meth:`.People.add_notes`:

.. code-block:: python

    client.people.add_notes(5555, text='Wears funny hats', view_restricted=True)

Note that the `alias <Aliases>`_ *view_restricted* is used instead of the original data parameter name
*isViewRestricted* in the previous example.

In some cases, query arguments in the EveryAction API begin with a dollar sign (``$``). In this case, the dollar sign
may be omitted when specifying keyword arguments. The following gets a person as before, but
`expands <https://docs.everyaction.com/reference/expansion>`__ their phones and emails (note that the *$expand* query
argument begins with ``$``):

.. code-block:: python

    person = client.people.get(1234, expand='emails,phones')

As a final note, *$expand* is handled as a special case, allowing using to specify a sequence of strings if they
prefer. The following code does the same thing as the previous block:

.. code-block:: python

    person = client.people.get(1234, expand=['emails', 'phones'])

.. _aliases:

Aliases
-------

The following code creates an :class:`.Event` with an :class:`EventType` with ID ``5555`` and
:class:`voter registration batches <.VoterRegistrationBatch>` that have the IDs ``141``, ``173``, and ``200``
respectively:

.. code-block:: python

    event_id = client.events.create(
        eventType={'eventTypeId': 5555},
        voterRegistrationBatches=[
            {'voterRegistrationBatchId': 141},
            {'voterRegistrationBatchId': 173},
            {'voterRegistrationBatchId': 200}
        ]
    )

This code works, but it is quite verbose, especially considering the fact that we are only specifying 4 small pieces of
information (the IDs for the event type and the voter registration batches). We can save a lot of work by leveraging
aliases, which are shorter, snake_cased names which may be used in place of the original and often lengthy camelCased
names which appear in the documentation. In particular, when specifying an object with an ID, the alias *id* may be used
instead of the full property name. Additionally, :class:`.Event` objects recognize the aliases *type* for *eventType*
and *batches* for *voterRegistrationBatches*. Thus, the previous code may be made much more compact:

.. code-block:: python

    event_id = client.events.create(
        type={'id': 5555},
        batches=[
            {'id': 141},
            {'id': 173},
            {'id': 200}
        ]
    )

This is less work, but we can actually do even better by considering the following 2 facts about the implementation of
this package:

* `EveryAction Objects`_ which have IDs may always be constructed by specifying the ID as the first parameter. For
  example, ``event_type = EventType(5555)`` constructs an :class:`.EventType` with the ID ``5555``.
* When a non-mapping, non-tuple value is specified in place of where a particular EveryAction Object is expected, an
  attempt is made to implicitly construct an object of that type using that value as a constructor argument.

What these two facts imply is that we do not need to specify mappings for the simple (see
`A Note About Simple Objects <https://docs.everyaction.com/reference/events-overview>`__) :class:`.EventType` and
:class:`.VoterRegistrationBatch` objects, allowing for the following succinct code:

.. code-block:: python

    event_id = client.events.create(
        type=5555,
        batches=[141, 173, 200]
    )

In additional to usual aliases, there is also a special kind of alias called a "singular alias" which is an alias that
may be used to conveniently specify a single value where multiple values are expected. For example, if we only needed to
specify one voter registration batch with the ID 141, we could use the singular alias *batch* for
*voterRegistrationBatches* to do the following:

.. code-block:: python

    event_id = client.events.create(
        type=5555,
        batch=141
    )

The utility of singular aliases is even more apparent in the case of methods such as :meth:`.Person.find`, where it is
common to specify a single phone and/or email to lookup a person. Since phones may take a phone number as their first
constructor argument, and emails may take the email address, the singular aliases *phone* and *email* allow us to
translate the following "vanilla" call to find:

.. code-block:: python

    person = client.people.find(
        phones=[{'phoneNumber': '0123456789'}],
        emails=[{'email': '123@fakeemail.com'}]
    )

to this more compact call:

.. code-block:: python

    person = client.people.find(
        phone='0123456789',
        email='123@fakeemail.com'
    )

Now that the usage of aliases has been demonstrated, here are some general facts about aliases:

* Aliases are usually snake_cased (whereas the aliased property is almost always camelCased).
* Properties may have multiple aliases, or no aliases at all (like for the property *name*).
* The snake_cased version of a property name is *always* an alias for that property (i.e., *is_view_restricted* is an
  alias for *isViewRestricted*).
* Every property has at most one singular alias.
* Aliases may be used to access and set attributes on `EveryAction Objects`_.
* Singular aliases may *not* be used to access attributes on EveryAction Objects due to ambiguity (for example, if more
  than one phone is listed for a person, what should the value of ``person.phone`` be?). However, they may be used to
  set attributes: ``person.phone = '5555555555'``.
* When an object has a property whose name contains a prefix referencing the object it is a property for, such as the
  properties *financialBatchId*, *financialBatchNumber*, and *financialBatchName* for a :class:`.FinancialBatch`, the
  "un-prefixed" name will be an alias for that property, in this case *id*, *name*, and *number* respectively.
* When an object has a property which is an ID for another kind of object, the property name without "Id" is almost
  always an alias for that property, such as *designation* for *designationId* in
  :class:`DisclosureFieldValues <.DisclosureFieldValue>`.

EveryAction Objects
-------------------

EveryAction objects are objects referred to in the EveryAction documentation, usually under the "Common Models" section
for a particular service. For example, under the
`Common Models section for People <https://docs.everyaction.com/reference/common-models>`__, the various properties of
the "Person" API object are listed. Each documented EveryAction object has a corresponding Python class in this library,
such as the :class:`.Person` class, called "EAObjects". When EveryAction objects are in the response data for that
endpoint, the method corresponding to that endpoint will return the corresponding Python class, such as an
:class:`.ActivistCode` for the :meth:`.ActivistCodes.get` method. Additionally, when such objects have other EveryAction
objects as properties, the value of those properties will also be an instance of the corresponding Python class. Like
endpoint methods, these classes make use of `Aliases`_ to allow for more succinct property access: for instance, the
:class:`.Person` property *lastName* can be accessed with the aliases *last_name* and *last*:

.. code-block:: python

    from everyaction.objects import Person
    p = Person()
    p.lastName = 'Last 1'
    p.last = 'Last 2'
    p.lastName == p.last  # True

Aliases may also be used in initialization:

.. code-block:: python

    from everyaction.objects import Person
    p = Person(last='Smith')

Aside from organizing common properties, EAObjects may also be used to populate arguments for endpoints expecting an
EveryAction object, often the case when creating such objects in the EveryAction database such as when invoking
:meth:`.Codes.create`:

.. code-block:: python

    from everyaction import EAClient
    from everyaction.objects import Code, SupportedEntity
    client = EAClient()
    code = Code(
        'example',
        type='Tag',
        entities=[SupportedEntity('Events', searchable=True), SupportedEntity('Contacts', searchable=True)]
    )
    Codes.create(**code)

Unpacking ``code`` with ``**`` has the same affect as using keyword arguments with it's corresponding properties as
values, equivalent to

.. code-block:: python

    Codes.create(
        name='example',
        type='Tag',
        entities=[SupportedEntity('Events', searchable=True), SupportedEntity('Contacts', searchable=True)]
    )

A final note concerning the initialization of EAObjects: When an EveryAction object has a property corresponding to an
ID or a name, the corresponding EAObject takes an optional positional parameter in its constructor which will set the ID
(if it is an ``int``) or the name (if it is a ``str``) of the resulting object. This is the reason why, for the previous
example, the :class:`SupportedEntities <.SupportedEntity>` accepted positional arguments, as well as the created
:class:`.Code` object: in both cases, this has the same effect as using ``name='...'``.

Paginated Methods
-----------------

Paginated methods, such as :meth:`.ActivistCodes.list`, support the *limit* and *skip* keyword arguments:

.. code-block:: python

    from everyaction import EAClient
    client = EAClient()
    activist_codes = client.activist_codes.list(limit=23, skip=10)

The previous example will return at most 23 activist codes, starting from the tenth. While *skip* corresponds
exactly to the EveryAction parameter *$skip* described in the
`EveryAction documentation <https://docs.everyaction.com/reference/pagination>`__, *limit* does not exactly correspond
to *$top* because it may be set arbitrarily high: when it exceeds the maximum value for *$top* described for the
particular paginated method, multiple requests are sent and consolidated in the returned ``list``. If *limit* is not
specified, the configured default value in the :class:`.EAClient` instance will be used instead. This default value is,
by default ("the default for the default"), 50, but may be changed by setting the *default_limit* attribute of
:class:`.EAClient`:

.. code-block:: python

    from everyaction import EAClient
    client = EAClient()
    client.default_limit = 10
    activist_codes = client.activist_codes.list()  # Gets at most 10 activist codes.

Additionally, setting *limit* to 0 makes the number of results unlimited. If *default_limit* is set to 0, then an
unlimited amount of results will be retrieved when *limit* is unspecified.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
