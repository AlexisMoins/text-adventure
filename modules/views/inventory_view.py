from colorama import Fore

from modules import utils
from modules.characters.character import Character


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
            print('Your inventory contains:')
            print(f'slots: {self.slot_bar()}\n')
        else:
            print('Your inventory is empty')
            print(f'slots: {self.slot_bar()}')

        for item in self.inventory.items:
            indicator = f'{Fore.RED}e{Fore.WHITE}' if self.inventory.item_is_equipped(item) else ' '
            print(f'[{indicator}] x{item.quantity} {utils.indefinite_determiner(str(item))}')

    def display_commands(self) -> None:
        """"""
        print(f'\n[{Fore.CYAN}q{Fore.WHITE}] Close the inventory')

        if self.inventory.items:
            print(f'[{Fore.CYAN}l{Fore.WHITE}] Look at a particular item')
            print(f'[{Fore.CYAN}d{Fore.WHITE}] Drop items in the room')

            if len(self.inventory.wearable_items()) > 0:
                print(f'[{Fore.CYAN}w{Fore.WHITE}] Wear a piece of equipment')

            if self.inventory.equipments:
                print(f'[{Fore.CYAN}t{Fore.WHITE}] Take off a piece of equipment')

    def slot_bar(self) -> str:
        """"""
        percentage = round(len(self.inventory.items) / self.inventory.capacity * 10)
        bar = '[' + Fore.YELLOW + '#' * percentage + Fore.WHITE + ' ' * (10 - percentage) + ']'
        return f'{bar} {Fore.YELLOW}{len(self.inventory.items)}{Fore.WHITE} ({Fore.YELLOW}{self.inventory.capacity}{Fore.WHITE})'
