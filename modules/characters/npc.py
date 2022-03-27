from dataclasses import dataclass

from modules.characters.character import Character


@dataclass(kw_only=True)
class NPC(Character):
    """Class representing a non playable character"""
    is_friendly: bool = True

    def __post_init__(self) -> None:
        """Additional steps to initialize the instance"""
        for item in self.inventory.filter('equip'):
            self.equip_item(item)


@dataclass(kw_only=True)
class Enemy(NPC):
    """Class representing an enemy"""
    is_friendly: bool = False
