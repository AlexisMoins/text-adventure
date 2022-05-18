import importlib
from typing import Any

from src import dungeon, utils, factory
from src.models.items.items import Item
from src.models.collections import SizedContainer


# Mapping item name and its properties
items: dict[str, dict] = {}

# List of the possible item names
population: list[str] = []

# List of the chances of generating the corresponding item in the population
weights: list[int] = []


def parse_floor(floor: str) -> None:
    """Load the given floor's item generation file"""
    global items

    items = utils.get_content(dungeon.PATH, floor, 'items.yaml')
    generation = items.pop('generation')

    global weights
    global population

    weights = list(generation.values())
    population = list(generation.keys())


def generate(item_id: str) -> Item:
    """Return the given item after it has been generated"""
    item = items[item_id].copy()
    return factory.create(item)


def generate_many(k: int) -> list[Item]:
    """Generates k randomly generated items"""
    number = min(len(population), k)
    return [generate(item_id) for item_id
            in dungeon.RANDOM.choices(population, weights=weights, k=number)]


def parse_inventory(field: Any, size: int = 8) -> SizedContainer:
    """Return a Container of the given size (default 8) and the given field"""
    items = utils.parse_field(field, importlib.import_module('src.generators.item_generator'))
    return SizedContainer(size, iterable=items)
