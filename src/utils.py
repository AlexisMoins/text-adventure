import os
import yaml
import random

from types import ModuleType
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, DefaultDict, Literal, Protocol

from src.models.entity import Entity
from src.generators import item_generator
from src.models.collections import SizedContainer


class Generator(Protocol):
    """Represents a generator (used for prototyping modules)"""

    def generate(self, entity_id: str) -> Entity:
        """"""
        pass

    def generate_many(self, k: int) -> list[Entity]:
        """"""
        pass


def get_content(*path: str) -> Any:
    """Return the content of the file at the given path"""
    path = os.path.join(*path)
    with open(path, 'r') as data:
        return yaml.safe_load(data)
