from typing import Dict, List
from random import randint, choice

from modules import utils
from modules.generators.locations.room_generator import RoomGenerator

from modules.models.locations.room import Room
from modules.models.locations.floor import Floor
from modules.models.locations.coordinates import Coordinates


class FloorGenerator:
    """Class generating floors based on the provided configuration files"""

    def __init__(self, dungeon_path: str) -> None:
        """Constructor creating a new generator of floors"""
        self.room_generator = RoomGenerator(dungeon_path)
        self.dungeon = dungeon_path
        self.rules: Dict = None

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the floor generator"""
        self.rules = utils.load_resource(f'{self.dungeon}/{floor}/rules.yaml')
        self.room_generator.load_floor(floor)

    def generate_one(self) -> Floor:
        """Generates a new floor"""
        number = self.rules['room_number']
        if type(number) == list:
            number = randint(number[0], number[1])

        rooms = self.room_generator.generate_many(max(number, 1))
        return Floor(self.dungeon, self.create_room_layout(rooms))

    def create_room_layout(self, rooms: List[Room]) -> Dict[Coordinates, Room]:
        """Return the map of the floor, comprised of coordinates and their associated room"""
        layout = dict()
        coordinates = Coordinates(0, 0)

        for room in rooms:
            layout[coordinates] = room
            room.coordinates = coordinates

            neighbours = coordinates.neighbours()
            candidates = set(neighbours) - set(layout.keys())
            coordinates = choice(list(candidates))

        return layout
