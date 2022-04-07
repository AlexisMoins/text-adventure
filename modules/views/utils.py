from enum import Enum
from typing import Any, List
from colorama import Fore

from modules import utils
from modules.models.items.inventory import Inventory


class Action(Enum):
    """Class representing the actions used in input handlers"""

    IDLE = 0
    QUIT = 1
    DROP = 2
    TAKE = 3
    INVENTORY = 4
    LOOK = 5


class SelectionView:
    """Class representing the general view for selecting items from a given list"""

    def __init__(self) -> None:
        """Parameterised constructor creating a new selection view"""
        self.message = ''
        self.quit_action = ('q', 'Cancel')
        self.validate_action = ('v', 'Validate selection')

    def _display(self, items: List) -> None:
        utils.clear_screen()
        print(f'{self.message}\n')

        for index, item in enumerate(items):
            print(f'[{Fore.CYAN}{index}{Fore.WHITE}] {item}')

        print(f'\n[{Fore.CYAN}{self.quit_action[0]}{Fore.WHITE}] {self.quit_action[1]}')

    def _display_selection(self, items: List, selection: List):
        """"""
        utils.clear_screen()
        print(f'{self.message}\n')

        for index, item in enumerate(items):
            indicator = f'{Fore.GREEN}*{Fore.WHITE}' if selection[index] else ' '
            print(f'[{indicator}] [{Fore.CYAN}{index}{Fore.WHITE}] {item}')

        print(f'\n[{Fore.CYAN}{self.quit_action[0]}{Fore.WHITE}] {self.quit_action[1]}')
        print(f'[{Fore.CYAN}{self.validate_action[0]}{Fore.WHITE}] {self.validate_action[1]}')

    def choose(self, items: List) -> List[Any]:
        """"""
        return self.choose_many(items) if len(items) > 1 else [self.choose_one(items)]


# General view for selecting one or many items from a list
selection_view = SelectionView()


def yes_no_menu(message: str) -> bool:
    while True:
        utils.clear_screen()
        print(f'{message}\n')

        print(f'[{Fore.CYAN}y{Fore.WHITE}] Yes')
        print(f'[{Fore.CYAN}n{Fore.WHITE}] No')

        user_input = input('\n> ').lower()
        if user_input == 'y':
            return True
        if user_input == 'n':
            return False


def message_without_input(message: str) -> None:
    """"""
    utils.clear_screen()
    print(f'{message}')
    input(f'Press any key to continue {Fore.CYAN}[.]{Fore.WHITE} ')