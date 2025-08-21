# selectPossibleParents.py
# Selección de algoritmo para selección de padres. Por ahora solo tournament

from config import SELECTION_METHOD
from individual import Individual
from .tournament import tournament

#Dependiendo el metodo de selección de padres elegidos (Ruleta | torneo) define la función a utilizarse
def selectPossibleParents(population: list[Individual]) -> list[Individual]:
    
    selectedPossibleParents: list[Individual] = []
    if SELECTION_METHOD == "tournament":  
      selectedPossibleParents = tournament(population)

    return selectedPossibleParents;

