from src.field import parse_inventory, parse_statistics
from src.models.characters.character import Character


def get_player() -> Character:
    """
    Create and return the Character representing the player.

    Return value:
    A character object
    """
    inventory = parse_inventory({'armor': 1, 'sword': 1})

    statistics = parse_statistics({
        'health': 10, 
        'max-health': 10,

        'magic': 5, 
        'max-magic': 5,
        
        'strength': 5, 
        'resistance': 2,
        'intelligence': 3
    })

    return Character(inventory=inventory, statistics=statistics,
            name='Player', description='')
