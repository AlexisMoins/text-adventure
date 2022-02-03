
from typing import Dict, Any
from text_adventure.items.items import Item, Consumable

def test_new_item(items: Dict[str, Any]) -> None:
    """Test to ensure the creation of a new object Item is working"""
    item_data: Dict[str, Any] = items['mock_item']
    item = Item(**item_data)
    item_attributes_test(item)

def item_attributes_test(item: Item) -> None:
    """Test the validity of the attributes of Item"""
    assert item.name == 'my item'
    assert item.description == 'a basic item'
    assert item.price == 10
    assert 'buy' in item.actions

def test_new_consumable(items: Dict[str, Any]) -> None:
    """Test to ensure the creation of a new object Consumable is working"""
    item_data: Dict[str, Any] = items['mock_consumable']
    item = Consumable(**item_data)
    consumable_attributes_test(item)

def consumable_attributes_test(item: Consumable) -> None:
    """Test the validity of the attributes of Consumable"""
    assert item.name == 'my consumable'
    assert item.description == 'a basic consumable'
    assert item.price == 10
    assert len(item.actions) == 2
    assert 'drink' in item.actions
    assert 'thow' in item.actions
    assert 'health' in item.statistics.keys()
    assert item.statistics['health'] == 15

