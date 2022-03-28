from typing import List, Dict
from dataclasses import dataclass, field


def determiner(item_name: str) -> str:
    """"""
    vowels = 'aeiouy'
    return 'an' if item_name[0] in vowels else 'a'


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
        return f'{determiner(self.name)} {self.name}'

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
