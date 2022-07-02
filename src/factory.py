from typing import Any, Callable


# List of entities types and their corresponding class
entities: dict[str, Callable[..., Any]] = {}


def register(entity_id: str) -> None:
    """Decorator adding the decorated class to the list of available entities for
    parsing YAML configuration files"""
    def decorator(the_class: Callable) -> None:
        entities[entity_id] = the_class

        return the_class
    return decorator


def create_entity(data: dict[str, Any], *, entity_id: str | None = None) -> Any:
    """
    Create and return a new entity based on the given data and the given entity type.

    Argument:
    data -- the data needed to create the entity. This dictionary will be directly given
    to the constructor of the class corresponding to the entity_id (see below).

    For instance, the following data (A) will be passed to the class (B) to create the
    entity:
    
    (A)
    {
        'type': 'barrel',
        'description': 'This barrel is used to store goods of various types.',
        'items': <SizedContainer object>,
        'durability': [20, 20]
    }

    (B)
    @register('barrel')
    @dataclass(kw_only=True)
    class Barrel:
        description: str
        items: SizedContainer
        durability: list[int]

    Keyword argument:
    entity_id -- the type of the entity (default: None). If entity_id is None, the type
    of the entity is retreived from the data argument (it must be present in the form of
    a 'type' key whose value is the name of the class used to create the entity, as given
    to the 'register' decorator).

    Return value:
    An object of any class registered with the 'register' decorator
    """
    global entities

    if not entity_id:
        entity_id: str = data.pop('type')

    entity: Callable = entities[entity_id]
    return entity(**data)
