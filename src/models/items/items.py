from colorama import Fore
from dataclasses import dataclass, field

from src.utils import indefinite_determiner


@dataclass(kw_only=True)
class Item:
    """Class representing a generic item"""
    name: str
    price: int = 0
    description: str
    quantity: int = 1
    actions: list[str] = field(default_factory=list)
    is_in_inventory: bool = field(init=False, default=False)

    def __str__(self) -> str:
        """String representation of the item"""
        return f'{indefinite_determiner(self.name)}'


@dataclass(kw_only=True)
class Consumable(Item):
    """Class representing a general"""
    statistics: dict[str, int] = field(default_factory=dict)


@dataclass(kw_only=True)
class Spell(Consumable):
    """Class representing spells"""
    damage: int
    spell_type: str
    spell_range: str


@dataclass(kw_only=True)
class Equipment(Item):
    """Class representing a generic equipment"""
    slot: str = None
    durability: int
    statistics: dict[str, int] = field(default_factory=dict)
    is_equipped: bool = field(default=False, init=False)

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
    spells: list[Spell] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        super().slot = 'spellbook'
