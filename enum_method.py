from enum import Enum

class Method(Enum):
    """
    Enum class for different methods of chromosome selection.
    """
    ROULETTE = 1
    TOURNAMENT = 2