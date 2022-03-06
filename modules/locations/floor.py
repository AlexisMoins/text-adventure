from typing import Dict

from modules.locations.room import Room
from modules.locations.coordinates import Coordinates


class Floor:
    """Class representing a collection of rooms"""

    def __init__(self, rooms: Dict[Coordinates, Room]) -> None:
        """Parameterised constructor creating a new floor"""
        self.rooms = rooms
        self.is_finished = False
        self.current_room = self.rooms[Coordinates(0, 0)]
