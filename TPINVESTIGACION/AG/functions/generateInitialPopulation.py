# functions/generatePopulation.py

import random
from typing import List, Tuple, Iterable
import numpy as np

from ..config import (
    POPULATION_SIZE,
    RNG_SEED,
    GRID_ROWS,
    GRID_COLS,
    GRID_START,
    GRID_GOAL,
    INITIAL_NOISE_PROB,        # p.ej. 0.08 -> 8% de celdas flip
    FRACTION_SEEDED_WITH_PATH, # p.ej. 0.6 -> 60% individuos contienen un camino semilla
)
from ..individual import Individual
from ..grid import Grid

# Importa las funciones de scoring que ya tenés
from ..functions.targetFunction import targetFunction
from ..functions.testFitness import testFitness

# -------------------------
# Helpers
# -------------------------
def _empty_matrix(rows: int, cols: int) -> List[List[int]]:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def _manhattan_path(start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Genera una ruta Manhattan simple (primer mueve en rows luego en cols).
    Devuelve la lista de celdas (r,c) que forman el camino, incluyendo start y goal.
    """
    (r0, c0), (r1, c1) = start, goal
    path = []
    r, c = r0, c0
    path.append((r, c))
    # mover en filas
    dr = 1 if r1 > r0 else -1
    while r != r1:
        r += dr
        path.append((r, c))
    # mover en columnas
    dc = 1 if c1 > c0 else -1
    while c != c1:
        c += dc
        path.append((r, c))
    return path


def _apply_noise_to_matrix(mat: List[List[int]], noise_prob: float, grid: Grid) -> None:
    """
    Invierte el valor de las celdas con probabilidad noise_prob, excepto start/goal and obstacles.
    Modifica la matriz en-place.
    """

    for r in GRID_ROWS:
        for c in GRID_COLS:
            if (r, c) == GRID_START or (r, c) == GRID_GOAL:
                continue
            # no permitir 1 en obstaculos
            if grid.is_obstacle((r, c)):
                mat[r][c] = 0
                continue
            if random.random() < noise_prob:
                mat[r][c] = 1 - mat[r][c]  # flip


def _force_path_into_matrix(mat: List[List[int]], path: Iterable[Tuple[int, int]]) -> None:
    """Asegura que las celdas en `path` tengan valor 1."""
    for (r, c) in path:
        mat[r][c] = 1

def _ensure_connectivity_by_repair(mat: List[List[int]], grid: Grid) -> None:
    """
    Reparador simple: si no hay camino entre start y goal, conecta componentes activando
    las celdas de una Manhattan path (puede sobrescribir obstáculos si lo preferís).
    Preferimos no tocar obstáculos; en ese caso la reparación usa path ignorando obstáculos
    y activa celdas que no estén marcadas ni como obstáculos.
    """
    # Construir grafo simple mediante BFS sobre celdas con 1
    start = GRID_START
    goal = GRID_GOAL

    # BFS para ver si existe camino
    from collections import deque

    rows = GRID_ROWS
    cols = GRID_COLS
    visited = [[False] * cols for _ in range(rows)]
    q = deque()
    if mat[start[0]][start[1]] == 1:
        q.append(start)
        visited[start[0]][start[1]] = True

    found = False
    while q:
        r, c = q.popleft()
        if (r, c) == goal:
            found = True
            break
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and mat[nr][nc] == 1:
                visited[nr][nc] = True
                q.append((nr, nc))

    if found:
        return  # ya hay conectividad

    # Si no se encontró camino, forzamos una Manhattan path (sin tocar obstáculos si es posible)
    path = _manhattan_path(start, goal)
    for (r,c) in path:
        # si la celda es obstáculo, saltarla (no sobreescribir). En ese caso la reparación puede fallar,
        # pero la estrategia alternativa puede ser habilitar la celda aún siendo obstáculo (si querés).
        if not grid.is_obstacle((r,c)):
            mat[r][c] = 1
    # Nota: tras forzar la path, la conectividad debería existir (si no había obstáculos sobre la path).

# -------------------------
# Función principal
# -------------------------
def generateInitialPopulation(grid: Grid, model) -> List[Individual]:
    """
    Genera POPULATION_SIZE individuos. Cada cromosoma es una matriz binaria.
    """
    population: List[Individual] = []
    rows = GRID_ROWS
    cols = GRID_COLS

    # Cantidad de individuos que iniciamos con el camino semilla garantizado
    n_seeded = int(round(FRACTION_SEEDED_WITH_PATH * POPULATION_SIZE))

    for i in range(POPULATION_SIZE):
        # 1) crear matriz vacía
        mat = _empty_matrix(rows, cols)

        # 2) si estamos en la fracción seeded, forzamos una Manhattan path base
        if i < n_seeded:
            base_path = _manhattan_path(grid.start(), grid.goal())
            _force_path_into_matrix(mat, base_path)

        # 3) aplicar ruido (flips) para diversidad
        _apply_noise_to_matrix(mat, INITIAL_NOISE_PROB, grid)

        # 4) aseguramos que start y goal sean 1
        sr, sc = GRID_START
        gr, gc = GRID_GOAL
        mat[sr][sc] = 1
        mat[gr][gc] = 1

        # 5) forzamos 0s en obstaculos
        for r in range(rows):
            for c in range(cols):
                if grid.is_obstacle((r, c)):
                    mat[r][c] = 0

        # 6) reparar si no hay conectividad
        _ensure_connectivity_by_repair(mat, grid)

        # 7) calcular targetFunction y fitness (se espera que targetFunction acepte matriz)
        #    Nota: targetFunction debe decodificar la matriz a ruta (por ejemplo construyendo
        #    un grafo con las celdas 1 y buscando el shortest path en tiempo).
        tfv = targetFunction(mat, grid=grid, model=model)
        fit = testFitness(mat, tfv)

        # 8) crear Individual y añadir
        ind = Individual(chromosome=mat, targetFunctionValue=tfv, fitness=fit)
        population.append(ind)

    return population
