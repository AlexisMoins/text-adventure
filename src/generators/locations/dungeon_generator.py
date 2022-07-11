import random
from typing import Any

from src import utils

from src.generators.abc import RandomGenerator

from src.generators.item_generator import ItemGenerator
from src.generators.locations.room_generator import RoomGenerator
from src.generators.locations.floor_generator import FloorGenerator
from src.generators.characters.enemy_generator import CharacterGenerator

from src.models.locations.dungeon import Dungeon


def generate_dungeon(path: str = 'dungeon') -> Dungeon:
    """
    Create a new dungeon using yaml generation files.

    Argument:
    path -- the path to the dungeon directory containing all
    the floors' generation files

    Return value:
    A new dungeon object
    """
    data = utils.get_content(path, 'floors.yaml')
    generators = get_generators(path)

    floor_generator = FloorGenerator(path, generators)

    floors = [floor_generator.generate(floor) for floor in get_floor_list(data)]
    player = utils.get_player(generators['item'])

    return Dungeon(floors, player, generators)


def get_generators(path: str) -> dict[str, RandomGenerator]:
    """
    Return the generators used to create the dungeon.

    Argument:
    path -- the path to the dungeon directory

    Return value:
    A dictionary of generators and their name
    """
    generators = dict()

    item_generator = ItemGenerator(path)
    generators['item'] = item_generator

    character_generator = CharacterGenerator(path, generators, file='enemies.yaml', field='enemies')
    generators['enemy'] = character_generator

    npc_generator = CharacterGenerator(path, generators, file='npc.yaml', field='npc')
    generators['npc'] = npc_generator

    room_generator = RoomGenerator(path, generators)
    generators['room'] = room_generator

    return generators


def get_floor_list(data: dict[str, Any]) -> list[str]:
    """
    Return a list of (almost) randomly generated floor name.

    Argument:
    data -- a field like

    Return value:
    A list of floor names
    """
    return [choose_one(floor) if type(floor) is dict else floor for floor in data]


def choose_one(selection: dict[str, int]) -> str:
    """
    Returns a floor name randomly choosen from a dictionary of floor
    names and their weight.

    Argument:
    selection -- a dictionary of floor names and their weight

    Return value:
    A floor name
    """
    population = selection.keys()
    weights = selection.values()

    choice = random.choices(tuple(population), tuple(weights))
    return choice[0]
