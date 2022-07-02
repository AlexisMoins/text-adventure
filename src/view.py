import os
import textwrap
from colorama import Fore

from src import dungeon
from src.models.locations.room import Room
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


def display_room(room: Room, previous_direction: Direction | None = None) -> None:
    """Display the given room"""
    # print(f'{get_character_status(dungeon.PLAYER)}    position: {dungeon.current_room.coordinates}\n')

    print(textwrap.fill(room.description, width=75))

    if room.entities:
        display_room_entities(room)

    if room.exits:
        display_room_exits(room, previous_direction)


def display_room_exits(room: Room, previous_direction: Direction | None) -> None:
    """
    Display the visible exits of the current room.

    Argument:
    previous_direction -- the direction the player entered the room from
    """
    print('\nVisible exits:' if len(dungeon.current_room.exits) > 1 else '\nVisible exit:')

    for direction, room in dungeon.current_room.exits.items():
        sign = f'{Fore.YELLOW}*{Fore.WHITE}' if direction is previous_direction else ' '
        explored = f' {Fore.YELLOW}(explored){Fore.WHITE}' if room.explored else ''
        print(f'{sign} {direction}{explored}')


def display_room_entities(room: Room) -> None:
    """Display the items present in the room"""
    word = 'are' if len(room.entities) > 1 else 'is'
    print(f'\nAround you {word}:')

    for item in dungeon.current_room.entities:
        print(f'{Fore.CYAN}x{item.quantity}{Fore.WHITE} {item}')


def display_item(item: Item) -> None:
    """
    Display the given |item| on screen.

    Argument:
    iten -- the item to display
    """
    print(f'{Fore.RED}({item.name}){Fore.WHITE}')
    print(textwrap.fill(item.description))

    price = f'price: {Fore.RED}{str(item.price)} gold{Fore.WHITE}'
    quantity = f'quantity: {Fore.RED}x{str(item.quantity)}{Fore.WHITE}'
    print(f'\n{price:<30}{quantity}')

    if 'equip' in item.actions:
        display_equipment(item)


def display_equipment(item: Equipment) -> None:
    """Display the equipment's information"""
    slot = f'slot: {Fore.RED}{item.slot}{Fore.WHITE}'
    equipped = f'equipped: {Fore.RED}{"yes" if item.equipped else "no"}{Fore.WHITE}'
    print(f'{slot:<30}{equipped}')

    statistics = f'statistics: {Fore.RED}'
    statistics += ', '.join([f'{stat} +{value}' for stat, value in item.statistics.items()]) + Fore.WHITE

    print(f'\ndurability: {disply_durability(item)}')
    print(f'{statistics:<30}')


def disply_durability(item: Equipment) -> str:
    """
    Return the durability bar
    """
    value = item.durability[0]
    maximum = item.durability[1]
    return get_bar(value, maximum, Fore.RED, '>')


def display_slots(character: Character) -> None:
    """"""
    print('Your current equipment:')
    for slot, item in character.equipments.items():
        print(f'{item} on slot {Fore.YELLOW}{slot.upper()}{Fore.WHITE}')


def display_inventory(character: Character):
    """Display the player's inventory"""
    print('Your inventory is empty' if character.inventory.is_empty() else 'Your inventory contains:')
    # dislpay_slot_bar(inventory)

    if not character.inventory.is_empty():
        print()

    for item in character.inventory:
        indicator = f'{Fore.RED}e{Fore.WHITE}' if item in character.equipments.values() else ' '
        print(f'[{indicator}] x{item.quantity} {item}')
