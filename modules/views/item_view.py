from importlib import resources
import resource
from textwrap import wrap
from colorama import Fore

from modules.models.items.items import Item

from modules.views.view import View


class ItemView(View):
    """Class representing the view of an item"""

    def __init__(self, item: Item) -> None:
        """Parameterised constructor creating a new view over an item"""
        self.item = item

    def display(self) -> None:
        """Display the current view"""
        print('\n'.join(wrap(self.item.description)))

        price = f'price: {Fore.MAGENTA}{str(self.item.price)} gold{Fore.WHITE}'
        quantity = f'quantity: {Fore.MAGENTA}x{str(self.item.quantity)}{Fore.WHITE}'
        print(f'\n{price:<30}{quantity}')

        if 'equip' in self.item.actions:
            self.display_equipment()

        # actions = self.item.get_actions()
        # self.display_actions(actions.keys(), self.resources['item']['actions'])

    def display_equipment(self) -> None:
        """Display the equipment's information"""
        slot = f'slot: {Fore.MAGENTA}{self.item.slot}{Fore.WHITE}'
        equipped = f'equipped: {Fore.MAGENTA}{"yes" if self.item.is_equipped else "no"}{Fore.WHITE}'
        print(f'{slot:<30}{equipped}')

        statistics = f'statistics: {Fore.MAGENTA}'
        statistics += ', '.join([f'{stat} +{value}' for stat, value in self.item.statistics.items()]) + Fore.WHITE

        print(f'\ndurability: {self.durability_bar}')
        print(f'{statistics:<30}')

    @property
    def durability_bar(self) -> str:
        """Return the durability bar"""
        value = self.item.durability
        maximum = self.item.max_durability
        return self.get_bar(value, maximum, Fore.MAGENTA, '>')
