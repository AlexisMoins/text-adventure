from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, OrderedDict

from modules.models.items.items import Item
from modules.models.locations.coordinates import Coordinates, Direction

from modules.controllers.actions import Action


@dataclass(kw_only=True)
class Room:
    """Class representing a generic room"""
    description: str
    items: Any = field(default_factory=list)
    enemies: Any = field(default_factory=list)
    npc: Any = field(default_factory=list)
    actions: List[str] = field(default_factory=list, init=False)

    visited: bool = field(init=False, default=False)
    coordinates: Coordinates = field(init=False, default=None)
    exits: Dict[Direction, Coordinates] = field(default_factory=dict, init=False)

    def is_empty(self) -> bool:
        """Return true if the room is empty, return false otherwise"""
        return len(self.entities) == 0

    @property
    def entities(self) -> List:
        """Return the list of all entities present in the room"""
        return self.items + self.enemies + self.npc

    def remove(self, item: Item) -> Item:
        """Remove the given item from the current room"""
        return self.items.pop(self.items.index(item))

    def add(self, item: Item) -> None:
        """Add the given item to the current room"""
        self.items.append(item)

    def get_actions(self) -> Dict[str, Action]:
        """Return a map of the keys and their associated actions in the room"""
        actions = OrderedDict()
        actions['i'] = Action.INVENTORY
        actions['c'] = Action.TRAVEL

        if not self.is_empty():
            actions['l'] = Action.LOOK

        if self.items:
            actions['p'] = Action.TAKE

        actions['q'] = Action.QUIT
        return actions

    def __str__(self) -> str:
        """Return the string representation of the room"""
        return f'{self.coordinates}'
