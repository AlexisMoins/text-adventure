from random import randint
from typing import Any
from src import utils

from src.models.characters.npc import Enemy
from src.models.characters.character import Character

import src.factories.generator_factory as generator_factory
from src.models.items.inventory import Inventory
from src.generators.field_generator import FieldGenerator


class CharacterGenerator:
    """Class generating enemies based on the provided configuration files"""

    def __init__(self, dungeon_path: str) -> None:
        """Constructor creating a new generator of enemies"""
        self.dungeon = dungeon_path

    def load_floor(self, file_name: str) -> None:
        """Loads a floor into the enemy generator"""
        data = utils.load_resource(file_name)
        self.generation_table = data.pop('generation')
        self.characters = data

    def generate(self, character: str) -> Character | None:
        """Return the given character after it has been generated"""
        if character not in self.characters.keys():
            return None
        copy = self.characters[character].copy()
        return self._deserialize_character(copy)

    def generate_one(self) -> Character | None:
        """Generates a random enemy character"""
        number = randint(1, sum(self.generation_table.values()))
        for enemy, weight in self.generation_table.items():
            if number <= weight:
                return self.generate(enemy)
            number -= weight
        return None

    def generate_many(self, n: int) -> list[Character]:
        """Generates n random items"""
        number = min(len(self.generation_table), n)
        return [self.generate_one() for _ in range(number)]

    def generate_inventory(self, data):
        """Generate an inventory with the given data"""
        items = FieldGenerator.generate(generator_factory.generators['item'], data.pop('inventory'))
        return Inventory(items=items, gold=data.pop('gold'))


class EnemyGenerator(CharacterGenerator):
    """"""

    def __init__(self, dungeon_path: str) -> None:
        """Parameterised constructor creating a new generator of enemies"""
        super().__init__(dungeon_path)

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the enemy generator"""
        super().load_floor(f'{self.dungeon}/{floor}/enemies.yaml')

    def _deserialize_character(self, data: dict[str, Any]) -> Enemy:
        """Returns the enemy deserialized from the given data"""
        inventory = super().generate_inventory(data)
        return Enemy(**data, inventory=inventory)
