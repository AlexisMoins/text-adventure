from yaml import safe_load
from random import randint
from typing import Dict, List

from text_adventure.items.items import *
from text_adventure.items.equipments import *


class ItemGenerator:
    """Class generating items based on the provided configuration files"""

    def __init__(self, floor_path: str) -> None:
        """Constructor creating a new generator of items"""
        with open(f"{floor_path}/items.yaml", "r") as file:
            data = safe_load(file)
        self.generation_table = data.pop("generation")
        self.total_weight = sum(self.generation_table.values())
        self.items = data

    def generate_one(self, luck: int = 0) -> Item | None:
        """Generates a random item"""
        number = min(self.total_weight, randint(1, self.total_weight) + luck)
        for item, weight in self.generation_table.items():
            if number <= weight:
                return self.deserialize_item(dict(self.items[item]))
            number -= weight

    def deserialize_item(self, data: Dict) -> Item | None:
        """Returns the item deserialized from the given data"""
        item_type = data.pop("type")
        if item_type == "weapon":
            return Weapon(**data)
        if item_type == "armor":
            return Armor(**data)
        return None

    def generate_many(self, n: int, luck: int = 0) -> List[Item]:
        """Generates n random items"""
        return [self.generate_item(luck) for item in range(n)]
