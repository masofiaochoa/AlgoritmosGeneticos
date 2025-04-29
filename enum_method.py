from enum import Enum

class Method(Enum):
    """
    Enum class for different methods of chromosome selection.
    """
    # Data processing methods
    method1 = "Roulette"
    method2 = "Tournament"