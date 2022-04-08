from modules.utils import resources

from modules.models.items.items import Item
from modules.models.items.inventory import Inventory

from modules.views.utils import ask

from modules.controllers.controller import Controller


class ItemController(Controller):
    """Class controlling the actions performed in an item view"""
    views = ['item']
    controllers = []

    def __init__(self) -> None:
        """Parameterised constructor creating a new item controller"""
        super().__init__(self.views, self.controllers)
        self.dropped_item = None
        self.inventory: Inventory
        self.item: Item

    def initialize(self) -> None:
        """Initialize the current controller"""
        self.is_running = True
        self.view('item').item = self.item
        self.view('item').inventory = self.inventory

    def run(self) -> None:
        """Run the controller"""
        self.initialize()
        while self.is_running:
            self.view('item').display()

            user_input = input('\n> ').lower()
            actions = self.item.get_actions(self.inventory)
            if user_input not in actions:
                continue

            self.handle_action(actions[user_input])

    def handle_action(self, action: Action) -> None:
        """Handle the action received by the controller"""
        if action == Action.QUIT:
            self.is_running = False

        if action == Action.TAKE_OFF:
            self.inventory.take_off(self.view.item)

        if action == Action.WEAR:
            self.inventory.equip(self.view.item)

        if action == Action.DROP:
            if self.inventory.item_is_equipped(self.view.item):
                if not ask(resources['item']['interface']['warning'].format(self.view.item),
                           warning=True):
                    return Action.IDLE
            self.dropped_item = self.inventory.drop(self.view.item)
            return Action.DROP

        if action == Action.TAKE:
            pass
