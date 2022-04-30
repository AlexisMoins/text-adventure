import math
import random
from typing import Any

from src import utils
from src.models.items.items import Item

from src.factories import item_factory as factory


class ItemGenerator:
    """Class generating items based on the provided configuration files"""

    def __init__(self, dungeon_path: str) -> None:
        """Parameterised constructor creating a new generator of items"""
        self.dungeon = dungeon_path

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the item generator"""
        data = utils.load_resource(f'{self.dungeon}/{floor}/items.yaml')
        self.generation_table = data.pop('generation')
        self.items: dict[str, dict] = data

    def generate(self, item_name: str) -> Item | None:
        """Return the given item after it has been generated"""
        if item_name not in self.items.keys():
            return None

        item = self.items[item_name].copy()
        if 'statistics' in item.keys():
            self.random_statistics(item)

        return factory.create(item)

    def random_statistics(self, item: dict[str, Any]) -> None:
        """Randomize the statistics of the item"""
        statistics = dict()
        for name, value in item['statistics'].items():
            percentage = value * 0.20
            statistics[name] = random.randint(math.floor(value-percentage), math.ceil(value+percentage))

        item['statistics'] = statistics

    def generate_one(self) -> Item | None:
        """Generates a random item"""
        number = random.randint(1, 100)
        for item, weight in self.generation_table.items():
            if number <= weight:
                return self.generate(item)
            number -= weight
        return None

    def generate_many(self, n: int) -> list[Item]:
        """Generates n random items"""
        return [self.generate_one() for _ in range(n)]
