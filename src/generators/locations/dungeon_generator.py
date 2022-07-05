import random
from typing import Any
from collections import deque

from src import dungeon, utils
from src.generators.locations import floor_generator


def generate(path: str = 'dungeon') -> None:
    """Create a new dungeon using the generation files found in the given path"""
    dungeon.PATH = path
    data = utils.get_content(path, 'floors.yaml')

    dungeon.FLOORS = floor_list(data)

    first_floor = dungeon.FLOORS.popleft()
    floor_generator.generate(first_floor)


def floor_list(data: dict[str, Any]) -> deque[str]:
    """Returns a queue of almost randomly generated floor name"""
    iterable = [choose_one(floor) if type(floor) is dict else floor for floor in data]
    return deque(iterable)


def choose_one(selection: dict[str, int]) -> str:
    """Returns a floor name after it has been randomly choosen from the items in the given selection"""
    population, weights = selection.keys(), selection.values()
    choice = random.choices(tuple(population), tuple(weights))
    return choice[0]
