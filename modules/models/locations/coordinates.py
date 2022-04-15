from enum import Enum
from colorama import Fore
from typing import Any, Dict, List


class Direction(Enum):
    """Class representing the four cardinal directions"""

    NORTH = (0, 1, 'north')
    EAST = (1, 0, 'east')
    SOUTH = (0, -1, 'south')
    WEST = (-1, 0, 'west')

    def __str__(self) -> str:
        """Return the name of the current direction"""
        return self.value[2]


class Coordinates:
    """Class representing a set of coordinates"""

    def __init__(self, x: int, y: int) -> None:
        """Parameterised constructor creating a new set of coordinates"""
        self.x, self.y = (x, y)

    def next_towards(self, direction: Direction) -> 'Coordinates':
        """Return the coordinates in the given direction"""
        return Coordinates(self.x + direction.value[0], self.y + direction.value[1])

    def neighbours(self) -> Dict['Coordinates', Direction]:
        """Returns the list of all neighbouring coordinates"""
        return {self.next_towards(direction): direction for direction in list(Direction)}

    def __eq__(self, other: Any) -> bool:
        """Returns true if the current coordinates is equal to the other coordinates"""
        return isinstance(other, Coordinates) and other.x == self.x and other.y == self.y

    def __hash__(self) -> int:
        """Returns the hashed value of the current coordinates"""
        coordinates = (self.x, self.y)
        return hash(coordinates)

    def __repr__(self) -> str:
        """Return the representation of the current coordinate"""
        return f'Coordinates(x={self.x}, y={self.y})'

    def __str__(self) -> str:
        """Return the string representation of the coordinates"""
        return f'{Fore.YELLOW}[{self.x}, {self.y}]{Fore.WHITE}'
