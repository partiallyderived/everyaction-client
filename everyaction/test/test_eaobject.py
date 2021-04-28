import pytest

from everyaction.core import EAObject, EAObjectWithID, EAObjectWithIDAndName, EAObjectWithName, EAProperty


class BasicObject(
    EAObject,
    simple=EAProperty('sim'),
    withFactory=EAProperty('factory', 'fact', factory=int),
    arrayProp=EAProperty('array', 'arr', singular_alias='single', factory=int)
):
    pass


# The following is intentionally the same as the above, for equality testing purposes.
class OtherBasicObject(
    EAObject,
    simple=EAProperty('sim'),
    withFactory=EAProperty('factory', 'fact', factory=int),
    arrayProp=EAProperty('array', 'arr', singular_alias='single', factory=int)
):
    pass


def test_basic():
    obj = BasicObject(sim=1, withFactory='2', single='3')

    # Test that factories are called correctly, aliases are resolved correctly, and that getattr and getitem behave
    # the same way.
    assert obj.sim == obj['sim'] == obj.simple == obj['simple'] == 1
    assert obj.fact == 2
    assert obj.array_prop == [3]

    # Make sure each property shows up in the object's repr.
    for string in ['simple=1', 'withFactory=2', 'arrayProp=[3]']:
        assert string in str(obj)

    # Make sure repr formatted correctly.
    assert str(obj).startswith('BasicObject(')
    assert str(obj).endswith(')')

    # Try to set array_prop, make sure factory still called and wrapping occurs when using singular alias.
    obj.single = '4'
    assert obj.array_prop == [4]

    obj.array_prop = ['3', 4]
    assert obj.array_prop == [3, 4]

    with pytest.raises(AttributeError, match='Singular aliases may only be used to set values'):
        # Should not be able to getattr using a singular alias.
        obj.single

    with pytest.raises(AttributeError, match='asdf'):
        # Just make sure getting arbitrary attributes raises an AttributeError.
        obj.asdf

    # Make sure getting deleted attribute gives None rather than AttributeError.
    del obj['array_prop']
    assert obj.array_prop is obj['array_prop'] is None

    # Make sure no AttributeErrors are raised when getting absent but valid properties.
    obj = BasicObject(sim=1)
    assert obj.withFactory is None
    assert obj.arrayProp is None

    # Check that repr with no properties is as expected.
    obj.sim = None
    assert str(obj) == 'BasicObject()'

    # Test equality.

    assert BasicObject() == BasicObject()

    # Need to match both properties and type.
    assert BasicObject() != {}
    assert BasicObject() != OtherBasicObject()

    assert BasicObject(sim=1) == BasicObject(simple=1)
    assert BasicObject(sim=1) != OtherBasicObject(sim=1)
    assert BasicObject(simple=1) != {'simple': 1}

    assert BasicObject() != BasicObject(sim=1)
    assert BasicObject(sim=1) != BasicObject(sim=2)
    assert BasicObject(sim=1) != BasicObject(sim=1, fact=3)

    with pytest.raises(ValueError, match='Multiple aliases given for simple'):
        # Make sure specifying multiple names for the same property is not allowed.
        BasicObject(sim=1, simple=2)


def test_nested():
    class NestedObject(
        EAObject, basic=EAProperty(factory=BasicObject), basics=EAProperty(is_array=True, factory=BasicObject)
    ):
        pass

    assert NestedObject(basic=BasicObject(simple=1)) == NestedObject(basic=BasicObject(simple=1))
    # dict should be fine instead of explicit BasicObject.
    assert NestedObject(basic=BasicObject(simple=1)) == NestedObject(basic={'simple': 1})

    # Instance should automatically convert dict to BasicObject.
    assert NestedObject(basic={'simple': 1}).basic == BasicObject(simple=1)

    # Same but with a sequence.
    assert (
        NestedObject(basics=[BasicObject(simple=1), {'simple': 2}])
        == NestedObject(basics=[{'simple': 1}, BasicObject(simple=2)])
    )


def test_common_keys():
    # "add" these properties so we may test that common properties specified via _keys are correctly applied.
    EAProperty.share(a=EAProperty(), b=EAProperty(factory=int), c=EAProperty(singular_alias='single', factory=int))

    class ObjectWithCommonProps(EAObject, _keys={'a', 'b', 'c'}, d=EAProperty()):
        pass

    obj = ObjectWithCommonProps(a=1, b='2', single='3', d=4)
    assert obj.a == 1
    assert obj.b == 2
    assert obj.c == [3]
    assert obj.d == 4


def test_prefixed():
    # Add these properties so that EAMeta can find them.
    EAProperty.share(
        doorBell=EAProperty(),
        e=EAProperty(factory=int),
        f=EAProperty(singular_alias='single', factory=int)
    )

    class PrefixedObject(
        EAObject,
        _prefix='pre',
        _prefixed={'doorBell', 'e', 'f'}
    ):
        pass

    # Ensure instances can be created with prefixed and un-prefixed aliases.
    obj = PrefixedObject(doorBell=1, preE='2', single='3')
    assert obj.preDoorBell == obj.doorBell == obj.door_bell == 1
    assert obj.preE == obj.e == 2
    assert obj.preF == obj.f == [3]

    # Check __dict__ to show what the properties' true names are (the keys that will appear in JSON data for
    # requests).
    for string in ['preDoorBell', 'preE', 'preF']:
        assert string in obj.__dict__

    # Test that the aliases will not appear in __dict__.
    for string in ['doorBell', 'door_bell', 'e', 'f']:
        assert string not in obj.__dict__


