from typing import List

from modules.factories import generator_factory

from modules.models.locations.room import Room
from modules.models.locations.floor import Floor


class Dungeon:
    """Model representing a dungeon with its list of floors"""

    def __init__(self, floors: List[str]) -> None:
        """Parameterised constructor creating a new dungeon"""
        self.floors: List[str] = floors
        self.floor_generator = generator_factory.get('floor')
        self.current_floor: Floor
        self.next_floor()

    @property
    def current_room(self) -> Room:
        """Return the current room"""
        return self.current_floor.current_room

    def next_floor(self) -> None:
        """Ascend to the next floor"""
        new_floor = self.floors.pop(0)
        generator_factory.change_floor(new_floor)
        self.current_floor = self.floor_generator.generate_one()
