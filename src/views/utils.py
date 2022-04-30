import os
from colorama import Fore


def yes_no_question(message: str, warning: bool = False) -> bool:
    """Return true if the user chooses yes, return false otherwise"""
    keys = ['y', 'n']
    while True:
        display_message(message, warning=warning)

        user_input = input('\n> ').lower()
        if user_input == keys[0]:
            return True

        if user_input == keys[1]:
            return False


def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_message(message: str, wait: bool = False, warning: bool = False) -> None:
    """Display the given message on screen, optionaly waiting for an input"""
    if warning:
        print(f'{Fore.RED}Warning{Fore.WHITE}\n')
    print(f'{message}')

    if wait:
        input(f'Press any key to continue {Fore.CYAN}[...]{Fore.WHITE} ')


def display_actions(keys: list[str], actions: dict[str, str]) -> None:
    """Display the possible actions available in the current context"""
    print('')
    for key in keys:
        if key in actions:
            print(f'[{Fore.CYAN}{key}{Fore.WHITE}] {actions[key]}')
