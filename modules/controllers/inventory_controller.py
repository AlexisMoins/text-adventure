from modules.controllers.selection import choose_many, choose_one
from modules.models.characters.character import Character

from modules.views.inventory_view import display_inventory
from modules.views.utils import clear_screen

from modules.controllers.actions import Action

from modules.controllers.item_controller import ItemController
from modules.utils import resources


class InventoryController:
    """Class controlling the player's inventory"""

    def __init__(self, player: Character, item_controller: ItemController) -> None:
        """Parameterised constructor creating a new controller over the player's inventory"""
        self.item_controller = item_controller
        self.dungeon = item_controller.dungeon
        self.inventory = player.inventory
        self.player = player

    def run(self) -> None:
        """Run the controller"""
        self.is_running = True
        while self.is_running:
            clear_screen()
            actions = self.inventory.get_actions()

            display_inventory(self.inventory, actions.keys())

            actions['2'] = Action.STATISTICS
            user_input = input('\n> ').lower()
            if user_input not in actions:
                continue

            self.handle_action(actions[user_input])

    def handle_action(self, action: Action) -> None:
        """Handle the action received by the engine"""
        if action == Action.QUIT:
            self.is_running = False

        if action == Action.LOOK:
            message = resources['selection']['interface']['look'].format('the item')
            if item := choose_one(message, self.inventory.items, self.inventory):
                self.item_controller.run(item)

        if action == Action.DROP:
            message = resources['selection']['interface']['drop']
            for item in choose_many(message, self.inventory.items, self.inventory):
                self.player.drop(item, self.dungeon.current_room)

        if action == Action.TAKE_OFF:
            message = resources['selection']['interface']['take_off']
            for item in choose_many(message, self.inventory.equipments.values()):
                self.inventory.take_off(item)

        if action == Action.WEAR:
            message = resources['selection']['interface']['wear']
            for item in choose_many(message, self.inventory.wearable_items):
                self.inventory.equip(item)

        if action == Action.STATISTICS:
            pass
