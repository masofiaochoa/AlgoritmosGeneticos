import random

from config import *
from individual import Individual
from .targetFunction import targetFunction
from .testFitness import testFitness


def generateInitialPopulation():
    initialPopulation: list[Individual] = []
    TARGET_FUNCTION_TOTAL: float = 0.0
    maxTargetFunctionValue: float = 1
    minTargetFunctionValue: float = 0

    for _ in range(POPULATION_SIZE):
        newChromosome: int = random.randint(0, 2**CHROMOSOME_LEN - 1) #genero un numero binario que como maximo sea 2 elevado a el largo del cromosoma - 1 (Ej si es un cromosoma de 3, el maximo numero representable es 2^2 + 2^1 + 2^0 = 2^3 - 1)
        newTargetFunctionValue: float = targetFunction(newChromosome)
        TARGET_FUNCTION_TOTAL += newTargetFunctionValue #Acumulo el total de la funcion objetivo para calcular el fitness de cada individuo
        initialPopulation.append(Individual(newChromosome, newTargetFunctionValue, None))


    for _ in range(POPULATION_SIZE): #calculo el fitness de cada individuo
        initialPopulation[_].fitness = testFitness(initialPopulation[_], TARGET_FUNCTION_TOTAL)

    # Ordeno el arreglo de individuos (población) de mayor a menor según fitness
    initialPopulation = sorted(initialPopulation, key = lambda individual: individual.fitness, reverse = True)

    #COMPARATIVOS
    if(initialPopulation[0].targetFunctionValue > maxTargetFunctionValue):
        maxTargetFunctionValue = initialPopulation[_].targetFunctionValue
    if(initialPopulation[POPULATION_SIZE - 1].targetFunctionValue > minTargetFunctionValue):
        minTargetFunctionValue = initialPopulation[_].targetFunctionValue
    
    return initialPopulation
