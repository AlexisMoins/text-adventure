from typing import DefaultDict
from collections import defaultdict
from dataclasses import dataclass, field

from src.factory import register
from src.models.entity import Entity
from src.models.items.items import Item, Equipment

from src.models.collections import Container, SizedContainer


@register('character')
@dataclass(slots=True)
class Character(Entity):
    """Class representing a generic character"""
    inventory: SizedContainer
    spells: Container = field(default_factory=Container)
    equipments: dict[str, Equipment] = field(default_factory=dict)
    statistics: DefaultDict[str, int] = field(default_factory=lambda: defaultdict(int))

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        for item in self.inventory.filter('equip'):
            self.equip(item)

    def is_alive(self) -> bool:
        """Return true if this character is alive"""
        return self.statistics['health'] > 0

    def add_to_inventory(self, entity: Entity):
        """Attempt to put the given entity in this character's inventory"""
        if not isinstance(entity, Item):
            print(f'You want to put THAT in your inventory ? Don\'t be silly...')

        elif not 'take' in entity.actions:
            print('There is no way you could put that in your inventory')

        elif self.inventory.is_full():
            print('You\'re carrying too many things right now!')

        else:
            self.inventory.append(entity)
            print('Done!')

    def equip(self, item: Equipment) -> None:
        """"""
        self.equipments[item.slot] = item

    def take_off(self, equipment: Equipment) -> None:
        """"""
        if equipment.slot in self.equipments:
            del self.equipments[equipment.slot]
