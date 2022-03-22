from typing import List
from yaml import safe_load
from random import randint

from models.items.items import Item
from models.items.equipments import Weapon, Armor

from models.factories import item_factory
from models.generators.generator import Generator


class ItemGenerator(Generator):
    """Class generating items based on the provided configuration files"""

    def __init__(self, path: str) -> None:
        """Parameterised constructor creating a new generator of items"""
        self.path = path
        item_factory.register('weapon', Weapon)
        item_factory.register('armor', Armor)

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the item generator"""
        with open(f'{self.path}/{floor}/items.yaml', 'r') as file:
            data = safe_load(file)
            self.generation_table = data.pop('generation')
            self.total_weight = sum(self.generation_table.values())
            self.items = data

    def generate(self, item: str) -> Item | None:
        """Return the given item after it has been generated"""
        if item not in self.items.keys():
            return None
        return item_factory.create(self.items[item])

    def generate_one(self) -> Item | None:
        """Generates a random item"""
        number = randint(1, self.total_weight)
        for item, weight in self.generation_table.items():
            if number <= weight:
                return item_factory.create(self.items[item])
            number -= weight
        return None

    def generate_many(self, n: int) -> List[Item]:
        """Generates n random items"""
        return [self.generate_one() for i in range(n)]
