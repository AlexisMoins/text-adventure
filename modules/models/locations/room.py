from typing import Any, Dict, List
from textwrap import wrap
from dataclasses import dataclass, field
from colorama import Fore

from modules import utils
from modules.views.utils import Action


@dataclass(kw_only=True)
class Room:
    """Class representing a generic room"""
    description: str
    items: Any = field(default_factory=list)
    enemies: Any = field(default_factory=list)
    npc: Any = field(default_factory=list)
    actions: List[str] = field(default_factory=list, init=False)

    def is_empty(self) -> bool:
        """Return true if the room is empty, return false otherwise"""
        return len(self.entities) == 0

    @property
    def entities(self) -> List:
        """Return the list of all entities present in the room"""
        return self.items + self.enemies + self.npc

    def get_actions(self) -> Dict[str, Action]:
        """Return a map of the keys and their associated actions in the room"""
        actions = dict()
        actions['i'] = Action.INVENTORY

        if not self.is_empty():
            actions['l'] = Action.LOOK

        if self.items:
            actions['p'] = Action.TAKE

        actions['q'] = Action.QUIT
        return actions