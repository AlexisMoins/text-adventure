from typing import Dict, Callable, Any

from modules.models.items.items import Item
from modules.models.items.equipments import Equipment

"""List of item types and their corresponding class"""
items: Dict[str, Callable[..., Item]] = dict()


def register(item_type: str, item: Callable[..., Item]) -> None:
    """Add an item type and its corresponding class to the items dictionnary"""
    items[item_type] = item


def create(data: Dict[str, Any]) -> Item:
    """Create a new item based on the item type retreived from the given data"""
    item_type = data.pop('type')
    item: Callable[..., Item] = items[item_type]
    return item(**data)


register('equipment', Equipment)
