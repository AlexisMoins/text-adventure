from typing import Any, List
from textwrap import wrap
from dataclasses import dataclass, field
from colorama import Fore

from modules import utils


@dataclass(kw_only=True)
class Room:
    """Class representing a generic room"""
    description: str
    items: Any = field(default_factory=list)
    enemies: Any = field(default_factory=list)
    npc: Any = field(default_factory=list)
    actions: List[str] = field(default_factory=list, init=False)

    def display(self) -> None:
        """"""
        print('\n'.join(wrap(self.description)))

        if self.items or self.enemies or self.npc:
            word = 'are' if len(self.items) + len(self.enemies) + len(self.npc) else 'is'
            print(f'\nAround you {word}:')
            self.display_entities()

        self.display_actions()

    def display_actions(self) -> None:
        """Display the possible actions available in the current room"""
        print(f'\n[{Fore.CYAN}q{Fore.WHITE}] Leave the dungeon')
        print(f'[{Fore.CYAN}i{Fore.WHITE}] Open the inventory')
        print(f'[{Fore.CYAN}c{Fore.WHITE}] Continue your exploration')

    def display_entities(self) -> None:
        """Display the items present in the room"""
        item_list = [utils.indefinite_determiner(str(entity)) for entity in self.items + self.enemies + self.npc]

        if len(item_list) > 1:
            item_list[-1] = 'and ' + item_list[-1]
        item_list[0] = item_list[0].capitalize()
        print(', '.join(item_list))
