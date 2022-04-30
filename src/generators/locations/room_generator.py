from abc import ABC, abstractmethod
from random import randint
from typing import Any

from src import utils
from src.models.locations.room import Room

from src.generators.field_generator import FieldGenerator
from src.generators.items.item_generator import ItemGenerator
from src.generators.characters.character_generator import EnemyGenerator


class Generator(ABC):
    """"""

    @abstractmethod
    def load_floor(self, floor: str) -> None:
        """"""
        pass


class RoomGenerator(Generator):
    """Class generating rooms based on the provided configuration files"""

    def __init__(self, dungeon_path: str) -> None:
        """Constructor creating a new generator of rooms"""
        self.dungeon = dungeon_path
        self.item_generator = ItemGenerator(dungeon_path)
        self.enemy_generator = EnemyGenerator(dungeon_path)

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the floor generator"""
        data = utils.load_resource(f'{self.dungeon}/{floor}/rooms.yaml')
        self.generation_table = data.pop('generation')
        self.rooms = data

        self.item_generator.load_floor(floor)
        self.enemy_generator.load_floor(floor)

    def total_weight(self) -> int:
        """Returns the total weight of the rooms in the generation table"""
        return sum(self.generation_table.values())

    def generate(self, room: str) -> Room | None:
        """Returns the given room after it has been generated"""
        if room not in self.rooms.keys():
            return None
        return self._deserialize_room(self._pop_room(room))

    def generate_one(self) -> Room | None:
        """Generates a random room"""
        number = randint(1, self.total_weight())
        for room, weight in self.generation_table.items():
            if number <= weight:
                return self.generate(room)
            number -= weight
        return None

    def generate_many(self, n: int) -> list[Room]:
        """Generates n random rooms"""
        number = min(len(self.generation_table), n)
        return [self.generate_one() for _ in range(number)]

    def _deserialize_room(self, data: dict[str, Any]) -> Room:
        """Returns the room deserialized from the given data"""
        room = Room(**data)
        room.items = FieldGenerator.generate(self.item_generator, room.items)
        room.enemies = FieldGenerator.generate(self.enemy_generator, room.enemies)
        return room

    def _pop_room(self, room) -> dict[str, Any]:
        """Returns the given room's data and remove it from the generator"""
        if room in self.generation_table:
            del self.generation_table[room]
        return self.rooms.pop(room)
