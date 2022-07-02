from colorama import Fore
from models.characters.character import Character

from src.models.items.items import Item


def display_inventory(character: Character):
    """Display the player's inventory"""
    print('Your inventory is empty' if character.inventory.is_empty() else 'Your inventory contains:')
    # dislpay_slot_bar(inventory)

    if not character.inventory.is_empty():
        print()

    for item in character.inventory:
        indicator = f'{Fore.RED}e{Fore.WHITE}' if item in character.equipments.values() else ' '
        print(f'[{indicator}] x{item.quantity} {item}')


# def dislpay_slot_bar(inventory: Inventory) -> str:
#     """Display the slot bar of the inventory"""
#     percentage = round(len(inventory.items) / inventory.capacity * 10)
#     bar = '[' + Fore.YELLOW + '#' * percentage + Fore.WHITE + ' ' * (10 - percentage) + ']'
#     print(f'{bar} {Fore.YELLOW}{len(inventory.items)}{Fore.WHITE} ({Fore.YELLOW}{inventory.capacity}{Fore.WHITE})')


def display_slots(character: Character) -> None:
    """"""
    for slot, item in character.equipments.items():
        print(f'{item} on slot {Fore.YELLOW}({slot}){Fore.WHITE}')
