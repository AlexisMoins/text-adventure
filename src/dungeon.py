from typing import Deque
from collections import deque

from src.models.locations.room import Room
from src.models.characters.character import Character


# Path to the dungeon directory
PATH: str = 'dungeon'

# Score of the player
score = 0

# The number of moves performed by the player
moves = 0

# The current room
current_room: Room | None = None

PLAYER: Character | None = None
"""The playable character wandering through the dungeon"""

# Double linked-list of floor names
FLOORS: Deque[str] = deque()

# The current context of the dungeon and player
CONTEXT: set[str] = set()

# Wether the dungeon is running or not
is_running: bool = True
