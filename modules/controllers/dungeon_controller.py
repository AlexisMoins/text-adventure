from modules.utils import resources

from modules.models.items.items import Item
from modules.models.locations.dungeon import Dungeon
from modules.models.characters.character import Character

from modules.views.room_view import RoomView

from modules.controllers.actions import Action
from modules.controllers.controller import Controller
from modules.controllers.selection import choose_many, choose_one, choose_one_destination
from modules.controllers.item_controller import ItemController
from modules.controllers.inventory_controller import InventoryController


class DungeonController(Controller):
    """Class representing a dungeon controller"""

    def __init__(self, dungeon: Dungeon, player: Character) -> None:
        """Parameterised constructor creating a new dungeon engine"""
        self.item_controller = ItemController(player, dungeon)
        self.inventory_controller = InventoryController(self.item_controller)
        # self.npc_controller = NpcController()

        self.room_view = RoomView(player, dungeon)
        self.dungeon = dungeon
        self.player = player

    def run(self) -> None:
        """Run the current controller"""
        self.is_running = True
        while self.is_running and self.player.is_alive():
            self.room_view.display()

            user_input = input('\n> ').lower()
            actions = self.dungeon.current_room.get_actions()
            if user_input not in actions:
                continue

            self.handle_action(actions[user_input])

    def handle_action(self, action: Action) -> None:
        """Handle the action received by the controller"""
        if action == Action.QUIT:
            self.is_running = False

        if action == Action.INVENTORY:
            self.inventory_controller.run()

        if action == Action.TRAVEL:
            if coordinates := choose_one_destination(self.dungeon.current_room):
                self.dungeon.travel(coordinates)

        if action == Action.LOOK:
            message = resources['selection']['interface']['look'].format('what')
            if entity := choose_one(message, self.dungeon.current_room.entities):
                self.item_controller.run(entity) if isinstance(entity, Item) else self.npc_controller.run(entity)

        if action == Action.TAKE:
            message = resources['selection']['interface']['take']
            for item in choose_many(message, self.dungeon.current_room.items):
                self.player.take(item, self.dungeon.current_room)
