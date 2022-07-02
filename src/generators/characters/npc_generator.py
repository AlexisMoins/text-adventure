import random
from typing import Any
from src import utils, factory

from src.models.characters.npc import NPC
from src import dungeon, utils, factory, field


# Mapping npc name and its properties
npc: dict[str, dict[str, Any]] = {}


# List of the possible npc names
population: list[str] = []


# List of the chances of generating the corresponding npc in the population
weights: list[int] = []


def get_npc_data(npc_id: str) -> dict[str, Any]:
    """
    Return the data of the of
    """
    global npc
    return npc[npc_id].copy()


def parse_floor(floor: str) -> None:
    """Load the given floor's character generation file"""
    global npc

    npc = utils.get_content(dungeon.PATH, floor, 'npc.yaml')
    generation = npc.pop('generation')

    global weights
    global population

    weights = list(generation.values())
    population = list(generation.keys())


def generate(npc_id: str, quantity: int = 1) -> NPC:
    """Return the given character after it has been generated"""
    data = get_npc_data(npc_id)

    data['statistics'] = field.parse_statistics(data['statistics'])
    data['inventory'] = field.parse_inventory(data['inventory'])

    data['quantity'] = quantity
    _type = data.pop('type', 'NPC')

    return factory.create_entity(data, _type)


def generate_many(k: int) -> list[NPC]:
    """Generates k randomly generated items"""
    number = min(len(population), k)
    return [generate(item_id) for item_id in random.choices(population, weights, number)]
