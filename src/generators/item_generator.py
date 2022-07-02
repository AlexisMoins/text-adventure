import random

from src import dungeon, utils, factory
from src.models.items.items import Item


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


def generate(item_id: str, quantity: int = 1) -> Item:
    """
    Generate the item corresponding to an item ID.

    Argument:
    item_id -- the identifier

    Keyword argument:
    quantity -- the quantity of the item

    Return value:
    An item
    """
    item = items[item_id].copy()
    item['quantity'] = quantity

    return factory.create_entity(item)


def generate_many(k: int) -> list[Item]:
    """Generates k randomly generated items"""
    number = min(len(population), k)
    return [generate(item_id) for item_id
            in random.choices(population, weights=weights, k=number)]


def generate_all(items: dict[str, int]) -> list[Item]:
    """
    Generate all the elements in a dictionary.

    Argument:
    entities -- a dictionary of item IDs and their corresponding quantity

    Return value:
    A list of items
    """
    return [generate(item_id, quantity)
            for item_id, quantity in items.items()]
