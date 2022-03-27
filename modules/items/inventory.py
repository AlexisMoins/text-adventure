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

    def filter(self, action: str) -> List[Item]:
        """Returns a list of items with the given action"""
        return filter(lambda item: action in item.actions, self.items)

    def equip_item(self, item: Equipment) -> None:
        """Equips the given item into the corresponding equipment slot"""
        self.equipments[item.slot] = item

    def wearable_items(self) -> List[Item]:
        """"""
        return [item for item in self.filter('equip') if item not in self.equipments.values()]
