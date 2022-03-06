from modules.generators.locations.dungeon_generator import DungeonGenerator

if __name__ == '__main__':
    dungeon = DungeonGenerator.generate('dungeon')

    dungeon.start('test')
    for coordinates, room in dungeon.current_floor.rooms.items():
        print(f'({coordinates.x}, {coordinates.y}) {room}\n')
