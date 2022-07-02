from src import dungeon, handler, view, utils
from src.generators.locations import dungeon_generator


def open_dungeon() -> None:
    """
    Open the doors of the dungeon and start the game!
    """
    dungeon.current_room.explored = True
    view.display_room(dungeon.current_room)

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
