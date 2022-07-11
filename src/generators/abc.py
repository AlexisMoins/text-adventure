"""
Module providing an abstract base class for all random generator
"""
from random import random
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Any, Generic, TypeVar

from src.models.statistics import Statistics
from src.models.collections import SizedContainer


ELEMENT = TypeVar('ELEMENT')


class RandomGenerator(ABC, Generic[ELEMENT]):
    """
    Class representing a basic abstract Generator. All generators defined
    in the game must inherit from this class.
    """

    def __init__(self, path: str, *, field: str = '') -> None:
        """
        Initialize a new abstract generator.

        Argument:
        path -- the path to the directory containing the dungeon generation
        files for floors

        field -- the name of the field associated with this generator. For
        instance, if the field is 'items', then the value of the field 'items'
        in 'rooms.yaml' will use this generator
        """
        self.PATH = path
        self.FIELD_NAME = field

    @abstractmethod
    def parse_floor(self, floor_name: str) -> None:
        """
        Parse a floor and load the files required by this generator. All
        generators must parse the new floors before starting to generate
        any entity.

        Argument:
        floor_name -- the name of the floor. The name must match the name
        of the floor directory containing all generation-related files.
        """
        pass

    @abstractmethod
    def generate(self, entity_id: str) -> ELEMENT:
        """
        Generate the entity corresponding to an entity ID.

        Argument:
        entity_id -- the identifier of the entity

        Return value:
        An entity (or sub-class)
        """
        pass

    @abstractmethod
    def generate_all(self, entities: dict[str, int]) -> list[ELEMENT]:
        """
        Generate all the entities in a dictionary.

        Argument:
        entities -- a dictionary of entity IDs and their quantity

        Return value:
        A list of entities
        """
        pass

    @abstractmethod
    def generate_many(self, k: int) -> list[ELEMENT]:
        """
        Generate k random entities

        Argument:
        k -- the number of entities to generate

        Return value:
        A list of entities
        """
        pass

    def _parse_dict_field(self, field: dict[str, Any]) -> list[ELEMENT]:
        """

        """
        generate_number = field.pop('generate', 1)

        if all(isinstance(value, dict) for value in field.values()):

            population = list(field.keys())
            weights = [field[item]['chances'] for item in population]

            field = {item: field[item]['quantity']
                     for item in random.choices(population, weights, k=generate_number)}

        field = {key: value if type(value) is int else random.randint(*value)
                 for key, value in field.items()}

        return self.generate_all(field)

    def parse_field(self, field: Any) -> list[ELEMENT]:
        """
        Parse the given data and return a new field.

        Arguments:
        field -- the field's data.

        field may be one of the following types: an integer, a range (a list
        of integers [size 2]) or a dictionary of str to integer or range

        Return value:
        A list of entities
        """
        if not field:
            return []

        if type(field) is int:
            return self.generate_many(field)

        if type(field) is list and len(field) == 2:
            value = random.randint(*field)
            return self.generate_many(value)

        if type(field) is dict:
            return self._parse_dict_field(field)

        raise Exception('field type accepts only int, list or dict')

    def parse_inventory(self, inventory: Any, size: int = 8) -> SizedContainer:
        """
        Return a new container of the given size. The container will be
        filled with the entities generated from the 'inventory' argument.

        Argument:
        inventory -- a dictionary of a statistic name and the value
        it is associated with. The value may be an integer or a valid
        range, that is to say either a list, a tuple or a set of integers
        of size 2.

        Keyword argument:
        size -- the maximum size of the container (default: 8)

        Return value:
        A container with a maximim size
        """
        entities = self.parse_field(inventory)
        return SizedContainer(size, iterable=entities)

    def parse_statistics(self, statistics: dict[str, Any]) -> Statistics:
        """
        Return a Statistics object containing statistics.

        Argument:
        statistics -- a dictionary of a statistic name and the value
        it is associated with. The value may be an integer or a valid
        range, that is to say either a list, a tuple or a set of integers
        of size 2.

        Return value:
        A new Statistics object
        """
        dictionary = defaultdict(int)
        for stat, value in statistics.items():

            if type(value) in [list, set, tuple] and len(value) == 2:
                value = random.randint(*value)

            dictionary[stat] = value
        return Statistics(dictionary)
