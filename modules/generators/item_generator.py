from yaml import safe_load
from random import randint
from typing import Dict, List

from modules.items.items import *
from modules.items.equipments import *


class ItemGenerator:
    """Class generating items based on the provided configuration files"""

    def __init__(self, path: str) -> None:
        """Parameterised constructor creating a new generator of items"""
        self.path = path

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the floor generator"""
        with open(f'{self.path}/{floor}/items.yaml', 'r') as file:
            data = safe_load(file)
        self.generation_table = data.pop('generation')
        self.total_weight = sum(self.generation_table.values())
        self.items = data

    def generate_one(self) -> Item | None:
        """Generates a random item"""
        number = randint(1, self.total_weight)
        for item, weight in self.generation_table.items():
            if number <= weight:
                return self.__deserialize_item(dict(self.items[item]))
            number -= weight

    def __deserialize_item(self, data: Dict) -> Item | None:
        """Returns the item deserialized from the given data"""
        item_type = data.pop('type')
        if item_type == 'weapon':
            return Weapon(**data)
        if item_type == 'armor':
            return Armor(**data)
        return None

    def generate_many(self, n: int) -> List[Item]:
        """Generates n random items"""
        return [self.generate_one() for i in range(n)]

    def generate(self, item: str) -> Item | None:
        """Return the given item after it has been generated"""
        if item not in self.items.keys():
            return None
        return self.__deserialize_item(dict(self.items[item]))

    def generate_field(self, data: List[str | int] | int) -> List[Item]:
        """Returns a list of the data deserialized using the given generator"""
        if not data:
            return []
        if type(data) == int:
            return self.generate_many(data)
        if type(data) == list:
            if type(data[0]) == int and len(data) > 1:
                return self.generate_many(randint(data[0], data[1]))
            if type(data[0]) == str:
                return [self.generate(item) for item in data]