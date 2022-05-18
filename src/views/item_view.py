import textwrap
from colorama import Fore

from view import view
from src.models.items.items import Item, Equipment


def display(item: Item) -> None:
    """Display the current view"""
    print(f'{Fore.MAGENTA}({item.name}){Fore.WHITE}')
    print(textwrap.fill(item.description))

    price = f'price: {Fore.MAGENTA}{str(item.price)} gold{Fore.WHITE}'
    quantity = f'quantity: {Fore.MAGENTA}x{str(item.quantity)}{Fore.WHITE}'
    print(f'\n{price:<30}{quantity}')

    if 'equip' in item.actions:
        display_equipment(item)

    # actions = self.item.get_actions()
    # self.display_actions(actions.keys(), self.resources['item']['actions'])


def display_equipment(item: Equipment) -> None:
    """Display the equipment's information"""
    slot = f'slot: {Fore.MAGENTA}{item.slot}{Fore.WHITE}'
    equipped = f'equipped: {Fore.MAGENTA}{"yes" if item.equipped else "no"}{Fore.WHITE}'
    print(f'{slot:<30}{equipped}')

    statistics = f'statistics: {Fore.MAGENTA}'
    statistics += ', '.join([f'{stat} +{value}' for stat, value in item.statistics.items()]) + Fore.WHITE

    print(f'\ndurability: {disply_durability(item)}')
    print(f'{statistics:<30}')


def disply_durability(item: Equipment) -> str:
    """Return the durability bar"""
    value = item.durability
    maximum = item.max_durability
    return view.get_bar(value, maximum, Fore.MAGENTA, '>')
