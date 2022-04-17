# This module contains core code and implementation details for the Python EveryAction client. Users are not expected to
# interact with entities in this module directly.

from __future__ import annotations

import copy
import json
import re
import textwrap
import typing
from abc import ABC, ABCMeta
from collections.abc import Mapping, MutableMapping
from json import JSONEncoder
from typing import Any, Callable, Dict, Iterator, List, NewType, Optional, Set, Tuple, Type, TypeVar, Union

from makefun import wraps

from everyaction.exception import EAException, EAHTTPException

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from everyaction.client import EAClient


# Name of the reference to the section of documentation about aliases. Used for linking lists of aliases to this page.
_ALIAS_REF = 'aliases'

# Regex used to insert underscores before all sequences of capital letters in an attribute name to convert from
# camelCase of UpperCase to snake_case.
_CAMEL_TO_SNAKE_REGEX = re.compile(r'([A-Z]+)')

# The standard maximum value for top supported by EveryAction (see
# https://docs.everyaction.com/reference/overview#pagination).
_DEFAULT_MAX_TOP = 200

# For documentation purposes, keep track on properties added to methods decorated with @ea_endpoint.
_ENDPOINT_PROPERTIES = {}

# Debug flag: When set, return raw response instead of the processed JSON.
_RAW_RESPONSE = False

# All request types we will use to interact with EveryAction.
_SUPPORTED_REQUEST_TYPES = {'delete', 'get', 'patch', 'post', 'put'}

# Regex used to replace $top query arg in path.
_TOP_REGEX = re.compile(r'\$top=\d*')

# Type parameter for types bounded by EAObjects.
E = TypeVar('E', bound='EAObject')

# Type of values present in JSON data and query arguments for EveryAction.
EAValue = NewType('EAValue', Optional[Union[bool, int, float, str, None, List['EAValue'], 'EAObject']])

# Type of mappings from str to EAValue.
EAMap = NewType('EAMap', typing.MutableMapping[str, EAValue])


def _parse_path_params(route: str) -> List[str]:
    # Gives a list of the path parameters of the given string in the order in which they appear.
    # Assumes a route like e.g. a/b/{var1}/c/{var2}/{var1} where the braces literally appear, and otherwise assumes that
    # the route is "simple" in that it contains no difficult to parse components/edge cases, as is the case for
    # EveryAction endpoints.
    with_duplicates = re.findall(r'[^{]*{([^}]*)}', route)
    found = set()
    result = []
    for path_param in with_duplicates:
        if path_param not in found:
            found.add(path_param)
            result.append(path_param)
    return result


