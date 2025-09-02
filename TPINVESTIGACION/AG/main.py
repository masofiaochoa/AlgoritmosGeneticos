# main.py — Genetic Algorithm (GA) for fastest path on a grid (matrix of 25 m cells)
# ----------------------------------------------------------------------------
# This is a skeleton to wire your GA loop with a grid-based path-planning problem
# that uses your previously trained ML model (ridge_model) to estimate per-step time.
# Fill the TODOs in the referenced modules. Keep APIs stable so main.py stays simple.
# ----------------------------------------------------------------------------

# IMPORTS
import random
import statistics as st
import copy

# Los imports de sys, pathlib son para poder importar la clase Model de mainML.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from individual import Individual  # must expose: chromosome, targetFunctionValue, fitness
from config import (               # centralizes all tunables
    POPULATION_SIZE,
    TARGET_GENERATION,
    TARGET_FITNESS,
    SELECTION_METHOD,
    CROSSOVER_CHANCE,
    MUTATION_CHANCE,
    ELITISM_CHOSEN_INDIVIDUAL_AMOUNT,
    REMAINDER_POPULATION,

    GRID_COLS,
    GRID_ROWS,
    GRID_CELL_SIZE,
    GRID_START,
    GRID_GOAL
)

# Grid + scenario adapters (no logic here, just facades)
from grid import Grid         # grid with cell_size, bounds, obstacles, currents, wind
from mainML import Model

# GA utilities (you can replace internals without touching main.py)
from functions.generateInitialPopulation import generateInitialPopulation
from functions.selectPossibleParents import selectPossibleParents
from functions.crossover import crossover
from functions.mutate import mutate
from functions.testFitness import testFitness
from functions.targetFunction import targetFunction  # must return a score (higher is better)
from functions.printCurrentGen import printCurrentGen

from functions.helpers.calculatePathLength import calculatePathLength

# ----------------------------------------------------------------------------
# GLOBAL STATE
# ----------------------------------------------------------------------------
POPULATION: list[Individual] = []
GENERATION: int = 0

MAXIMUMS: list[float] = []
MINIMUMS: list[float] = []
AVERAGES: list[float] = []

# ----------------------------------------------------------------------------
# Inicialización básica
# ----------------------------------------------------------------------------

def bootstrap() -> tuple[Grid, Model]:
    # 1) Construir la grilla que usaremos como simplificación del entorno.

    grid = Grid(rows=GRID_ROWS, cols=GRID_COLS, cell_size=GRID_CELL_SIZE,
            start=GRID_START, goal=GRID_GOAL)

    # 2) Cargar el modelo de machine learning a la clase Model.
    model = Model()

    return grid, model

# ----------------------------------------------------------------------------
# INITIAL POPULATION
# ----------------------------------------------------------------------------

def initialize_population(grid: Grid, model: Model) -> None:
    global POPULATION

    initial = generateInitialPopulation(grid=grid, model=model)
    POPULATION.extend(initial)

    # Sort por fitness ascendente
    POPULATION.sort(key=lambda ind: ind.fitness, reverse=True)

    # Bookkeeping
    MINIMUMS.append(POPULATION[-1].fitness)
    MAXIMUMS.append(POPULATION[0].fitness)
    AVERAGES.append(st.mean(ind.fitness for ind in POPULATION))

    printCurrentGen(0, POPULATION, MINIMUMS[-1], MINIMUMS[-1])

def evolve_generation(grid: Grid, model: Model) -> None:
    global POPULATION, GENERATION

    # Ensure sorted
    POPULATION.sort(key=lambda ind: ind.fitness, reverse=True)

    next_generation: list[Individual] = []

    # 1) Selección de padres
    possible_parents = selectPossibleParents(POPULATION)

    # 2) Crossover
    for i in range(0, REMAINDER_POPULATION, 2):
        parents = [possible_parents[i], possible_parents[i + 1]]
        if random.random() <= CROSSOVER_CHANCE:
            children = crossover(parents)
        else:
            children = [copy.deepcopy(parents[0]), copy.deepcopy(parents[1])]
        next_generation.extend(children)

    # 3) Mutación
    for idx in range(len(next_generation)):
        if random.random() <= MUTATION_CHANCE:
            next_generation[idx] = mutate(next_generation[idx], grid)

    # 4) Elitismo
    for i in range(ELITISM_CHOSEN_INDIVIDUAL_AMOUNT):
        next_generation.append(POPULATION[i].clone())

    # 5) reemplazar poblacion
    POPULATION = next_generation

    # 6) Recompute objective score and fitness for all individuals
    #    IMPORTANT: targetFunction must use the ML adapter + grid to simulate time.
    target_sum = 0.0
    for i in range(POPULATION_SIZE):
        pathDistance = calculatePathLength(POPULATION[i].path)
        POPULATION[i].pathDistance = pathDistance
        tfv = targetFunction(POPULATION[i], model=model)
        POPULATION[i].targetFunctionValue = tfv
        target_sum += tfv

    for i in range(POPULATION_SIZE):
        POPULATION[i].fitness = testFitness(POPULATION[i], target_sum)

    # 7) Generation ++ and statistics
    GENERATION += 1
        # Sort descending by target function (score)

    POPULATION.sort(key=lambda ind: ind.fitness, reverse=True)

    MAXIMUMS.append(POPULATION[0].fitness)
    MINIMUMS.append(POPULATION[-1].fitness)
    AVERAGES.append(st.mean(ind.fitness for ind in POPULATION))

    printCurrentGen(GENERATION, POPULATION, MINIMUMS[-1], MAXIMUMS[-1])

# ----------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------

def main() -> None:
    grid, model = bootstrap()
    initialize_population(grid, model)

    # Stop either by generation limit or by reaching a target score threshold
    while GENERATION < TARGET_GENERATION and MAXIMUMS[-1] < TARGET_FITNESS:
        evolve_generation(grid, model)



if __name__ == "__main__":
    main()