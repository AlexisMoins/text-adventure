from typing import Dict, List
from dataclasses import dataclass, field

from modules.models.items.items import Item
from modules.models.items.equipments import Equipment

from modules.controllers.actions import Action


@dataclass(kw_only=True)
class Inventory:
    """Class representing an inventory, with gold and items"""
    gold: int = 0
    capacity: int = 6
    items: List[Item] = field(default_factory=list)
    equipments: Dict[str, Item] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Equip the default items"""
        for item in self.items:
            item.is_in_inventory = True

    def is_full(self) -> bool:
        """Return true if the inventory is full"""
        return len(self.items) == self.capacity

    def is_empty(self) -> bool:
        """Return true if the inventory is empty"""
        return len(self.items) == 0

    def add(self, item: Item) -> None:
        """Add the given item to the inventory"""
        self.items.append(item)
        item.is_in_inventory = True

    def filter(self, action: str) -> List[Item]:
        """Return a list of items with the given action"""
        return filter(lambda item: action in item.actions, self.items)

    def equip(self, item: Equipment) -> None:
        """Equip the given item into the corresponding equipment slot"""
        if item.slot in self.equipments.keys():
            self.equipments[item.slot].is_equipped = False

        item.is_equipped = True
        self.equipments[item.slot] = item

    def take_off(self, item: Equipment) -> None:
        """Remove the given item from its corresponding equipment slot"""
        item.is_equipped = False
        del self.equipments[item.slot]

    def drop(self, item: Item) -> Item | None:
        """"""
        if self.is_wore_or_held(item):
            self.take_off(item)
        item.is_in_inventory = False
        return self.items.pop(self.items.index(item))

    @property
    def wearable_items(self) -> List[Item]:
        """Return the list of items that can be wore but are not currenlty"""
        return [item for item in self.filter('equip') if not self.is_wore_or_held(item)]

    def contains(self, the_item: Item) -> bool:
        """Return true if the given item is in the inventory"""
        for item in self.items:
            if the_item is item:
                return True
        return False

    def is_wore_or_held(self, item: Item) -> bool:
        """Return true if the given item is currently equipped"""
        return isinstance(item, Equipment) and item.slot in self.equipments.keys() and self.equipments[item.slot] is item

    def find_items(self, pattern: str) -> List[Item]:
        """Return the list of items whose name matches the given pattern"""
        iterator = filter(lambda item: pattern in item.name, self.items)
        return list(iterator)

    def find_wearables(self, pattern: str) -> List[Item]:
        """Return the list of wearable items whose name matches the given pattern"""
        wearable_items = filter(lambda item: pattern in item.name, self.wearable_items)
        return list(wearable_items)
