from random import randint
from typing import Any, Dict, List
from yaml import safe_load

from modules.items.inventory import Inventory

from modules.characters.npc import NPC
from modules.characters.character import Character

from modules.generators.generator import Generator
from modules.generators.items.item_generator import ItemGenerator


class EnemyGenerator(Generator):
    """Class generating enemies based on the provided configuration files"""

    def __init__(self, path: str, item_generator: ItemGenerator) -> None:
        """Constructor creating a new generator of enemies"""
        self.path = path
        self.item_generator = ItemGenerator(path)

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the enemy generator"""
        with open(f'{self.path}/{floor}/enemies.yaml', 'r') as file:
            data = safe_load(file)
        self.generation_table = data.pop('generation')
        self.enemies = data

    def generate_one(self) -> Character | None:
        """Generates a random enemy character"""
        if not self.enemies or not self.generation_table:
            return None

        number = randint(1, sum(self.generation_table.values()))
        for enemy, weight in self.generation_table.items():
            if number <= weight:
                return self.__deserialize_enemy(dict(self.enemies[enemy]))
            number -= weight

    def __deserialize_enemy(self, data: Dict[str, Any]) -> Character:
        """Returns the room deserialized from the given data"""
        items = self.item_generator.generate_field(data.pop('inventory'))
        inventory = Inventory(items=items, gold=data.pop('gold'))
        return NPC(**data, inventory=inventory)

    def generate_many(self, n: int) -> List[Character]:
        """Generates n random items"""
        return [self.generate_one() for i in range(n)]

    def generate(self, enemy: str) -> Character | None:
        """Return the given character after it has been generated"""
        if enemy not in self.enemies.keys():
            return None
        return self.__deserialize_enemy(dict(self.enemies[enemy]))
