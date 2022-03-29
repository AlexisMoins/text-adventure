from typing import List, Dict
from dataclasses import dataclass, field


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

    def display(self) -> None:
        """"""
        print(f'Name: {self.name}    price: {self.price}')
        input()


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
