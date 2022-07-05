from typing import Iterable, Iterator, MutableSequence, SupportsIndex

from src.models.entity import Entity


class Container(MutableSequence):
    """Represents a generic container for entities"""

    def __init__(self, iterable: Iterable = None) -> None:
        """Parameterised constructor creating a new Container"""
        self._entities = list(iterable) if iterable else list()

    def find(self, entity_name: str) -> Entity | None:
        """Return the entity matching the given name"""
        entities = [entity for entity in self._entities if entity_name in entity.name]
        return entities[0]

    def take(self, entity_name: str) -> Entity | None:
        """Return and remove the entity matching the given name from the container"""
        entity = self.find(entity_name)

        if entity is not None:
            self._entities.remove(entity)

        return entity

    def is_empty(self) -> bool:
        """Return true if this container is empty"""
        return (self._entities) == 0

    def __getitem__(self, *args) -> Entity:
        """Same as container[x]"""
        self._entities.__getitem__(*args)

    def __setitem__(self, *args) -> None:
        """Set self[key] to value"""
        self._entities.__setitem__(*args)

    def __delitem__(self, *args) -> None:
        """Delete self[key]"""
        self._entities.__delitem__(*args)

    def insert(self, index: SupportsIndex, entity: Entity) -> None:
        """Insert entity before index"""
        self._entities.insert(index, entity)

    def __contains__(self, entity: Entity) -> bool:
        """Return true if the given entity is in the container"""
        return self._entities.__contains__(entity)

    def __iter__(self) -> Iterator[Entity]:
        """Return an iterator over the entities in the container"""
        return self._entities.__iter__()

    def __len__(self) -> int:
        """Return the length of the container"""
        return self._entities.__len__()


class SizedContainer(Container):
    """Represents a generic sized container for entities"""

    def __init__(self, size: int, iterable: Iterable = None) -> None:
        """Parameterised constructor creating a new Container"""
        if iterable is not None and len(iterable) > size:
            raise Exception(f'Cannot create SizedContainer object of size {size} with iterable of size {len(iterable)}')

        self.size = size
        super().__init__(iterable)

    @property
    def indicator(self) -> str:
        """Return the indicator of the size of the container"""
        return f'{len(self._entities)}/{self.size}'

    def filter(self, action: str) -> Iterator[Entity]:
        """Return an iterator of entities that have the given action"""
        return filter(lambda entity: action in entity.actions, self._entities)

    def is_full(self) -> bool:
        """Return true if this container is full"""
        return len(self._entities) >= self.size

    def append(self, entity: Entity) -> None:
        """Add an entity to this container. Raise an exception is the container is full"""
        if self.is_full():
            raise Exception('SizeContainer object is full')

        self._entities.append(entity)
