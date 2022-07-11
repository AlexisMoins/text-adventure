import random

from src import utils, field
from src.generators.abc import RandomGenerator

from src.models.characters.npc import Enemy
from src.models.characters.character import Character


class CharacterGenerator(RandomGenerator):
    """
    Class representing a character generator. Can be used to generate
    different types of characters like 'NPCs' or 'enemies'.
    """

    def __init__(self, path: str, generators: dict[str, RandomGenerator], *, file: str, field: str = '') -> None:
        """
        Initialize a new (empty) character generator. To use the generator, call the
        'parse_floor' method on a floor name.

        Arguments:
        path -- the path to the dungeon directory containing the generation files
        for each floor

        generators -- the dictionary of generators used to create a character

        Keyword argument:
        file -- the name of the configuration file that will be read

        field -- the name of the field that will use this generator
        """
        super().__init__(path, field=field)

        # Dictionary of generators used to create the character
        self.generators = generators

        # Name of the configuration file that will be read
        self.FILE = file

        # Mapping enemy name and its properties
        self.characters: dict[str, dict] = {}

        # List of the possible enemy names
        self.population: list[str] = []

        # List of the chances of generating the corresponding enemy in the population
        self.weights: list[int] = []

    def parse_floor(self, floor_name: str) -> None:
        """
        Parse a floor and load the files required by this generator. All
        generators must parse the new floors before starting to generate
        any entity.

        Argument:
        floor_name -- the name of the floor. The name must match the name
        of the floor directory containing all generation-related files.
        """
        self.characters = utils.get_content(self.PATH, floor_name, self.FILE)
        self.generation = self.characters.pop('generation')

        self.weights = list(self.generation.values())
        self.population = list(self.generation.keys())

    def generate(self, character_name: str) -> Character:
        """
        Generate the character corresponding to a character ID.

        Argument:
        character_id -- the identifier of the character

        Return value:
        An character object (or sub-class)
        """
        character = self.characters[character_name].copy()

        character['statistics'] = field.parse_statistics(character['statistics'])
        character['inventory'] = self.generators['item'].parse_inventory(character['inventory'])

        _type = character.pop('type').lower()

        if _type == 'enemy':
            return Enemy(**character)

        return Character(**character)

    def generate_all(self, characters: dict[str, int]) -> list[Character]:
        """
        Generate all the characters in a dictionary.

        Argument:
        characters -- a dictionary of character IDs and their corresponding quantity

        Return value:
        A list of characters
        """
        return [self.generate(item_id) for item_id in characters]

    def generate_many(self, k: int) -> list[Character]:
        """Generates k randomly generated items"""
        number = min(len(self.population), k)
        choices = random.choices(self.population, self.weights, k=number)
        return [self.generate(item_id) for item_id in choices]
