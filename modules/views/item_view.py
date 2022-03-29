from textwrap import wrap
from colorama import Fore

from modules import utils
from modules.items.items import Item
from modules.items.inventory import Inventory

class ItemView:
    """Class representing the view of an item"""

    def __init__(self, item: Item, inventory: Inventory) -> None:
        """Parameterised constructor creating a new view over an item"""
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
        bar = '[' + Fore.MAGENTA + '#' * percentage + Fore.WHITE + ' ' * (10 - percentage) + ']'
        return f'{bar} {Fore.MAGENTA}{self.item.durability}{Fore.WHITE} ({Fore.MAGENTA}{self.item.durability}{Fore.WHITE})'
