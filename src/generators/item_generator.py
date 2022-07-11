import random
from typing import Any

from src import utils, field
from src.generators.abc import RandomGenerator
from src.models.items.items import Chest, Equipment, Item


class ItemGenerator(RandomGenerator):
    """

    """

    def __init__(self, path: str) -> None:
        """
        Initialize a new (empty) item generator. To use the generator, call the
        'parse_floor' method on a floor name.

        Argument:
        path -- the path to the dungeon directory containing the generation files
        for each floor
        """
        super().__init__(path, field='items')

        # Mapping item name and its properties
        self.items: dict[str, dict] = {}

        # List of the possible item names
        self.population: list[str] = []

        # List of the chances of generating the corresponding item in the population
        self.weights: list[int] = []

    def parse_floor(self, floor_name: str) -> None:
        """
        Parse a floor and load the files required by this generator. All
        generators must parse the new floors before starting to generate
        any entity.

        Argument:
        floor_name -- the name of the floor. The name must match the name
        of the floor directory containing all generation-related files.
        """
        self.items = utils.get_content(self.PATH, floor_name, 'items.yaml')
        generation = self.items.pop('generation')

        self.weights = list(generation.values())
        self.population = list(generation.keys())

    def get_entity_data(self, entity_id: str) -> dict[str, Any]:
        """

        """
        entity = self.items[entity_id]
        return entity.copy()

    def generate(self, entity_id: str) -> Item:
        """
        Generate the entity corresponding to an entity ID.

        Argument:
        entity_id -- the identifier of the entity

        Return value:
        An entity (or sub-class)
        """
        item = self.get_entity_data(entity_id)

        if 'statistics' in item:
            item['statistics'] = field.parse_statistics(item['statistics'])

        _type = item.pop('type').lower()

        if _type == 'chest':
            return Chest(**item)

        if _type == 'equipment':
            return Equipment(**item)

        return Item(**item)

    def generate_all(self, entities: dict[str, int]) -> list[Item]:
        """
        Generate all the items in a dictionary.

        Argument:
        entities -- a dictionary of entity IDs and their quantity

        Return value:
        A list of entities
        """
        return [self.generate(item_id) for item_id in entities]

    def generate_many(self, k: int) -> list[Item]:
        """

        """
        number = min(len(self.population), k)
        return [self.generate(item_id) for item_id
                in random.choices(self.population, weights=self.weights, k=number)]
