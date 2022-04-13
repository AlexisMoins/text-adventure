from colorama import Fore
from typing import Any, List
from modules.models.items.equipments import Equipment

from modules.utils import resources
from modules.views.utils import display_actions


def display_selection(items: List, keys: List[str], inventory: bool) -> None:
    """Display a selection menu"""
    print('')
    for index, item in enumerate(items):
        line = inventory_single_selection_format(index, item, isinstance(
            item, Equipment) and item.is_equipped) if inventory else single_selection_format(index, item)
        print(line)

    display_actions(keys, resources['selection']['actions'])


def display_multi_selection(items: List, selection: List, keys: List[str], inventory: bool) -> None:
    """Display a selection menu"""
    print('')
    for index, item in enumerate(items):
        line = inventory_multi_selection_format(index, item, selection, isinstance(
            item, Equipment) and item.is_equipped) if inventory else multi_selection_format(index, item, selection)
        print(line)

    display_actions(keys, resources['selection']['actions'])


def inventory_single_selection_format(index: int, item: Any, is_equipped: bool) -> str:
    """Return the string used to select the given item"""
    line = single_selection_format(index, item).split(']')
    line.insert(1, f' [{Fore.RED}e{Fore.WHITE}' if is_equipped else ' [ ')
    return ']'.join(line)


def inventory_multi_selection_format(index: int, item: Any, selection: List[bool], is_equipped: bool) -> str:
    """Return the string used to select the given item"""
    line = multi_selection_format(index, item, selection).split(']')
    line.insert(1, f' [{Fore.RED}e{Fore.WHITE}' if is_equipped else ' [ ')
    return ']'.join(line)


def multi_selection_format(index: int, item: Any, selection: List[bool]) -> str:
    """Return the string used to select the given item"""
    line = single_selection_format(index, item).split('[')
    line[0] = f'[{Fore.GREEN}*{Fore.WHITE}] ' if selection[index] else '[ ] '
    return '['.join(line)


def single_selection_format(index: int, item: Any) -> str:
    """Return the string used to select the given item"""
    return f'[{Fore.CYAN}{index}{Fore.WHITE}] {item}'
