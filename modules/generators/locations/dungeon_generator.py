import random
from typing import Any, Dict, List

from modules import utils
from modules.locations.dungeon import Dungeon


def generate(floor_path: str) -> Dungeon:
    """Returns a new dungeon generated using the data in the given path"""
    data = utils.load_resource(floor_path + '/floors.yaml')
    floors = floor_list(data)
    return Dungeon(floors, floor_path)


def floor_list(data: Dict[str, Any]) -> List[str]:
    """Returns a list of (almost) randomly generated floor name"""
    return [choose_one(floor) if type(floor) == dict else floor for floor in data]


def choose_one(selection: Dict[str, int]) -> str | None:
    """Returns a floor name after it has been randomly choosen from the items in the given selection"""
    total_weight = sum(selection.values())
    number = random.randint(1, total_weight)
    for floor, weight in selection.items():
        if number <= weight:
            return floor
        number -= weight
    return None
