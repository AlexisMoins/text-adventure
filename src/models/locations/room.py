from __future__ import annotations

import textwrap
from dataclasses import dataclass, field

from src.models.collections import Container
from src.models.locations.coordinates import Coordinates, Direction


@dataclass(kw_only=True)
class Room:
    """Represents a room, a space containing entities (characters and/or items)"""
    description: str
    entities: Container = field(default_factory=Container)

    explored: bool = field(init=False, default=False)
    coordinates: Coordinates | None = field(init=False, default=None)
    exits: dict[Direction, Room] = field(init=False, default_factory=dict)

    def add_exit(self, direction: Direction, room: Room) -> None:
        """Add a new exit to the curren room"""
        self.exits[direction] = room
        room.exits[direction.opposite] = self

        if room.coordinates is None:
            room.coordinates = self.coordinates.in_direction(direction)

    def display(self) -> None:
        """Display the given room"""
        clear_screen()
        print(f'{get_character_status(dungeon.PLAYER)}    position: {dungeon.current_room.coordinates}\n')

        print(textwrap.fill(dungeon.current_room.description))

        entities_and_exits = list(dungeon.current_room.entities) + list(dungeon.current_room.exits.keys())
        if entities_and_exits:
            word = 'are' if len(entities_and_exits) > 1 else 'is'
            print(f'\nAround you {word}:')
            display_entities()
