
class Inventory:
    '''Class representing a player's inventory'''

    def __init__(self, capacity: int, gold: int) -> None:
        '''Constructor creating a new inventory'''
        self.__items = []
        self.__equipped_items = {}
        self.__capacity = capacity
        self.gold = gold

    def __len__(self) -> int:
        '''Returns the size of the inventory'''
        return len(self.__items) + len(self.__equipped_items)

    # TODO: Faire hériter Inventory de dict et implementer les méthodes __getattr__ etc
    def __get(self, item_name: str) -> list:
        '''Returns the item whose name is matching the given string'''
        for item in self.__items:
            if item_name in item.name:
                return item
        return []
