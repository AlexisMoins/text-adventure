from typing import List
from modules.lexer import Lexer, Token

from modules.models.items.items import Item
from modules.models.locations.dungeon import Dungeon
from modules.models.characters.character import Character

from modules.views.room_view import RoomView
from modules.views.item_view import ItemView
from modules.views.inventory_view import InventoryView

from modules.controllers.actions import Action
from modules.controllers.selection import choose_one
from modules.controllers.item_controller import ItemController


class DungeonController:
    """Class representing a dungeon controller"""

    def __init__(self, dungeon: Dungeon, player: Character) -> None:
        """Parameterised constructor creating a new dungeon engine"""
        self.item_controller = ItemController(player, dungeon)

        self.inventory_view = InventoryView(player.inventory)
        # self.npc_controller = NpcController()
        self.room_view = RoomView(player, dungeon)
        self.dungeon = dungeon
        self.player = player
        self.lexer = Lexer()

    def run(self) -> None:
        """Run the current controller"""
        self.is_running = True
        self.room_view.display()

        while self.is_running and self.player.is_alive():
            user_input = input('\n> ').lower()
            sentence = self.lexer.parse(user_input)
            input(sentence)

            self.handle_sentence(sentence)

    def handle_sentence(self, sentence: List[Token]) -> None:
        """Handle the action received by the controller"""
        input(f'valid: {self.lexer.sentence_is_valid(sentence)}')

        if sentence[0] == Action.QUIT:
            self.is_running = False

        if sentence[0] == Action.INVENTORY:
            self.inventory_view.display()

        if sentence[0] == Action.TAKE:
            if items := self.dungeon.current_room.find_item(sentence[1]):
                if len(items) > 1:
                    if item := choose_one('Which item do you want to take ?', items):
                        if self.player.take(item, self.dungeon.current_room):
                            print('Done!')
                else:
                    if self.player.take(items[0], self.dungeon.current_room):
                        print('Done!')

        if sentence[0] == Action.LOOK:
            self.look(sentence[1])

        if sentence[0] == Action.TRAVEL:
            if self.dungeon.travel(sentence[1]):
                self.room_view.display()
            else:
                print('There is nothing in that direction')

    def look(self, pattern: str) -> None:
        """Look at the entity corresponding to the given pattern"""
        if not pattern or pattern == 'around':
            self.room_view.display()
        elif entities := self.find_entities(pattern):
            if len(entities) > 1:
                if entity := choose_one('Which one do you want to take a look at ?', entities):
                    ItemView(entity).display() if isinstance(entity, Item) else self.npc_controller.run(entity)
                else:
                    print('Ok')
            else:
                entity = entities[0]
                ItemView(entity).display() if isinstance(entity, Item) else self.npc_controller.run(entity)
        else:
            print('There is nothing like that here')

    def find_entities(self, pattern: str) -> List:
        """Return the list of entities matching the given pattern"""
        return self.dungeon.current_room.find_entities(pattern) + self.player.inventory.find_items(pattern)
