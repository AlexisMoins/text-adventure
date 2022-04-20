import re
from typing import List, Tuple
from modules.controllers.selection import choose_one

from modules.models.items.items import Item
from modules.models.locations.coordinates import Direction
from modules.models.locations.dungeon import Dungeon
from modules.models.characters.character import Character
from modules.utils import load_resource, split_items

from modules.views.room_view import RoomView
from modules.views.item_view import ItemView

from modules.views.inventory_view import display_inventory


class DungeonController:
    """Class representing a dungeon controller"""

    def __init__(self, dungeon: Dungeon, player: Character) -> None:
        """Parameterised constructor creating a new dungeon engine"""
        self.room_view = RoomView(player, dungeon)
        self.dungeon = dungeon
        self.player = player

    def find_entities(self, pattern: str) -> List:
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

    def parse_input(self, user_input: str) -> Tuple[str | None]:
        """Return a tuple of the the action corresponding to the given input and the matched expression"""
        resources = load_resource('data/actions.yaml')

        for action, pattern in resources.items():
            if expression := re.match(pattern, user_input):
                return action, expression
        return None, None

    def handle_action(self, action: str, expression: re.Match) -> None:
        """Handle the action received by the controller"""
        if action == 'quit':
            self.is_running = False

        if action == 'description':
            self.room_view.display()

        if action == 'look':
            entity = expression.group('entity')
            self.look_at(entity)

        if action == 'take':
            item = expression.group('item')
            for i in split_items(item):
                self.take(i)

        if action == 'drop':
            item = expression.group('item')
            for i in split_items(item):
                self.drop(item)

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

    def look_at(self, noun: str) -> None:
        """"""
        message = 'Which one do you want to take a look at ?'
        if entity := find_one(message, self.find_entities(noun)):
            ItemView(entity).display() if isinstance(entity, Item) else self.npc_controller.run(entity)

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


def find_one(message: str, items: List):
    """"""
    if items:
        if len(items) > 1:
            if item := choose_one(message, items):
                return item
            else:
                print('Ok')
        else:
            return items[0]
    else:
        print('There is nothing like that here...')