def ea_endpoint(
    path_template: str,
    req_type: str,
    query_arg_keys: Set[str] = frozenset(),
    paginated: bool = False,
    max_top: int = 0,
    path_params_to_data: Set[str] = frozenset(),
    prop_keys: Set[str] = frozenset(),
    props: Optional[Dict[str, 'EAProperty']] = None,
    data_type: Optional[Type[E]] = None,
    has_result: bool = True,
    result_array: bool = False,
    result_array_key: str = '',
    result_key: Optional[str] = None,
    result_factory: Optional[Callable] = None,
    exclude_keys: Set[str] = frozenset(),
    none_if_404: bool = False
) -> Callable:
    # This decorator uses consistencies and parameters (e.g., max value for top in a paginated request) in the
    # EveryAction API to "configure" how the request data and arguments are processed, how the request is sent, and how
    # the response data is processed in order to avoid repeating common logic. In fact, all of the logic for the
    # requests methods are implemented in this decorator: the methods themselves are placeholders existing for
    # documentation purposes.

    # Here is a description of each argument:

    # path_template: An API path which may use literal braces {} to indicate path parameters. See _parse_path_params
    # above for more info.

    # req_type: The request type (GET, PUT, etc.)

    # query_arg_keys: The names of the query args relevant for this request, excluding $expand, $skip, and $top which
    # are handled specially. Such names must resolve to a EAProperty (more on how this is done below), and the aliases
    # for that property may be used by the user to specify query args for this request.

    # paginated: Indicates whether the wrapped method will be for a paginated request. In the case that it is, the
    # keyword arguments "limit" and "skip" may be specified (more below), and the result of the request should be a
    # list.

    # max_top: Indicates what the maximum value for the $top query argument is for this request. When not specified and
    # paginated=True, _DEFAULT_MAX_TOP is assumed.

    # path_params_to_data: Indicates which path arguments should be copied as keys in data. At the time of writing, this
    # is currently only used for convenience in services.Events.patch.

    # prop_keys: The names of properties relevant for the JSON data of this request. Each name must resolve to an
    # EAProperty. Typically, prop_keys is used for JSON data keys which are not implicit in the EAObject associated with
    # this request, if any (see data_type below for more info).

    # props: Mapping from property names to EAProperty which are relevant to this request. This is sparsely used, as it
    # is preferred to use this parameter only when a property name conflicts with a more commonly used property.
    # Otherwise, the preference is to either get the property implicitly from data_type, or to specify it as a common
    # EAProperty via EAProperty.add.

    # data_type: The type of objects represents by the JSON data of this request. The purpose of specifying the type
    # here is solely as a convenient means of specifying a common set of properties for a method. Usage of the EAObjects
    # directly is unnecessary by the user, who may use keyword arguments of the names or aliases of the properties of
    # that object instead if they desire.

    # has_result: When True, response processing is foregone other than checking for an exception and the method returns
    # early.

    # result_array: When True, the structure of response data is assumed to be a list of objects which are individually
    # processed using result_factory.

    # result_array_key: When specified, the structure of response data is assumed to be a mapping with only this key,
    # with its value being a list of objects to be individually processed using result_factory.

    # result_key: When specified, the structure of response data (or of individual objects in array data) is assumed
    # to be a mapping with only this key, with its value being the data to return in this method. The purpose of this
    # parameter is to conveniently extract single-element maps for the user so they may avoid the frivolous step of
    # extracting a mapping value.

    # result_factory: When specified, the response data (or of individual objects in array data) is processed by calling
    # this, usually resulting in an EAObject corresponding to an EveryAction API object. Typically, the value for this
    # parameter is just a subclass of EAObject, and calling it just instantiates that object using its constructor.
    # Sometimes it is a more complicated factory, though.

    # exclude_keys: When specified, exclude these keys from the resulting data. Useful when multiple keys are returned
    # for the same property (i.e., both locationId and id in response data for a Location) and one must be suppressed
    # to prevent an error being raised in the constructor.

    # none_if_404: When specified, return None rather than erroring upon receiving a response with status code 404.

    # How EAProperty objects are resolved:
    # Firstly, if data_type is specified, data_type._properties() populates the collection of properties.
    #
    # Then, any properties specified in props populates the collection, overriding any which were already present.
    #
    # Finally, any properties specified in prop_keys, query_arg_keys, and/or path_params_to_data are assumed to be
    # common properties accessible via EAProperty.get if they were not specified by props; if they cannot be resolved
    # this way, an AssertionError is raised.
    #
    # Note that query_arg_keys, prop_keys, path_params_to_data are assumed to have no common keys (as that would be
    # redundant), and if they do, an AssertionError in raised.
    #
    # These keys are likewise assumed to be disjoint from the keys of data_type._properties(), as a need to specify
    # repeat keys in this way never arose and likely indicates a mistake, and thus an AssertionError is raised.
    #
    # Additionally, prop_keys and props are assumed to have no common keys (as that is likewise redundant), and if they
    # do, an AssertionError is raised.
    #
    # If the properties pass all checks, the collection is used to instantiate an EAProperties object, which will be
    # used to resolve aliases given by the user when calling this method.

    # Make sure there are no unexpected request types.
    if req_type not in _SUPPORTED_REQUEST_TYPES:
        raise AssertionError(
            f'Got "{req_type}" as a request type, expected one of: {", ".join(_SUPPORTED_REQUEST_TYPES)}'
        )

    # These args contradict each other.
    if result_key and result_factory:
        raise AssertionError(
            f'Only one of result_key={result_key} and result_factory={result_factory} may be specified'
        )
    if sum(bool(x) for x in [result_key, result_factory]) > 1:
        raise AssertionError(
            f'At most one of result_key={result_key}, or  result_factory={result_factory} '
            f'may be specified.'
        )

    # Make sure no args which suggest a result are specified when has_result=False.
    if not has_result and (
        paginated
        or result_array
        or result_array_key
        or result_key
        or result_factory
    ):
        raise AssertionError(
            f'has_result should be True when any of paginated={paginated}, result_array={result_array}, '
            f'result_array_key={result_array_key}, result_key={result_key}, or result_factory={result_factory}, are '
            f'True/present.'
        )

    props = props or {}

    # paginated, result_array, and result_array_key all specify different ways to extract a sequence of objects from
    # response data. They are therefore mutually exclusive.
    if sum(bool(x) for x in [paginated, result_array, result_array_key] if x) > 1:
        raise AssertionError(
            f'At most one of paginated={paginated}, result_array={result_array}, or '
            f'result_array_key={result_array_key} should be True/present.'
        )

    path_params = _parse_path_params(path_template)

    if any(k not in path_params for k in path_params_to_data):
        raise AssertionError(
            f'path_params_to_data={path_params_to_data} contains keys not in path_params={path_params}'
        )

    # This will keep track of all properties and will be used to create an EAProperties object.
    properties = {}

    if data_type:
        # First, take the properties from the class data_type, if specified.
        properties.update(data_type._properties())

    all_keys = prop_keys | {q.lstrip('$') for q in query_arg_keys} | path_params_to_data
    # Specifying keys in more than one of these sets is redundant. Check that they are disjoint sets by confirming that
    # the size of their unions is the sum of their sizes.
    if len(all_keys) != len(prop_keys) + len(query_arg_keys) + len(path_params_to_data):
        raise AssertionError(
            f'At least one key specified in more than one of prop_keys={prop_keys}, '
            f'query_arg_keys={query_arg_keys}, path_params_to_path={path_params_to_data}'
        )

    if data_type and (
        any(k in data_type._properties() for k in all_keys) or any(k in data_type._properties() for k in props)
    ):
        # No situation arose where it made sense to have keys in both data_type._properties() and any of the other
        # property sources, so this is assumed to be an error for now.
        raise AssertionError(
            f'{data_type.__name__} has at least one property in {data_type._properties()._properties} also specified '
            f'in at least one of prop_keys={prop_keys}, query_arg_keys={query_arg_keys}, '
            f'path_params_to_data={path_params_to_data}'
        )

    # Properties specified in props override properties from data_type._properties().
    properties.update(props)

    # Keys in props and prop_keys should be mutually exclusive, as they could have just been specified in props if they
    # are in both.
    if any(k in props for k in prop_keys):
        raise AssertionError(f'At least one key specified in both prop_keys={prop_keys} and props={props}')

    for k in all_keys:
        # Properties specified through props take precedence over properties specified through prop_keys.
        if k not in props:
            properties[k] = EAProperty.shared(k)

    properties = EAProperties(properties)

    # Allow paginated and result_array_key to imply result_array so the code logic is simpler.
    result_array = result_array or result_array_key or paginated

    # Set factory depending on if either of result_key or result_factory is specified.
    if result_key:
        factory = lambda x: x[result_key]
    elif result_factory is not None:
        # Explicit result factories should expand mapping data as keyword arguments in the given factory, or else apply
        # the factory directly if the argument is not a mapping.
        def factory(x: EAValue):
            if isinstance(x, MutableMapping):
                for k in exclude_keys:
                    del x[k]
                return result_factory(**x)
            else:
                return result_factory(x)
    else:
        # Use identity by default.
        factory = lambda x: x

    max_top = max_top or _DEFAULT_MAX_TOP

    def inner(func: Callable) -> Callable:
        # Name with which the decorated function will be referred to (e.g., "People.find_or_create") in error messages.
        func_ref_name = '.'.join(func.__qualname__.rsplit('.', 2)[1:])

        if properties and func.__doc__:
            # Add valid parameters for documentation purposes.
            properties.add_to_doc(func, 'Keyword Arguments')

        @wraps(func)
        def wrapper(
            self: EAService,
            *args: Any,
            data: Optional[EAValue] = None,
            limit: Optional[int] = None,
            skip: Optional[int] = None,
            top: Optional[int] = None,
            **kwargs: Any
        ) -> Any:
            # func is not actually called, all logic is implemented by wrappers.
            # The signature of func is for documentation purposes only.

            # *args is used exclusively to specify path parameters, and they may not be specified any other way.
            # These arguments are always documented explicitly in the decorated method stub as corresponding to a path
            # parameter.
            #
            # **kwargs is used to specify both query arguments and JSON data keys and values. Since EAObjects are
            # MutableMappings, there is no issue serializing them as JSON data and they may be specified here as if they
            # were mappings with their non-None attributes as keys. Additionally, this has the benefit of allowing the
            # aliases of that object to be used, either in constructing the EAObject or even when specifying its
            # properties via **kwargs since its properties are available in the EAProperties object constructed above.
            #
            # data may be specified by users to send unprocessed raw data. It is only documented in the decorated method
            # when the request JSON data is not a mapping, which is rare but requires data to be specified instead of
            # the JSON data keys, which assume a mapping.
            #
            # expand, skip, and top correspond to the query arguments $expand, $skip, and $top respectively.
            # $top however is not used for this library and an EAException is thrown if it is used.
            #
            # Instead, limit is used to specify an arbitrarily large (or unlimited when set to 0) number of records
            # which may be returned.

            # EAClient.{delete, get, patch, post, put}.
            request_method = getattr(self.ea, req_type)

            # Path param name -> value
            name_to_path_param = dict(zip(path_params, args))
            for param_name in path_params_to_data:
                # If path_params_to_data specifies path parameters which should be duplicated as JSON data, do so.
                if properties[param_name].find(param_name, kwargs) is None:
                    # Only add it if it is absent.
                    kwargs[param_name] = name_to_path_param[param_name]
            # Use Python str formatting to expand path parameters to the given values.
            route = path_template.format(**name_to_path_param)

            # Finally, process the arguments, resolving aliases to the actual keys expected by the EveryAction API.
            try:
                data_args = properties.process(kwargs)
            except KeyError as e:
                # Give a more helpful exception.
                attr = str(e).replace("'", '')
                raise EAException(f'Name or alias "{attr}" not recognized by {func_ref_name}.')
            query_args = {}
            for k in query_arg_keys:
                # Query args starting with $ may be specified without the $.
                stripped = k.lstrip('$')
                if stripped in data_args:
                    query_arg = data_args.pop(stripped)
                    if not isinstance(query_arg, str):
                        # Serialize all non-str query args as JSON.
                        query_arg = json.dumps(query_arg, cls=EAObjectEncoder)
                    query_args[k] = query_arg

            if paginated:
                if top is not None:
                    raise EAException('$top is not supported for the Python EveryAction API, use limit instead.')
                limit = self.ea.default_limit if limit is None else limit
                # The query arg for top needs to be at most max_top
                query_args['$top'] = min(limit, max_top) or max_top
                query_args['$skip'] = 0 if skip is None else skip
            else:
                # Complain if any pagination parameters are specified: since they are not specified as part of **kwargs,
                # erroneously specifying them will not result in an error response.
                if top is not None:
                    raise EAException(
                        f'top={top} given for {func_ref_name}, which is not paginated. Also, $top is not supported for '
                        f'the Python EveryAction API, use limit instead.'
                    )
                if skip is not None:
                    raise EAException(f'skip={skip} given for {func_ref_name}, which is not paginated.')
                if limit is not None:
                    raise EAException(f'limit={limit} given for {func_ref_name}, which is not paginated.')

            # If raw data is specified in the argument "data", use that instead of whatever remains in data_args.
            data = data or data_args
            json_data = json.dumps(data, cls=EAObjectEncoder)
            response = request_method(
                route,
                params=query_args,
                data=json_data or data_args,
                headers={'Content-Type': 'application/json'}
            )
            if _RAW_RESPONSE:
                return response

            if not response:
                if response.status_code == 404 and none_if_404:
                    return None
                raise EAHTTPException(response)

            if not has_result:
                # Return early instead of attempting response JSON data processing.
                return

            resp_data = response.json()

            if result_array:
                if paginated:
                    # If paginated, keep getting records until either we reach the requested limit or we get all
                    # records.

                    # Paginated responses always have an "items" key, which is a list of results.
                    items = resp_data['items']
                    next_page = resp_data['nextPageLink']
                    while (not limit or len(items) < limit) and next_page:
                        if 0 < limit - len(items) < max_top:
                            # Replace $top=<num> with $top={limit - len(items)} so we receive at most that many.
                            next_page = _TOP_REGEX.sub(f'$top={limit - len(items)}', next_page)
                        # Query arguments will be implicit in the URL given by nextPageLink.
                        response = request_method(next_page, json=json_data)
                        if not response:
                            raise EAHTTPException(response)
                        resp_data = response.json()
                        items += resp_data['items']
                        next_page = resp_data['nextPageLink']
                else:
                    # Sometimes response JSON data for arrays is a sequence, other times it's a map with a single key
                    # for the sequence.
                    if result_array_key:
                        items = resp_data[result_array_key]
                    else:
                        items = resp_data
                return [factory(x) for x in items]
            else:
                return factory(resp_data)
        return wrapper
    return inner


