from typing import Dict

from text_adventure.locations.coordinates import Coordinates
from text_adventure.locations.room import Room


class Floor:
    """"""

    def __init__(self, rooms: Dict[Coordinates, Room]) -> None:
        """"""
        self.rooms = rooms
