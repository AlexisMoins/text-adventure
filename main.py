from colorama import Fore

from src import dungeon, handler, view, utils
from src.generators.locations import dungeon_generator


def main_menu() -> None:
    """"""
    print(f'{Fore.CYAN}DUNGEONS OF TEXT{Fore.WHITE}, version alpha\n')

    instruction = input(f'Would you like to read instructions ? ')
    if instruction.lower() in ['y', 'yes']:
        input('INSTRUCTIONS\n')


def open_dungeon() -> None:
    """
    Open the doors of the dungeon and start the game!
    """
    view.display_room()

    while dungeon.is_running:
        user_input = handler.get_input()
        handler.handle_input(user_input)

        if not dungeon.PLAYER.is_alive():
            print('*** You died ***')
            break


if __name__ == '__main__':
    dungeon_generator.generate()

    dungeon.PLAYER = utils.get_player()
    open_dungeon()
