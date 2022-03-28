from typing import Any, Dict, List
from colorama import Fore
from textwrap import wrap

from modules import utils
from modules.items.inventory import Inventory
from modules.locations.room import Room
from modules.locations.dungeon import Dungeon
from modules.characters.character import Character

from modules.factories import generators
from modules.generators.locations import dungeon_generator
from modules.generators.characters import player_generator


class InventoryView:
    """Class representing the view of the player's inventory"""

    def __init__(self, player: Character) -> None:
        """Parameterised constructor creating a new view of the player's inventory"""
        self.player = player
        self.inventory = player.inventory

    def display(self):
        """Display the player's inventory"""
        utils.clear_screen()
        print(self.player.status_bar)

        if self.inventory.items:
            print(
                f'Occupied slots: {Fore.YELLOW}{len(self.inventory.items)}{Fore.WHITE} ({Fore.YELLOW}{self.inventory.capacity}{Fore.WHITE})')
            print('Your inventory contains:\n')

        for item in self.inventory.items:
            indicator = f'{Fore.GREEN}*{Fore.WHITE}' if item in self.inventory.equipments.values() else ' '
            print(f'[{indicator}] x{item.quantity} {item}')

        print(f'\n[{Fore.CYAN}q{Fore.WHITE}] Close the inventory')

        if self.inventory.items:
            print(f'[{Fore.CYAN}l{Fore.WHITE}] Look at a particular item')

            if len(self.inventory.wearable_items()) > 0:
                print(f'[{Fore.CYAN}w{Fore.WHITE}] Wear a piece of equipment')

            if self.inventory.equipments:
                print(f'[{Fore.CYAN}t{Fore.WHITE}] Take off a piece of equipment')


class InventoryController:
    """Class controlling the player's inventory"""

    def __init__(self, player: Character, room: Room) -> None:
        """Parameterised constructor creating a new controller over the player's inventory"""
        self.view = InventoryView(player)
        self.inventory = player.inventory
        self.room = room

    def run(self) -> None:
        """"""
        while True:
            self.view.display()

            user_input = input('\n> ').lower()
            if self._handle_input(user_input):
                return False

    def _handle_input(self, user_input: str) -> None:
        """Handle the input received by the controller"""
        if user_input == 'q':
            return True
        if user_input == 'l':
            selected_item = choose_one(
                'Select the equipment you want to take a look at:', self.inventory.items)
            if selected_item:
                selected_item.display()
        if user_input == 'w':
            selected_items = choose_many(
                'Select the equipment(s) you want to wear or handle:', self.inventory.wearable_items())
            self.inventory.equip_many(selected_items)
        if user_input == 't':
            selected_items = choose_many(
                'Select the equipment(s) you want to take off:', self.inventory.equipments.values())
            self.inventory.remove_many(selected_items)


def _display(message: str, items: List) -> None:
    utils.clear_screen()
    print(f'\n{message}')

    for index, item in enumerate(items):
        print(f'[{Fore.CYAN}{index}{Fore.WHITE}] {item}')

    print(f'\n[{Fore.CYAN}q{Fore.WHITE}] Equip nothing')


def _display_selection(message: str, items: List, selection: List):
    """"""
    utils.clear_screen()
    print(f'\n{message}')

    for index, item in enumerate(items):
        indicator = f'{Fore.GREEN}*{Fore.WHITE}' if selection[index] else ' '
        print(f'[{indicator}] ({Fore.CYAN}{index}{Fore.WHITE}) {item}')

    print(f'\n[{Fore.CYAN}q{Fore.WHITE}] Equip nothing')
    print(f'[{Fore.CYAN}v{Fore.WHITE}] Wear selected pieces of equipment')


def choose_many(message: str, items: List) -> Any:
    """"""
    selection = [False for _ in items]
    while True:
        _display_selection(message, items, selection)

        user_input = input('\n> ').lower()
        if user_input == 'q':
            return None
        if user_input == 'v':
            return [item for item, selected in zip(items, selection) if selected]
        index = int(user_input)
        if items and 0 <= index < len(items):
            selection[index] = not selection[index]


def choose_one(message: str, items: List) -> Any:
    """"""
    while True:
        _display(message, items)

        user_input = input('\n> ').lower()
        if user_input == 'q':
            return None
        index = int(user_input)
        if items and 0 <= index < len(items):
            return items[index]


class RoomController:
    """Class representing the view of a room"""

    def __init__(self, room: Room, player: Character) -> None:
        """Parameterised constructor creating a new view over a room"""
        self.inventory_controller = InventoryController(player, room)
        self.room = room
        self.player = player

    def display(self) -> None:
        """Run the controller and start the game"""
        while True:  # self.player.is_alive():
            utils.clear_screen()
            print(self.player.status_bar)
            self.room.display()

            user_input = input('\n> ').lower()
            if self._handle_input(user_input):
                return False

    def _handle_input(self, user_input: str) -> None:
        """Handle the input received by the controller"""
        if user_input == 'q':
            return True
        if user_input == 'i':
            self.inventory_controller.run()
        # if user_input == 'c':
        #     accessible_rooms =
        #     next_room = choose_one(
        #         '\nWhere do you want to go ?', self.room)


class DungeonController:
    """Class representing a dungeon controller"""

    def __init__(self, dungeon: Dungeon) -> None:
        """Parameterised constructor creating a new controller of a dungeon"""
        self.dungeon = dungeon
        room = dungeon.current_room()
        self.room_view = RoomController(room, dungeon.player)

    def run(self) -> bool:
        """Run the controller and start the game"""
        while True:
            next_floor = self.room_view.display()
            if not next_floor:
                break


if __name__ == '__main__':

    path = 'resources/dungeon'
    generators.initialize(path)

    dungeon = dungeon_generator.generate(path)

    # TODO: resources = ResourcesLoader.load('resources/interfaces/room.yaml')

    player = player_generator.generate_one()

    dungeon.add_player(player)

    controller = DungeonController(dungeon)

    controller.run()
