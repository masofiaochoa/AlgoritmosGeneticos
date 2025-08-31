# mutate.py
# La idea es dado un individuo, mutar su camino de alguna manera para explorar nuevas soluciones.

import copy
import random
from typing import Tuple


from config import GRID_GOAL
from individual import Individual
from grid import Grid
from functions.helpers.neighbors import neighbors

def mutate(individual: Individual, grid: Grid) -> Individual:
    mutantInd = copy.deepcopy(individual)
    
    if len(mutantInd.path) < 3:
        return mutantInd

    p = mutantInd.path
    
    i = random.randrange(1, len(mutantInd.path)-1)   # mutar nodo intermedio
    
    anchor_prev = p[i-1]
    anchor_next = p[i+1]

    neighbors_i = neighbors(grid, p[i])

    # Filtrar solo nodos que sean vecinos tanto del anterior como del siguiente y que no sean igual al nodo siguiente para evitar duplicados
    candidates = [n for n in neighbors_i
                if n in neighbors(grid, anchor_prev) 
                and anchor_next in neighbors(grid, n)
                and n != anchor_next]

    if not candidates:
        # No hay nodo intermedio que cumpla la condición, devolvemos el individuo original
        return mutantInd

    # Elegimos un candidato al azar y reemplazamos p[i]
    chosen = random.choice(candidates)
    mutantInd.replaceStepAtPos(chosen, i)

    return mutantInd