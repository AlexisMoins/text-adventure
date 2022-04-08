from modules.factories import generator_factory

from modules.generators.locations import dungeon_generator
from modules.generators.characters import player_generator

from modules.controllers.dungeon_controller import DungeonController


if __name__ == '__main__':
    # Initialize the generator factory
    generator_factory.set_dungeon_path('data/dungeon')

    dungeon_generator = generator_factory.get('dungeon')
    dungeon = dungeon_generator.generate()

    player = player_generator.generate_one()

    controller = DungeonController(dungeon, player)
    controller.run()
