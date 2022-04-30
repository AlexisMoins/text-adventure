import resource
from typing import Dict
from dataclasses import dataclass, field

from src.models.items.inventory import Inventory
from src.models.items.equipments import Equipment
from src.models.items.items import Item
from src.models.locations.room import Room
from src.views.utils import yes_no_question

from src.utils import resources


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
        if 'equip' in item.actions:
            self.inventory.equip(item)
            print('Done!')

    def take_off(self, item: Equipment) -> None:
        """Take off the given equipment"""
        if item and self.inventory.is_wore_or_held(item):
            self.inventory.take_off(item)

    def is_alive(self) -> bool:
        """Return true if the current character is alive, return false otherwise"""
        return self.get_statistic('health') > 0

    def take(self, item: Item, room: Room) -> None:
        """Take the given item and add it to the current player's inventory"""
        if self.inventory.is_full():
            print('Your inventory is full')
        else:
            self.inventory.add(room.remove(item))
            print('Done!')

    def drop(self, item: Item, room: Room) -> None:
        """Drop the given item in the given room"""
        if self.inventory.is_wore_or_held(item):
            self.take_off(item)
        room.add(self.inventory.drop(item))
        print('Done!')
