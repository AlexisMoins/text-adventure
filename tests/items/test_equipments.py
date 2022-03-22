from typing import Dict, Any

from tests.items.test_items import new_item_test
from models.items.equipments import Equipment, Armor, Weapon


def test_new_equipment(items: Dict[str, Any]) -> None:
    """Test to ensure the creation of a new equipment is not allowed"""
    data = items['mock_equipment']
    item = Equipment(**data)
    new_equipment_test(item, data)


def new_equipment_test(item: Equipment, data: Dict[str, Any]) -> None:
    """Ensure the Equipment class was correctly inherited"""
    new_item_test(item, data)
    assert item.durability == data['durability']
    assert item.max_durability == data['durability']


def test_new_armor(items: Dict[str, Any]) -> None:
    """Test to ensure the creation of a new armor is working"""
    data = items['mock_armor']
    item = Armor(**data)
    new_armor_test(item, data)


def new_armor_test(item: Armor, data: Dict[str, Any]) -> None:
    """Ensure the armor  was correctly created"""
    new_equipment_test(item, data)
    assert item.slot == data['slot']
    assert item.protection == data['protection']


def test_new_weapon(items: Dict[str, Any]) -> None:
    """Test to ensure the creation of a new armor is working"""
    data = items['mock_weapon']
    item = Weapon(**data)
    new_weapon_test(item, data)


def new_weapon_test(item: Weapon, data: Dict[str, Any]) -> None:
    """Ensure the weapon was correctly created"""
    new_equipment_test(item, data)
    assert item.damage == data['damage']
