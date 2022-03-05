from text_adventure.generators.dungeon_generator import DungeonGenerator

if __name__ == '__main__':
    dungeon = DungeonGenerator.generate_one()
    print(dungeon.floors)
