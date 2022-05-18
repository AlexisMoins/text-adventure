from src import utils, factory

from src import dungeon, utils, factory
from src.models.characters.npc import NPC


# Mapping npc name and its properties
npc: dict[str, dict] = {}

# List of the possible npc names
population: list[str] = []

# List of the chances of generating the corresponding npc in the population
weights: list[int] = []


def parse_floor(floor: str) -> None:
    """Load the given floor's character generation file"""
    global npc

    npc = utils.get_content(dungeon.PATH, floor, 'npc.yaml')
    generation = npc.pop('generation')

    global weights
    global population

    weights = list(generation.values())
    population = list(generation.keys())


def generate(npc_name: str) -> NPC:
    """Return the given character after it has been generated"""
    npc = npc[npc_name].copy()
    npc['statistics'] = utils.parse_statistics(npc['statistics'])
    npc['inventory'] = utils.parse_inventory(npc['inventory'])
    return factory.create(npc)


def generate_many(k: int) -> list[NPC]:
    """Generates k randomly generated items"""
    number = min(len(population), k)
    return [generate(item_id) for item_id in dungeon.RANDOM.choices(population, weights, number)]
