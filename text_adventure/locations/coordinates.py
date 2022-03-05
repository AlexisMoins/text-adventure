from enum import Enum
from typing import List


class Direction(Enum):
    """Class representing the four cardinal directions"""

    NORTH = (0, 1)
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)


class Coordinates:
    """Class representing a set of coordinates"""

    def __init__(self, x: int, y: int) -> None:
        """Parameterised constructor creating a new set of coordinates"""
        self.x = x
        self.y = y

    def next_towards(self, direction: Direction) -> 'Coordinates':
        """Return the coordinates in the given direction"""
        return Coordinates(self.x + direction.value[0], self.y + direction.value[1])

    def neighbours(self) -> List['Coordinates']:
        """Returns the list of all neighbouring coordinates"""
        return [self.next_towards(direction) for direction in list(Direction)]
