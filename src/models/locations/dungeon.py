from src import view
from src.generators.abc import RandomGenerator

from src.models.locations.floor import Floor
from src.models.characters.character import Character


class Dungeon:
    """

    """

    def __init__(self, floors: list[Floor], player: Character, generators: dict[str, RandomGenerator]) -> None:
        """

        """
        self.floors = floors
        self.player = player
        self.generators = generators

        self.is_open = True
        self.floor_number = 0

        floor = self.floors[self.floor_number]
        self.current_room = floor.start

    def open(self) -> None:
        """
        Open the doors of the dungeon and start exploring.
        """
        view.clear_screen()
        view.display_room(self.current_room)

        while self.is_open and self.player.is_alive:

            user_input = self.get_input()
            self.handle_input(user_input)

    def get_input(self) -> str:
        """
        Return the raw command typed by the player.

        Return value:
        A string
        """
        user_input = input('\n> ')
        return user_input.lower().strip()

    def handle_input(self, user_input: str) -> None:
        """
        Handle the given user input.

        Argument:
        user_input -- the raw command typed by the player
        """
        match user_input.split():

            case ['q' | 'quit']:
                self.is_open = False

            case ['cl' | 'clear']:
                view.clear_screen()

            case ['desc' | 'description']:
                print(self.current_room)

            case _:
                print('I don\'t understand that')
