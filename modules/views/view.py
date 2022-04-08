from colorama import Fore
from typing import Dict, List
from abc import ABC, abstractmethod

from modules.utils import load_resource


# All the resources used in the different views
resources = load_resource('data/views.yaml')


class View(ABC):
    """Class representing a generic view"""

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
