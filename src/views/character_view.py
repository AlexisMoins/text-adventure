from colorama import Fore

from src.views.view import View
from src.models.characters.character import Character


class CharacterView(View):
    """Class representing the view of a character"""

    def __init__(self, character: Character) -> None:
        """Parameterised constructor creating a new character view"""
        self.character = character

    def display(self) -> None:
        """Display the current character"""
        pass

    @property
    def status_bar(self) -> str:
        """Return the status bars of the current character"""
        return f'health {self.health_bar}    mana: {self.mana_bar}'

    @property
    def health_bar(self) -> str:
        """Return the health bar of the current character"""
        value = self.character.get_statistic('health')
        maximum = self.character.get_statistic('max_health')
        return self.get_bar(value, maximum, Fore.RED, '=')

    @property
    def mana_bar(self) -> str:
        """Return the mana bar of the current character"""
        value = self.character.get_statistic('mana')
        maximum = self.character.get_statistic('max_mana')
        return self.get_bar(value, maximum, Fore.GREEN, '=')
