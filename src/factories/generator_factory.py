from typing import Callable

from src.generators.items.item_generator import ItemGenerator
from src.generators.locations.room_generator import RoomGenerator
from src.generators.locations.floor_generator import FloorGenerator
from src.generators.characters.character_generator import EnemyGenerator


# List of generators
generators: dict[str, Callable] = {}


# Default generators
default_generators = {
    'floor': FloorGenerator,
    'enemy': EnemyGenerator,
    'room': RoomGenerator,
    'item': ItemGenerator,
}


def set_dungeon_path(path: str) -> None:
    """Initialize the generators with the given dungeon path"""
    for key, generator in default_generators.items():
        register(key, generator(path))


def register(generator_type: str, generator) -> None:
    """Add an generator type and its corresponding class to the items dictionnary"""
    generators[generator_type] = generator


def change_floor(floor: str) -> None:
    """Tell all generators to load a new floor"""
    for generator in generators.values():
        generator.load_floor(floor)
