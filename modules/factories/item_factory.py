from typing import Dict, Callable, Any

from modules.items.items import Item

# List of item types and their corresponding class
items: Dict[str, Callable[..., Item]] = {}


def register(item_type: str, function: Callable[..., Item]) -> None:
    """Add an item type and its corresponding class to the items dictionnary"""
    items[item_type] = function


def create(data: Dict[str, Any]) -> Item:
    """Creates """
    copy = data.copy()
    item_type = copy.pop('type')
    create: Callable[..., Item] = items[item_type]
    return create(**copy)
