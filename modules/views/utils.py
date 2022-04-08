import os
from enum import Enum, auto
from colorama import Fore
from typing import Dict, List

from modules.utils import resources


class Action(Enum):
    """Class representing the actions used in input handlers"""

    LOOK = auto()
    IDLE = auto()
    QUIT = auto()
    DROP = auto()
    WEAR = auto()
    TAKE = auto()
    TAKE_OFF = auto()
    INVENTORY = auto()
    STATISTICS = auto()


def ask(message: str) -> bool:
    """Return true if the user chooses yes, return false otherwise"""
    keys = ['y', 'n']
    while True:
        display_message(message)
        display_actions(keys, resources['utils']['actions'])

        user_input = input('\n> ').lower()
        if user_input == keys[0]:
            return True

        if user_input == keys[1]:
            return False


def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_message(message: str, wait: bool = False, warning: bool = False) -> None:
    """Display the given message on screen, optionaly waiting for an input"""
    clear_screen()
    if warning:
        print(f'{Fore.RED}Warning{Fore.WHITE}\n')
    print(f'{message}\n')

    if wait:
        input(f'Press any key to continue {Fore.CYAN}[.]{Fore.WHITE} ')


def display_actions(keys: List[str], actions: Dict[str, str]) -> None:
    """Display the possible actions available in the current context"""
    print('')
    for key in keys:
        if key in actions:
            print(f'[{Fore.CYAN}{key}{Fore.WHITE}] {actions[key]}')
