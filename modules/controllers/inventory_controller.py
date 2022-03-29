from modules.locations.room import Room
from modules.characters.character import Character

from modules.views.inventory_view import InventoryView
from modules.views.selection_view import selection_view


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

            user_input = input('\n> ').lower()
            if self._handle_input(user_input):
                return False

    def _handle_input(self, user_input: str) -> None:
        """Handle the input received by the controller"""
        if user_input == 'q':
            return True
        if user_input == 'l':
            selection_view.message = 'Select the equipment you want to take a look at:'
            selected_item = selection_view.choose_one(self.inventory.items)
            if selected_item:
                selected_item.display()
        if user_input == 'w':
            selection_view.message = 'Select the equipment(s) you want to wear or handle:'
            selected_items = selection_view.choose_many(self.inventory.wearable_items())
            self.inventory.equip_many(selected_items)
        if user_input == 't':
            selection_view.message = 'Select the equipment(s) you want to take off:'
            selected_items = selection_view.choose_many(self.inventory.equipments.values())
            self.inventory.remove_many(selected_items)
