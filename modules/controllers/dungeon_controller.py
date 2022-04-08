from modules.utils import resources

from modules.models.locations.dungeon import Dungeon
from modules.models.characters.character import Character

from modules.views.utils import Action

from modules.controllers.controller import Controller
from modules.controllers.selection import choose_one


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
        self.controller('inventory').inventory = self.player.inventory
        self.controller('item').inventory = self.player.inventory

    def run(self) -> None:
        """Run the current controller"""
        self.initialize()
        while self.is_running and self.player.is_alive():
            # print(self.player.status_bar)
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

        # if action == Action.TRAVEL:
        #     self.travel()

        if action == Action.LOOK:
            self.look()

    def look(self) -> None:
        """Look at the given entity"""
        entity = choose_one(resources['selection']['interface']['look'].format('what'),
                            self.dungeon.current_room.items)

        name = type(entity).__name__.lowe()
        controller = self.controller(name)
        action = controller.run()

        # if action == Action.TAKE:
        #     if self.player.inventory.is_full():
        #         message_without_input(f'{Fore.RED}Warning{Fore.WHITE}\n\nYour inventory is full')
        #         return Action.IDLE
        #     self.player.inventory.items.append(self.room.items.pop(self.room.items.index(selected_item)))

    def travel(self) -> None:
        """"""
        pass
