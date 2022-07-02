from dataclasses import dataclass

from colorama import Fore

from src.factory import register
from src.models.characters.character import Character


@register('npc')
@dataclass(kw_only=True)
class NPC(Character):
    """Class representing a non playable character"""
    friendly: bool = True


@register('enemy')
@dataclass(kw_only=True)
class Enemy(NPC):
    """Class representing an enemy"""
    friendly: bool = False

    def __str__(self) -> str:
        """Return the string representation of the current enemy"""
        return f'{self.name} {Fore.RED}[!]{Fore.WHITE}'
