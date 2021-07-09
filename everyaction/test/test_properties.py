import pytest

import everyaction.core as core
from everyaction import EAException
from everyaction.core import EAProperty, EAProperties


class TestProperties:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.simple = EAProperty('sim')
        self.with_factory = EAProperty('factory', 'fact', factory=int)
        self.array_prop = EAProperty('array', 'arr', singular_alias='single', factory=int)
        self.simple2 = EAProperty('sim2')
        self.properties = EAProperties({
            'simple': self.simple,
            'withFactory': self.with_factory,
            'arrayProp': self.array_prop
        })
        yield

    def test_camel_to_snake(self):
        assert core.to_snake('firstName') == 'first_name'
        assert core.to_snake('first') == 'first'
        assert core.to_snake('first_name') == 'first_name'

    def test_property_find(self):
        property_map = {
            'long_simple': 1,
            'with_factory': '2',
            'single': [3],
            'sim2': 4
        }

        # Make sure exact name can be found.
        assert self.simple.find('long_simple', property_map) == 1

        assert self.simple.find('simple', property_map) is None
        assert self.with_factory.find('with_factory', property_map) == 2
        assert self.with_factory.find('factory', property_map) is None
        # Pop these two to make sure that works.
        assert self.array_prop.find('array_prop', property_map, pop=True) == [3]
        assert self.simple2.find('simple2', property_map, pop=True) == 4

        assert property_map == {'long_simple': 1, 'with_factory': '2'}

    def test_property_get(self):
        # Add these, then try to get them with their names.
        EAProperty.share(simple=self.simple, with_factory=self.with_factory, array_prop=self.array_prop)

        assert EAProperty.shared('simple') == self.simple
        assert EAProperty.shared('with_factory') == self.with_factory
        assert EAProperty.shared('array_prop') == self.array_prop

        with pytest.raises(AssertionError, match='NotAProperty is not a shared property'):
            EAProperty.shared('NotAProperty')

        with pytest.raises(AssertionError, match='simple is already a shared property'):
            # Make sure we can't add the same property twice.
            EAProperty.share(simple=self.simple)

    def test_property_value(self):
        # Should just give the passed in value (no factory).
        assert self.simple.value('example', 'value') == 'value'

        # Should call int to change '30' to 30.
        assert self.with_factory.value('example', '30') == 30

        # Should call int on each element.
        assert self.array_prop.value('example', ['1', '2', '3', '4']) == [1, 2, 3, 4]

        # Should call int on 3.1 and wrap in list for singular alias.
        assert self.array_prop.value('single', 3.1) == [3]
        with pytest.raises(TypeError, match='Expected sequence for "example", got float: 3.1'):
            # Should raise TypeError when sequence not given for non-singular alias.
            self.array_prop.value('example', 3.1)

    def test_properties_resolve(self):
        assert len(self.properties) == 3

        # Make sure all resolved names match the true name for each property.
        assert self.properties.resolve('simple') == self.properties.resolve('sim') == 'simple'
        assert (
            self.properties.resolve('withFactory')
            == self.properties.resolve('with_factory')
            == self.properties.resolve('factory')
            == self.properties.resolve('fact')
            == 'withFactory'
        )
        assert (
            self.properties.resolve('arrayProp')
            == self.properties.resolve('array_prop')
            == self.properties.resolve('array')
            == self.properties.resolve('arr')
            == 'arrayProp'
        )

    def test_properties_getitem(self):
        # Make sure all aliases and the true name yield the expected properties.
        assert self.properties['simple'] == self.properties['sim'] == self.simple
        assert (
            self.properties['withFactory']
            == self.properties['with_factory']
            == self.properties['factory']
            == self.properties['fact']
            == self.with_factory
        )
        assert (
            self.properties['arrayProp']
            == self.properties['array_prop']
            == self.properties['array']
            == self.properties['arr']
            == self.array_prop
        )

    def test_properties_process(self):
        property_map1 = {
            'simple': 1,
            'with_factory': '2',
            'array': ['1', '2', '3']
        }

        # Make sure EAProperties object correct calls factories and resolves aliases.
        # Note that only the true names are in the processed map.
        assert self.properties.process(property_map1) == {
            'simple': 1,
            'withFactory': 2,
            'arrayProp': [1, 2, 3]
        }

        property_map2 = {
            'sim': 1,
            'single': '2'
        }

        # Make sure using singular alias processes so that '2' is converted to int and wrapped in list.
        assert self.properties.process(property_map2) == {
            'simple': 1,
            'arrayProp': [2]
        }

        # Make sure specifying multiple aliases for a property results in an exception.
        property_map3 = {
            'sim': 1,
            'simple': 2
        }

        with pytest.raises(EAException, match='Multiple aliases for "simple" given'):
            self.properties.process(property_map3)
