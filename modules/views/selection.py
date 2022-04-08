import resource
from colorama import Fore
from typing import Any, List

from modules.models.items.inventory import Inventory

from modules.utils import resources
from modules.views.utils import display_actions


def display_selection(items: List, keys: List[str]) -> None:
    """Display a selection menu"""
    for index, item in enumerate(items):
        line = single_selection_format(index, item)
        print(line)

    display_actions(keys, resources['selection']['actions'])


def display_multi_selection(items: List, selection: List, keys: List[str]) -> None:
    """Display a selection menu"""
    for index, item in enumerate(items):
        line = multi_selection_format(index, item, selection)
        print(line)

    display_actions(keys, resources['selection']['actions'])


def inventory_single_selection_format(index: int, item: Any, inventory: Inventory) -> str:
    """Return the string used to select the given item"""
    line = single_selection_format(index, item).split(']')
    line.insert(1, f' [{Fore.RED}e{Fore.WHITE}' if inventory.item_is_equipped(item) else ' [ ')
    return ']'.join(line)


def inventory_multi_selection_format(index: int, item: Any, inventory: Inventory, selection: List[bool]) -> str:
    """Return the string used to select the given item"""
    line = multi_selection_format(index, item, selection).split(']')
    line.insert(1, f' [{Fore.RED}e{Fore.WHITE}' if inventory.item_is_equipped(item) else ' [ ')
    return ']'.join(line)


def multi_selection_format(index: int, item: Any, selection: List[bool]) -> str:
    """Return the string used to select the given item"""
    line = single_selection_format(index, item).split('[')
    line[0] = f'[{Fore.GREEN}*{Fore.WHITE}] ' if selection[index] else '[ ] '
    return '['.join(line)


def single_selection_format(index: int, item: Any) -> str:
    """Return the string used to select the given item"""
    return f'[{Fore.CYAN}{index}{Fore.WHITE}] {item}'
