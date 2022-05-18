from typing import Any

from src.models.collections import Container

from src import utils, dungeon
from src.models.locations.room import Room

from src.generators import item_generator
from src.generators.characters import npc_generator
from src.generators.characters import enemy_generator


# Mapping room name -> properties
rooms: dict[str, Any] = {}

# List of the possible room names
population: list[str] = []

# List of the chances of generating corresponding room in the population
weights: list[int] = []


def parse_floor(floor: str) -> None:
    """Load the given floor's room generation file"""
    global rooms

    rooms = utils.get_content(dungeon.PATH, floor, 'rooms.yaml')
    generation = rooms.pop('generation')

    global weights
    global population

    weights = list(generation.values())
    population = list(generation.keys())


def generate(room_id: str) -> Room:
    """Returns the given room after it has been generated"""
    data = pop_room(room_id)
    return deserialize_room(data)


def generate_one() -> Room | None:
    """Generates a random room"""
    number = dungeon.RANDOM.randint(1, sum(weights))
    for room, weight in zip(population, weights):
        if number <= weight:
            return generate(room)
        number -= weight


def generate_many(k: int) -> list[Room]:
    """Generates k randomly generated rooms"""
    number = min(len(population), k)
    return [generate_one() for _ in range(number)]


def deserialize_room(data: dict[str, Any]) -> Room:
    """Returns the room deserialized from the given data"""
    items = utils.parse_field(data.pop('items', []), item_generator)
    enemies = utils.parse_field(data.pop('enemies', []), enemy_generator)
    npc = utils.parse_field(data.pop('npc', []), npc_generator)

    entities = items + enemies + npc
    return Room(**data, entities=Container(entities))


def pop_room(room_id) -> dict[str, Any]:
    """Returns the given room's data and remove it from the generator"""
    if room_id in population:
        index = population.index(room_id)

        del weights[index]
        population.remove(room_id)

    return rooms.pop(room_id)
