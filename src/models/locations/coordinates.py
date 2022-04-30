from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

from colorama import Fore
from typing import Any


class Direction(Enum):
    """Class representing the four cardinal directions"""

    NORTH = (0, 1)
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)

    @staticmethod
    def parse(direction: str) -> Direction:
        directions = {'n': Direction.NORTH, 'e': Direction.EAST,
                      's': Direction.SOUTH, 'w': Direction.WEST}

        return directions[direction[0]]

    def __str__(self) -> str:
        """Return the name of the current direction"""
        return self.name.lower()


@dataclass(frozen=True)
class Coordinates:
    """Class representing a set of bi-dimensional coordinates"""
    x: int
    y: int

    def next_towards(self, direction: Direction) -> Coordinates:
        """Return the coordinates in the given direction"""
        return Coordinates(self.x + direction.value[0], self.y + direction.value[1])

    def neighbours(self) -> dict[Coordinates, Direction]:
        """Returns the list of all neighbouring coordinates"""
        return {self.next_towards(direction): direction for direction in list(Direction)}

    def __eq__(self, other: Any) -> bool:
        """Returns true if the current coordinates is equal to the other coordinates"""
        return isinstance(other, Coordinates) and other.x == self.x and other.y == self.y

    def __hash__(self) -> int:
        """Returns the hashed value of the current coordinates"""
        coordinates = (self.x, self.y)
        return hash(coordinates)

    def __str__(self) -> str:
        """Return the string representation of the coordinates"""
        return f'{Fore.YELLOW}[{self.x}, {self.y}]{Fore.WHITE}'
