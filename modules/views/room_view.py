from textwrap import wrap

from modules.views.view import View, resources

from modules.models.locations.room import Room
from modules.utils import indefinite_determiner


class RoomView(View):
    """Class representing the view of a room"""

    def __init__(self) -> None:
        """Non parameterised constructor creating a new room view"""
        self.room: Room = None

    def display(self) -> None:
        """Display the given room"""
        print('\n'.join(wrap(self.room.description)))

        if self.room.entities:
            word = 'are' if len(self.room.entities) > 1 else 'is'
            print(f'\nAround you {word}:')
            self.display_entities()

        actions = self.room.get_actions()
        self.display_actions(actions.keys(), resources['room']['actions'])

    def display_entities(self) -> None:
        """Display the items present in the room"""
        item_list = [indefinite_determiner(str(entity)) for entity in self.room.entities]

        if len(item_list) > 1:
            item_list[-1] = 'and ' + item_list[-1]
        item_list[0] = item_list[0].capitalize()
        print(', '.join(item_list))
