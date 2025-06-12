#IMPORTS
import copy
import random
import statistics as st

from individual import Individual

from config import *

from functions.testFitness import testFitness
from functions.selectPossibleParents import selectPossibleParents
from functions.crossover import crossover
from functions.mutate import mutate
from functions.printCurrentGen import printCurrentGen
from functions.targetFunction import targetFunction
from functions.generatePopulation import generateInitialPopulation
from plots.plot_utils import drawGenData, generateTable

#VARIABLES GLOBALES
POPULATION: list[Individual] = [];
GENERATION: int = 0;

MAX_FITNESS: float = 0.0
MIN_FITNESS: float = 1.0

MAXIMUMS: list[Individual] = []
MINIMUMS: list[Individual] = []
AVERAGES: list[float] = []

TARGET_FITNESS: float = 0.95 #Fitness objetivo del while loop
TARGET_GENERATION: int = 200  #Generacion objetivo del while loop

TARGET_FUNCTION_TOTAL: float = 0.0 #Total de la funcion objetivo para calcular el fitness de cada individuo 

#Variable auxiliares para llevar la cuenta de maximos y minimos
maxTargetFunctionValue: float = 0
minTargetFunctionValue: float = 1

#PROGRAMA

#GENERAR POBLACIÓN INICIAL Y REALIZAR CALCULOS SOBRE LA MISMA
initialPopulation: list[Individual] = generateInitialPopulation()
POPULATION.extend(initialPopulation)


#Maximos y minimos de f. objetivo generacionales
maxTargetFunctionValue = POPULATION[0].targetFunctionValue
MAXIMUMS.append(POPULATION[0])

minTargetFunctionValue = POPULATION[-1].targetFunctionValue
MINIMUMS.append(POPULATION[-1])

#Promedio generacional
AVERAGES.append(st.mean([ind.targetFunctionValue for ind in POPULATION]))

#imprimo generacion actual
printCurrentGen(GENERATION, POPULATION, maxTargetFunctionValue, minTargetFunctionValue) #Para imprimir la población inicial

#LOOP PRINCIPAL PARA LAS GENERACIONES POSTERIORES A LA INICIAL
while(GENERATION < TARGET_GENERATION):
    POPULATION = sorted(POPULATION, key = lambda individual: individual.targetFunctionValue, reverse = True)
    nextGeneration: list[Individual] = [];
    maxTargetFunctionValue: float = 0
    minTargetFunctionValue: float = 1 

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

    #Calculo de función objetivo para cada individuo
    for i in range(POPULATION_SIZE):
        newTargetFunctionValue: float = targetFunction(POPULATION[i].chromosome)
        POPULATION[i].targetFunctionValue = newTargetFunctionValue
        TARGET_FUNCTION_TOTAL += newTargetFunctionValue

    #Calculo de funcion fitness para cada individuo
    for i in range(POPULATION_SIZE): #calculo el fitness de cada individuo
        newFitness: float = testFitness(POPULATION[i], TARGET_FUNCTION_TOTAL)
        POPULATION[i].fitness = newFitness

    GENERATION += 1;

    # Ordeno el arreglo de individuos (población) de mayor a menor según fitness
    POPULATION = sorted(POPULATION, key = lambda individual: individual.targetFunctionValue, reverse = True)
    
    #Maximos y minimos de f. objetivo generacionales
    maxTargetFunctionValue = POPULATION[0].targetFunctionValue
    MAXIMUMS.append(copy.deepcopy(POPULATION[0]))

    minTargetFunctionValue = POPULATION[-1].targetFunctionValue
   
    MINIMUMS.append(copy.deepcopy(POPULATION[-1]))

    #Promedio generacional
    AVERAGES.append(st.mean([ind.targetFunctionValue for ind in POPULATION]))

    #Muestro los datos de la generación actual

    printCurrentGen(GENERATION, POPULATION, maxTargetFunctionValue, minTargetFunctionValue)

    maxTargetFunctionValue: float = 0
    minTargetFunctionValue: float = 1

#Luego de finalizar el programa principal, muestro las graficas y tablas correspondientes con los datos de todas las generaciones
drawGenData(MAXIMUMS, MINIMUMS, AVERAGES)
generateTable(MAXIMUMS, MINIMUMS, AVERAGES)