def test_with_id():
    class WithID(EAObjectWithID, simple=EAProperty()):
        pass

    # Check that positional argument is allowed and is the same as specifying ID.
    assert WithID(3) == WithID(id=3)

    # Check that properties whose factory is an EAObjectWithID can form an object with just the int ID.
    id_factory_prop = EAProperty(factory=WithID)
    assert id_factory_prop.value('asdf', 3) == WithID(3)

    # Same but with an array property.
    array_id_factory_prop = EAProperty(is_array=True, factory=WithID)
    assert array_id_factory_prop.value('asdf', [1, 2, 3, 4]) == [WithID(1), WithID(2), WithID(3), WithID(4)]

    class WithIDAndPrefix(EAObjectWithID, _prefix='pre'):
        pass

    # Check that both id and preId recognized.
    assert WithIDAndPrefix(3) == WithIDAndPrefix(id=3) == WithIDAndPrefix(preId=3)

    # Test that the property's true name is preId.
    assert 'preId' in WithIDAndPrefix(3).__dict__
    assert 'id' not in WithIDAndPrefix(3).__dict__


def test_with_id_and_name():
    class WithIDAndName(EAObjectWithIDAndName):
        pass

    # Test that if the first positional argument is an int, the ID is specified, and that otherwise the name is
    # specified.
    assert WithIDAndName(3) == WithIDAndName(id=3)
    assert WithIDAndName('3') == WithIDAndName(name='3')
    assert WithIDAndName(3, name='3') == WithIDAndName(id=3, name='3')
    assert WithIDAndName('3', id=3) == WithIDAndName(id=3, name='3')
    assert 'id' in WithIDAndName(3).__dict__
    assert 'name' in WithIDAndName('3').__dict__

    # Test that factories may initialize with either the int ID or the str name.
    id_and_name_factory_prop = EAProperty(factory=WithIDAndName)
    assert id_and_name_factory_prop.value('asdf', 1) == WithIDAndName(id=1)
    assert id_and_name_factory_prop.value('asdf', '1') == WithIDAndName(name='1')

    # Same but with an array property.
    array_id_name_factory_prop = EAProperty(is_array=True, factory=WithIDAndName)
    assert array_id_name_factory_prop.value('asdf', [1, '2', 3, '4']) == [
        WithIDAndName(id=1),
        WithIDAndName(name='2'),
        WithIDAndName(id=3),
        WithIDAndName(name='4')
    ]

    class WithIDNameAndPrefix(EAObjectWithIDAndName, _prefix='pre'):
        pass

    # Test that ID is automatically prefixed when _prefix is specified.
    assert WithIDNameAndPrefix(3) == WithIDNameAndPrefix(id=3) == WithIDNameAndPrefix(preId=3)
    assert WithIDNameAndPrefix('3') == WithIDNameAndPrefix(name='3')
    assert 'id' not in WithIDNameAndPrefix(3).__dict__
    assert 'preId' in WithIDNameAndPrefix(3).__dict__
    assert 'name' in WithIDNameAndPrefix('3').__dict__

    with pytest.raises(AttributeError):
        WithIDNameAndPrefix(preName='3')

    class WithIDNameBothPrefixed(EAObjectWithIDAndName, _prefix='pre', _prefixed={'name'}):
        pass

    # Test that str positional arguments is the same as specifying name or preName.
    assert WithIDNameBothPrefixed('3') == WithIDNameBothPrefixed(name='3') == WithIDNameBothPrefixed(preName='3')
    assert 'name' not in WithIDNameBothPrefixed('3').__dict__
    assert 'preName' in WithIDNameBothPrefixed('3').__dict__

    # Edge case: make sure is 'name' is an alias for a given property, that it is not added as its own key.
    class WithPropHavingNameAlias(EAObjectWithIDAndName, formName=EAProperty('name')):
        pass

    assert (
        WithPropHavingNameAlias('3')
        == WithPropHavingNameAlias(name='3')
        == WithPropHavingNameAlias(formName='3')
    )

    assert 'name' not in WithPropHavingNameAlias('3').__dict__
    assert 'formName' in WithPropHavingNameAlias('3').__dict__

    class WithName(EAObjectWithName):
        pass

    assert WithName('name').name == 'name'


def test_inherit_properties():
    class Parent(EAObject, parentProp=EAProperty('parent')):
        pass

    class Child(Parent, childProp=EAProperty('child')):
        pass

    # Make sure Child object has parent property as well.
    obj = Child(parent=1, child=2)
    assert obj.parent == 1
    assert obj.childProp == 2

    assert 'childProp' in obj.__dict__
    assert 'parentProp' in obj.__dict__


def test_meta_assertions():
    EAProperty.share(preZ=EAProperty(), z=EAProperty())
    with pytest.raises(AssertionError, match='Resulting prefixed name preZ matches a value passed to _keys'):
        # Naming conflict where "preZ" explicitly specified as a key but is also implicitly a key since
        # "z" is prefixed by "pre" to yield the camelCased "preZ".
        class PrefixedMatchesKey(EAObject, _prefix='pre', _prefixed={'z'}, _keys={'preZ'}):
            pass

    with pytest.raises(AssertionError, match='Property z supplied both inside and outside kwargs.'):
        # Make sure we can't specify a both common property "z" and a specific property "z".
        class DuplicateKey(EAObject, _keys={'z'}, z=EAProperty()):
            pass


def test_ctor_attr_error():
    # Message is different when there are one versus multiple unrecognized attributes.
    with pytest.raises(AttributeError, match='The following property is unrecognized for BasicObject: fake_attr'):
        BasicObject(sim='asdf', fake_attr=3)
    with pytest.raises(
            AttributeError,
            match='The following properties are unrecognized for BasicObject: fake_attr1, fake_attr2'
    ):
        BasicObject(fake_attr1=1, sim='asdf', fake_attr2=2)