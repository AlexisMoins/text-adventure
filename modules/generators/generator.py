
from modules.items.items import Item


class Generator:

    def generate_field(self, data: list[str | int] | int) -> list[Item]:
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
