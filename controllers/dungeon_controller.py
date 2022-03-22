from typing import List
from curses import window

# from views.locations.room_view import RoomView

from models.locations.dungeon import Dungeon
from models.locations.coordinates import Direction


class DungeonController:
    """Class handling the view and model of a dungeon"""

    def __init__(self, context: window, model: Dungeon) -> None:
        """Parameterised constructor creating a new dungeon controller"""
        self.context = context
        self.dungeon = model
        # self.room_view = RoomView(context)

    # def run(self) -> bool:
    #     """Run the main loop of the controller"""
    #     while True:
    #         room = self.dungeon.current_room()
    #         self.room_view.show(room)
    #         actions = room.get_actions()
    #         if self.handle_input(actions):
    #             break

    def handle_input(self, actions: List[str]) -> bool:
        """"""
        choice = self.context.getch()
        if choice == 'i':
            print('inventory')

        return choice == 'q'

    def move_player(self, direction: Direction) -> None:
        """"""
        position = self.dungeon.get_player_position()

    def display_inventory(self):
        """"""
        # inventory_view = InventoryView.show(self.context, self.dungeon.player.inventory)
