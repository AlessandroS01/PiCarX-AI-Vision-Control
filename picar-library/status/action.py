from enum import Enum

class Action(Enum):
    """Enumeration for different actions that can be performed by the car."""
    FORWARD = 1,
    BACKWARD = 2,
    LEFT = 3,
    RIGHT = 4,
    STOP = 5