from modules.utils import resources

from modules.models.items.items import Item
from modules.models.locations.dungeon import Dungeon
from modules.models.characters.character import Character

from modules.views.utils import display_message

from modules.controllers.actions import Action
from modules.controllers.selection import choose_one
from modules.controllers.controller import Controller


class DungeonController(Controller):
    """Class representing a dungeon controller"""
    views = ['room']
    controllers = ['inventory', 'item']

    def __init__(self, dungeon: Dungeon, player: Character) -> None:
        """Parameterised constructor creating a new dungeon engine"""
        super().__init__(self.views, self.controllers)
        self.dungeon = dungeon
        self.player = player

    def initialize(self) -> None:
        """Initialize the current controller"""
        self.is_running = True
        self.view('room').room = self.dungeon.current_room
        self.controller('item').inventory = self.player.inventory
        self.controller('inventory').player = self.player

    def run(self) -> None:
        """Run the current controller"""
        self.initialize()
        while self.is_running and self.player.is_alive():
            print(self.player.status_bar)
            self.view('room').display()

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
            self.controller('inventory').run()

        if action == Action.LOOK:
            self.look()

    def look(self) -> None:
        """Look at the given entity"""
        message = resources['selection']['interface']['look'].format('what')
        entity = choose_one(message, self.dungeon.current_room.items)
        self.look_at_item(entity) if isinstance(entity, Item) else self.look_at_npc()

    def look_at_item(self, item: Item) -> None:
        """Look at the given item"""
        self.controller('item').item = item
        action = self.controller('item').run()

        if action == Action.TAKE:
            if self.player.inventory.is_full():
                display_message('Your inventory is full', wait=True, warning=True)
                return Action.IDLE

            item = self.controller('item')
            self.dungeon.current_room.remove(item)
            self.player.take(item)
