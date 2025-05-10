import math
import random

from config import *
from individual import Individual
from enum_method import Method
from roulette import roulette

def selectPossibleParents(method: Method, population: list[Individual]) -> list[Individual]:
    
    selectedPossibleParents: list[Individual] = []
    
    if method == Method.ROULETTE:
        selectedPossibleParents = roulette(population, REMAINDER_POPULATION)
    elif method == Method.TOURNAMENT:
        # selectedPossibleParents = tournament(population, REMAINDER_POPULATION)
        pass

    return selectedPossibleParents;

