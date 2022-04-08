from modules.controllers.selection import choose_one
from modules.models.locations.room import Room
from modules.models.characters.character import Character

from modules.views.inventory import display_inventory
from modules.views.utils import Action, ask, clear_screen

from modules.controllers.item_controller import ItemController
from modules.utils import resources


def iterate(function, iterator) -> None:
    """Iterate over the given iterator, passing each item to the given function"""
    if iterator:
        for item in iterator:
            function(item)


class InventoryController:
    """Class controlling the player's inventory"""

    def __init__(self, player: Character, room: Room) -> None:
        """Parameterised constructor creating a new controller over the player's inventory"""
        self.inventory = player.inventory
        # self.character_controller = CharacterController(player)
        self.player = player
        self.room = room

    def run(self) -> None:
        """Run the controller"""
        self.is_running = True
        while self.is_running and self.player.is_alive():
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
            entity = choose_one(resources['selection']['interface']['look'].format('the item'),
                                self.inventory.items)
            # self.look(entity)

        if action == Action.STATISTICS:
            pass
            # action = self.character_controller.run()
            # if action == Action.QUIT:
            #     self.is_running = False

        # if action == 'l':
        #     # TODO: show which item is currently equipped
        #     selection_view.message = 'Select the item you want to take a look at:'
        #     selected_item = selection_view.choose_one(self.inventory.items)
        #     if selected_item:
        #         controller = ItemController(selected_item, self.inventory)
        #         action = controller.run()
        #         if action == Action.DROP:
        #             self.room.items.append(controller.dropped_item)

        # if user_input == 'w':
        #     selection_view.message = 'Select the equipment(s) you want to wear or handle:'
        #     selected_items = selection_view.choose(self.inventory.wearable_items())
        #     iterate(self.inventory.equip, selected_items)

        # if user_input == 't':
        #     selection_view.message = 'Select the equipment(s) you want to take off:'
        #     selected_items = selection_view.choose(self.inventory.equipments.values())
        #     iterate(self.inventory.take_off, selected_items)

        # if user_input == 'd':
        #     # TODO: show which item is currently equipped
        #     selection_view.message = 'Select the item(s) you want to drop:'
        #     selected_items = selection_view.choose(self.inventory.items)
        #     if selected_items:
        #         for index, item in enumerate(selected_items):
        #             if self.inventory.item_is_equipped(item):
        #                 if not ask(resources['item']['interface']['warning'].format(item),
        #                            warning=True):
        #                     return Action.IDLE
        #             self.room.items.append(self.view.inventory.drop(item))
