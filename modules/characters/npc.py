from dataclasses import dataclass

from modules.characters.character import Character


@dataclass(kw_only=True)
class NPC(Character):
    """Class representing a non playable character"""
    is_friendly: bool = True


@dataclass(kw_only=True)
class Enemy(NPC):
    """Class representing an enemy"""
    is_friendly: bool = False
