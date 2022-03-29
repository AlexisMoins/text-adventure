from colorama import Fore

from modules.locations.room import Room
from modules.characters.character import Character

from modules.views.inventory_view import InventoryView
from modules.views.utils import selection_view

from modules.controllers.item_controller import ItemController

from modules.views.utils import Action, yes_no_menu


class InventoryController:
    """Class controlling the player's inventory"""

    def __init__(self, player: Character, room: Room) -> None:
        """Parameterised constructor creating a new controller over the player's inventory"""
        self.view = InventoryView(player)
        self.inventory = player.inventory
        self.room = room

    def run(self) -> None:
        """"""
        while True:
            self.view.display()
            self.view.display_commands()

            user_input = input('\n> ').lower()
            action = self._handle_input(user_input)
            if action == Action.QUIT:
                break

    def _handle_input(self, user_input: str) -> None:
        """Handle the input received by the controller"""
        if user_input == 'q':
            return Action.QUIT
        if user_input == 'l':
            selection_view.message = 'Select the item you want to take a look at:'
            selected_item = selection_view.choose_one(self.inventory.items)
            if selected_item:
                controller = ItemController(selected_item, self.inventory)
                controller.run()

        if user_input == 'w':
            selection_view.message = 'Select the equipment(s) you want to wear or handle:'
            selected_items = selection_view.choose_many(self.inventory.wearable_items())
            self.inventory.equip_many(selected_items)

        if user_input == 't':
            selection_view.message = 'Select the equipment(s) you want to take off:'
            selected_items = selection_view.choose_many(self.inventory.equipments.values())
            self.inventory.remove_many(selected_items)

        if user_input == 'd':
            selection_view.message = 'Select the item(s) you want to drop:'
            selected_items = selection_view.choose_many(self.inventory.items)
            if selected_items:
                for index, item in enumerate(selected_items):
                    if self.inventory.item_is_equipped(item):
                        if not yes_no_menu(f'{Fore.RED}Warning {index + 1}/{len(selected_items)}{Fore.WHITE}\n\nThis item is equipped: {str(item)}\nDo you want to drop it anyway ?'):
                            return Action.IDLE
                    self.room.items.append(self.view.inventory.drop_item(item))
