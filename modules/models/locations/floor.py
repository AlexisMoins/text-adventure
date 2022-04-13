from typing import Dict

from modules.models.locations.room import Room
from modules.models.locations.coordinates import Coordinates


class Floor:
    """Class representing a collection of rooms"""

    def __init__(self, name: str, rooms: Dict[Coordinates, Room]) -> None:
        """Parameterised constructor creating a new floor"""
        self.name = name
        self.rooms = rooms
        self.is_finished = False
        self.player_position = Coordinates(0, 0)

    def current_room(self) -> Room:
        """Return the current room"""
        return self.rooms[self.player_position]
