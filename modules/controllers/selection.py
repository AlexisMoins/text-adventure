from typing import Any, List
from modules.models.items.inventory import Inventory

from modules.views.utils import display_message
from modules.views.selection import display_multi_selection, display_selection, inventory_single_selection_format


def choose_one(message: str, items: List, inventory: Inventory = None) -> Any:
    """"""
    keys = ['q', 'v']
    while True:
        display_message(message)
        display_selection(items, ['q'], inventory)

        user_input = input('\n> ').lower()
        if user_input == keys[0]:
            return None

        if (is_integer(user_input)):
            index = int(user_input)
            if items and 0 <= index < len(items):
                return items[index]


def choose_many(message: str, items: List, inventory: Inventory = None) -> List[Any]:
    """Return a list of items chosen from the given list"""
    keys = ['q', 'v']
    selection = [False for _ in items]

    while True:
        display_message(message)
        display_multi_selection(items, selection, keys, inventory)

        user_input = input('\n> ').lower()
        if user_input == keys[0]:
            return []

        if user_input == keys[1]:
            return [item for item, selected in zip(items, selection) if selected]

        if (is_integer(user_input)):
            index = int(user_input)
            if items and 0 <= index < len(items):
                selection[index] = not selection[index]


def is_integer(string: str) -> bool:
    """Return true if the given string is an integer, return false otherwise"""
    try:
        int(string)
        return True
    except ValueError:
        return False
