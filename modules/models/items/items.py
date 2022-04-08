from typing import List, Dict
from dataclasses import dataclass, field

from modules.views.utils import Action


@dataclass(kw_only=True)
class Item:
    """Class representing a generic item"""
    name: str
    price: int = 0
    description: str
    actions: List[str] = field(default_factory=list)
    quantity: int = 1

    def __str__(self) -> str:
        """String representation of the item"""
        return f'{self.name}'

    def get_actions(self) -> Dict[str, Action]:
        """Return a map of the keys and their associated actions in the room"""
        actions = dict()

        actions['q'] = Action.QUIT
        return actions

        # if self.inventory.contains(self.item):
        #     if self.inventory.item_is_equipped(self.item):
        #         print(f'[{Fore.CYAN}t{Fore.WHITE}] Take off')
        #     else:
        #         print(f'[{Fore.CYAN}w{Fore.WHITE}] Wear or hold')
        #     print(f'[{Fore.CYAN}d{Fore.WHITE}] Drop in the room')
        # else:
        #     print(f'[{Fore.CYAN}p{Fore.WHITE}] Put in your inventory')


@dataclass(kw_only=True)
class Consumable(Item):
    """Class representing a general"""
    statistics: Dict[str, int] = field(default_factory=dict)


@dataclass(kw_only=True)
class Spell(Consumable):
    """Class representing spells"""
    damage: int
    spell_type: str
    spell_range: str
