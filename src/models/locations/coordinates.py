from __future__ import annotations

from enum import Enum
from colorama import Fore
from dataclasses import dataclass


class Direction(Enum):
    """Class representing the four cardinal directions"""

    # The direction to the north
    NORTH = (0, 1)

    # The direction to the east
    EAST = (1, 0)

    # The direction to the south
    SOUTH = (0, -1)

    # The direction to the west
    WEST = (-1, 0)

    @staticmethod
    def parse(string: str) -> Direction | None:
        """Return the direction corresponding to the given string"""
        for direction in Direction:
            if direction.name.startswith(string.lower()):
                return direction

    @property
    def opposite(self) -> Direction:
        """Return the opposite direction"""
        movement = (self.value[0] * -1, self.value[1] * -1)
        return Direction(movement)

    def __str__(self) -> str:
        """Return the name of the current direction"""
        return self.name.lower()


@dataclass(frozen=True, unsafe_hash=True)
class Coordinates:
    """Class representing a set of bi-dimensional coordinates"""
    x: int
    y: int

    def in_direction(self, direction: Direction) -> Coordinates:
        """Return the coordinates in the given direction"""
        return Coordinates(self.x + direction.value[0], self.y + direction.value[1])

    def neighbours(self) -> dict[Direction, Coordinates]:
        """Returns a mapping of direction to coordinates"""
        return {direction: self.in_direction(direction) for direction in list(Direction)}

    def __str__(self) -> str:
        """Return the string representation of the coordinates"""
        return f'{Fore.YELLOW}[{self.x}, {self.y}]{Fore.WHITE}'
