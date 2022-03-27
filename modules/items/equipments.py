from typing import List
from dataclasses import dataclass, field
from colorama import Fore

from modules.items.items import Item, Spell


@dataclass(kw_only=True)
class Equipment(Item):
    """Class representing a generic equipment"""
    durability: int

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        self.max_durability = self.durability


@dataclass(kw_only=True)
class Armor(Equipment):
    """Class representing any armor"""
    slot: str
    protection: int

    def __str__(self) -> str:
        """Return the string representation of the armor"""
        return f'{super().__str__()} {Fore.CYAN}(def +{self.protection}){Fore.WHITE}'


@dataclass(kw_only=True)
class Weapon(Equipment):
    """Class representing any weapon"""
    damage: int

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        self.slot = 'weapon'

    def __str__(self) -> str:
        """Return the string representation of the armor"""
        damage_type = 'mag' if 'cast' in self.actions else 'atk'
        return f'{super().__str__()} {Fore.RED}({damage_type} +{self.damage}){Fore.WHITE}'


@dataclass(kw_only=True)
class SpellBook(Equipment):
    """Class representing any spellbook"""
    size: int
    spells: List[Spell] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        self.slot = 'spellbook'
