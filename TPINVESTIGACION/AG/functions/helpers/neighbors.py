# neighbors.py
# Define los vecinos válidos dado una celda y revisando si se permiten diagonales.

from typing import Tuple

from config import USE_DIAGONALS
from grid import Grid

def neighbors(grid: Grid, rc: Tuple[int, int]) -> list[Tuple[int, int]]:
    r, c = rc
    steps4 = [(1,0), (-1,0), (0,1), (0,-1)]
    steps8 = steps4 + [(1,1), (1,-1), (-1,1), (-1,-1)]
  
    deltas = steps8 if USE_DIAGONALS else steps4
    out = []
  
    for dr, dc in deltas:
        nr, nc = r + dr, c + dc
        nxt = (nr, nc)
        if grid.in_bounds(nxt) and not grid.is_obstacle(nxt):
            out.append(nxt)
    return out