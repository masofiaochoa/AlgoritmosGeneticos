# greedyConnect.py

from grid import Grid
from typing import Tuple

from neighbors import neighbors
from stepTowards import stepTowards

def greedyConnect(grid: Grid, current: Tuple[int,int], goal: Tuple[int,int], max_steps: int) -> list[Tuple[int,int]]:
    """
    Conector corto: desde `current` da pasos que acercan al `goal`.
    Si queda bloqueado antes de max_steps y no llega, devuelve lo que haya (caller decide).
    """
    path = []
    pos = current
    steps = 0
    while pos != goal and steps < max_steps:
        nbrs = neighbors(grid, pos)
        if not nbrs:
            break
        nxt = stepTowards(goal, nbrs)
        if nxt is None or nxt == pos:
            break
        path.append(nxt)
        pos = nxt
        steps += 1
    return path  # puede o no llegar; el caller puede volver a intentar o aceptar el resultado parcial