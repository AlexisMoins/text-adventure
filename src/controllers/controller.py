from abc import ABC, abstractmethod


class Controller(ABC):
    """Class representing a generic controller"""

    @abstractmethod
    def run(self) -> None:
        """Run the current controller"""
        pass

    @abstractmethod
    def handle_action(self, action: Action) -> None:
        """Handle the action received by the engine"""
        pass
