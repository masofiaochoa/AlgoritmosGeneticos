# mutate.py
# La idea es dado un individuo, mutar su camino de alguna manera para explorar nuevas soluciones.

import random
from typing import Tuple

from individual import Individual
from grid import Grid
from helpers.insertDetours import insertDetours

def mutate(individual: Individual, grid: Grid) -> Individual:
    # Se toma el path del individuo que mutaremos
    path_to_mutate = individual.path[:]
    
    mutated_path = insertDetours(path_to_mutate, grid)

    new_individual = Individual(path=mutated_path, targetFunctionValue=None, fitness=None)

    return new_individual