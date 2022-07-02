import random
from typing import Any
from types import ModuleType

from src import utils, dungeon
from src.field import parse_field

from src.models.locations.room import Room
from src.models.collections import Container

from src.generators import item_generator
from src.generators.characters import npc_generator
from src.generators.characters import enemy_generator


# Mapping room name -> properties
rooms: dict[str, Any] = {}

# List of the possible room names
population: list[str] = []

# List of the chances of generating corresponding room in the population
weights: list[int] = []

#
FIELDS: dict[str, ModuleType] = {
        'items': item_generator, 'enemies': enemy_generator, 'npc': npc_generator }


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
    number = random.randint(1, sum(weights))
    for room, weight in zip(population, weights):
        if number <= weight:
            return generate(room)
        number -= weight


def generate_many(k: int) -> list[Room]:
    """Generates k randomly generated rooms"""
    number = min(len(population), k)
    return [generate_one() for _ in range(number)]


def deserialize_room(field: dict[str, Any]) -> Room:
    """Returns the room deserialized from the given data"""
    entities = []
    for name, generator in FIELDS.items():
        if name in field:
            data = field.pop(name)
            print(f'\n{name}: {data}')
            entities.extend(parse_field(data, generator))  # type: ignore
            print(entities)

    return Room(**field, entities=Container(entities))


def pop_room(room_id) -> dict[str, Any]:
    """Returns the given room's data and remove it from the generator"""
    if room_id in population:
        index = population.index(room_id)

        del weights[index]
        population.remove(room_id)

    return rooms.pop(room_id)
