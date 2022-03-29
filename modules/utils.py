import os
from typing import Any
from yaml import safe_load


def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def load_resource(resource: str) -> Any:
    """Return the given resources once loaded and converted"""
    with open(resource, 'r') as data:
        return safe_load(data)


def definite_determiner(item_name: str) -> str:
    """"""
    vowels = 'aeiouy'
    determiner = 'the ' if item_name[0] in vowels else 'the '
    return determiner + item_name


def indefinite_determiner(item_name: str) -> str:
    """"""
    vowels = 'aeiouy'
    determiner = 'an ' if item_name[0] in vowels else 'a '
    return determiner + item_name
