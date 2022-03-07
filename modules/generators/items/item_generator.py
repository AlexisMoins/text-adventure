from yaml import safe_load
from random import randint
from typing import Dict, List

from modules.items.items import Item
from modules.items.equipments import *

from modules.meta.singleton import Singleton
from modules.generators.generator import Generator
from modules.factories import item_factory as factory


class ItemGenerator(Generator, metaclass=Singleton):
    """Class generating items based on the provided configuration files"""

    def __init__(self, path: str) -> None:
        """Parameterised constructor creating a new generator of items"""
        self.path = path
        factory.register('weapon', Weapon)
        factory.register('armor', Armor)

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
                return factory.create(self.items[item])
            number -= weight

    def generate_many(self, n: int) -> List[Item]:
        """Generates n random items"""
        return [self.generate_one() for i in range(n)]

    def generate(self, item: str) -> Item | None:
        """Return the given item after it has been generated"""
        if item not in self.items.keys():
            return None
        return factory.create(self.items[item])
