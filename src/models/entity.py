from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Entity:
    """Represents a generic entity, wether it be an item or a character"""
    name: str
    description: str
    quantity: int = 1
    actions: list[str] = field(default_factory=list)

    @property
    def indefinite(self) -> str:
        """Return the name of the """
        return indefinite_determiner(self)

    def __str__(self) -> str:
        """Return the string representation of the current entity"""
        return self.name


def indefinite_determiner(entity: Entity) -> str:
    """Return the correct indefinite determiner followed by the given entity name"""
    vowels = 'aeiouy'
    determiner = 'an' if entity.name[0] in vowels else 'a'
    return f'{determiner} {entity}'
