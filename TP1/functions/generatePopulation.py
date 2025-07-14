import random

from config import *
from individual import Individual
from .targetFunction import targetFunction
from .testFitness import testFitness

#Genera la población inicial iterando una generación de cromosomas aleatorios por la cantidad de población y luego evaluando el fitness para cada uno de ellos
def generateInitialPopulation():
    initialPopulation: list[Individual] = []
    target_function_total: float = 0.0

    for _ in range(POPULATION_SIZE):
        newChromosome: int = random.randint(0, 2**CHROMOSOME_LEN - 1) #genero un numero binario que como maximo sea 2 elevado a el largo del cromosoma - 1 (Ej si es un cromosoma de 3, el maximo numero representable es 2^2 + 2^1 + 2^0 = 2^3 - 1)
        newTargetFunctionValue: float = targetFunction(newChromosome)
        target_function_total += newTargetFunctionValue #Acumulo el total de la funcion objetivo para calcular el fitness de cada individuo
        initialPopulation.append(Individual(newChromosome, newTargetFunctionValue, 0))


    for i in range(POPULATION_SIZE): #calculo el fitness de cada individuo
        initialPopulation[i].fitness = testFitness(initialPopulation[i], target_function_total)

    # Ordeno el arreglo de individuos (población) de mayor a menor según función objetivo
    initialPopulation = sorted(initialPopulation, key = lambda individual: individual.targetFunctionValue, reverse = True)
    
    return initialPopulation
