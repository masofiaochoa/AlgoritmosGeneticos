import math
from typing import List, Tuple
from config import GRID_CELL_SIZE


def calculatePathLength(path: List[Tuple[int,int]]) -> float:
    """
    Calcula la longitud total de un path.
    Cada celda es un cuadrado de LxL metros
    Diagonales se cuentan como sqrt(L^2 + L^2).
    """
    if not path or len(path) == 1:
        return 0.0
    
    length: float = 0.0
    for i in range(1, len(path)):
        currentRow, currentCol = path[i-1]
        nextRow, nextCol = path[i]
        dr = abs(nextRow - currentRow)
        dc = abs(nextCol - currentCol)
        if dr == 1 and dc == 1:
            # diagonal
            length += math.sqrt((GRID_CELL_SIZE**2) + (GRID_CELL_SIZE**2))
        else:
            # horizontal o vertical
            length += GRID_CELL_SIZE
    return length