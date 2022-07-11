import random
from typing import Any

from src import utils

from src.generators.abc import RandomGenerator

from src.models.locations.room import Room
from src.models.locations.floor import Floor
from src.models.locations.coordinates import Coordinates


class FloorGenerator:
    """

    """

    def __init__(self, path: str, generators: dict[str, RandomGenerator]) -> None:
        """

        """
        self.rules: dict[str, Any] = dict()

        self.PATH = path
        self.generators = generators

    def _parse_floor(self, floor_name: str):
        """
        Parse a floor and load the files required by all generators. All
        generators must parse the new floors before starting to generate
        any entity.

        Argument:
        floor_name -- the name of the floor. The name must match the name
        of the floor directory containing all generation-related files.
        """
        self.rules = utils.get_content(self.PATH, floor_name, 'rules.yaml')

        for generator in self.generators.values():
            generator.parse_floor(floor_name)

    def generate(self, floor: str) -> Floor:
        """
        Generate the given floor in the dungeon list of floors
        """
        self._parse_floor(floor)
        number = self.rules['number-of-rooms']

        if type(number) == list:
            number = random.randint(number[0], number[1])

        number = max(number, 1)

        room_generator: RandomGenerator[Room] = self.generators['room']

        first_room = room_generator.generate(self.rules['first-room'])
        first_room.explored = True

        last_room = self._create_layout(first_room, number - 1, room_generator)

        return Floor(first_room, last_room)

    def _create_layout(self, first_room: Room, number: int, room_generator: RandomGenerator[Room]) -> Room:
        """
        Return the map of the floor, comprised of coordinates and their associated room
        """
        first_room.coordinates = Coordinates(0, 0)

        rooms: list[Room] = [first_room]
        occupied_coordinates = {first_room.coordinates}

        for i in range(number):
            room = room_generator._generate_one()
            previous_room = rooms[i]

            if room is None:
                break

            neighbours = previous_room.coordinates.neighbours()
            direction = random.choice([direction for direction, coordinates in neighbours.items()
                                       if coordinates not in occupied_coordinates])

            previous_room.add_exit(direction, room)

            rooms.append(room)
            occupied_coordinates.add(room.coordinates)

        return rooms[-1]
