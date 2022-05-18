from typing import Any

from pytest import fixture
from yaml import safe_load


@fixture()
def items() -> dict[str, Any]:
    """Return the sample items used in the tests"""
    with open('tests/data/items.yaml', 'r') as data:
        items = safe_load(data)
    return items
