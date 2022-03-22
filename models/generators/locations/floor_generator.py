from yaml import safe_load
from typing import Dict, List
from random import randint, choice

from models.locations.room import Room
from models.locations.floor import Floor
from models.locations.coordinates import Coordinates

import models.factories.generator_factory as factory


class FloorGenerator:
    """Class generating floors based on the provided configuration files"""

    def __init__(self, path: str) -> None:
        """Constructor creating a new generator of floors"""
        self.path = path
        self.rules: Dict = None

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the floor generator"""
        with open(f'{self.path}/{floor}/rules.yaml', 'r') as file:
            self.rules = safe_load(file)

    def generate_one(self) -> Floor:
        """Generates a new floor"""
        number = self.rules['room_number']
        if type(number) == list:
            number = randint(number[0], number[1])
        rooms = factory.generators['room'].generate_many(max(number, 1))
        layout = self.__create_layout(rooms)
        return Floor(self.path, layout)

    def __create_layout(self, rooms: List[Room]) -> Dict[Coordinates, Room]:
        """Return the map of the floor, comprised of coordinates and their associated room"""
        coordinates = [Coordinates(0, 0)]

        for i in range(len(rooms) - 1):
            neighbours = coordinates[i].neighbours()
            candidates = set(neighbours) - set(coordinates)
            coordinates.append(choice(list(candidates)))

        return dict(zip(coordinates, rooms))
