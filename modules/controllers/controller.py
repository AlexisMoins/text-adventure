from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod

from modules.factories import view_factory, controller_factory

from modules.views.view import View
from modules.controllers.actions import Action


class Controller(ABC):
    """Class representing a generic controller"""

    def __init__(self, views: List[str], controllers: List[str]) -> None:
        """Parameterised constructor creating a new controller"""
        self._controllers = {controller: controller_factory.get(controller)
                             for controller in controllers}

        self._views = {view: view_factory.get(view)
                       for view in views}

    def view(self, name: str) -> View:
        """Return the view corresponding to the given name"""
        return self._views[name] if name in self._views.keys() else None

    def controller(self, name: str) -> Controller:
        """Return the controller corresponding to the given name"""
        return self._controllers[name] if name in self._controllers.keys() else None

    @abstractmethod
    def initialize(self) -> None:
        """Initialize the current controller"""
        pass

    @abstractmethod
    def run(self) -> None:
        """Run the current controller"""
        pass

    @abstractmethod
    def handle_action(self, action: Action) -> None:
        """Handle the action received by the engine"""
        pass
