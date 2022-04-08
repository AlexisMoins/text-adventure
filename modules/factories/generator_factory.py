from typing import Dict, Any

from modules.generators.items.item_generator import ItemGenerator
from modules.generators.locations.room_generator import RoomGenerator
from modules.generators.locations.floor_generator import FloorGenerator
from modules.generators.characters.character_generator import EnemyGenerator


# List of generators
generators: Dict[str, Any] = dict()


def get(generator: str) -> Any:
    """"""
    return generators[generator] if generator in generators else None


def set_dungeon_path(path: str) -> None:
    """Initialize the generators with the given dungeon path"""
    for generator in generators.values():
        generator.path = path


def register(generator_type: str, generator) -> None:
    """Add an generator type and its corresponding class to the items dictionnary"""
    generators[generator_type] = generator()


def load_floor(floor: str) -> None:
    """Tell all generators to load a new floor"""
    for generator in generators.values():
        generator.load_floor(floor)


register('floor', FloorGenerator)
register('enemy', EnemyGenerator)
register('room', RoomGenerator)
register('item', ItemGenerator)
