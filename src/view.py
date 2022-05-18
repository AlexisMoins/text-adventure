import os
import textwrap
from colorama import Fore

from src import dungeon
from src.models.items.items import Equipment, Item
from src.models.characters.character import Character
from src.models.locations.coordinates import Direction


def clear_screen() -> None:
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_bar(value: int, maximum: int, color, character: str) -> str:
    """Return a status bar with the given values, color and character to fill the bar"""
    percentage = round(value / maximum * 10)
    bar = f'[{color}{character * percentage}{Fore.WHITE}{" " * (10 - percentage)}]'
    return f'{bar} {color}{value}{Fore.WHITE} ({color}{maximum}{Fore.WHITE})'


def get_character_status(character: Character) -> str:
    """Return the """
    return 'health {}    mana: {}'.format(
        get_bar(character.statistics['health'], character.statistics['max-health'], Fore.RED, '='),
        get_bar(character.statistics['mana'], character.statistics['max-mana'], Fore.GREEN, '=')
    )


def display_room(previous_direction: Direction = None) -> None:
    """Display the given room"""
    clear_screen()
    print(f'{get_character_status(dungeon.PLAYER)}    position: {dungeon.current_room.coordinates}\n')

    print(textwrap.fill(dungeon.current_room.description, width=75))

    entities_and_exits = list(dungeon.current_room.entities) + list(dungeon.current_room.exits.keys())
    if entities_and_exits:
        word = 'are' if len(entities_and_exits) > 1 else 'is'
        print(f'\nAround you {word}:')
        display_entities(previous_direction)


def display_entities(previous_direction: Direction | None) -> None:
    """Display the items present in the room"""
    indicator = f'{Fore.YELLOW}*{Fore.WHITE}'
    item_list = [entity.indefinite for entity in dungeon.current_room.entities]
    item_list += [f'an exit{indicator if direction is previous_direction else ""} {Fore.YELLOW}({direction}){Fore.WHITE}'
                  for direction in dungeon.current_room.exits.keys()]

    if len(item_list) > 1:
        item_list[-1] = 'and ' + item_list[-1]
    item_list[0] = item_list[0].capitalize()
    print(', '.join(item_list))


def display(item: Item) -> None:
    """Display the current view"""
    print(f'{Fore.MAGENTA}({item.name}){Fore.WHITE}')
    print(textwrap.fill(item.description))

    price = f'price: {Fore.MAGENTA}{str(item.price)} gold{Fore.WHITE}'
    quantity = f'quantity: {Fore.MAGENTA}x{str(item.quantity)}{Fore.WHITE}'
    print(f'\n{price:<30}{quantity}')

    if 'equip' in item.actions:
        display_equipment(item)


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
    return get_bar(value, maximum, Fore.MAGENTA, '>')


def display_slots(character: Character) -> None:
    """"""
    for slot, item in character.equipments.items():
        print(f'{item} on slot {Fore.YELLOW}({slot}){Fore.WHITE}')


def display_inventory(character: Character):
    """Display the player's inventory"""
    print('Your inventory is empty' if character.inventory.is_empty() else 'Your inventory contains:')
    # dislpay_slot_bar(inventory)

    if not character.inventory.is_empty():
        print()

    for item in character.inventory:
        indicator = f'{Fore.RED}e{Fore.WHITE}' if item in character.equipments.values() else ' '
        print(f'[{indicator}] x{item.quantity} {item}')
