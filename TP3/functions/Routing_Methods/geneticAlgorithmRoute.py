import random
from typing import Dict, List
from functions.AG.crossover import crossover
from functions.AG.generateInitialPopulation import generateInitialPopulation
from functions.AG.getPopulationFitness import getPopulationFitness
from functions.AG.mutate import mutate
from functions.AG.selectPossibleParents import selectPossibleParents
from capital import Capital
from capitalRoute import CapitalRoute
from config import *

def geneticAlgorithmRoute(capitals: Dict[str, Capital]) -> tuple[list[str], float]:
    #Genero poblacion inicial
    GENERATION: int = 0
    POPULATION = generateInitialPopulation(capitals)
    

    #loop principal
    for i in range(0, TARGET_GENERATION):
        nextGeneration: list[CapitalRoute] = [];

        #SELECCIONAR POSIBLES PADRES
        possibleParents: list[CapitalRoute] = selectPossibleParents(SELECTION_METHOD, POPULATION);

        #CRUZA
        for i in range(0, REMAINDER_POPULATION, 2):
            parents: list[CapitalRoute] = [possibleParents[i], possibleParents[i + 1]]
            children: list[CapitalRoute] = []

            if(random.random() <= CROSSOVER_CHANCE):
                children = crossover(parents)
            else:
                children = parents

            nextGeneration.extend(children)

        #MUTACION
        for i in range(len(nextGeneration)):
            if(random.random() <= MUTATION_CHANCE):
                mutant: CapitalRoute = mutate(nextGeneration[i]);
                nextGeneration[i] = mutant;
        
        #ELITISMO
        for i in range(0, ELITISM_CHOSEN_INDIVIDUAL_AMOUNT):
            nextGeneration.append(POPULATION[i]) #los individuos del principio del arreglo son los de mayor fitness

        #finalmente calculamos fitness y ordenamos la problacion
        POPULATION = getPopulationFitness(nextGeneration);
        POPULATION = sorted(POPULATION, key = lambda individual: individual.distance)

        GENERATION += 1;
        
    return POPULATION