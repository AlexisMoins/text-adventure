from typing import Any
from textwrap import wrap
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Room:
    """Class representing a generic room"""
    description: str
    items: Any = field(default_factory=list)
    enemies: Any = field(default_factory=list)
    npc: Any = field(default_factory=list)

    def __str__(self) -> str:
        """Return the string representation of the current room"""
        return '\n'.join(wrap(self.description))
