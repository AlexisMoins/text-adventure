from yaml import safe_load
from random import randint
from typing import Dict, List, Any

from text_adventure.locations.room import Room
from text_adventure.generators.item_generator import ItemGenerator


class RoomGenerator:
    """Class generating rooms based on the provided configuration files"""

    def __init__(self, floor_path: str, item_generator: ItemGenerator) -> None:
        """Constructor creating a new generator of rooms"""
        with open(f"{floor_path}/rooms.yaml", "r") as file:
            data = safe_load(file)

        self.generation_table = data.pop("generation")
        self.total_weight = self.total_weight()
        self.item_generator = item_generator
        self.rooms = data

    def total_weight(self) -> int:
        """Returns the total weight of the rooms in the generation table"""
        return sum(self.generation_table.values())

    def generate_one(self) -> Room | None:
        """Generates a random room"""
        if not self.rooms:
            return None

        number = min(self.total_weight, randint(1, self.total_weight))
        for room, weight in self.generation_table.items():
            if number <= weight:
                return self.__deserialize_room(self.rooms.pop(room))
            number -= weight

    def __deserialize_room(self, data: Dict) -> Room:
        """Returns the room deserialized from the given data"""
        room = Room(**data)
        room.items = self.__generate_items(room.items, self.item_generator)
        # room.enemies = self.generate(room.enemies, self.enemy_generator)
        # room.npc = self.generate(room.npc, self.npc_generator)
        return room

    def __generate_items(self, data: Any, generator) -> List[Room]:
        """Returns a list of the data deserialized using the given generator"""
        if type(data) == int:
            number = data
        elif type(data) == list:
            if len(data) > 1:
                number = randint(data[0], data[1])
            elif not data:
                return data
        return [generator.generate_one() for i in range(number)]

    def generate_many(self, n: int) -> List[Room]:
        """Generates n random rooms"""
        return [self.generate_one() for i in range(min(len(self.rooms), n))]
