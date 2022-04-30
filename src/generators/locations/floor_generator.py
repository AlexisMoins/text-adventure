from random import randint, choice

from src import utils
from src.generators.locations.room_generator import RoomGenerator

from src.models.locations.room import Room
from src.models.locations.floor import Floor
from src.models.locations.coordinates import Coordinates


class FloorGenerator:
    """Class generating floors based on the provided configuration files"""

    def __init__(self, dungeon_path: str) -> None:
        """Constructor creating a new generator of floors"""
        self.room_generator = RoomGenerator(dungeon_path)
        self.dungeon = dungeon_path
        self.rules: dict = None

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

    def create_room_layout(self, rooms: list[Room]) -> dict[Coordinates, Room]:
        """Return the map of the floor, comprised of coordinates and their associated room"""
        layout: dict[Coordinates, Room] = dict()
        coordinates = Coordinates(0, 0)

        for room in rooms:
            layout[coordinates] = room
            room.coordinates = coordinates

            neighbours = coordinates.neighbours()
            candidates = set(neighbours.keys()) - set(layout.keys())
            coordinates = choice(list(candidates))

        for coordinates, room in layout.items():
            neighbours = coordinates.neighbours()
            for coord, direction in neighbours.items():
                if coord in layout.keys():
                    room.exits[direction] = coord

        return layout
