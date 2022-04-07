from typing import Dict, List
from dataclasses import dataclass, field

from modules.models.items.items import Item
from modules.models.items.equipments import Equipment


@dataclass(kw_only=True)
class Inventory:
    """Class representing an inventory, with gold and items"""
    gold: int = 0
    items: List[Item] = field(default_factory=list)
    equipments: Dict[str, Item] = field(default_factory=dict)
    capacity: int = 6

    def is_full(self) -> bool:
        """Return true if the inventory is full"""
        return len(self.items) == self.capacity

    def filter(self, action: str) -> List[Item]:
        """Return a list of items with the given action"""
        return filter(lambda item: action in item.actions, self.items)

    def equip(self, item: Equipment) -> None:
        """Equip the given item into the corresponding equipment slot"""
        if item:
            self.equipments[item.slot] = item

    def take_off(self, item: Equipment) -> None:
        """Remove the given item from its corresponding equipment slot"""
        if item:
            del self.equipments[item.slot]

    def drop(self, item: Item) -> Item | None:
        """"""
        if self.item_is_equipped(item):
            self.take_off(item)
        return self.items.pop(self.items.index(item))

    def wearable_items(self) -> List[Item]:
        """Return the list of items that can be wore but are not currenlty"""
        return [item for item in self.filter('equip') if not self.item_is_equipped(item)]

    def contains(self, the_item: Item) -> bool:
        """Return true if the given item is in the inventory"""
        for item in self.items:
            if the_item is item:
                return True
        return False

    def item_is_equipped(self, item: Item) -> bool:
        """"""
        if not isinstance(item, Equipment) or item.slot not in self.equipments.keys():
            return False

        if self.equipments[item.slot] is item:
            return True
        return False
