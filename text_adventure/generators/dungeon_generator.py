from yaml import safe_load
from random import randint
from typing import Any, Dict, List

from text_adventure.locations.dungeon import Dungeon


class DungeonGenerator:
    """Class representing a generator of dungeons"""

    @staticmethod
    def generate_one(path: str = 'dungeon') -> Dungeon:
        """Returns a new dungeon generated using the data in the given path"""
        with open(f'{path}/floors.yaml', 'r') as file:
            data = safe_load(file)
        floors = DungeonGenerator.__floor_list(data)
        floor_paths = [f'{path}/{floor}' for floor in floors]
        return Dungeon(floor_paths)

    @staticmethod
    def __floor_list(data: Dict[str, Any]) -> List[str]:
        """Returns a list of (almost) randomly generated floor paths"""
        return [
            DungeonGenerator.__choose(floor) if type(floor) == dict else floor
            for floor in data
        ]

    @staticmethod
    def __choose(selection: Dict[str, int]) -> str | None:
        """Returns a floor path after it has been randomly choosen from the items in the given selection"""
        total_weight = sum(selection.values())
        number = randint(1, total_weight)
        for floor, weight in selection.items():
            if number <= weight:
                return floor
            number -= weight
        return None
