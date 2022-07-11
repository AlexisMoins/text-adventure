from src.generators.locations.dungeon_generator import generate_dungeon


def main() -> None:
    """
    Start a new run in the dungeon
    """
    dungeon = generate_dungeon()
    dungeon.open()


if __name__ == '__main__':
    main()
