import re
from typing import Pattern

# Regular expression to capture a named group
_group = '(?P<{}>.+)'

# Regular expression to (optionaly) capture articles
_articles = '(the |a |an )?'


def parse_expression(expression: str) -> Pattern:
    """Return a regular expression pattern parsed from the given command"""
    patterns = []

    # TODO parse multiple item names with 'and' or ',' ?
    for word in expression.split():

        # Words in uppercase are parsed as named groups
        if word.isupper():
            patterns.append(_articles)
            patterns[-1] += _group.format(word.lower())

        # Add any other word as a required keyword
        else:
            patterns.append(word)

    pattern = ' '.join(patterns)
    return re.compile(f'^{pattern}$')
