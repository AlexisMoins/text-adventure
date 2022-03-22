from typing import Dict, Any

from models.generators.items.item_generator import ItemGenerator
from models.generators.locations.room_generator import RoomGenerator
from models.generators.locations.floor_generator import FloorGenerator


"""List of generators"""
generators: Dict[str, Any] = dict()


def initialize(dungeon: str) -> None:
    """Initialize the generators with the given dungeon path"""
    _register('floor', FloorGenerator(dungeon))
    _register('enemy', ItemGenerator(dungeon))
    _register('room', RoomGenerator(dungeon))
    _register('item', ItemGenerator(dungeon))


def _register(generator_type: str, generator) -> None:
    """Add an generator type and its corresponding class to the items dictionnary"""
    generators[generator_type] = generator


def load_floor(floor: str) -> None:
    """Tell all generators to load a new floor"""
    for generator in generators.values():
        generator.load_floor(floor)
