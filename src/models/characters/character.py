from colorama import Fore
from dataclasses import dataclass, field

from src.factory import register
from src.models.entity import Entity
from src.models.items.items import Equipment

from src.models.statistics import Statistics
from src.models.collections import Container, SizedContainer


@register('character')
@dataclass(slots=True)
class Character(Entity):
    """
    Class representing a generic character with an inventory, statistics
    and even spells. Mind blowing!
    """
    statistics: Statistics
    inventory: SizedContainer

    spells: Container = field(default_factory=Container)
    equipments: dict[str, Equipment] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        for item in self.inventory.filter('equip'):  # TODO inventory.filter_action(action, _type=Equipment)
            self.wear_or_equip(item, silent=True)

    def is_alive(self) -> bool:
        """
        Return true wether this character is alive or not.

        Return value:
        A boolean
        """
        return self.statistics['health'] > 0

    def add_to_inventory(self, entity: Entity):
        """Attempt to put the given entity in this character's inventory"""
        # if not isinstance(entity, Item):
        #     print(f'You want to put THAT in your inventory ? Don\'t be silly...')
        #
        # elif not 'take' in entity.actions:
        #     print('There is no way you could put that in your inventory')
        #
        # elif self.inventory.is_full():
        #     print('You\'re carrying too many things right now!')
        #
        # else:

        # TODO move the check logic related to the player somewhere else because
        # it is bad to have it for other characters
        self.inventory.append(entity)

    def wear_or_equip(self, equipment: Equipment, *, silent: bool = False) -> None:
        """
        Wear (or equip) a piece of equipment.

        Argument:
        equipment -- the equipment that should be wore / equipped

        Keyword argument:
        silent -- wheter this function should display text to explain what has
        been done or not
        """
        old_equipment = self.equipments.get(equipment.slot, None)

        if old_equipment:
            self.take_off(old_equipment)

        self.equipments[equipment.slot] = equipment
        self.statistics.add(equipment.statistics.dump)

        if not silent:
            print(f'You wear the {equipment.name} {Fore.GREEN}({equipment.statistics}){Fore.WHITE}')

    def take_off(self, equipment: Equipment, *, silent: bool = False) -> None:
        """"""
        if equipment.slot in self.equipments:
            reverse_stats = equipment.statistics.reverse
            self.statistics.add(reverse_stats.dump)

            if not silent:
                print(f'You take off your {equipment.name} {Fore.RED}({reverse_stats}){Fore.WHITE}')

            del self.equipments[equipment.slot]
