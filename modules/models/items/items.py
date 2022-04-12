from typing import List, Dict, OrderedDict
from dataclasses import dataclass, field

from modules.controllers.actions import Action
from modules.utils import indefinite_determiner


@dataclass(kw_only=True)
class Item:
    """Class representing a generic item"""
    name: str
    price: int = 0
    description: str
    quantity: int = 1
    actions: List[str] = field(default_factory=list)
    is_in_inventory: bool = field(init=False, default=False)

    def __str__(self) -> str:
        """String representation of the item"""
        return f'{indefinite_determiner(self.name)}'

    def get_actions(self) -> OrderedDict[str, Action]:
        """Return a map of the keys and their associated actions in the room"""
        actions = OrderedDict()

        if self.is_in_inventory:
            actions['d'] = Action.DROP
        else:
            actions['p'] = Action.TAKE

        actions['q'] = Action.QUIT
        return actions


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
