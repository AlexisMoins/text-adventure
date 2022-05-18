from src.factories import generator_factory as factory
from src.models.locations.coordinates import Direction
from src.models.locations.floor import Floor
from src.models.locations.room import Room


class Dungeon:
    """Model representing a dungeon with its list of floors"""

    def __init__(self, floors: list[str]) -> None:
        """Parameterised constructor creating a new dungeon"""
        self.floors: list[str] = floors
        self.floor_generator = factory.generators['floor']
        self.current_floor: Floor
        self.next_floor()

    @property
    def current_room(self) -> Room:
        """Return the current room"""
        return self.current_floor.current_room()

    def next_floor(self) -> None:
        """Ascend to the next floor"""
        new_floor = self.floors.pop(0)
        factory.change_floor(new_floor)
        self.current_floor = self.floor_generator.generate_one()

    def travel(self, direction: Direction) -> bool:
        """Travel to another room"""
        coordinates = self.current_room.coordinates.in_direction(direction)
        if coordinates in self.current_floor.rooms.keys():
            self.current_floor.player_position = coordinates
            self.current_room.visited = True
            return True
        return False
