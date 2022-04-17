import resource
from typing import Dict
from dataclasses import dataclass, field

from modules.models.items.inventory import Inventory
from modules.models.items.equipments import Equipment
from modules.models.items.items import Item
from modules.models.locations.room import Room
from modules.views.utils import yes_no_question

from modules.utils import resources


@dataclass(kw_only=True)
class Character:
    """Class representing a generic character"""
    name: str
    statistics: Dict[str, int] = field(default=dict)
    inventory: Inventory = field(default_factory=list)

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        self.statistics['max_health'] = self.get_statistic('health')
        self.statistics['max_mana'] = self.get_statistic('mana')

        for item in self.inventory.filter('equip'):
            self.equip(item)

    def get_statistic(self, statistic: str) -> int:
        """Returns the value of the given statistic for the current character"""
        return self.statistics[statistic] if statistic in self.statistics else 0

    def equip(self, item: Equipment) -> None:
        """Equips the given item into the corresponding equipment slot"""
        if item and 'equip' in item.actions and self.inventory.contains(item):
            self.inventory.equip(item)

    def take_off(self, item: Equipment) -> None:
        """Take off the given equipment"""
        if item and self.inventory.is_wore_or_held(item):
            self.inventory.take_off(item)

    def is_alive(self) -> bool:
        """Return true if the current character is alive, return false otherwise"""
        return self.get_statistic('health') > 0

    def take(self, item: Item, room: Room) -> bool:
        """Take the given item and add it to the current player's inventory"""
        if self.inventory.is_full():
            print('Your inventory is full')
            return False
        self.inventory.add(room.remove(item))
        return True

    def drop(self, item: Item, room: Room) -> None:
        """Drop the given item in the given room"""
        message = resources['player']['interface']['drop warning']
        if not self.inventory.is_wore_or_held(item) or yes_no_question(message.format(item), warning=True):
            room.add(self.inventory.drop(item))
