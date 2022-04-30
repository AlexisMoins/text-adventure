from typing import Callable

from src.models.items.items import *

"""List of item types and their corresponding class"""
items: dict[str, Callable] = {}


def register(item_type: str, item: Callable) -> None:
    """Add an item type and its corresponding class to the items dictionnary"""
    items[item_type] = item


def create(data: dict) -> Item:
    """Create a new item based on the item type retreived from the given data"""
    item_type = data.pop('type')
    item: Callable = items[item_type]
    return item(**data)


register('equipment', Equipment)
