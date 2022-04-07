from modules.factories import generators
from modules.controllers.engine import Engine

from modules.generators.locations import dungeon_generator
from modules.generators.characters import player_generator


if __name__ == '__main__':

    path = 'data/dungeon'
    generators.initialize(path)

    dungeon = dungeon_generator.generate(path)

    # TODO: resources = ResourcesLoader.load('resources/interfaces/room.yaml')

    player = player_generator.generate_one()

    engine = Engine(dungeon, player)

    engine.run()
