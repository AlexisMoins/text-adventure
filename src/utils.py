import os
import yaml

from collections import defaultdict
from typing import Any, DefaultDict, Protocol

from src import dungeon
from src.models.entity import Entity


class Generator(Protocol):
    """Represents a generator (used for prototyping modules)"""

    def generate(self, entity_id: str) -> Entity:
        """"""
        pass

    def generate_many(self, k: int) -> list[Entity]:
        """"""
        pass


def get_content(*path: str) -> Any:
    """Return the content of the file at the given path"""
    path = os.path.join(*path)
    with open(path, 'r') as data:
        return yaml.safe_load(data)


def parse_statistics(statistics: dict[str, int]) -> DefaultDict:
    """Return a DefaultDict of the given statistics"""
    dictionary = defaultdict(int)
    for stat, value in statistics.items():
        dictionary[stat] = value
    return dictionary


def parse_field(field: Any, generator: Generator) -> list[Any]:
    """Returns a list of the data deserialized using the given generator"""
    if not field:
        return []

    if type(field) == int:
        return generator.generate_many(field)

    if type(field) == list:
        if type(field[0]) == int and len(field) > 1:
            n = dungeon.RANDOM.randint(field[0], field[1])
            return generator.generate_many(n)

        if type(field[0]) == str:
            return [generator.generate(item) for item in field]
