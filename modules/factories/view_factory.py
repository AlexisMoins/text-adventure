from typing import Dict, Callable, Any, Protocol

from modules.views.item_view import ItemView


class View(Protocol):
    """Class representing a generic view"""
    entity: Any

    def display(self) -> None:
        """Display the current view"""
        pass


"""List of views types and their corresponding class"""
views: Dict[str, Callable] = dict()


def get(entity: Any) -> View | None:
    """Return the view corresponding to the given entity"""
    key = type(entity).__name__
    return views[key] if key in views.keys() else None


def register(view_type: str, view: Callable) -> None:
    """Add a view type and its corresponding class to the dictionary of views"""
    views[view_type] = view()
