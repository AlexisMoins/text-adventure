from yaml import safe_load
from random import randint
from typing import Any, Dict, List

from models.locations.dungeon import Dungeon


def generate(path: str) -> Dungeon:
    """Returns a new dungeon generated using the data in the given path"""
    with open(f'{path}/floors.yaml', 'r') as file:
        data = safe_load(file)
    floors = _floor_list(data)
    return Dungeon(floors, path)


def _floor_list(data: Dict[str, Any]) -> List[str]:
    """Returns a list of (almost) randomly generated floor name"""
    return [_choose_one(floor) if type(floor) == dict else floor for floor in data]


def _choose_one(selection: Dict[str, int]) -> str | None:
    """Returns a floor name after it has been randomly choosen from the items in the given selection"""
    total_weight = sum(selection.values())
    number = randint(1, total_weight)
    for floor, weight in selection.items():
        if number <= weight:
            return floor
        number -= weight
    return None
