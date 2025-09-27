import random

from capitalRoute import CapitalRoute
from config import *

#Selecciona posibles padres a partir de realizar un torneo entre el 40% de la población en el cual gana el individuo que mayor fitness
def tournament(population: list[CapitalRoute]) -> list[CapitalRoute]:
    
    selectedPossibleParents: list[CapitalRoute] = []

    while (len(selectedPossibleParents) < REMAINDER_POPULATION): # realizamos varios torneos hasta tener la cantidad necesaria
        contestants: list[CapitalRoute] = [] # contiene los participantes de un torneo
        r = int(POPULATION_SIZE) # Tamaño de población * Porcentaje de torneo = Cant participantes (40%)
        maxFitness = 0
        winner: CapitalRoute

        for _ in range(0, r): # se seleccionan los participantes aleatoriamente
            i = random.randint(0, len(population) - 1)
            contestants.append(population[i])

        for contestant in contestants: # se realiza un torneo, el ganador es aquel con mayor fitness
            if contestant.fitness > maxFitness:
                maxFitness = contestant.fitness
                winner = contestant
        
        selectedPossibleParents.append(winner) # el ganador del torneo puede reproducirse

    return selectedPossibleParents