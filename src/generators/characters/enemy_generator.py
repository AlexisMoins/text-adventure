import random
from src import utils, factory

from src import dungeon, utils, factory, field
from src.models.characters.npc import Enemy


# Mapping enemy name and its properties
enemies: dict[str, dict] = {}

# List of the possible enemy names
population: list[str] = []

# List of the chances of generating the corresponding enemy in the population
weights: list[int] = []


def parse_floor(floor: str) -> None:
    """Load the given floor's character generation file"""
    global enemies

    enemies = utils.get_content(dungeon.PATH, floor, 'enemies.yaml')
    generation = enemies.pop('generation')

    global weights
    global population

    weights = list(generation.values())
    population = list(generation.keys())


def generate(character_name: str, quantity: int = 1) -> Enemy:
    """Return the given character after it has been generated"""
    character = enemies[character_name].copy()

    character['quantity'] = quantity

    character['statistics'] = field.parse_statistics(character['statistics'])
    character['inventory'] = field.parse_inventory(character['inventory'])

    return factory.create_entity(character)


def generate_many(k: int) -> list[Enemy]:
    """Generates k randomly generated items"""
    number = min(len(population), k)
    return [generate(item_id) for item_id in random.choices(population, weights, number)]


def generate_all(enemies: dict[str, int]) -> list[Enemy]:
    """
    Generate all the enemies in a dictionary.

    Argument:
    enemies -- a dictionary of enemy IDs and their corresponding quantity

    Return value:
    A list of enemies
    """
    return [generate(item_id, quantity)
            for item_id, quantity in enemies.items()]
