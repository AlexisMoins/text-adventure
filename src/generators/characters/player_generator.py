from random import choice
from yaml import safe_load

from src.models.items.inventory import Inventory
from src.models.characters.character import Character

import src.factories.generator_factory as factory
from src.generators.field_generator import FieldGenerator


"""Dictionnary containing the different classes available"""
with open('data/classes.yaml', 'r') as data:
    _classes = safe_load(data)


def generate_one() -> Character:
    """Generate a random character to act as the player"""
    key = choice(list(_classes))
    data = _classes[key]
    items = FieldGenerator.generate(factory.generators['item'], data.pop('inventory'))
    inventory = Inventory(items=items, gold=data.pop('gold'))
    return Character(**data, inventory=inventory)
