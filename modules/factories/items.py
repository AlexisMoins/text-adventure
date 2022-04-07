from typing import Dict, Callable, Any

from modules.models.items.items import Item
from modules.models.items.equipments import Equipment

"""List of item types and their corresponding class"""
items: Dict[str, Callable[..., Item]] = dict()


def register(item_type: str, function: Callable[..., Item]) -> None:
    """Add an item type and its corresponding class to the items dictionnary"""
    items[item_type] = function


def create(data: Dict[str, Any]) -> Item:
    """Create a new item based on the item type retreived from the given data"""
    copy = data.copy()
    item_type = copy.pop('type')
    function: Callable[..., Item] = items[item_type]
    return function(**copy)


register('equipment', Equipment)
