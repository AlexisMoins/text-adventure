from colorama import Fore
from textwrap import wrap
from modules.models.characters.npc import Enemy
from modules.models.locations.dungeon import Dungeon

from modules.models.locations.room import Room
from modules.models.characters.character import Character
from modules.utils import indefinite_determiner

from modules.views.utils import clear_screen
from modules.views.view import View, resources
from modules.views.character_view import CharacterView


class RoomView(View):
    """Class representing the view of a room"""

    def __init__(self, player: Character, dungeon: Dungeon) -> None:
        """Non parameterised constructor creating a new room view"""
        self.player_view = CharacterView(player)
        self.dungeon = dungeon

    def display(self) -> None:
        """Display the given room"""
        clear_screen()
        print(f'{self.player_view.status_bar}    {self.dungeon.current_room}\n')

        print('\n'.join(wrap(self.dungeon.current_room.description)))

        if self.dungeon.current_room.entities + list(self.dungeon.current_room.exits.keys()):
            word = 'are' if len(self.dungeon.current_room.entities +
                                list(self.dungeon.current_room.exits.keys())) > 1 else 'is'
            print(f'\nAround you {word}:')
            self.display_entities()

        # indicator = 's' if len(self.dungeon.current_room.exits) > 1 else ''
        # print(f'\nAvailable exit{indicator}:')
        # exits = [f'{direction} {coordinates}' for direction, coordinates in self.dungeon.current_room.exits.items()]
        # print(','.join(exits))

        # actions = self.dungeon.current_room.get_actions()
        # self.display_actions(actions.keys(), resources['room']['actions'])

    def display_entities(self) -> None:
        """Display the items present in the room"""
        item_list = [str(entity) for entity in self.dungeon.current_room.entities]
        item_list += [f'an exit {Fore.YELLOW}({direction}){Fore.WHITE}' for direction in self.dungeon.current_room.exits.keys()]

        if len(item_list) > 1:
            item_list[-1] = 'and ' + item_list[-1]
        item_list[0] = item_list[0].capitalize()
        print(', '.join(item_list))
