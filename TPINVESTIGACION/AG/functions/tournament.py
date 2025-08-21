# tournament.py
# Algoritmo de torneo para selección de padres aptos.

import random

from individual import Individual
from config import POPULATION_SIZE, TOURNAMENT_PERCENTAGE

#Selecciona posibles padres a partir de realizar un torneo entre el 40% de la población en el cual gana el individuo que mayor fitness
def tournament(population: list[Individual]) -> list[Individual]:
    
    selectedPossibleParents: list[Individual] = []

    while len(selectedPossibleParents): # realizamos varios torneos hasta tener la cantidad necesaria
        contestants: list[Individual] = [] # contiene los participantes de un torneo
        r = int(POPULATION_SIZE * TOURNAMENT_PERCENTAGE) # Tamaño de población * Porcentaje de torneo = Cant participantes (40%)
        maxFitness = 0
        winner: Individual

        for _ in range(0, r): # se seleccionan los participantes aleatoriamente
            i = random.randint(0, len(population) - 1)
            contestants.append(population[i])

        for contestant in contestants: # se realiza un torneo, el ganador es aquel con mayor fitness
            if contestant.fitness > maxFitness:
                maxFitness = contestant.fitness
                winner = contestant
        selectedPossibleParents.append(winner) # el ganador del torneo puede reproducirse

    return selectedPossibleParents