def to_snake(attr: str) -> str:
    # Convert camelCased or UpperCased attribute name to a snake_cased attribute name.
    # Use lower() to force all characters to be lower-cased after they are replaced.
    return attr[0].lower() + _CAMEL_TO_SNAKE_REGEX.sub(r'_\1', attr[1:]).lower()


class EAService(ABC):
    # Abstract base class of groups of API endpoints, like People or Contributions.
    def __init__(self, ea: EAClient) -> None:
        """Initialize this service with the given client.

        :param ea: The client to initialize this with.
        """
        self.ea = ea


class EAProperty:
    # Represents a single property associated with an EveryAction object.
    # Users are not expected to interact with this class directly.

    # Reuse properties when able by storing them in this dict.
    # The principle behind when properties are added to _shared is that they are always added, even if they are only
    # used once, except when there are name conflicts with a more or equally-common usage of the property name, or if
    # the contextually relevant aliases for a property are particularly specific (e.g., the property "eventDescription"
    # would have the alias "event_desc" when it is a property of a non-Event object, but "desc" when it is a property
    # of event. In the latter case, it should not be specified as a shared property).
    # This "aggressive reuse" strategy allows developers to forego time spent determining whether a property is
    # "common enough" to be added here and maximally limit code reuse.
    _shared = {}

    @staticmethod
    def share(**kwargs: 'EAProperty') -> None:
        # Add an EAProperty to shared properties.
        for k, v in kwargs.items():
            # Adding a property of the same name twice is not allowed, so assert this is False as it is assumed that
            # developers add a finite amount of constant properties.
            if k in EAProperty._shared:
                raise AssertionError(f'{k} is already a shared property')
            # Add snake-cased name as alias if it hasn't been already.
            as_snake = to_snake(k)
            if as_snake != k:
                v.aliases.add(as_snake)
            EAProperty._shared[k] = v

    @staticmethod
    def shared(name: str) -> 'EAProperty':
        # Get a shared EAProperty.
        if name not in EAProperty._shared:
            # AssertionError raised because this is only called when creating decorators and data types, both of which
            # are finite in number and done by the developer, not the user.
            raise AssertionError(f'{name} is not a shared property')
        return EAProperty._shared[name]

    def __init__(
        self,
        *aliases: str,
        is_array: bool = False,
        singular_alias: Optional[str] = None,
        factory: Optional[Callable[..., EAValue]] = None
    ) -> None:
        # Initialize an EAProperty
        #
        # aliases: aliases for which this property may be referred. The actual name should be excluded, as their are
        # mechanisms to reuse properties with different names (see _prefix and _prefixed in EAMeta).
        #
        # is_array: When True, this property is for a sequence of values rather than a single value. In this case, the
        # given factory will be applied to each element of the sequence rather than the value itself.
        #
        # singular_alias: When specified, this special alias may be used to set an set an attribute which corresponds
        # to this property, which is assumed to be a sequence, to a single value which is of the sequence's element
        # type, which is then wrapped in a list under the hood. See EAObject.__setattr__ for more info. Setting this
        # argument will also set is_array to True.
        #
        # factory: When specified, use this Callable to transform "raw" values for this property, usually into an
        # EAObject through which aliases will be recognized. See EAProperty.value below for more info.

        # Allow singular_alias to imply is_array.
        is_array = is_array or bool(singular_alias)

        self.is_array = is_array
        self.aliases = set(aliases)
        self.singular_alias = singular_alias
        self.factory = factory

    def __eq__(self, other: 'EAProperty') -> bool:
        # Useful for testing purposes.
        return (
            (self.is_array, self.aliases, self.singular_alias, self.factory)
            == (other.is_array, other.aliases, other.singular_alias, other.factory)
        )

    def _create(self, arg: Any) -> E:
        if isinstance(arg, EAObject) or not self.factory:
            # Just return the argument when creation is redundant (EAObjects are never subjected to additional
            # processing) or if self.factory is None.
            return arg
        if isinstance(arg, Mapping):
            # Mappings will be used to pass keyword arguments to the factory. This is the most common scenario,
            # other than perhaps already having an EAObject.
            return self.factory(**arg)
        # Expand arg as positional arguments for the factory by first ensuring it is a tuple.
        # This allows EAObjects to be implicitly created from single parameters or tuples. Most commonly, they may
        # be implicitly created from their IDs, which is enormously useful for users. For example, the following is
        # the verbose, "vanilla" way to set simple (ID-only) VoterRegistrationBatches for posting Events:
        #     voterRegistrationBatches=[
        #         {'voterRegistrationBatchId': 1},
        #         {'voterRegistrationBatchId': 2},
        #         {'voterRegistrationBatchId': 3}
        #     ]
        #
        # Compare this with what is possible with aliases and implicit construction:
        #     batches=[1, 2, 3]
        if not isinstance(arg, tuple):
            arg = (arg,)
        return self.factory(*arg)

    def find(self, name: str, args: EAMap, pop: bool = False) -> Optional[EAValue]:
        snake_name = to_snake(name)
        # Return the value of this property in args or None if it is not found. An EAException is raised if multiple
        # aliases for this property are found in the given map. When pop is True, also remove it from the map.
        result = None

        # Need to include the property's real name and singular alias for searching purposes.
        all_aliases = {name, snake_name} | self.aliases
        if self.singular_alias:
            all_aliases.add(self.singular_alias)
        for alias in all_aliases:
            new_result = args.get(alias)
            if new_result is not None:
                if result is not None:
                    # Specifying multiple aliases for a property is not allowed.
                    raise EAException(f'Found multiple aliases for {name} in {args}')
                result = new_result
                if pop:
                    args.pop(alias)
        return self.value(name, result)

    def value(self, name_or_alias: str, arg: Any) -> Optional[Union[E, List[E]]]:
        if arg is None:
            # Always return None for None arg.
            return None
        # Get the processed value for arg using data in this property.
        if self.is_array:
            # If the alias given is the singular alias, assume arg is meant to be a sequence element of an array
            # property.
            if name_or_alias == self.singular_alias:
                return [self._create(arg)]
            # Otherwise, call self.factory for each element.
            if not isinstance(arg, list):
                raise TypeError(f'Expected list for "{name_or_alias}", got {type(arg).__name__}: {arg}')
            return [self._create(x) for x in arg]
        # Not an array property, just call self.factory on arg.
        return self._create(arg)


