# functions/generatePopulation.py
# Genera población inicial usando cromosomas como rutas explícitas (lista de celdas).
# - Parte de seeds Manhattan y random walks sesgados.
# - Aplica pequeñas perturbaciones y reconexión greedy si hace falta.
# - Calcula targetFunction y fitness para cada individuo.

import random
from typing import Tuple, Optional

from config import (
    POPULATION_SIZE,
    FRACTION_WITH_MANHATTAN_PATH,
    RNG_SEED,
    GRID_ROWS,
    GRID_COLS,
    USE_DIAGONALS,
    MAX_INITIAL_DETOURS,         # ej. 2     (cantidad de “desvíos” a insertar)
    MAX_GREEDY_CONNECT_STEPS,    # ej. 4*max(GRID_ROWS, GRID_COLS)
    USE_DIAGONALS,               # bool: si permitís 8-vecinos
)

from individual import Individual
from grid import Grid
from functions.targetFunction import targetFunction
from functions.testFitness import testFitness

from helpers.neighbors import neighbors
from helpers.insertDetours import insertDetours
from helpers.greedyConnect import greedyConnect
from helpers.stepTowards import stepTowards

# -----------------------------
# Generadores de caminos
# -----------------------------

# Generador de path estilo manhattan
def _manhattan_path(start: Tuple[int,int], goal: Tuple[int,int]) -> list[Tuple[int,int]]:
    """
    Camino basico. Se mueve primero en filas y luego en columnas. Genera un camino en L.
    """
    (r0, c0), (r1, c1) = start, goal
    path = [(r0, c0)]
    r, c = r0, c0
    dr = 1 if r1 > r0 else -1
    while r != r1:
        r += dr
        path.append((r, c))
    dc = 1 if c1 > c0 else -1
    while c != c1:
        c += dc
        path.append((r, c))
    return path

def _random_walk_biased(grid: Grid, start: Tuple[int,int], goal: Tuple[int,int], max_steps: int) -> list[Tuple[int,int]]:
    """
    Random walk con sesgo: con alta prob. elige vecino que acerca al goal; con baja, explora.
    Termina si llega a goal o si agota max_steps. Si no llega, el caller intentará reconectar.
    """
    path = [start]
    pos = start
    for _ in range(max_steps):
        if pos == goal:
            break
        nbrs = neighbors(grid, pos, USE_DIAGONALS)
        if not nbrs:
            break
        # 50%: paso que acerca; 50%: random
        if random.random() < 0.5:
            nxt = stepTowards(goal, nbrs)
        else:
            nxt = random.choice(nbrs)
        if nxt == pos:
            break
        path.append(nxt)
        pos = nxt
    return path

# Checkeador de camino
def _ensure_start_goal(path: list[Tuple[int,int]], start: Tuple[int,int], goal: Tuple[int,int]) -> list[Tuple[int,int]]:
    if not path or path[0] != start:
        path = [start] + path
    if path[-1] != goal:
        path = path + [goal]
    return path


# -----------------------------
# Población inicial (principal)
# -----------------------------

def generateInitialPopulation(grid: Grid, model) -> list[Individual]:
    """
    Genera POPULATION_SIZE individuos donde cada cromosoma es un PATH (lista de celdas).
    - Un porcentaje se inicializa con path Manhattan + pequeños desvíos.
    - El resto con random walks sesgados + reconexión greedy si es necesario.
    - Evalúa targetFunction y fitness para cada individuo.
    """
    random.seed(RNG_SEED)

    population: list[Individual] = []
    start = grid.start()
    goal = grid.goal()
    n_seeded = int(round(FRACTION_WITH_MANHATTAN_PATH * POPULATION_SIZE))
    max_steps_rw = (GRID_ROWS + GRID_COLS) * 2  # cota razonable para random walk inicial

    for i in range(POPULATION_SIZE):
        if i < n_seeded:
            # Seed determinista + variación local
            base = _manhattan_path(start, goal)
            varied = insertDetours(grid, base, goal, MAX_INITIAL_DETOURS)
            path = _ensure_start_goal(varied, start, goal)
        else:
            # Random walk con sesgo + reconexión si hace falta
            rw = _random_walk_biased(grid, start, goal, max_steps_rw)
            if rw[-1] != goal:
                tail = greedyConnect(grid, rw[-1], goal, MAX_GREEDY_CONNECT_STEPS)
                if tail and tail[-1] == goal:
                    rw = rw + tail
                else:
                    # Si igual no llegó, como fallback usa Manhattan (garantiza validez)
                    rw = _manhattan_path(start, goal)
            path = _ensure_start_goal(rw, start, goal)

        # Evaluación
        tfv = targetFunction(path, model)
        targetFunction_total += tfv

        population.append(Individual(path=path, targetFunctionValue=tfv, fitness=None))
    
    for i in range(POPULATION_SIZE):  # Calcular fitness de cada individuo
        individual = population[i]
        individual.fitness = testFitness(individual.path, model)

    return population
