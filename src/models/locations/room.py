from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

from src.models.items.items import Item
from src.models.locations.coordinates import Coordinates, Direction


@dataclass(kw_only=True)
class Room:
    """Class representing a generic room"""
    description: str
    items: Any = field(default_factory=list)
    enemies: Any = field(default_factory=list)
    npc: Any = field(default_factory=list)
    actions: list[str] = field(default_factory=list, init=False)

    visited: bool = field(init=False, default=False)
    coordinates: Coordinates = field(init=False, default=None)
    exits: dict[Direction, Coordinates] = field(default_factory=dict, init=False)

    def is_empty(self) -> bool:
        """Return true if the room is empty, return false otherwise"""
        return len(self.entities) == 0

    @property
    def entities(self) -> list:
        """Return the list of all entities present in the room"""
        return self.items + self.enemies + self.npc

    def remove(self, item: Item) -> Item:
        """Remove the given item from the current room"""
        return self.items.pop(self.items.index(item))

    def add(self, item: Item) -> None:
        """Add the given item to the current room"""
        self.items.append(item)

    def find_items(self, pattern: str) -> list[Item]:
        """Return the list of items corresponding to the given pattern"""
        items = filter(lambda item: pattern in item.name, self.items)
        return list(items)

    def find_entities(self, pattern: str) -> list[Any]:
        """Return the list of items whose name matches the given pattern"""
        iterator = filter(lambda entity: pattern in entity.name, self.entities)
        return list(iterator)

    def __str__(self) -> str:
        """Return the string representation of the room"""
        return f'{self.coordinates}'