# These are needed to define classes later.
EAProperty.share(id=EAProperty(), name=EAProperty())


class EAProperties(Mapping):
    # Represents a collection of EAProperty instances.
    # Implements a Mapping for ease of use. MutableMapping is unnecessary as EAProperties are assumed to be immutable
    # after creation.
    # Used to resolve aliases for a collection of properties when supplying request keywords or when getting/setting
    # attributes for EAObjects.

    def __init__(self, mapping: EAMap) -> None:
        # Initialize by populating mapping of aliases to the resolved EveryAction property name.
        alias_map = {}
        for name, prop in mapping.items():
            # The actual name will functionally serve as an alias for itself.
            alias_map[name] = name
            for alias in prop.aliases:
                alias_map[alias] = name
            if prop.singular_alias:
                # Just add the singular alias as another alias: it will be distinguished as a singular alias when
                # EAProperty.value is called.
                alias_map[prop.singular_alias] = name
            # Add snake-cased version of name as alias, as this was always found to be a desired alias, and lots of
            # typing can be saved from not having to explicitly specify snake-cased names as aliases.
            as_snake = to_snake(name)
            alias_map[as_snake] = name
        self._alias_map = alias_map
        self._properties = copy.deepcopy(mapping)

    def __getitem__(self, key: str) -> EAProperty:
        # Allow getting items with alias.
        return self._properties[self.resolve(key)]

    def __iter__(self) -> Iterator[str]:
        return iter(self._properties)

    def __len__(self) -> int:
        return len(self._properties)

    def add_to_doc(self, entity: Any, header_name: str) -> None:
        doc_str = entity.__doc__
        # These are string components to be joined later to create the documentation with the properties added.
        components = []

        # Dedent docs since indentation consistent with the definition only matters for the source code, and it is more
        # efficient and less painful to deal with dedented doc strings.
        # Need to find where indentation starts in order to dedent (note that the first line of a doc string will not
        # be indented in the string itself, only in the source code).
        first_line_and_rest = doc_str.split('\n', 1)
        if len(first_line_and_rest) == 2:
            first_line, rest = first_line_and_rest
            components.append(first_line)
            components.append('\n')
            components.append(textwrap.dedent(rest))
        else:
            # No newline, just use original doc string.
            components.append(doc_str)
        components.append(f'\n\n:{header_name}:')

        for name, prop in sorted(list(self.items()), key=lambda x: x[0]):
            if isinstance(prop.factory, type) and issubclass(prop.factory, EAObject):
                # Put property as a bolded link to the expected type.
                prop_str = f'\n    * :class:`{name} <.{prop.factory.__name__}>`'
            else:
                # Put property as a bolded list element.
                prop_str = f'\n    * **{name}**'
            components.append(prop_str)
            if prop.aliases or prop.singular_alias:
                # List each alias separated by commas in descending order of length.
                aliases = [f'{alias}' for alias in sorted(list(prop.aliases), key=lambda x: -len(x))]
                if prop.singular_alias:
                    aliases.append(f'{prop.singular_alias} (singular)')
                components.append(f'\n      :ref:`({", ".join(aliases)}) <{_ALIAS_REF}>`')
        entity.__doc__ = ''.join(components)

    def process(self, args: EAMap) -> EAMap:
        # Process a mapping by retrieving each key's EAProperty and applying EAProperty.value to its value for each item
        # in args.
        result = {}
        for k, v in args.items():
            resolved = self.resolve(k)
            if resolved in result:
                raise EAException(f'Multiple aliases for "{resolved}" given in {args}')
            prop = self[resolved]
            value = prop.value(k, v)
            result[resolved] = value
        return result

    def resolve(self, alias: str) -> str:
        # Give the name of the attribute corresponding to the given alias, raising a KeyError if it is not an alias for
        # any attribute.
        result = self._alias_map.get(alias)
        if result is None:
            raise KeyError(alias)
        return result


