from colorama import Fore

from modules.models.items.inventory import Inventory
from modules.models.items.items import Item


def display_inventory(inventory: Inventory):
    """Display the player's inventory"""
    print('Your inventory contains:' if inventory.is_empty() else 'Your inventory is empty')
    dislpay_slot_bar(inventory)

    if not inventory.is_empty():
        print()

    for item in inventory.items:
        display_item(inventory, item)


def display_item(inventory: Inventory, item: Item) -> None:
    """Display the given item"""
    indicator = f'{Fore.RED}e{Fore.WHITE}' if inventory.is_wore_or_held(item) else ' '
    print(f'[{indicator}] x{item.quantity} {item}')


def dislpay_slot_bar(inventory: Inventory) -> str:
    """Display the slot bar of the inventory"""
    percentage = round(len(inventory.items) / inventory.capacity * 10)
    bar = '[' + Fore.YELLOW + '#' * percentage + Fore.WHITE + ' ' * (10 - percentage) + ']'
    print(f'{bar} {Fore.YELLOW}{len(inventory.items)}{Fore.WHITE} ({Fore.YELLOW}{inventory.capacity}{Fore.WHITE})')
