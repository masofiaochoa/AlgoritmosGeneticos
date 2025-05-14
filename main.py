#IMPORTS
import random

from individual import Individual

from config import *

from functions.testFitness import testFitness
from functions.selectPossibleParents import selectPossibleParents
from functions.crossover import crossover
from functions.mutate import mutate
from functions.printCurrentGen import printCurrentGen
from functions.targetFunction import targetFunction
from functions.generatePopulation import generateInitialPopulation

#GLOBAL VARIABLES
POPULATION: list[Individual] = [];
GENERATION: int = 0;

MAX_FITNESS: float = 0.0
MIN_FITNESS: float = 1.0

TARGET_FITNESS: float = 0.95 #Fitness objetivo del while loop
TARGET_GENERATION: int = 20  #Generacion objetivo del while loop

TARGET_FUNCTION_TOTAL: float = 0.0 #Total de la funcion objetivo para calcular el fitness de cada individuo 

maxTargetFunctionValue: float = 0
minTargetFunctionValue: float = 1


#PROGRAM

#GENERATE INITIAL POPULATION
initialPopulation: list[Individual] = generateInitialPopulation()
POPULATION.extend(initialPopulation)

#COMPARATIVOS: esto deberia estar en la función de generateInitialPopulation, por prolijidad
#if(POPULATION[0].targetFunctionValue > maxTargetFunctionValue):
maxTargetFunctionValue = POPULATION[0].targetFunctionValue
#if(POPULATION[POPULATION_SIZE - 1].targetFunctionValue < minTargetFunctionValue):
minTargetFunctionValue = POPULATION[POPULATION_SIZE - 1].targetFunctionValue

printCurrentGen(GENERATION, POPULATION, maxTargetFunctionValue, minTargetFunctionValue) #para imprimir la población inicial

maxTargetFunctionValue: float = 1
minTargetFunctionValue: float = 0


#LOOP PRINCIPAL
while(GENERATION < TARGET_GENERATION):
    POPULATION = sorted(POPULATION, key = lambda individual: individual.fitness, reverse = True)
    nextGeneration: list[Individual] = [];
    maxTargetFunctionValue: float = 0
    minTargetFunctionValue: float = 0

 
    #SELECCIONAR POSIBLES PADRES
    possibleParents: list[Individual] = selectPossibleParents(SELECTION_METHOD, POPULATION);

   #CRUZA
    for i in range(0, REMAINDER_POPULATION, 2):
        parents: list[Individual] = [possibleParents[i], possibleParents[i + 1]]
        children: list[Individual] = []

        if(random.random() <= CROSSOVER_CHANCE):
            children = crossover(parents)
        else:
            children = parents

        nextGeneration.extend(children)

    #MUTACION
    for i in range(len(nextGeneration)):
        if(random.random() <= MUTATION_CHANCE):
            mutant: Individual = mutate(nextGeneration[i]);
            nextGeneration[i] = mutant;
    

    #ELITISMO
    for i in range(0, ELITISM_CHOSEN_INDIVIDUAL_AMOUNT):
        nextGeneration.append(POPULATION[i])

    #finalmente nuestra poblacion será esta nueva generación
    POPULATION = nextGeneration;

    TARGET_FUNCTION_TOTAL = 0.0 


    for _ in range(POPULATION_SIZE):
        newTargetFunctionValue: float = targetFunction(POPULATION[_].chromosome)
        POPULATION[_].targetFunctionValue = newTargetFunctionValue
        TARGET_FUNCTION_TOTAL += newTargetFunctionValue

    for _ in range(POPULATION_SIZE): #calculo el fitness de cada individuo
        newFitness: float = testFitness(POPULATION[_], TARGET_FUNCTION_TOTAL)
        POPULATION[_].fitness = newFitness

    GENERATION += 1;

    # Ordeno el arreglo de individuos (población) de mayor a menor según fitness
    POPULATION = sorted(POPULATION, key = lambda individual: individual.fitness, reverse = True)
    
    #COMPARATIVOS
    #if(initialPopulation[0].targetFunctionValue > maxTargetFunctionValue): 
    maxTargetFunctionValue = POPULATION[0].targetFunctionValue
    #if(initialPopulation[POPULATION_SIZE - 1].targetFunctionValue < minTargetFunctionValue):
    minTargetFunctionValue = POPULATION[POPULATION_SIZE - 1].targetFunctionValue

    printCurrentGen(GENERATION, POPULATION, maxTargetFunctionValue, minTargetFunctionValue)

    maxTargetFunctionValue: float = 0
    minTargetFunctionValue: float = 0
    

#print(f"Maximo fitness alcanzado: { MAX_FITNESS }")
#print(f"Minimo fitness alcanzado: { MIN_FITNESS }")