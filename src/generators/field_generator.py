import random
from typing import Any, Protocol


class Generator(Protocol):
    """"""

    def generate() -> Any:
        """"""
        pass

    def generate_one(name: str) -> Any:
        """"""
        pass

    def generate_many(self, n: int) -> list[Any]:
        """"""
        pass


class FieldGenerator:
    """"""

    @staticmethod
    def generate(generator: Generator, data: list[str | int] | int) -> list[Any]:
        """Returns a list of the data deserialized using the given generator"""
        if not data:
            return []
        if type(data) == int:
            return generator.generate_many(data)
        if type(data) == list:
            if type(data[0]) == int and len(data) > 1:
                n = random.randint(data[0], data[1])
                return generator.generate_many(n)
            if type(data[0]) == str:
                return [generator.generate(item) for item in data]
