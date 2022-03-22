from colorama import Fore
from textwrap import wrap

from utils import clear_screen
from models.locations.room import Room
from models.locations.dungeon import Dungeon
from models.characters.character import Character

from models.factories import generator_factory
from models.generators.locations import dungeon_generator
from models.generators.characters import player_generator


class RoomView:
    """Class representing the view of a room"""

    def __init__(self, room: Room, player: Character) -> None:
        """Parameterised constructor creating a new view over a room"""
        self.room = room
        self.player = player

    def display(self) -> None:
        """Run the controller and start the game"""
        while True:  # self.player.is_alive():
            self._display_room()

            user_input = input('\n> ').lower()
            if self._handle_input(user_input):
                return False

    def _handle_input(self, user_input: str) -> None:
        """Handle the input received by the controller"""
        if user_input == 'q':
            return True

    def _display_room(self) -> None:
        clear_screen()
        health = f'health: {Fore.MAGENTA}{self.player.get_statistic("health")}{Fore.WHITE} ({Fore.MAGENTA}{self.player.get_statistic("max_health")}{Fore.WHITE})'
        print(f'{health}',
              end='    ')

        print(
            f'mana: {Fore.MAGENTA}{self.player.get_statistic("mana")}{Fore.WHITE} ({Fore.MAGENTA}{self.player.get_statistic("max_mana")}{Fore.WHITE})', end='    ')

        print(f'gold: {Fore.MAGENTA}{self.player.inventory.gold}{Fore.WHITE}\n')

        for line in wrap(self.room.description):
            print(line)

        print(f'\n[{Fore.CYAN}q{Fore.WHITE}] quit')


class DungeonController:
    """Class representing a dungeon controller"""

    def __init__(self, dungeon: Dungeon) -> None:
        """Parameterised constructor creating a new controller of a dungeon"""
        self.dungeon = dungeon
        room = dungeon.current_room()
        self.room_view = RoomView(room, dungeon.player)

    def run(self) -> bool:
        """Run the controller and start the game"""
        while True:
            next_floor = self.room_view.display()
            if not next_floor:
                break


if __name__ == '__main__':

    path = 'dungeon'
    generator_factory.initialize(path)

    dungeon = dungeon_generator.generate(path)

    # TODO: resources = ResourcesLoader.load('resources/interfaces/room.yaml')

    player = player_generator.generate_one()

    dungeon.add_player(player)

    controller = DungeonController(dungeon)

    controller.run()
