from text_adventure.generators.item_generator import ItemGenerator
from text_adventure.generators.room_generator import RoomGenerator

if __name__ == "__main__":
    item_generator = ItemGenerator("dungeon/Sentient Valley")
    room_generator = RoomGenerator("dungeon/Sentient Valley", item_generator)

    room1 = room_generator.generate_one()
    print(room1)

    room2 = room_generator.generate_one()
    print(room2)

    rooms = room_generator.generate_many(2)
    print(rooms)

    room_generator = RoomGenerator("dungeon/Sentient Valley", item_generator)
    rooms = room_generator.generate_many(3)
    print(rooms)
