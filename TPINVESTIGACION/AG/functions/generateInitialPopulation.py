# functions/generatePopulation.py
# Genera población inicial usando cromosomas como rutas explícitas (lista de celdas).
# - Parte de seeds Manhattan y random walks sesgados.
# - Aplica pequeñas perturbaciones y reconexión greedy si hace falta.
# - Calcula targetFunction y fitness para cada individuo.

from math import floor
import random
from typing import Tuple, Optional

from config import (
    POPULATION_SIZE,
    FRACTION_WITH_MANHATTAN_PATH,
    GRID_ROWS,
    GRID_COLS,
    GRID_CELL_SIZE,
    MAX_INITIAL_DETOURS,         # ej. 2     (cantidad de “desvíos” a insertar)
    MAX_GREEDY_CONNECT_STEPS,    # ej. 4*max(GRID_ROWS, GRID_COLS)
)

from individual import Individual
from grid import Grid
from functions.targetFunction import targetFunction
from functions.testFitness import testFitness

from .helpers.neighbors import neighbors
from .helpers.greedyConnect import greedyConnect
from .helpers.stepTowards import stepTowards


# -----------------------------
# Generadores de caminos
# -----------------------------

# Generador de path estilo manhattan
def manhattan_path_stepwise(ind: Individual, goal: Tuple[int, int]):
    """
    Genera un path en forma de L desde el último nodo del individuo hasta goal,
    agregando cada paso con addPathStep() para aplicar variaciones por corriente.
    """
    current_row, current_col = ind.path[-1]
    goal_row, goal_col = goal

    # Avanzar en filas
    row_step = 1 if goal_row > current_row else -1
    while current_row != goal_row:
        current_row += row_step
        ind.addPathStep((current_row, current_col))

    # Avanzar en columnas
    col_step = 1 if goal_col > current_col else -1
    while current_col != goal_col:
        current_col += col_step
        ind.addPathStep((current_row, current_col))



import random

def random_walk_biased_stepwise(ind: Individual, grid: Grid, goal: Tuple[int,int], max_steps: int):
    """
    Random walk con sesgo paso a paso:
    - 50% elige vecino que acerque al objetivo.
    - 50% elige vecino al azar.
    - Cada paso se agrega con addPathStep() para aplicar variaciones por corriente
    """
    current_pos = ind.path[-1]

    for _ in range(max_steps):
        if current_pos == goal:
            break

        neighbors_list = neighbors(grid, current_pos)

        if not neighbors_list:
            break
        
        if current_pos[1] !=  grid.goal[1]: #Si no estamos en la ultima columna entonces no permitir movimientos repetidos
            neighbors_list = [n for n in neighbors_list if n not in ind.path]
            
        # Elegir próximo paso
        if random.random() < 0.7:
            next_pos = stepTowards(goal, neighbors_list)
        else:
            next_pos = random.choice(neighbors_list)

        # Evitar quedarse en el mismo lugar
        if next_pos == current_pos:
            break

        # Agregar el paso al path y aplicar drift
        ind.addPathStep(next_pos)
        current_pos = next_pos



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

    population: list[Individual] = []
    start = grid.get_start()
    goal = grid.get_goal()
    n_seeded = int(round(FRACTION_WITH_MANHATTAN_PATH * POPULATION_SIZE))
    max_steps_rw = (GRID_ROWS + GRID_COLS) * 2  # cota razonable para random walk inicial
    target_function_total = 0

    for i in range(POPULATION_SIZE):
    
        ind = Individual(path=[start], pathDistance=0, targetFunctionValue=0, fitness=None)

        if i < n_seeded:
            manhattan_path_stepwise(ind, goal)
        else:
            random_walk_biased_stepwise(ind, grid, goal, max_steps_rw)
            # reconexión si no llegó
            if ind.path[-1] != goal:
                tail = greedyConnect(grid, ind.path[-1], goal, MAX_GREEDY_CONNECT_STEPS)
                if tail and tail[-1] == goal:
                    for step in tail[1:]:  # agregar cada paso al individuo
                        ind.addPathStep(step)
                else:
                    manhattan_path_stepwise(ind, goal)
        
        # Evaluación
        tfv = targetFunction(ind, model)
        
        ind.targetFunctionValue = tfv
        
        target_function_total += tfv

        population.append(ind)
    
    for i in range(POPULATION_SIZE):  # Calcular fitness de cada individuo
        individual = population[i]
        print(f"target function del individual = {individual.targetFunctionValue}\ntargetfunctionTotal: {target_function_total}\n\n")
        individual.fitness = testFitness(individual, target_function_total)

    return population
