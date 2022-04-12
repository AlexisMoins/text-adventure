from modules.factories import generator_factory

from modules.generators.characters import player_generator
from modules.generators.locations.dungeon_generator import DungeonGenerator

from modules.controllers.dungeon_controller import DungeonController


if __name__ == '__main__':

    path = 'data/dungeon'
    # Initialize the generator factory
    generator_factory.set_dungeon_path(path)

    dungeon = DungeonGenerator.generate(path)
    player = player_generator.generate_one()

    controller = DungeonController(dungeon, player)
    controller.run()
