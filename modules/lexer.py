
from dataclasses import dataclass, field
from posixpath import split
from typing import Any, Dict, List, OrderedDict, Tuple

from modules.utils import load_resource


@dataclass(kw_only=True)
class Token:
    """"""
    group: str
    body: str


class PatternParser:
    """"""

    @staticmethod
    def parse(sentence: str) -> Tuple:
        """"""
        pattern = list()
        for word in sentence.split():
            if word.startswith('!'):
                pass

        return tuple(pattern)


class Lexer:
    """Lexical analyzer parsing a sentence"""

    def __init__(self) -> None:
        """"""
        data: Dict[str, Any] = load_resource('data/grammar.yaml')
        self.patterns = data.pop('patterns')
        self.grammar = data

    def parse(self, sentence: str) -> List[Token]:
        """Return the list of tokens reteived from the parsed given sentence"""
        tokens = list()

        for word in sentence.split():
            token = self.get_token(word)
            tokens.append(token)

        return tokens

    def get_token(self, word: str) -> Token:
        """Return the Token corresponding to the given word"""
        for group, elements in self.grammar.items():
            for element in elements:

                if type(element) == list and word in element:
                    return Token(group=group, body=element[0])

                if word == element:
                    return Token(group=group, body=element)

        return Token(group='nouns', body=word)

    def sentence_is_valid(self, sentence: List[Token]) -> bool:
        """Return true if the structure of the given sentence is valid"""
        if not sentence or sentence[0].body not in self.patterns.keys():
            return False

        pattern = self.patterns[sentence[0].body]

        i = 0
        j = 0
        while i < len(sentence) and j < len(pattern):
            word = sentence[i]
            structure = pattern[j]

            # print(f'\nword: {word} (i: {i})')
            # print(f'structure: {structure} (j: {j})')

            if word.body == structure or word.group[:-1] == structure:
                i += 1
                j += 1
                continue

            if type(structure) == list:
                if word.group == structure[0] and word.body in self.grammar[structure[0]]:
                    i += 1
                    j += 1
                    continue

                j += 1
                continue

            return False

        return i == len(sentence) and j == len(pattern)

    @staticmethod
    def get_noun(sentence: List[Token]) -> str:
        """Return the noun of the sentence"""
        tokens = filter(lambda word: word.group == 'nouns', sentence)
        nouns = [token.body for token in tokens]
        return ' '.join(nouns)
