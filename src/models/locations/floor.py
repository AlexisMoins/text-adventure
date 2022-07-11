from dataclasses import dataclass

from src.models.locations.room import Room


@dataclass(slots=True, frozen=True)
class Floor:
    """
    Class representing a floor from the dungeon. It contains
    the starting room (entry) and the exit.
    """
    start: Room
    exit: Room
