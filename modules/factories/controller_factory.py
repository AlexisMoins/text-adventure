from typing import Any, Dict, Callable

from modules.controllers.item_controller import ItemController


"""List of views types and their corresponding class"""
controllers: Dict[str, Callable] = dict()


def get(controller_type: str) -> Any:
    """Return the view corresponding to the given entity"""
    return controllers[controller_type] if controller_type in controllers.keys() else None


def register(controller_type: str, controller: Callable) -> None:
    """Add a controller type and its corresponding class to the dictionary of controllers"""
    controllers[controller_type] = controller()


register('item', ItemController)
