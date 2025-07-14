from config import *
from individual import Individual
from enum_method import Method
from .roulette import roulette
from .tournament import tournament

#Dependiendo el metodo de selección de padres elegidos (Ruleta | torneo) define la función a utilizarse
def selectPossibleParents(method: Method, population: list[Individual]) -> list[Individual]:
    
    selectedPossibleParents: list[Individual] = []
    
    if method == Method.ROULETTE:
        selectedPossibleParents = roulette(population)
    elif method == Method.TOURNAMENT:
        selectedPossibleParents = tournament(population)

    return selectedPossibleParents;

