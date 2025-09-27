import random
from typing import List
from capitalRoute import CapitalRoute
from config import REMAINDER_POPULATION

def accumulateProportions(proportions: List[float]) -> List[float]:
    #Acumula los valores de la lista para generar la ruleta
    cumulativeProportions: List[float] = []
    acc = 0.0
    for p in proportions:
        acc += p
        cumulativeProportions.append(acc)
    return cumulativeProportions

#Selección por ruleta proporcional al fitness.
def roulette(population: List[CapitalRoute]) -> List[CapitalRoute]:
    selectedPossibleParents: List[CapitalRoute] = []

    #Obtener los fitness y normalizar
    fitnessValues = [ind.fitness for ind in population]
    totalFitness = sum(fitnessValues)
    if totalFitness == 0:
        # Si todos los fitness son 0, seleccionamos aleatoriamente
        normalizedFitness = [1/len(population)] * len(population)
    else:
        normalizedFitness = [f/totalFitness for f in fitnessValues]

    #Generar la ruleta acumulativa
    cumulativeProportions = accumulateProportions(normalizedFitness)  # último valor = 1

    #Seleccionar individuos
    while len(selectedPossibleParents) < REMAINDER_POPULATION:
        r = random.random()  # número entre 0 y 1
        for i, cp in enumerate(cumulativeProportions):
            if r <= cp:
                selectedPossibleParents.append(population[i])
                break

    return selectedPossibleParents
