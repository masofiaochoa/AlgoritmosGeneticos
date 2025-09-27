from config import *
from capitalRoute import CapitalRoute
from enum_method import AG_Method
from .roulette import roulette
from .tournament import tournament

#Dependiendo el metodo de selección de padres elegidos (Ruleta | torneo) define la función a utilizarse
def selectPossibleParents(method: AG_Method, population: list[CapitalRoute]) -> list[CapitalRoute]:
    
    selectedPossibleParents: list[CapitalRoute] = []
    
    if method == AG_Method.ROULETTE:
        selectedPossibleParents = roulette(population)
    elif method == AG_Method.TOURNAMENT:
        selectedPossibleParents = tournament(population)

    return selectedPossibleParents;

