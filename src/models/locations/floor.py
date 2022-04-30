from typing import Dict

from colorama import Fore
from modules.controllers.selection import is_integer
from modules.models.locations.room import Room
from modules.models.locations.coordinates import Coordinates
from modules.views.selection import display_selection
from modules.views.utils import display_message


class Floor:
    """Class representing a collection of rooms"""

    def __init__(self, name: str, rooms: Dict[Coordinates, Room]) -> None:
        """Parameterised constructor creating a new floor"""
        self.name = name
        self.rooms = rooms
        self.is_finished = False

        self.player_position = Coordinates(0, 0)
        self.current_room().visited = True

    def current_room(self) -> Room:
        """Return the current room"""
        return self.rooms[self.player_position]

    def choose_destination(self) -> Coordinates | None:
        """Choose a destination from the current room's available exits"""
        room = self.current_room()
        keys = ['q']
        destinations = [
            f'{direction}{f" {Fore.MAGENTA}(visited){Fore.WHITE}" if self.rooms[coordinates].visited else ""} {coordinates}' for direction, coordinates in room.exits.items()]

        while True:
            display_message(f'Your current position is {room}\nContinue exploring in which direction ?')
            display_selection(destinations, keys, inventory=False)

            user_input = input('\n> ').lower()
            if user_input == keys[0]:
                return None

            if (is_integer(user_input)):
                index = int(user_input)
                if room.exits and 0 <= index < len(room.exits):
                    keys = list(room.exits.keys())
                    return room.exits[keys[index]]
