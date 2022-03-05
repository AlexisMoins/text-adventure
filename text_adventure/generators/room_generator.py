from yaml import safe_load
from random import randint
from typing import Dict, List, Any

from text_adventure.items.items import Item
from text_adventure.locations.room import Room
from text_adventure.generators.item_generator import ItemGenerator


class RoomGenerator:
    """Class generating rooms based on the provided configuration files"""

    def __init__(self, item_generator: ItemGenerator) -> None:
        """Constructor creating a new generator of rooms"""
        self.item_generator = item_generator
        self.floor_path = self.item_generator.floor_path
        with open(f'{self.floor_path}/rooms.yaml', 'r') as file:
            data = safe_load(file)

        self.generation_table = data.pop('generation')
        self.rooms = data

    def total_weight(self) -> int:
        """Returns the total weight of the rooms in the generation table"""
        return sum(self.generation_table.values())

    def generate_one(self) -> Room | None:
        """Generates a random room"""
        if not self.rooms or not self.generation_table:
            return None

        number = randint(1, self.total_weight())
        for room, weight in self.generation_table.items():
            if number <= weight:
                print(f"Rolled a {number}")
                print(f"Found {room} with weight {weight}\n")
                return self.__deserialize_room(self.__pop_room(room))
            number -= weight

    def __deserialize_room(self, data: Dict[str, Any]) -> Room:
        """Returns the room deserialized from the given data"""
        room = Room(**data)
        room.items = self.__generate_field(room.items, self.item_generator)
        # room.enemies = self.__generate_field(room.enemies, self.enemy_generator)
        # room.npc = self.__generate_field(room.npc, self.npc_generator)
        return room

    def __generate_field(self, data: Any, generator) -> List[Item]:
        """Returns a list of the data deserialized using the given generator"""
        if not data:
            return []
        if type(data) == int:
            return generator.generate_many(data)
        if type(data) == list:
            if type(data[0]) == int:
                return generator.generate_many(randint(data[0], data[1]))
            if type(data[0]) == str:
                return [generator.generate(item) for item in data]

    def generate_many(self, n: int) -> List[Room]:
        """Generates n random rooms"""
        return [self.generate_one() for i in range(min(len(self.rooms), n))]

    def generate(self, room: str) -> Room | None:
        """Returns the given room after it has been generated"""
        if room not in self.rooms.keys():
            return None
        return self.__deserialize_room(self.__pop_room(room))

    def __pop_room(self, room) -> Dict[str, Any]:
        """Returns the given room's data and remove it from the generator"""
        if room in self.generation_table:
            del self.generation_table[room]
        return self.rooms.pop(room)
