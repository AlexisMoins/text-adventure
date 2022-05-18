import importlib
from typing import Any

from src import dungeon, utils
from src.generators.locations import room_generator

from src.models.locations.room import Room
from src.models.locations.coordinates import Coordinates, Direction


# Mapping of the rules of the floor
rules: dict[str, Any] = dict()


def parse_floor(floor: str):
    """Load the given floor's rules and """
    global rules
    rules = utils.get_content(dungeon.PATH, floor, 'rules.yaml')

    generators = ('item_generator', 'characters.npc_generator',
                  'characters.enemy_generator', 'locations.room_generator')

    for generator in generators:
        module = importlib.import_module(f'src.generators.{generator}')
        module.parse_floor(floor)


def generate(floor: str) -> None:
    """Generate the given floor in the dungeon list of floors"""
    parse_floor(floor)
    number = rules['number-of-rooms']

    if type(number) == list:
        number = dungeon.RANDOM.randint(number[0], number[1])

    number = max(number, 1)
    dungeon.current_room = room_generator.generate(rules['first-room'])

    create_layout(dungeon.current_room, number - 1)


def create_layout(first_room: Room, number: int) -> None:
    """Return the map of the floor, comprised of coordinates and their associated room"""
    first_room.coordinates = Coordinates(0, 0)

    rooms: list[Room] = [first_room]
    occupied_coordinates = {first_room.coordinates}

    for i in range(number):
        room = room_generator.generate_one()
        previous_room = rooms[i]

        if room is None:
            break

        neighbours = previous_room.coordinates.neighbours()
        direction = dungeon.RANDOM.choice([direction for direction, coordinates in neighbours.items()
                                           if coordinates not in occupied_coordinates])

        previous_room.add_exit(direction, room)

        rooms.append(room)
        occupied_coordinates.add(room.coordinates)
