from enum import Enum, auto


class Action(Enum):
    """Class representing the actions used in input handlers"""

    LOOK = auto()
    IDLE = auto()
    QUIT = auto()
    DROP = auto()
    WEAR = auto()
    TAKE = auto()
    TAKE_OFF = auto()
    INVENTORY = auto()
    STATISTICS = auto()
