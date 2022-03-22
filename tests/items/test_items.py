from typing import Dict, Any

from models.items.items import Item, Consumable, Spell


def test_new_item(items: Dict[str, Any]) -> None:
    """Test to ensure the creation of a new object Item is working"""
    data: Dict = items['mock_item']
    item = Item(**data)
    new_item_test(item, data)


def new_item_test(item: Item, data: Dict[str, Any]) -> None:
    """Ensure the Item instance was correctly created"""
    assert item.name == data['name']
    assert item.description == data['description']
    if item.price:
        assert item.price == data['price']
    if item.actions:
        for action in data['actions']:
            assert action in item.actions


def test_new_consumable(items: Dict[str, Any]) -> None:
    """Test to ensure the creation of a new object Consumable is working"""
    data = items['mock_consumable']
    item = Consumable(**data)
    new_consumable_test(item, data)


def new_consumable_test(item: Consumable, data: Dict[str, Any]) -> None:
    """Ensure the Consumable instance was correctly created"""
    new_item_test(item, data)
    if item.statistics:
        for statistic, value in data['statistics'].items():
            assert item.statistics[statistic] == value


def test_new_spell(items: Dict[str, Any]) -> None:
    """Test to ensure the creation of a new object Spell is working"""
    data = items['mock_spell']
    item = Spell(**data)
    new_spell_test(item, data)


def new_spell_test(item: Spell, data: Dict[str, Any]) -> None:
    """Ensure the Spell instance was correctly created"""
    new_consumable_test(item, data)
    assert item.damage == data['damage']
    assert item.spell_type == data['spell_type']
    assert item.spell_range == data['spell_range']
