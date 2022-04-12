from colorama import Fore
from typing import Dict, List
from abc import ABC, abstractmethod
from modules.controllers.selection import is_integer

from modules.utils import load_resource


# All the resources used in the different views
resources = load_resource('data/views.yaml')


class View(ABC):
    """Class representing a generic view"""
    resources = load_resource('data/views.yaml')

    @abstractmethod
    def display(self) -> None:
        """Display the current view"""
        pass

    def display_actions(self, keys: List[str], actions: Dict[str, str]) -> None:
        """Display the possible actions available in the current context"""
        print('')
        for key in keys:
            if key in actions:
                print(f'[{Fore.CYAN}{key}{Fore.WHITE}] {actions[key]}')

    @staticmethod
    def get_bar(value: int, maximum: int, color, character: str) -> str:
        """Return a status bar with the given values, color and character to fill the bar"""
        percentage = round(value / maximum * 10)
        bar = f'[{color}{character * percentage}{Fore.WHITE}{" " * (10 - percentage)}]'
        return f'{bar} {color}{value}{Fore.WHITE} ({color}{maximum}{Fore.WHITE})'
