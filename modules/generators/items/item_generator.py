import random
from typing import List

from modules import utils
from modules.items.items import Item
from modules.factories import items as factory


class ItemGenerator:
    """Class generating items based on the provided configuration files"""

    def __init__(self, path: str) -> None:
        """Parameterised constructor creating a new generator of items"""
        self.path = path
        factory.initialize()

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the item generator"""
        data = utils.load_resource(f'{self.path}/{floor}/items.yaml')
        self.generation_table = data.pop('generation')
        self.items = data

    def generate(self, item: str) -> Item | None:
        """Return the given item after it has been generated"""
        if item not in self.items.keys():
            return None
        return factory.create(self.items[item])

    def generate_one(self) -> Item | None:
        """Generates a random item"""
        number = random.randint(1, 100)
        for item, weight in self.generation_table.items():
            if number <= weight:
                return self.generate(item)
            number -= weight
        return None

    def generate_many(self, n: int) -> List[Item]:
        """Generates n random items"""
        return [self.generate_one() for _ in range(n)]