class EAMeta(ABCMeta):
    # Meta class for EveryAction objects. Allows snake-cased versions of properties to automatically serve as aliases,
    # and implements the logic needed to create each class's alias map and EAProperties object.

    @staticmethod
    def _init_fn(self, **kwargs: EAValue) -> None:
        # Keep track of aliases given to detect when multiple aliases are erroneously specified.
        attr_to_alias = {}
        unrecognized = []
        for k, v in kwargs.items():
            if v is not None:
                try:
                    resolved = self._resolve_attr(k)
                except AttributeError:
                    # See if we can set the attribute, such as through a property.
                    try:
                        setattr(self, k, v)
                    except AttributeError:
                        # Keep track of unrecognized attributes to give a more informative exception.
                        unrecognized.append(k)
                else:
                    old_value = None
                    if resolved in attr_to_alias:
                        old_value = self[resolved]
                    attr_to_alias[resolved] = k
                    self._setattr(k, resolved, v)
                    if old_value is not None and self[resolved] != old_value:
                        raise ValueError(
                            f'Multiple aliases with different values given for {resolved}: '
                            f'{attr_to_alias[resolved]}: {old_value}, {k}: {self[resolved]}'
                        )
        if unrecognized:
            if len(unrecognized) == 1:
                str_component = 'property is'
            else:
                str_component = 'properties are'
            raise AttributeError(
                f'The following {str_component} unrecognized for {self.__class__.__name__}: '
                f'{", ".join(unrecognized)}'
            )

    @staticmethod
    def _default_init() -> Callable[['EAObject', ...], None]:
        def __init__(self, **kwargs: EAValue) -> None:
            """Initialize by setting the specified property names and aliases. Note that values will automatically be
            converted to API objects when appropriate.

            :param kwargs: Mapping of (alias or name) -> value.
            :raise AttributeError: If any unrecognized properties are given in *kwargs*.
            :raise ValueError: If multiple aliases are given for the same property but with different values.
            """
            EAMeta._init_fn(self, **kwargs)
        return __init__

    @staticmethod
    def _id_init() -> Callable[['EAObject', Optional[int], ...], None]:
        def __init__(self, id: Optional[int] = None, **kwargs: EAValue) -> None:
            """Initialize by setting the specified property names and aliases. Note that values will automatically be
            converted to API objects when appropriate.

            :param id: ID to initialize with. When given alone, a simple object results (see
                `A Note About Simple Objects <https://docs.everyaction.com/reference/events-overview#overview-19>`__).
            :param kwargs: Mapping of (alias or name) -> value.
            :raise AttributeError: If any unrecognized properties are given in *kwargs*.
            :raise ValueError: If multiple aliases are given for the same property but with different values.
            """
            EAMeta._init_fn(self, id=id, **kwargs)
        return __init__

    @staticmethod
    def _name_init() -> Callable[['EAObject', Optional[str], ...], None]:
        def __init__(self, name: Optional[str] = None, **kwargs: EAValue) -> None:
            """Initialize by setting the specified property names and aliases. Note that values will automatically be
            converted to API objects when appropriate.

            :param name: Name to initialize the object with.
            :param kwargs: Mapping of (alias or name) -> value.
            :raise AttributeError: If any unrecognized properties are given in *kwargs*.
            :raise ValueError: If multiple aliases are given for the same property but with different values.
            :raise TypeError: If *id_or_name* is neither an ``int`` nor a ``str``.
            """
            EAMeta._init_fn(self, name=name, **kwargs)
        return __init__

    @staticmethod
    def _id_and_name_init() -> Callable[['EAObject', Optional[Union[int, str]], ...], None]:
        def __init__(self, id_or_name: Optional[Union[int, str]] = None, **kwargs: EAValue) -> None:
            """Initialize by setting the specified property names and aliases. Note that values will automatically be
            converted to API objects when appropriate.

            :param id_or_name: ID (if an integer) or name (if a string) to initialize with. A simple object will result
                when an integer is given (see
                `A Note About Simple Objects <https://docs.everyaction.com/reference/events#overview-19>`__).
                When a string is given instead, it is assumed to correspond to the object's name, accessible via
                instance.name.
            :param kwargs: Mapping of (alias or name) -> value.
            :raise AttributeError: If any unrecognized properties are given in *kwargs*.
            :raise ValueError: If multiple aliases are given for the same property but with different values.
            :raise TypeError: If *id_or_name* is neither an ``int`` nor a ``str``.
            """
            if id_or_name is not None:
                if isinstance(id_or_name, int):
                    # Assume id for int.
                    EAMeta._init_fn(self, id=id_or_name, **kwargs)
                elif isinstance(id_or_name, str):
                    # Assume name for str.
                    EAMeta._init_fn(self, name=id_or_name, **kwargs)
                else:
                    raise TypeError(
                        f'Expected int or str for id_or_name, got {type(id_or_name).__name__}: {id_or_name}'
                    )
            else:
                EAMeta._init_fn(self, **kwargs)
        return __init__

    def __new__(
        mcs,
        name: str,
        bases: Tuple[type, ...],
        dct: Dict[str, Any],
        /,
        *,
        _id: str = '',
        _name: str = '',
        _prefix: str = '',
        _prefixed: Set[str] = None,
        _shared: Set[str] = None,
        **kwargs: EAProperty
    ) -> type:
        # name, bases, and dct are standard metaclass __new__ arguments.
        #
        # _id: If specified, this EAObject has an ID. In this case, instances of this EAObject may be constructed with
        # just one positional argument, the ID, in addition to any keyword arguments. The ID may still be set via
        # keyword if desired.
        #
        # _name: If specified, this EAObject has a name. In this case, instances of this EAObject may be constructed
        # with just one positional argument, the name, in addition to any keyword arguments. The name may still be set
        # via keyword if desired.
        #
        # If both _id and _name are specified, the EAObject may still be constructed from just one positional argument.
        # If this is the case, this argument is assumed to be the ID if it is an int and the name if it is a str.
        #
        # _prefix: A string prefix which may be specified which allows properties whose names start with _prefix to
        # "defer" to shared properties with the un-prefixed name. For example, with a _prefix of "event",
        # "eventDescription" can defer to the shared property "description" (note that the first character of the
        # un-prefixed name is converted to lower-case so that the camelCased property can be found).
        # When _id is also specified, it is assumed that the ID is prefixed (as in "eventId") as this is almost always
        # the case. Other prefixed properties must be specified with their un-prefixed names in _prefixed.
        #
        # _prefixed: See _prefix above.
        #
        # _shared: The names of shared properties accessible via EAProperty.get to add to the created class's
        # properties. This is the most common way to add properties to a class.
        #
        # **kwargs: Used to specify new EAProperty objects as properties for the created class.
        # For example, newProp=EAProperty('prop') will add a property named "newProp" with the alias "prop".
        # Using EAProperty.add to register shared properties instead of adding them here is the preferred way to create
        # new properties. See comments under EAProperty for more info.

        # Create an __init__ method if it is not already present.
        _prefixed = _prefixed or set()
        _shared = _shared or set()
        init = None
        if name == 'EAObject':
            # Ideally, this __init__ method would just be placed directly in EAObject. However, a no-op __init__ with a
            # different signature appears in EAObject instead. The reason for this is to prevent PyCharm from
            # complaining about unexpected arguments when generated __init__ methods take a positional argument
            # Otherwise, users of the package who use PyCharm would observe highlighted errors for typical and correct
            # use-cases.
            init = mcs._default_init()
        elif '__init__' not in dct:
            if _id:
                if _name:
                    init = mcs._id_and_name_init()
                else:
                    init = mcs._id_init()
            elif _name:
                init = mcs._name_init()
            # Otherwise, keep EAObject's __init__.
        if init:
            init.__qualname__ = f'{name}.__init__'
            dct['__init__'] = init

        ea_type = super().__new__(mcs, name, bases, dct)

        properties = {}
        for base in bases:
            if isinstance(base, EAMeta):
                # Inherit properties from base classes.
                properties.update(base._properties())

        if _id:
            # Assume ID is prefixed if present (or in other words, if there is an ID only use a prefix if the ID is
            # prefixed).
            if _prefix:
                _prefixed.add(_id)
            elif _id not in kwargs:
                _shared.add(_id)

        if _name and _name not in kwargs and _name not in _prefixed:
            _shared.add(_name)

        if _prefix:
            for prop_name in _prefixed:
                # Assume property is camel-cased in EveryAction, so capitalize the first letter of the prefixed name
                # when prepending the prefix.
                # prefixed should exactly be the name of a property in EveryAction.
                prefixed = _prefix + prop_name[0].upper() + prop_name[1:]
                if prefixed in _shared:
                    raise AssertionError(f'Resulting prefixed name {prefixed} matches a value passed to _shared')
                # Check kwargs first for the property, then EAProperty.shared if it is not found in kwargs.
                # The property from kwargs should be deleted so it won't be redundantly processed later.
                base_prop = kwargs.pop(prop_name, None) or EAProperty.shared(prop_name)

                # Add the un-prefixed name and the snake-cased versions of the full and un-prefixed names as aliases so
                # that property may be accessed that way.
                new_aliases = base_prop.aliases | {prop_name, to_snake(prop_name), to_snake(prefixed)}
                properties[prefixed] = EAProperty(
                    *new_aliases,
                    is_array=base_prop.is_array,
                    singular_alias=base_prop.singular_alias,
                    factory=base_prop.factory
                )

        # Set all the properties from _shared.
        for prop_name in _shared:
            properties[prop_name] = EAProperty.shared(prop_name)

        # Set all the properties from kwargs.
        for k, v in kwargs.items():
            if k in properties:
                raise AssertionError(f'Property {k} supplied in both _shared and kwargs.')
            properties[k] = v

        # Finally, set the _PROPERTIES class attribute to the resulting EAProperties object, which is expected to never
        # be modified.
        ea_type._PROPERTIES = EAProperties(properties)
        if properties and ea_type.__doc__:
            ea_type._PROPERTIES.add_to_doc(ea_type, 'Properties')
        return ea_type


