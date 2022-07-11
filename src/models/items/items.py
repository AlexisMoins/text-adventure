from colorama import Fore
from dataclasses import dataclass, field

from src.models.entity import Entity
from src.models.statistics import Statistics
from src.models.collections import SizedContainer


@dataclass(kw_only=True)
class Item(Entity):
    """
    Class representing a generic item
    """
    durability: list[int]
    price: int = 0

    def __str__(self) -> str:
        """Return the string representation of this item"""
        return self.name


@dataclass(kw_only=True)
class Chest(Item):
    """Represents any container item with a size"""
    items: SizedContainer
    is_locked: bool = False

    def __str__(self) -> str:
        """Return the string representation of the chest"""
        return f'{self.name} {Fore.MAGENTA}[{self.items.indicator}]{Fore.WHITE}'


@dataclass(kw_only=True)
class Equipment(Item):
    """
    Class representing a generic equipment
    """
    slot: str
    statistics: Statistics = field(default_factory=Statistics)
    equipped: bool = field(default=False, init=False)

    def __str__(self) -> str:
        """Return the string representation of the armor"""
        return f'{self.name} {Fore.MAGENTA}[{self.statistics}]{Fore.WHITE}'
