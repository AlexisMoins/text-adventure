from random import randint
from typing import Any, Dict, List
from yaml import safe_load

from models.characters.npc import Enemy
from models.characters.character import Character

from models.items.inventory import Inventory
from models.generators.generator import Generator


class CharacterGenerator(Generator):
    """Class generating enemies based on the provided configuration files"""

    def __init__(self, path: str, item_generator: Generator) -> None:
        """Constructor creating a new generator of enemies"""
        self.path = path
        self.item_generator = item_generator

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the enemy generator"""
        with open(f'{self.path}/{floor}/enemies.yaml', 'r') as file:
            data = safe_load(file)
            self.generation_table = data.pop('generation')
            self.enemies = data

    def generate(self, enemy: str) -> Character | None:
        """Return the given character after it has been generated"""
        if enemy not in self.enemies.keys():
            return None
        copy = self.enemies[enemy].copy()
        return self._deserialize_enemy(copy)

    def generate_one(self) -> Character | None:
        """Generates a random enemy character"""
        number = randint(1, sum(self.generation_table.values()))
        for enemy, weight in self.generation_table.items():
            if number <= weight:
                return self.generate(enemy)
            number -= weight
        return None

    def generate_many(self, n: int) -> List[Character]:
        """Generates n random items"""
        number = min(len(self.generation_table), n)
        return [self.generate_one() for _ in range(number)]

    def _deserialize_enemy(self, data: Dict[str, Any]) -> Enemy:
        """Returns the enemy deserialized from the given data"""
        items = self.item_generator.generate_field(data.pop('inventory'))
        inventory = Inventory(items=items, gold=data.pop('gold'))
        return Enemy(**data, inventory=inventory)
