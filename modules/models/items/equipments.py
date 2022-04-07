import statistics
from colorama import Fore
from typing import Dict, List
from dataclasses import dataclass, field

from modules.models.items.items import Item, Spell


@dataclass(kw_only=True)
class Equipment(Item):
    """Class representing a generic equipment"""
    slot: str = None
    durability: int
    statistics: Dict[str, int] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        self.max_durability = self.durability

    def __str__(self) -> str:
        """Return the string representation of the armor"""
        statistics = ', '.join([f'{stat} +{value}' for stat, value in self.statistics.items()])
        return f'{super().__str__()} {Fore.MAGENTA}[{statistics}]{Fore.WHITE}'


@dataclass(kw_only=True)
class SpellBook(Equipment):
    """Class representing any spellbook"""
    capacity: int
    spells: List[Spell] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        super().slot = 'spellbook'
