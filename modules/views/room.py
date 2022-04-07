from typing import List
from textwrap import wrap
from colorama import Fore

from modules import utils
from modules.models.locations.room import Room

actions = utils.load_resource('data/views.yaml')['room']['actions']


def display_room(room: Room, actions: List[str]) -> None:
    """Display the given room"""
    print('\n'.join(wrap(room.description)))

    if room.entities:
        word = 'are' if len(room.entities) > 1 else 'is'
        print(f'\nAround you {word}:')
        display_entities(room)

    display_actions(actions)


def display_entities(room: Room) -> None:
    """Display the items present in the room"""
    item_list = [utils.indefinite_determiner(str(entity)) for entity in room.entities]

    if len(item_list) > 1:
        item_list[-1] = 'and ' + item_list[-1]
    item_list[0] = item_list[0].capitalize()
    print(', '.join(item_list))


def display_actions(keys: List[str]) -> None:
    """Display the possible actions available in the current context"""
    print('')
    for key in keys:
        print(f'[{Fore.CYAN}{key}{Fore.WHITE}] {actions[key]}')
