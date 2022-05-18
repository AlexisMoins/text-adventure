from typing import Any

from src.models.items.items import *


def test_new_item(items: dict[str, Any]) -> None:
    """Test to ensure the creation of a new object Item is working"""
    data: dict = items['mock_item']
    item = Item(**data)
    new_item_test(item, data)


def new_item_test(item: Item, data: dict[str, Any]) -> None:
    """Ensure the Item instance was correctly created"""
    assert item.name == data['name']

    if 'price' in data.keys():
        assert item.price == data['price']

    assert item.description == data['description']
    assert item.quantity == data['quantity']

    if 'actions' in data.keys():
        assert data['actions'] == item.actions


def test_new_consumable(items: dict[str, Any]) -> None:
    """Test to ensure the creation of a new object Consumable is working"""
    data = items['mock_consumable']
    item = Consumable(**data)
    new_consumable_test(item, data)


def new_consumable_test(item: Consumable, data: dict[str, Any]) -> None:
    """Ensure the Consumable instance was correctly created"""
    new_item_test(item, data)
    if item.statistics:
        for statistic, value in data['statistics'].items():
            assert item.statistics[statistic] == value


def test_new_spell(items: dict[str, Any]) -> None:
    """Test to ensure the creation of a new object Spell is working"""
    data = items['mock_spell']
    item = Spell(**data)
    new_spell_test(item, data)


def new_spell_test(item: Spell, data: dict[str, Any]) -> None:
    """Ensure the Spell instance was correctly created"""
    new_consumable_test(item, data)
    assert item.damage == data['damage']
    assert item.spell_type == data['spell_type']
    assert item.spell_range == data['spell_range']


def test_new_equipment(items: dict[str, Any]) -> None:
    """Test to ensure the creation of a new equipment is not allowed"""
    data = items['mock_equipment']
    item = Equipment(**data)
    new_equipment_test(item, data)


def new_equipment_test(item: Equipment, data: dict[str, Any]) -> None:
    """Ensure the Equipment class was correctly inherited"""
    new_item_test(item, data)
    assert item.slot == data['slot']
    assert item.durability == data['durability']
    assert item.max_durability == data['durability']
    assert item.statistics == data['statistics']
    assert item.equipped == False
