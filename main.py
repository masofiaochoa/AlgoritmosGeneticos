#IMPORTS
import random

from individual import Individual

from config import *

from functions.testFitness import testFitness
from functions.selectPossibleParents import selectPossibleParents
from functions.crossover import crossover
from functions.mutate import mutate
from functions.printCurrentGen import printCurrentGen

#GLOBAL VARIABLES
POPULATION: list[Individual] = [];
GENERATION: int = 0;

MAX_FITNESS: float = 0.0
MIN_FITNESS: float = 1.0

TARGET_FITNESS: float = 0.95 #Fitness objetivo del while loop
TARGET_GENERATION: int = 20  #Generacion objetivo del while loop


#estrategia de mutacion: complemento del gen (0 a 1 y 1 a 0)
#Creo que aca se podría agregar un parametro 'strategy' y un parametro 'geneAmount' para hacerlo mas general (estrategias de mutacion y cantidad de genes a mutar)



#PROGRAM
#GENERATE INITIAL POPULATION
for _ in range(POPULATION_SIZE):
    newChromosome: int = random.randint(0, 2**CHROMOSOME_LEN - 1) #genero un numero binario que como maximo sea 2 elevado a el largo del cromosoma - 1 (Ej si es un cromosoma de 3, el maximo numero representable es 2^2 + 2^1 + 2^0 = 2^3 - 1)
    newFitness: float = testFitness(newChromosome)
    POPULATION.append(Individual(newChromosome, newFitness));

# Ordeno el arreglo de individuos (población) de mayor a menor según fitness
POPULATION = sorted(POPULATION, key = lambda individual: individual.fitness, reverse = True)
#COMPARATIVOS
if(POPULATION[0].fitness > MAX_FITNESS):
    MAX_FITNESS = POPULATION[0].fitness

if(POPULATION[POPULATION_SIZE - 1].fitness < MIN_FITNESS):
    MIN_FITNESS = POPULATION[POPULATION_SIZE - 1].fitness

#LOOP PRINCIPAL
#while(POPULATION[0].fitness < TARGET_FITNESS):
while(GENERATION < TARGET_GENERATION):
    POPULATION = sorted(POPULATION, key = lambda individual: individual.fitness, reverse = True)
    nextGeneration: list[Individual] = [];
 
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

    GENERATION += 1;

    # Ordeno el arreglo de individuos (población) de mayor a menor según fitness
    POPULATION = sorted(POPULATION, key = lambda individual: individual.fitness, reverse = True)
    
    #COMPARATIVOS
    if(POPULATION[0].fitness > MAX_FITNESS):
        MAX_FITNESS = POPULATION[0].fitness
    
    if(POPULATION[POPULATION_SIZE - 1].fitness < MIN_FITNESS):
        MIN_FITNESS = POPULATION[POPULATION_SIZE - 1].fitness


    printCurrentGen(GENERATION, POPULATION)
    

print(f"Maximo fitness alcanzado: { MAX_FITNESS }")
print(f"Minimo fitness alcanzado: { MIN_FITNESS }")