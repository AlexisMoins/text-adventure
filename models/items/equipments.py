from typing import List
from dataclasses import dataclass, field

from models.items.items import Item, Spell


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


@dataclass(kw_only=True)
class Weapon(Equipment):
    """Class representing any weapon"""
    damage: int

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        self.slot = 'weapon'


@dataclass(kw_only=True)
class SpellBook(Equipment):
    """Class representing any spellbook"""
    size: int
    spells: List[Spell] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        self.slot = 'spellbook'
