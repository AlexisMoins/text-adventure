from collections import deque
from dataclasses import dataclass
from typing import Any, Callable, Deque, Match, Pattern

from src import dungeon, parser, view

from src.models.items.items import Chest, Equipment, Item
from src.models.locations.coordinates import Direction


@dataclass(frozen=True)
class _Command:
    """
    Class representing a command
    """
    pattern: Pattern
    function: Callable
    context: str | None
    parameters: dict[str, Any]

    def apply(self, match: Match) -> None:
        """
        Apply the command to the given match.

        Argument:
        match -- the match
        """
        groups = match.groupdict()
        self.function(**groups, **self.parameters)


# Double linked-list of commands
_commands: Deque[_Command] = deque()


def when(expression: str, context: str | None = None, **parameters: dict[str, Any]) -> Callable:
    """
    Registers the decorated function as a valid command the player can use.

    Arguments:
    expression -- the pattern typed by the player where lowercase letters are required
    and uppercase ones will match the remaining words then be passed to the decorated
    function as argument. Notice that articles are removed from the typed command.

    For instance, 'examine the sharp knife' will match the pattern 'examine ENTITY'
    and 'sharp knife' will be passed to the function in the 'entity' argument. Thus
    the function should take a paramater 'entity' of type 'str' (See below).

    @when('examine ENTITY')
    def examine(entity: str) -> None:
        pass

    Keyword arguments:
    context -- the context required to validate the use of the command
    parameters -- the rest of the parameters grouped together in a dictionary

    Return value:
    ?
    """
    def decorator(function: Callable) -> Callable[..., None]:
        pattern = parser.parse_expression(expression)
        _commands.appendleft(
            _Command(pattern, function, context, parameters))

        return function
    return decorator


def get_input() -> str:
    """
    Return the raw command typed by the player.

    Return value:
    A string
    """
    user_input = input('\n> ')
    return user_input.lower().strip()


def handle_input(user_input: str) -> None:
    """
    Handle the given user input.

    Argument:
    user_input -- the raw command typed by the player
    """
    for command in _commands:
        # Skip the command if not in the right context
        if command.context is not None and command.context not in dungeon.CONTEXT:
            continue

        match = command.pattern.match(user_input)
        if match is not None:
            command.apply(match)
            break
    else:
        print('I don\'t understand that')


@when('q')
@when('quit')
@when('leave')
def quit() -> None:
    """Leave the dungeon"""
    dungeon.is_running = False


@when('inv')
@when('inventory')
def inventory() -> None:
    """Display the content of the player's inventory"""
    view.display_inventory(dungeon.PLAYER)


@when('stat')
@when('statistics')
def statistics() -> None:
    """
    Display the statistics of the player
    """
    view.display_statistics(dungeon.PLAYER)


@when('look at ENTITY')
@when('examine ENTITY')
def look_at(entity: str) -> None:
    """
    Look at something in the current room.

    Argument:
    entity -- the name of the considered entity
    """
    the_entity = dungeon.current_room.entities.find(entity)
    if the_entity is None:
        print(f'There is no {entity} here')
    else:
        if isinstance(the_entity, Item):
            view.display_item(the_entity)


@when('look at ENTITY in CONTAINER')
def look_at_from(entity: str, container: str) -> None:
    """Look at something in a container in the room"""
    the_container = dungeon.current_room.entities.find(container)
    if the_container is None:
        print(f'There is no {container} here')
    elif not isinstance(the_container, Chest):
        print(f'Looking inside {the_container.indefinite} ? What a strange thing to do...')
    else:
        the_item = the_container.items.find(entity)
        if the_item is None:
            print(f'There is no {entity} inside the {the_container}')
        else:
            dungeon.PLAYER.add_to_inventory(the_item)


@when('get ITEM')
@when('take ITEM')
def take(item: str) -> None:
    """
    Take an item from the room and put it in the player's inventory

    Argument:
    item -- the name or parts of the name of the considered item
    """
    the_item = dungeon.current_room.entities.take(item)

    if the_item is None:
        print(f'There is no {item} here')
        return

    # function = dungeon.PLAYER.add_to_inventory
    # hook.execute('take', the_item, function, [the_item])
    dungeon.PLAYER.add_to_inventory(the_item)


@when('get ITEM from CONTAINER')
@when('take ITEM from CONTAINER')
def take_from(item: str, container: str) -> None:
    """Take an item from a container in the room and put it in your inventory"""
    the_container = dungeon.current_room.entities.find(container)
    if the_container is None:
        print(f'There is no {container} here')
    elif not isinstance(the_container, Chest):
        print(f'Taking something from {the_container.indefinite} ? What\'s wrong with you ?')
    else:
        the_item = the_container.items.take(item)
        if the_item is None:
            print(f'There is no {item} inside the {the_container}')
        else:
            dungeon.PLAYER.add_to_inventory(the_item)


@when('drop ITEM')
def drop(item: str) -> None:
    """"""
    the_item = dungeon.PLAYER.inventory.take(item)
    if the_item is None:
        print(f'What are you saying ? You don\'t even have that in your inventory!')
    else:
        dungeon.PLAYER.take_off(the_item)
        dungeon.current_room.entities.append(the_item)
        print('Done!')


@when('wear ITEM')
def wear(item: str) -> None:
    """"""
    the_item = dungeon.PLAYER.inventory.find(item)
    if the_item is None:
        print(f'You are not carrying any {item}')
    elif not isinstance(the_item, Equipment):
        print('Come on, how would you wear that ?!')
    else:
        dungeon.PLAYER.equip(the_item)
        print('Done!')


@when('cast SPELL')
def cast(spell: str) -> None:
    """Cast a spell from your equipped spell book"""
    the_spell = dungeon.PLAYER.spells.find(spell)


@when('slots')
def slots() -> None:
    """Display the equipments currently held or wore by the player"""
    view.display_slots(dungeon.PLAYER)


@when('e', direction='east')
@when('w', direction='west')
@when('n', direction='north')
@when('s', direction='south')
@when('east', direction='east')
@when('west', direction='west')
@when('north', direction='north')
@when('south', direction='south')
def move(direction: str) -> None:
    """"""
    the_direction = Direction[direction.upper()]
    if the_direction in dungeon.current_room.exits:
        new_room = dungeon.current_room.exits[the_direction]
        new_room.explored = True

        dungeon.current_room = new_room
        view.display_room(new_room, the_direction.opposite)
    else:
        print('There is nothing in this direction')
