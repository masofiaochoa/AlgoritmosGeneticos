# neighbors.py
# Define los vecinos válidos dado una celda

from typing import Tuple
from grid import Grid

def neighbors(grid: Grid, currentGridPosition: Tuple[int, int]) -> list[Tuple[int, int]]:
    currentGridRow, currentGridColumn = currentGridPosition
    validDirections = [(1,0), (-1,0), (0,1), (1,1), (-1, 1)] #Solo se permiten movimientos verticales, horizontales hacia la derecha o diagonales hacia la derecha
    neighboringPositions = []
  
    for directionRow, directionColum in validDirections:
        nr, nc = currentGridRow + directionRow, currentGridColumn + directionColum
        nextPossibleGridPosition = (nr, nc)
        if grid.in_bounds(nextPossibleGridPosition):
            neighboringPositions.append(nextPossibleGridPosition)
    return neighboringPositions