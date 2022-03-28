import random
from typing import List, Any


def generate_field(generator, data: List[str | int] | int) -> List[Any]:
    """Returns a list of the data deserialized using the given generator"""
    if not data:
        return []
    if type(data) == int:
        return generator.generate_many(data)
    if type(data) == list:
        if type(data[0]) == int and len(data) > 1:
            return generator.generate_many(random.randint(data[0], data[1]))
        if type(data[0]) == str:
            return [generator.generate(item) for item in data]
