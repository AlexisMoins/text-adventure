from colorama import Fore

from modules import utils
from modules.locations.room import Room
from modules.characters.character import Character

from modules.controllers.item_controller import ItemController
from modules.controllers.inventory_controller import InventoryController

from modules.views.utils import Action, message_without_input, selection_view


class RoomController:
    """Class representing the view of a room"""

    def __init__(self, room: Room, player: Character) -> None:
        """Parameterised constructor creating a new view over a room"""
        self.inventory_controller = InventoryController(player, room)
        self.room = room
        self.player = player

    def run(self) -> None:
        """Run the controller and start the game"""
        while True:
            utils.clear_screen()
            print(self.player.status_bar)
            self.room.display()

            user_input = input('\n> ').lower()
            action = self._handle_input(user_input)
            if action == Action.QUIT:
                break

    def _handle_input(self, user_input: str) -> None:
        """Handle the input received by the controller"""
        if user_input == 'q':
            return Action.QUIT
        if user_input == 'i':
            self.inventory_controller.run()
        if user_input == 'l':
            selection_view.message = 'Select the item you want to take a look at:'
            selected_item = selection_view.choose_one(self.room.items)
            if selected_item:
                controller = ItemController(selected_item, self.player.inventory)
                action = controller.run()
                if action == Action.TAKE:
                    if self.player.inventory.is_full():
                        message_without_input(
                            f'{Fore.RED}Warning 1/1{Fore.WHITE}\n\nYour inventory is full')
                        return Action.IDLE
                    self.player.inventory.items.append(self.room.items.pop(self.room.items.index(selected_item)))