class EAObject(MutableMapping, metaclass=EAMeta):
    # Subclass from which all EveryAction objects inherit.
    # This class implements the MutableMapping interface by deferring to its attribute dict __dict__, as well as
    # leveraging aliases to get and set items using their alias rather than their camelCased name in the EveryAction
    # API.

    @classmethod
    def _properties(cls) -> EAProperties:
        return cls._PROPERTIES

    @classmethod
    def _resolve_attr(cls, alias: str) -> str:
        try:
            return cls._properties().resolve(alias)
        except KeyError:
            raise AttributeError(alias)

    def _setattr(self, attr: str, resolved: str, value: EAValue) -> None:
        # Helper method to set an attribute when the attribute name has already been resolved.
        prop = self._properties()[resolved]

        # Note that it is necessary to pass attr here, not resolved, in case attr corresponds to a singular alias.
        result = prop.value(attr, value)
        object.__setattr__(self, resolved, result)

    # noinspection PyUnusedLocal
    def __init__(self, arg: Any = None, **kwargs: EAValue) -> None:
        # Dummy __init__ method used to keep PyCharm from complaining about signatures in subclasses which define either
        # or both an ID and a name, which have their __init__ methods auto-generated and which accept a single
        # positional argument, while the default __init__ does not. The real __init__ method for EAObject is
        # EAMeta._default_init.
        pass

    def __delitem__(self, k: str) -> None:
        del self.__dict__[self._resolve_attr(k)]

    def __eq__(self, other: E) -> bool:
        return (type(self) == type(other)) and super().__eq__(other)

    def __getattr__(self, attr: str) -> EAValue:
        # This __getattr__ implementation will search for aliases for the given attribute.
        # Note that we only reach this method if attr could not be found in self.__dict__, as that is how Python is
        # designed to call this method.
        resolved = self._resolve_attr(attr)
        prop = self._properties()[resolved]
        if attr == prop.singular_alias:
            # Setting a value using a singular alias is unambiguous, but the behavior of getting a value using a
            # singular alias is either going to be unintuitive or inconsistent (what should happen if the value is a
            # list with more than one element?).
            raise AttributeError(
                f'Singular aliases may only be used to set values, not get them (tried getting {resolved} with {attr})'
            )
        # Use get to intentionally return None when _resolve_attr does not raise an AttributeError, since the property
        # then exists but is not defined.
        return self.__dict__.get(resolved)

    def __getitem__(self, k: str) -> EAValue:
        try:
            return getattr(self, k)
        except AttributeError:
            # If we are accessing with [], give KeyError rather than AttributeError.
            # Necessary for __contains__ inherited from Mapping to work correctly.
            raise KeyError(k)

    def __iter__(self) -> Iterator[str]:
        return iter(self.__dict__)

    def __len__(self) -> int:
        return len(self.__dict__)

    def __repr__(self) -> str:
        # Formatted like: Person(firstName=Alice, lastName=Terwilliger, ...)
        return f'{type(self).__name__}({", ".join(f"{k}={v}" for k, v in self.items())})'

    def __setattr__(self, attr: str, value: EAValue) -> None:
        try:
            resolved = self._resolve_attr(attr)
        except AttributeError:
            if hasattr(self, attr):
                object.__setattr__(self, attr, value)
                return
            else:
                raise
        if value is None:
            if resolved in self.__dict__:
                # Be consistent about not including attributes with value None in self.__dict__.
                del self.__dict__[resolved]
        else:
            self._setattr(attr, resolved, value)

    def __setitem__(self, k: str, v: EAValue) -> None:
        setattr(self, k, v)


class EAObjectEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, EAObject):
            return o.__dict__
        return super().default(o)
