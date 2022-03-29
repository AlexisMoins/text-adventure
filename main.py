from modules import utils
from modules.controllers.inventory_controller import InventoryController, ItemController
from modules.locations.room import Room
from modules.locations.dungeon import Dungeon
from modules.characters.character import Character

from modules.factories import generators
from modules.generators.locations import dungeon_generator
from modules.generators.characters import player_generator
from modules.views.selection_view import selection_view


class RoomController:
    """Class representing the view of a room"""

    def __init__(self, room: Room, player: Character) -> None:
        """Parameterised constructor creating a new view over a room"""
        self.inventory_controller = InventoryController(player, room)
        self.room = room
        self.player = player

    def run(self) -> None:
        """Run the controller and start the game"""
        while True:  # self.player.is_alive():
            utils.clear_screen()
            print(self.player.status_bar)
            self.room.display()

            user_input = input('\n> ').lower()
            if self._handle_input(user_input):
                return False

    def _handle_input(self, user_input: str) -> None:
        """Handle the input received by the controller"""
        if user_input == 'q':
            return True
        if user_input == 'i':
            self.inventory_controller.run()
        if user_input == 'l':
            selection_view.message = 'Select the equipment you want to take a look at:'
            selected_item = selection_view.choose_one(self.room.items)
            if selected_item:
                if ItemController(selected_item, self.player.inventory).run():
                    self.room.items.append(self.inventory.drop_one(self.view.dropped_item))
            # if user_input == 'c':
            #     accessible_rooms =
            #     next_room = choose_one(
            #         '\nWhere do you want to go ?', self.room)


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
