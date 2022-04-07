from typing import Any
from colorama import Fore

from modules import utils
from modules.models.locations.dungeon import Dungeon
from modules.models.characters.character import Character

from modules.views.utils import Action
from modules.views.room import display_room

from modules.controllers.item import ItemController
from modules.controllers.selection import choose_one
from modules.controllers.inventory import InventoryController


class Engine:
    """Class representing a game engine / dungeon controller"""

    def __init__(self, dungeon: Dungeon, player: Character) -> None:
        """Parameterised constructor creating a new dungeon engine"""
        self.dungeon = dungeon
        self.player = player

        self.is_running = True
        self.inventory_controller = InventoryController(player, dungeon.current_room)

    def run(self) -> None:
        """Run the controller and start the game"""
        while self.is_running and self.player.is_alive():
            utils.clear_screen()
            actions = self.dungeon.current_room.get_actions()

            print(self.player.status_bar)
            display_room(self.dungeon.current_room, actions.keys())

            user_input = input('\n> ').lower()
            if user_input not in actions:
                continue

            self.handle_action(actions[user_input])

    def handle_action(self, action: Action) -> None:
        """Handle the action received by the engine"""
        if action == Action.QUIT:
            self.is_running = False

        if action == Action.INVENTORY:
            self.inventory_controller.run()

        if action == Action.LOOK:
            entity = choose_one(interface['look'], self.room.items)
            self.look(entity)

    def look(self, entity: Any) -> None:
        """"""
        if entity:
            controller = ItemController(entity, self.player.inventory)
            action = controller.run()
            if action == Action.TAKE:
                if self.player.inventory.is_full():
                    message_without_input(
                        f'{Fore.RED}Warning{Fore.WHITE}\n\nYour inventory is full')
                    return Action.IDLE
                self.player.inventory.items.append(self.room.items.pop(self.room.items.index(selected_item)))
