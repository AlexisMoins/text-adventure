from typing import List
from colorama import Fore

from modules.utils import resources, indefinite_determiner

from modules.models.items.inventory import Inventory
from modules.views.utils import clear_screen, display_actions


def display_inventory(inventory: Inventory, keys: List[str]):
    """Display the player's inventory"""
    if inventory.items:
        print('Your inventory contains:')
        print(f'slots: {slot_bar(inventory)}\n')
    else:
        print('Your inventory is empty')
        print(f'slots: {slot_bar(inventory)}')

    for item in inventory.items:
        display_item(item, inventory)

    print(f'\n[{Fore.GREEN}*{Fore.WHITE}] Inventory')
    print(f'[{Fore.GREEN}2{Fore.WHITE}] Statistics')

    display_actions(keys, resources['inventory']['actions'])


def display_item(item, inventory: Inventory) -> None:
    """Display the given item"""
    indicator = f'{Fore.RED}e{Fore.WHITE}' if inventory.item_is_equipped(item) else ' '
    print(f'[{indicator}] x{item.quantity} {indefinite_determiner(str(item))}')


def slot_bar(inventory: Inventory) -> str:
    """Display the slot bar of the inventory"""
    percentage = round(len(inventory.items) / inventory.capacity * 10)
    bar = '[' + Fore.YELLOW + '#' * percentage + Fore.WHITE + ' ' * (10 - percentage) + ']'
    return f'{bar} {Fore.YELLOW}{len(inventory.items)}{Fore.WHITE} ({Fore.YELLOW}{inventory.capacity}{Fore.WHITE})'
