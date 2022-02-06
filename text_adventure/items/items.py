from typing import List, Dict
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Item:
    """Class representing a generic item"""

    name: str
    price: int = 0
    description: str
    actions: List[str] = field(default_factory=list)


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
