from textwrap import wrap
from modules import utils
from colorama import Fore
from modules.items.equipments import Equipment
from modules.items.inventory import Inventory
from modules.items.items import Item
from modules.locations.room import Room
from modules.characters.character import Character

from modules.views.inventory_view import InventoryView
from modules.views.selection_view import selection_view


class ItemView:
    """"""

    def __init__(self, item: Item, inventory: Inventory) -> None:
        """"""
        self.item = item
        self.inventory = inventory

    def display(self) -> None:
        """"""
        utils.clear_screen()

        print(f'{Fore.MAGENTA}{self.item.name.capitalize()}{Fore.WHITE}\n')
        print('\n'.join(wrap(self.item.description)))

        if hasattr(self.item, 'durability'):
            print(f'\ndurability: {self.durability_bar()}')

        price = f'price: {Fore.MAGENTA}{str(self.item.price)} gold{Fore.WHITE}'
        quantity = f'quantity: {Fore.MAGENTA}x{str(self.item.quantity)}{Fore.WHITE}'

        slot = f' slot: {Fore.MAGENTA}'
        equipped = f'equipped: {Fore.MAGENTA}'
        if 'equip' in self.item.actions:
            slot += f'{self.item.slot}{Fore.WHITE}'
            if self.inventory.item_is_equipped(self.item):
                equipped += f'yes{Fore.WHITE}'
            else:
                equipped += f'no{Fore.WHITE}'
        else:
            slot += f'none{Fore.WHITE}'
            equipped += f'no{Fore.WHITE}'

        print(f'\n{price:<30}{quantity}')
        print(f'{slot:<30}{equipped}')

    def display_commands(self) -> None:
        print(f'\n[{Fore.CYAN}q{Fore.WHITE}] Return')

        if self.inventory.contains(self.item):
            if self.inventory.item_is_equipped(self.item):
                print(f'[{Fore.CYAN}t{Fore.WHITE}] Take off')
            else:
                print(f'[{Fore.CYAN}w{Fore.WHITE}] Wear or hold')
            print(f'[{Fore.CYAN}d{Fore.WHITE}] Drop in the room')
        else:
            print(f'[{Fore.CYAN}p{Fore.WHITE}] Put in your inventory')

    def durability_bar(self) -> str:
        """"""
        percentage = round(self.item.durability / self.item.durability * 10)
        bar = '[' + Fore.MAGENTA + '=' * percentage + Fore.WHITE + ' ' * (10 - percentage) + ']'
        return f'{bar} {Fore.MAGENTA}{self.item.durability}{Fore.WHITE} ({Fore.MAGENTA}{self.item.durability}{Fore.WHITE})'


class ItemController:
    """"""

    def __init__(self, item: Item, inventory: Inventory) -> None:
        """"""
        self.view = ItemView(item, inventory)
        self.dropped_item = None

    def run(self) -> None:
        """"""
        while True:
            self.view.display()
            self.view.display_commands()

            user_input = input('\n> ').lower()
            if self._handle_input(user_input):
                return False

    def _handle_input(self, user_input: str) -> None:
        """Handle the input received by the controller"""
        if user_input == 'q':
            return True
        if user_input == 't':
            self.view.inventory.remove_one(self.view.item)
        if user_input == 'w':
            self.view.inventory.equip_one(self.view.item)
        if user_input == 'd':
            self.dropped_item = self.view.item
            return True


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
            selection_view.message = 'Select the equipment you want to take a look at:'
            selected_item = selection_view.choose_one(self.inventory.items)
            if selected_item:
                ItemController(selected_item, self.inventory).run()
        if user_input == 'w':
            selection_view.message = 'Select the equipment(s) you want to wear or handle:'
            selected_items = selection_view.choose_many(self.inventory.wearable_items())
            self.inventory.equip_many(selected_items)
        if user_input == 't':
            selection_view.message = 'Select the equipment(s) you want to take off:'
            selected_items = selection_view.choose_many(self.inventory.equipments.values())
            self.inventory.remove_many(selected_items)
