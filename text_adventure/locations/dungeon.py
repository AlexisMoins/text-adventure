from typing import List
from yaml import safe_load
from random import randint

from text_adventure.generators.floor_generator import FloorGenerator


class Dungeon:
    """Class representing a dungeon with its list of floors"""

    def __init__(self, floors: List[str], path: str) -> None:
        """Parameterised constructor creating a new dungeon"""
        self.floors = floors
        self.floor_generator = FloorGenerator(path)

    def start(self, player) -> None:
        """Starts the ascension of the dungeon"""
        self.player = player
        self.next_floor()

    def next_floor(self) -> None:
        """Ascend to the next floor"""
        self.floor_generator.load_floor(self.floors.pop(0))
        self.current_floor = self.floor_generator.generate_one()
