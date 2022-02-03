
from typing import List, Dict
from dataclasses import dataclass

@dataclass(kw_only=True)
class Item:
    name: str
    description: str
    price: int
    actions: List[str]

@dataclass(kw_only=True)
class Consumable(Item):
    statistics: Dict[str, int]

@dataclass(kw_only=True)
class Spell(Consumable):
    """Class representing spells"""
    spell_type: str
    spell_range: str

    def execute(self, character: str) -> None:
        """Execute the current spell on the given character"""
        pass

@dataclass(kw_only=True)
class Equipment(Item):
    """Class representing any equipment or weapon"""
    durability: int
    statistics: Dict[str, int]
    body_part: str

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        self.max_durability = self.durability
