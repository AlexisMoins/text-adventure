
from .inventory import Inventory

class Player:
    '''Class representing a player'''

    def __init__(self, health: int, max_health: int, strength: int, resistance: int):
        '''Constructor creating a new player'''
        self.health = health
        self.max_health = max_health

        self.strength = strength
        self.resistance = resistance

        self.__inventory = Inventory(capacity=8, gold=30)

    def drop_item(self, item_name: str, quantity: int = 1) -> None:
        '''Removes an item from the inventory and returns it'''
        # return self.__inventory.remove(item_name, quantity)

    def add_item(self, item, quantity: int = 1) -> bool:
        '''Returns true if the given item has been added to the inventory, returns false otherwise'''
        # return self.__inventory.add(item, quantity)
