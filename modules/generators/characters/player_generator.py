from random import choice
from yaml import safe_load

from modules.models.items.inventory import Inventory
from modules.models.characters.character import Character

import modules.factories.generator_factory as factory
from modules.generators.field_generator import generate_field


"""Dictionnary containing the different classes available"""
with open('data/classes.yaml', 'r') as data:
    _classes = safe_load(data)


def generate_one() -> Character:
    """Generate a random character to act as the player"""
    key = choice(list(_classes))
    data = _classes[key]
    items = generate_field(factory.generators['item'], data.pop('inventory'))
    inventory = Inventory(items=items, gold=data.pop('gold'))
    return Character(**data, inventory=inventory)
