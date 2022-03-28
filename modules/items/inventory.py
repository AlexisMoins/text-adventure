from typing import Dict, List
from dataclasses import dataclass, field

from modules.items.items import Item
from modules.items.equipments import Equipment


@dataclass(kw_only=True)
class Inventory:
    """Class representing an inventory, with gold and items"""
    gold: int = 0
    items: List[Item] = field(default_factory=list)
    equipments: Dict[str, Item] = field(default_factory=dict)
    capacity: int = 9

    def filter(self, action: str) -> List[Item]:
        """Return a list of items with the given action"""
        return filter(lambda item: action in item.actions, self.items)

    def equip_one(self, item: Equipment) -> None:
        """Equip the given item into the corresponding equipment slot"""
        if item:
            self.equipments[item.slot] = item

    def equip_many(self, items: List[Item]) -> None:
        """Equip the given items into the corresponding equipment slots"""
        if items:
            for item in items:
                self.equip_one(item)

    def remove_one(self, item: Equipment) -> None:
        """Remove the given item from its corresponding equipment slot"""
        if item:
            del self.equipments[item.slot]

    def remove_many(self, items: List[Item]) -> None:
        """Remove the given items from their corresponding equipment slots"""
        if items:
            for item in items:
                self.remove_one(item)

    def wearable_items(self) -> List[Item]:
        """Return the list of items that can be wore but are not currenlty"""
        return [item for item in self.filter('equip') if item not in self.equipments.values()]
