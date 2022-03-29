from enum import Enum

from modules.items.items import Item
from modules.items.inventory import Inventory

from modules.views.utils import Action, yes_no_menu
from modules.views.item_view import ItemView


class ItemController:
    """Class controlling the actions performed in an item view"""

    def __init__(self, item: Item, inventory: Inventory) -> None:
        """Parameterised constructor creating a new item controller"""
        self.view = ItemView(item, inventory)
        self.dropped_item = None

    def run(self) -> Action:
        """Run the current controller"""
        while True:
            self.view.display()
            self.view.display_commands()

            user_input = input('\n> ').lower()
            action = self._handle_input(user_input)
            if action != Action.IDLE:
                return action

    def _handle_input(self, user_input: str) -> Action:
        """Handle the input received by the controller"""
        if user_input == 'q':
            return Action.QUIT
        if user_input == 't':
            self.view.inventory.remove_one(self.view.item)
        if user_input == 'w':
            self.view.inventory.equip_one(self.view.item)
        if user_input == 'd':
            if self.view.inventory.item_is_equipped(self.view.item):
                if not yes_no_menu('This item is equipped. Do you want to drop it anyway ?'):
                    return Action.IDLE
            self.dropped_item = self.view.inventory.drop_item(self.view.item)
            return Action.DROP
        return Action.IDLE
