from typing import Any, List

from modules import utils
from modules.views.selection import display_selection
from modules.views.utils import Action


def choose_one(message: str, items: List) -> List[Any]:
    """"""
    actions = {'q': Action.QUIT}

    while True:
        utils.clear_screen()
        print(f'{message}\n')

        display_selection(items, actions)

        user_input = input('\n> ').lower()
        if user_input == self.quit_action[0]:
            return None
        index = int(user_input)
        if items and 0 <= index < len(items):
            return items[index]


def choose_many(self, items: List) -> Any:
    """"""
    selection = [False for _ in items]
    while True:
        display_selection(items, selection, actions)

        user_input = input('\n> ').lower()
        if user_input == self.quit_action[0]:
            return None
        if user_input == self.validate_action[0]:
            return [item for item, selected in zip(items, selection) if selected]
        index = int(user_input)
        if items and 0 <= index < len(items):
            selection[index] = not selection[index]
