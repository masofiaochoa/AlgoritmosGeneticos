from capitalRoute import CapitalRoute
from config import *
from functions.AG.testFitness import testFitness

def getPopulationFitness(population: list[CapitalRoute]):
    targetFunctionTotal: float = 0.0
    targetFunctionTotal = sum(cp.distance for cp in population)
        
    for i in range(POPULATION_SIZE): #calculo el fitness de cada individuo
        population[i].fitness = testFitness(population[i], targetFunctionTotal)

    # Ordeno el arreglo de población de mayor a menor según función objetivo
    population = sorted(population, key = lambda individual: individual.distance)
    return population