from typing import Any, Callable

from src.models.entity import Entity

"""List of entities types and their corresponding class"""
entities: dict[str, Callable] = {}


def add(entity_id: str) -> None:
    """Decorator adding the decorated class to the list of available entities for
    parsing YAML configuration files"""
    def decorator(the_class: Callable) -> None:
        entities[entity_id] = the_class

        return the_class
    return decorator


def create(data: dict[str, Any]) -> Entity:
    """Create a new entity based on the entity type retreived from the data"""
    entity_type = data.pop('type')
    entity: Callable = entities[entity_type]
    return entity(**data)
