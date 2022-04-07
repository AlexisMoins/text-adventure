from random import randint
from typing import Dict, List, Any

from modules import utils
from modules.generators.field_generator import generate_field
from modules.models.locations.room import Room
import modules.factories.generators as factory


class RoomGenerator:
    """Class generating rooms based on the provided configuration files"""

    def __init__(self, path: str) -> None:
        """Constructor creating a new generator of rooms"""
        self.path = path

    def load_floor(self, floor: str) -> None:
        """Loads a floor into the floor generator"""
        data = utils.load_resource('{0}/{1}/rooms.yaml'.format(self.path, floor))
        self.generation_table = data.pop('generation')
        self.rooms = data

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

    def generate_many(self, n: int) -> List[Room]:
        """Generates n random rooms"""
        number = min(len(self.generation_table), n)
        return [self.generate_one() for _ in range(number)]

    def _deserialize_room(self, data: Dict[str, Any]) -> Room:
        """Returns the room deserialized from the given data"""
        room = Room(**data)
        room.items = generate_field(factory.generators['item'], room.items)
        room.enemies = generate_field(factory.generators['enemy'], room.enemies)
        return room

    def _pop_room(self, room) -> Dict[str, Any]:
        """Returns the given room's data and remove it from the generator"""
        if room in self.generation_table:
            del self.generation_table[room]
        return self.rooms.pop(room)
