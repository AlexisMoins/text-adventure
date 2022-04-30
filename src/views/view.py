from colorama import Fore
from abc import ABC, abstractmethod
from src.controllers.selection import is_integer

from src.utils import load_resource


class View(ABC):

    @abstractmethod
    def display(self) -> None:
        """Display the current view"""
        pass

    @staticmethod
    def get_bar(value: int, maximum: int, color, character: str) -> str:
        """Return a status bar with the given values, color and character to fill the bar"""
        percentage = round(value / maximum * 10)
        bar = f'[{color}{character * percentage}{Fore.WHITE}{" " * (10 - percentage)}]'
        return f'{bar} {color}{value}{Fore.WHITE} ({color}{maximum}{Fore.WHITE})'
