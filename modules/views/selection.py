from typing import List

from modules import utils

actions = utils.load_resource('data/views.yaml')['selection']['actions']


def display_selection(items: List, actions: List[str]) -> None:
    """Display a selection menu"""
    for index, item in enumerate(items):
        line = multi_selection_format(index, item)
        print(line)


def display_selection(items: List, selection: List, actions: List[str]) -> None:
    """Display a selection menu"""
    for index, item in enumerate(items):
        line = multi_selection_format(index, item, selection)
        print(line)

    print(f'\n[{Fore.CYAN}{self.quit_action[0]}{Fore.WHITE}] {self.quit_action[1]}')
    print(f'[{Fore.CYAN}{self.validate_action[0]}{Fore.WHITE}] {self.validate_action[1]}')
