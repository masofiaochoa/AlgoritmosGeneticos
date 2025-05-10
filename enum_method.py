from enum import Enum

class Method(Enum):
    """
    Enum class for different methods of chromosome selection.
    """
    ROULETTE: int = 1
    TOURNAMENT: int  = 2