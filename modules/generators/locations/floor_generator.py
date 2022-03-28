from yaml import safe_load
from typing import Dict, List
from random import randint, choice
from modules import utils

from modules.locations.room import Room
from modules.locations.floor import Floor
from modules.locations.coordinates import Coordinates

import modules.factories.generators as factory


class FloorGenerator:
    """Class generating floors based on the provided configuration files"""

    def __init__(self, path: str) -> None:
        """Constructor creating a new generator of floors"""
        self.path = path
        self.rules: Dict = None

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the floor generator"""
        self.rules = utils.load_resource(f'{self.path}/{floor}/rules.yaml')

    def generate_one(self) -> Floor:
        """Generates a new floor"""
        number = self.rules['room_number']
        if type(number) == list:
            number = randint(number[0], number[1])
        rooms = factory.generators['room'].generate_many(max(number, 1))
        layout = self._create_layout(rooms)
        return Floor(self.path, layout)

    def _create_layout(self, rooms: List[Room]) -> Dict[Coordinates, Room]:
        """Return the map of the floor, comprised of coordinates and their associated room"""
        coordinates = [Coordinates(0, 0)]

        for i in range(len(rooms) - 1):
            neighbours = coordinates[i].neighbours()
            candidates = set(neighbours) - set(coordinates)
            coordinates.append(choice(list(candidates)))

        return dict(zip(coordinates, rooms))
