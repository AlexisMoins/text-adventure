from text_adventure.generators.floor_generator import FloorGenerator
from text_adventure.generators.item_generator import ItemGenerator
from text_adventure.generators.room_generator import RoomGenerator

if __name__ == "__main__":
    item_generator = ItemGenerator("dungeon/Sentient Valley")
    room_generator = RoomGenerator(item_generator)
    floor_generator = FloorGenerator(room_generator)

    floor = floor_generator.generate_one()
    for coord, room in floor.rooms.items():
        print(f'{coord.x}, {coord.y}: {room.description}\n')
