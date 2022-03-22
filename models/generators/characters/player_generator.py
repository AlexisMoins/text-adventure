from random import choice
from yaml import safe_load

from models.items.inventory import Inventory
from models.characters.character import Character

import models.factories.generator_factory as factory

"""Dictionnary containing the different classes available"""
with open('classes.yaml', 'r') as data:
    _classes = safe_load(data)


def generate_one() -> Character:
    """Generate a random character to act as the player"""
    key = choice(list(_classes))
    data = _classes[key]
    items = factory.generators['item'].generate_field(data.pop('inventory'))
    inventory = Inventory(items=items, gold=data.pop('gold'))
    return Character(**data, inventory=inventory)
