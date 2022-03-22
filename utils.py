from os import system, name


def clear_screen():
    """Clear the screen"""
    system('cls' if name == 'nt' else 'clear')
