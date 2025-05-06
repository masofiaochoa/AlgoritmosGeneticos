import math
import random

from individual import Individual
from enum_method import Method
from roulette import roulette

def selectPossibleParents(method: Method, population: list[Individual], fitnesses: list[float]) -> list[Individual]:
    selectedPossibleParents: list[Individual] = []
    if method == Method.method1:
        selectedPossibleParents = roulette(population, fitnesses)
    elif method == Method.method2:
        # selectedPossibleParents = tournament(population, fitness)
        pass

    return selectedPossibleParents;

