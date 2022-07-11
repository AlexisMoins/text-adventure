from __future__ import annotations
from dataclasses import dataclass, field

from src.models.collections import Container
from src.models.locations.coordinates import Coordinates, Direction


@dataclass(kw_only=True)
class Room:
    """Represents a room, a space containing entities (characters and/or items)"""
    description: str
    entities: Container = field(default_factory=Container)

    explored: bool = field(init=False, default=False)
    coordinates: Coordinates = field(init=False, default=None)
    exits: dict[Direction, Room] = field(init=False, default_factory=dict)

    def add_exit(self, direction: Direction, room: Room) -> None:
        """Add a new exit to the curren room"""
        self.exits[direction] = room
        room.exits[direction.opposite] = self

        if room.coordinates is None:
            room.coordinates = self.coordinates.in_direction(direction)
