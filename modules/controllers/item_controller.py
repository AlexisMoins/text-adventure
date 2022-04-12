from modules.models.items.items import Item
from modules.models.locations.dungeon import Dungeon
from modules.models.characters.character import Character

from modules.views.item_view import ItemView
from modules.controllers.actions import Action


class ItemController:
    """Class controlling the actions performed in an item view"""

    def __init__(self, player: Character, dungeon: Dungeon) -> None:
        """Parameterised constructor creating a new item controller"""
        self.dungeon = dungeon
        self.player = player

        self.item_view: ItemView = None
        self.item: Item = None

    def run(self, item: Item) -> None:
        """Run the current controller"""
        self.item_view = ItemView(item)
        self.is_running = True
        self.item = item

        while self.is_running:
            self.item_view.display()

            user_input = input('\n> ').lower()
            actions = self.item.get_actions()
            if user_input not in actions:
                continue

            action = actions[user_input]
            self.handle_action(action)

    def handle_action(self, action: Action) -> None:
        """Handle the action received by the controller"""
        if action == Action.QUIT:
            self.is_running = False

        if action == Action.TAKE_OFF:
            self.player.take_off(self.item)

        if action == Action.WEAR:
            self.player.equip(self.item)

        if action == Action.DROP:
            self.player.drop(self.item, self.dungeon.current_room)

        if action == Action.TAKE:
            self.player.take(self.item, self.dungeon.current_room)
