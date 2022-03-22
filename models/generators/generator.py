from random import randint
from typing import List, Any
from abc import ABC, abstractmethod


class Generator(ABC):
    """Class representing an abstract generator"""

    def generate_field(self, data: List[str | int] | int) -> List[Any]:
        """Returns a list of the data deserialized using the given generator"""
        if not data:
            return []
        if type(data) == int:
            return self.generate_many(data)
        if type(data) == list:
            if type(data[0]) == int and len(data) > 1:
                return self.generate_many(randint(data[0], data[1]))
            if type(data[0]) == str:
                return [self.generate(item) for item in data]

    @abstractmethod
    def generate(self, item: str) -> Any:
        """Return the given entity after it has been generated"""
