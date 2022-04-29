import re
from textwrap import wrap
from modules.controllers.selection import choose_one
from colorama import Fore

from modules.models.items.items import Item
from modules.models.locations.coordinates import Direction
from modules.models.locations.dungeon import Dungeon
from modules.models.characters.character import Character
from modules.utils import load_resource, split_items

from modules.views.room_view import RoomView
from modules.views.item_view import ItemView

from modules.views.inventory_view import display_inventory, display_slots

Entity = Character | Item


class DungeonController:
    """Class representing a dungeon controller"""

    def __init__(self, dungeon: Dungeon, player: Character) -> None:
        """Parameterised constructor creating a new dungeon engine"""
        self.room_view = RoomView(player, dungeon)
        self.dungeon = dungeon
        self.player = player

    def find_entities(self, pattern: str) -> list:
        """Return the list of entities matching the given pattern"""
        return self.dungeon.current_room.find_entities(pattern) + self.player.inventory.find_items(pattern)

    def run(self) -> None:
        """Run the current controller"""
        self.is_running = True
        self.room_view.display()

        while self.is_running and self.player.is_alive():
            user_input = input('\n> ').lower().strip()

            action, expression = self.parse_input(user_input)
            self.handle_action(action, expression) if action and expression else print('Huh ?')

    def parse_input(self, user_input: str) -> tuple[str | None, str | None]:
        """Return a tuple of the the action corresponding to the given input and the matched expression"""
        resources = load_resource('data/actions.yaml')

        for action, data in resources.items():
            for pattern in data['patterns']:
                if expression := re.match(pattern, user_input):
                    return action, expression
        return None, None

    def handle_action(self, action: str, expression: re.Match) -> None:
        """Handle the action received by the controller"""
        if action == 'quit':
            self.is_running = False

        if action == 'help':
            arguments = expression.groupdict()
            self.get_help(**arguments)

        if action == 'description':
            self.room_view.display()

        if action == 'look':
            arguments = expression.groupdict()
            self.look_at(**arguments)

        if action == 'take':
            item = expression.group('item')
            for i in split_items(item):
                self.take(i)

        if action == 'drop':
            item = expression.group('item')
            for i in split_items(item):
                self.drop(item)

        if action == 'slots':
            display_slots(self.player.inventory)

        if action == 'inventory':
            display_inventory(self.player.inventory)

        if action == 'wear':
            # Split the item by ',' and 'and
            verb = expression.group('verb')
            equipment = expression.group('equipment')
            self.wear(verb, equipment)

        if action == 'move':
            direction = expression.group('direction')
            self.move(direction)

    def get_help(self, command: str = None) -> None:
        """"""
        resources = load_resource('data/actions.yaml')
        if command:
            if command in resources.keys():
                print()
                for c in resources[command]["help"]:
                    print(f'  {Fore.GREEN}{c}{Fore.WHITE}')
                print('\n' + '\n'.join(wrap(resources[command]['description'])))
            else:
                print(f'There is no entry for \'{command}\' in the help manual')
        else:
            print('Here is what you can do in the dungeon:')
            commands = [f'{Fore.GREEN}{key}{Fore.WHITE}' for key in resources.keys()]
            print('\n  ' + '\n  '.join(wrap(', '.join(commands), width=120)))
        # TODO join keys in actions.yaml in a wrapped list with colors

    def look_at(self, entity: str, container: str = None) -> None:
        """Look at something, in a container or in the current room (default)"""
        collection = self.get_container(container)
        if collection is None:
            return None

        found_entity = find(entity, collection)
        if found_entity is None:
            return None

        ItemView(found_entity).display() if isinstance(found_entity, Item) else self.npc_controller.run(found_entity)

    def get_container(self, container: str) -> list[Entity] | None:
        """"""
        if not container:
            return self.dungeon.current_room.entities + self.player.inventory.items

        if container in ['inventory', 'inv']:
            return self.player.inventory.items

        if container in ['here', 'room']:
            return self.dungeon.current_room.entities

        # TODO look for containers in the current room
        print(f'There is no {container} here')
        return None

    def wear(self, verb: str, equipment: str) -> None:
        """"""
        message = f'Which equipment do you want to {verb} ?'
        if item := find_one(message, self.player.inventory.find_wearables(equipment)):
            self.player.equip(item)

    def take(self, noun: str) -> None:
        """"""
        message = 'Which item do you want to take ?'
        if item := find_one(message, self.dungeon.current_room.find_items(noun)):
            self.player.take(item, self.dungeon.current_room)

    def drop(self, noun: str) -> None:
        """"""
        message = 'Which item do you want to drop ?'
        if item := find_one(message, self.player.inventory.find_items(noun)):
            self.player.drop(item, self.dungeon.current_room)

    def move(self, noun: str):
        """Move to another room"""
        direction = Direction.parse(noun)
        self.room_view.display() if self.dungeon.travel(
            direction) else print('There is nothing in that direction!')


def find_one(message: str, collection: list[Entity]) -> Entity:
    """"""
    if collection:
        if len(collection) > 1:
            if item := choose_one(message, collection):
                return item
            else:
                print('Ok')
        else:
            return collection[0]
    else:
        print('There is nothing like that here...')


def find(name: str, collection: list[Entity]) -> Entity | None:
    """"""
    iterable = [entity for entity in collection if name in entity.name]
    if not iterable:
        print(f'There is no {name} here')
        return None

    if len(iterable) > 1:
        if item := choose_one('Which one of the following ?', iterable):
            return item
        else:
            print('Ok!')
    else:
        return iterable[0]
