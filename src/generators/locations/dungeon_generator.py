import random
from typing import Any, Dict, List

from src import utils
from src.models.locations.dungeon import Dungeon


class DungeonGenerator:
    """Class representing a generator of dungeons"""

    @staticmethod
    def generate(dungeon_path: str) -> Dungeon:
        """Returns a new dungeon generated using the data in the given path"""
        data = utils.load_resource(f'{dungeon_path}/floors.yaml')
        floors = DungeonGenerator.floor_list(data)
        return Dungeon(floors)

    @staticmethod
    def floor_list(data: Dict[str, Any]) -> List[str]:
        """Returns a list of (almost) randomly generated floor name"""
        return [DungeonGenerator.choose_one(floor) if type(floor) == dict
                else floor for floor in data]

    @staticmethod
    def choose_one(selection: Dict[str, int]) -> str | None:
        """Returns a floor name after it has been randomly choosen from the items in the given selection"""
        total_weight = sum(selection.values())
        number = random.randint(1, total_weight)
        for floor, weight in selection.items():
            if number <= weight:
                return floor
            number -= weight
        return None
