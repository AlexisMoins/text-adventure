import os
import yaml

from typing import Any
from src.generators.abc import RandomGenerator
from src.models.items.items import Item

from src.models.characters.character import Character
from src.field import parse_inventory, parse_statistics


def get_content(*path: str) -> Any:
    """
    Return the content of the file at the given path.

    Argument:
    path -- a tuple of path components without separators

    Return value:
    A yaml object representing the content of the file
    """
    _path = os.path.join(*path)
    with open(_path, 'r') as data:
        return yaml.safe_load(data)


def get_player(item_generator: RandomGenerator[Item]) -> Character:
    """
    Create and return the Character representing the player.

    Return value:
    A character object
    """
    inventory = parse_inventory({'armor': 1, 'sword': 1}, item_generator)

    statistics = parse_statistics({
        'health': 10,
        'max-health': 10,

        'mana': 5,
        'max-mana': 5,

        'strength': 5,
        'resistance': 2,
        'intelligence': 3
    })

    return Character(inventory=inventory, statistics=statistics,
                     name='player', description='')
