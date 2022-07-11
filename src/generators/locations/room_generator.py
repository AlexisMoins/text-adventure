import random
from typing import Any

from src import utils
from src.field import parse_field

from src.generators.abc import RandomGenerator

from src.models.locations.room import Room
from src.models.collections import Container
from src.models.locations.coordinates import Coordinates


class RoomGenerator(RandomGenerator):
    """

    """

    def __init__(self, path: str, generators: dict[str, RandomGenerator]) -> None:
        """
        Initialize a new (empty) room generator. To use the generator, call the
        'parse_floor' method on a floor name.

        Arguments:
        path -- the path to the dungeon directory containing the generation files
        for each floor

        generators -- the dictionary of generators used to parse fields
        """
        super().__init__(path)

        self.generators = generators

        # Mapping room name and its properties
        self.rooms: dict[str, dict] = {}

        # List of the possible room names
        self.population: list[str] = []

        # List of the chances of generating the corresponding room in the population
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
        self.rooms = utils.get_content(self.PATH, floor_name, 'rooms.yaml')
        generation = self.rooms.pop('generation')

        self.weights = list(generation.values())
        self.population = list(generation.keys())

    def get_entity_data(self, entity_id: str) -> dict[str, Any]:
        """

        """
        entity = self.rooms[entity_id]
        return entity.copy()

    def generate(self, entity_id: str) -> Room:
        """
        Generate the entity corresponding to an entity ID.

        Argument:
        entity_id -- the identifier of the entity

        Return value:
        An entity (or sub-class)
        """
        data = self._pop_room(entity_id)
        return self._deserialize_room(data)

    def generate_all(self, entities: dict[str, int]) -> list[Room]:
        """
        Generate all the items in a dictionary.

        Argument:
        entities -- a dictionary of entity IDs and their quantity

        Return value:
        A list of entities
        """
        return [self.generate(item_id) for item_id in entities]

    def generate_many(self, k: int) -> list[Room]:
        """

        """
        number = min(len(self.population), k)
        return [self._generate_one() for _ in range(number)]

    def _generate_one(self) -> Room:
        """

        """
        number = random.randint(1, sum(self.weights))
        for room, weight in zip(self.population, self.weights):

            if number <= weight:
                return self.generate(room)

            number -= weight
        raise Exception

    def _deserialize_room(self, field: dict[str, Any]) -> Room:
        """Returns the room deserialized from the given data"""
        entities = []
        for generator in self.generators.values():
            if generator.FIELD_NAME in field:
                data = field.pop(generator.FIELD_NAME)
                entities.extend(parse_field(data, generator))

        return Room(**field, entities=Container(entities))

    def _pop_room(self, room_id) -> dict[str, Any]:
        """
        Returns the given room's data and remove it from the generator
        """
        if room_id in self.population:
            index = self.population.index(room_id)

            del self.weights[index]
            self.population.remove(room_id)

        return self.rooms.pop(room_id)
