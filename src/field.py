from __future__ import annotations
from collections import defaultdict

import random
from typing import Any
from src.models.items.items import Item

from src.models.entity import Entity

from src.generators.abc import RandomGenerator

from src.models.statistics import Statistics
from src.models.collections import SizedContainer


def parse_field(field: Any, generator: RandomGenerator) -> list[Entity]:
    """
    Parse the given data and return a new field.

    Arguments:
    field -- the field's data.

    field may be one of the following types:
    - An integer
    - A range (a list of integers [size 2])
    - A dictionary of str to integer or a range

    If field is an integer n, n randomly selected entities will be
    created and returned. If field is a range from a to b, a n randomly
    selected entities will be created and returned, where n is a random
    number between a and b (both included).

    generator -- a module implementing the methods from the Generator
    protocol (which means at least generate_all and generate_many)

    Return value:
    A list of entities
    """
    if not field:
        return []

    if type(field) is int:
        return generator.generate_many(field)

    if type(field) is list and len(field) == 2:
        value = random.randint(*field)
        return generator.generate_many(value)

    if type(field) is dict:
        return _parse_dict_field(field, generator)

    raise Exception('field type accepts only int, list or dict')


def _parse_dict_field(field: dict[str, Any], generator: RandomGenerator) -> list[Entity]:
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

    return generator.generate_all(field)


def parse_inventory(inventory: Any, item_generator: RandomGenerator[Item], size: int = 8) -> SizedContainer:
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
    entities = parse_field(inventory, item_generator)
    return SizedContainer(size, iterable=entities)


def parse_statistics(statistics: dict[str, Any]) -> Statistics:
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
