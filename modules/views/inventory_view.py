from colorama import Fore

from modules.models.items.inventory import Inventory
from modules.models.items.items import Item


class InventoryView:
    """"""

    def __init__(self, inventory: Inventory) -> None:
        self.inventory = inventory

    def display(self):
        """Display the player's inventory"""
        print('Your inventory contains:' if self.inventory.items else 'Your inventory is empty')
        print(f'{self.slot_bar}\n')

        for item in self.inventory.items:
            self.display_item(item)

    def display_item(self, item: Item) -> None:
        """Display the given item"""
        indicator = f'{Fore.RED}e{Fore.WHITE}' if self.inventory.is_wore_or_held(item) else ' '
        print(f'[{indicator}] x{item.quantity} {item}')

    @property
    def slot_bar(self) -> str:
        """Display the slot bar of the inventory"""
        percentage = round(len(self.inventory.items) / self.inventory.capacity * 10)
        bar = '[' + Fore.YELLOW + '#' * percentage + Fore.WHITE + ' ' * (10 - percentage) + ']'
        return f'{bar} {Fore.YELLOW}{len(self.inventory.items)}{Fore.WHITE} ({Fore.YELLOW}{self.inventory.capacity}{Fore.WHITE})'
