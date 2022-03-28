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
