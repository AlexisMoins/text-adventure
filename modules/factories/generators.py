from typing import Dict, Any

from modules.generators.items.item_generator import ItemGenerator
from modules.generators.locations.room_generator import RoomGenerator
from modules.generators.locations.floor_generator import FloorGenerator
from modules.generators.characters.character_generator import EnemyGenerator


# List of generators
generators: Dict[str, Any] = dict()


def get(generator: str):
    return generators[generator]


def initialize(path: str) -> None:
    """Initialize the generators with the given dungeon path"""
    dungeon = path

    register_generator('floor', FloorGenerator(path))
    register_generator('enemy', EnemyGenerator(path))
    register_generator('room', RoomGenerator(path))
    register_generator('item', ItemGenerator(path))


def register_generator(generator_type: str, generator) -> None:
    """Add an generator type and its corresponding class to the items dictionnary"""
    generators[generator_type] = generator


def load_floor(floor: str) -> None:
    """Tell all generators to load a new floor"""
    for generator in generators.values():
        generator.load_floor(floor)
