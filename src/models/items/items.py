from colorama import Fore
from typing import DefaultDict
from collections import defaultdict
from dataclasses import dataclass, field

from src.factory import register
from src.models.entity import Entity
from src.models.collections import SizedContainer


@register('item')
@dataclass(kw_only=True)
class Item(Entity):
    """Represents a generic item"""
    durability: list[int]
    price: int = 0

    def __str__(self) -> str:
        """Return the string representation of this item"""
        return self.name


@register('chest')
@dataclass(kw_only=True)
class Chest(Item):
    """Represents any container item with a size"""
    items: SizedContainer
    is_locked: bool = False

    def __str__(self) -> str:
        """Return the string representation of the chest"""
        return f'{self.name} {Fore.MAGENTA}[{self.items.indicator}]{Fore.WHITE}'


@register('consumable')
@dataclass(slots=True)
class Consumable(Item):
    """Represents a general comsumable item such as a potion"""
    statistics: DefaultDict[str, int] = field(default_factory=lambda: defaultdict(int))


@register('equipment')
@dataclass(kw_only=True)
class Equipment(Item):
    """Class representing a generic equipment"""
    slot: str
    statistics: dict[str, int] = field(default_factory=dict)
    equipped: bool = field(default=False, init=False)

    def __str__(self) -> str:
        """Return the string representation of the armor"""
        statistics = ', '.join([f'{stat} +{value}' for stat, value in self.statistics.items()])
        return f'{self.name} {Fore.MAGENTA}[{statistics}]{Fore.WHITE}'
