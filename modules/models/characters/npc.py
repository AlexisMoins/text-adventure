from dataclasses import dataclass
from colorama import Fore

from modules.models.characters.character import Character


@dataclass(kw_only=True)
class NPC(Character):
    """Class representing a non playable character"""
    friendly: bool = True


@dataclass(kw_only=True)
class Enemy(NPC):
    """Class representing an enemy"""
    friendly: bool = False

    def __str__(self) -> str:
        """"""
        indicator = '[~]' if self.friendly else '[!]'
        return f'{self.name} {Fore.RED}{indicator}{Fore.WHITE}'
