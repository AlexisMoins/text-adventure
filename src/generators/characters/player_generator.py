from typing import Any

from src import dungeon, factory, utils
from src.generators import item_generator
from src.models.characters.character import Character


# Dictionnary containing the different classes available
classes: dict[str, Any] = utils.get_content('resources', 'classes.yaml')


def generate_player() -> Character:
    """Generate a random character to act as the player"""
    key = dungeon.RANDOM.choice(list(classes.keys()))
    character = classes[key]

    character['statistics'] = utils.parse_statistics(character['statistics'])
    character['inventory'] = item_generator.parse_inventory(character['inventory'])
    character['type'] = 'character'

    return factory.create(character)
