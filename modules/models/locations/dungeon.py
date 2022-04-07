from typing import List

from modules.models.locations.room import Room
from modules.factories import generators


class Dungeon:
    """Model representing a dungeon with its list of floors"""

    def __init__(self, floors: List[str]) -> None:
        """Parameterised constructor creating a new dungeon"""
        self.floors: List[str] = floors
        self.next_floor()

    @property
    def current_room(self) -> Room:
        """Return the current room"""
        return self.current_floor.current_room

    def next_floor(self) -> None:
        """Ascend to the next floor"""
        generators.load_floor(self.floors.pop(0))
        self.current_floor = generators.get('floor').generate_one()