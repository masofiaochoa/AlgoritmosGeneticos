import random

from individual import Individual
from config import *

def tournament(population: list[Individual]) -> list[Individual]:
    
    selectedPossibleParents: list[Individual] = []

    while (len(selectedPossibleParents) < REMAINDER_POPULATION): # realizamos varios torneos hasta tener la cantidad necesaria
        contestants: list[Individual] = [] # contiene los participantes de un torneo
        r = int(POPULATION_SIZE * TOURNAMENT_PERCENTAGE) # número de participantes (40%)
        maxFitness = 0
        winner: Individual = Individual
        
        print("selecciono", r)

        for _ in range(0, r): # se seleccionan los participantes aleatoriamente
            i = random.randint(0, len(population)-1)
            print("appendeo al numero", i)
            contestants.append(population[i])

        print("tengo estos contestants: ")
        for contestant in contestants: print(contestant.chromosome)
        print("hago torneo")

        for contestant in contestants: # se realiza un torneo, el ganador es aquel con mayor fitness
            if contestant.fitness > maxFitness:
                maxFitness = contestant.fitness
                winner = contestant
        print("el ganador de este torneo tiene: ", winner.chromosome, winner.fitness)
        selectedPossibleParents.append(winner) # el ganador del torneo puede reproducirse

    print("terminamos con ")
    for winner in selectedPossibleParents: print(winner.chromosome)

    return selectedPossibleParents