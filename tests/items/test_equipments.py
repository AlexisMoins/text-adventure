from typing import Dict
from .test_items import new_item_test
from text_adventure.items.equipments import Equipment, Armor, Weapon


def test_new_equipment(items: Dict) -> None:
    """Test to ensure the creation of a new equipment is not allowed"""
    data: Dict = items["mock_equipment"]
    item = Equipment(**data)
    new_equipment_test(item, data)


def new_equipment_test(item: Equipment, data: Dict) -> None:
    """Ensure the Equipment class was correctly inherited"""
    new_item_test(item, data)
    assert item.durability == data["durability"]
    assert item.max_durability == data["durability"]


def test_new_armor(items: Dict) -> None:
    """Test to ensure the creation of a new armor is working"""
    data: Dict = items["mock_armor"]
    item = Armor(**data)
    new_armor_test(item, data)


def new_armor_test(item: Armor, data: Dict) -> None:
    """Ensure the armor  was correctly created"""
    new_equipment_test(item, data)
    assert item.body_part == data["body_part"]
    assert item.protection == data["protection"]


def test_new_weapon(items: Dict) -> None:
    """Test to ensure the creation of a new armor is working"""
    data: Dict = items["mock_weapon"]
    item = Weapon(**data)
    new_weapon_test(item, data)


def new_weapon_test(item: Weapon, data: Dict) -> None:
    """Ensure the weapon was correctly created"""
    new_equipment_test(item, data)
    assert item.damage == data["damage"]
