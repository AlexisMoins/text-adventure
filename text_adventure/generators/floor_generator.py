from typing import Dict
from yaml import safe_load
from random import randint, choice

from text_adventure.locations.room import Room
from text_adventure.locations.floor import Floor
from text_adventure.locations.coordinates import Coordinates
from text_adventure.generators.room_generator import RoomGenerator


class FloorGenerator:
    """Class generating floors based on the provided configuration files"""

    def __init__(self, room_generator: RoomGenerator) -> None:
        """Constructor creating a new generator of floors"""
        self.room_generator = room_generator
        self.load_floor(room_generator.floor_path, cascade=False)

    def load_floor(self, path: str, cascade=True) -> None:
        """Loads a new floor into the floor generator"""
        self.floor_path = path
        if cascade:
            self.room_generator.load_floor(path)
        with open(f'{path}/rules.yaml', 'r') as file:
            self.rules = safe_load(file)

    def generate_one(self) -> Floor:
        """Generates a new floor"""
        number = self.rules['room_number']
        if type(number) == list:
            number = randint(number[0], number[1])
        rooms = self.__create_layout(number)
        return Floor(rooms)

    def __create_layout(self, n: int) -> Dict[Coordinates, Room]:
        """"""
        rooms = self.room_generator.generate_many(n)
        coordinates = [Coordinates(0, 0)]

        for i in range(len(rooms) - 1):
            neighbours = coordinates[i].neighbours()
            candidates = set(neighbours) - set(coordinates)
            coordinates.append(choice(list(candidates)))

        return dict(zip(coordinates, rooms))
