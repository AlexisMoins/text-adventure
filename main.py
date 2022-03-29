from modules.locations.dungeon import Dungeon

from modules.factories import generators
from modules.generators.locations import dungeon_generator
from modules.generators.characters import player_generator

from modules.controllers.room_controller import RoomController


class DungeonController:
    """Class representing a dungeon controller"""

    def __init__(self, dungeon: Dungeon) -> None:
        """Parameterised constructor creating a new controller of a dungeon"""
        self.dungeon = dungeon
        room = dungeon.current_room()
        self.room_controller = RoomController(room, dungeon.player)

    def run(self) -> bool:
        """Run the controller and start the game"""
        while True:
            next_floor = self.room_controller.run()
            if not next_floor:
                break


if __name__ == '__main__':

    path = 'resources/dungeon'
    generators.initialize(path)

    dungeon = dungeon_generator.generate(path)

    # TODO: resources = ResourcesLoader.load('resources/interfaces/room.yaml')

    player = player_generator.generate_one()

    dungeon.add_player(player)

    controller = DungeonController(dungeon)

    controller.run()
