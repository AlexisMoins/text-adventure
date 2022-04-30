from src.factories import generator_factory

from src.generators.characters import player_generator
from src.generators.locations.dungeon_generator import DungeonGenerator

from src.controllers.dungeon_controller import DungeonController

if __name__ == '__main__':

    path = 'data/dungeon'

    # Initialize the generator factory
    generator_factory.set_dungeon_path(path)

    dungeon = DungeonGenerator.generate(path)
    player = player_generator.generate_one()

    controller = DungeonController(dungeon, player)
    controller.run()
