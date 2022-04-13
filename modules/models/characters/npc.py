from dataclasses import dataclass
from colorama import Fore

from modules.models.characters.character import Character
from modules.utils import indefinite_determiner


@dataclass(kw_only=True)
class NPC(Character):
    """Class representing a non playable character"""
    friendly: bool = True


@dataclass(kw_only=True)
class Enemy(NPC):
    """Class representing an enemy"""
    friendly: bool = False

    def __str__(self) -> str:
        """Return the string representation of the current enemy"""
        return f'{indefinite_determiner(self.name)} {Fore.RED}[!]{Fore.WHITE}'
