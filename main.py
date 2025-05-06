#IMPORTS
import random

from individual import Individual

from config import POPULATION_SIZE, CHROMOSOME_LEN, MUTATION_CHANCE, CROSSOVER_CHANCE

from functions.testFitness import testFitness
from functions.selectPossibleParents import selectPossibleParents
from functions.crossover import crossover
from functions.mutate import mutate

#GLOBAL VARIABLES
POPULATION: list[Individual] = [];
FITNESSES: list[float] = [];
GENERATION: int = 0;
MAX_FITNESS: float = 0.0
MIN_FITNESS: float = 1.0
STOP_CONDITION: float = 0.95 # El fitness mínimo que tiene que alcanzar algun cromosoma de las generaciones para que se pare con el proceso

#estrategia de mutacion: complemento del gen (0 a 1 y 1 a 0)
#Creo que aca se podría agregar un parametro 'strategy' y un parametro 'geneAmount' para hacerlo mas general (estrategias de mutacion y cantidad de genes a mutar)

from functions.printCurrentGen import printCurrentGen

#PROGRAM
#GENERATE INITIAL POPULATION
for _ in range(POPULATION_SIZE):
    newChromosome: int = random.randint(0, 2**CHROMOSOME_LEN - 1) #genero un numero binario que como maximo sea 2 elevado a el largo del cromosoma - 1 (Ej si es un cromosoma de 3, el maximo numero representable es 2^2 + 2^1 + 2^0 = 2^3 - 1)
    POPULATION.append(Individual(newChromosome));

#? Una alternativa más limpia podría ser un map con testFitness
for individual in POPULATION:
    fitnessResult:float = testFitness(individual);
    FITNESSES.append(fitnessResult); 

#LOOP PRINCIPAL
while(max(FITNESSES) < STOP_CONDITION):
    #SELECT POSSIBLE PARENTS
    possibleParents: list[Individual] = selectPossibleParents(POPULATION, FITNESSES);

    #CROSSOVER ROULETTE
    nextGeneration: list[Individual] = [];

    for i in range(POPULATION_SIZE, 2): #si bien POPULATION_SIZE coincide con el tamaño de possibleParents, quizas sea mas claro poner len(possibleParents) como limite superior
        if(random.uniform(0.0, 1.0) <= CROSSOVER_CHANCE):
            parents: list[Individual] = [possibleParents[i], possibleParents[i + 1]];
            children: list[Individual] = crossover(parents);
            nextGeneration.extend(children);

    #Checkeo si hace falta añadir individuos extras para que la poblacion nueva mantenga el tamaño, uso elitismo en caso de haber faltantes (Elijo miembros de la poblacion anterior con el mayor fitness)
    if(len(nextGeneration) < POPULATION_SIZE):
        missingIndividuals: int = POPULATION_SIZE - len(nextGeneration);

        # Está mal hecho porque Elitismo pasa sin hacer Ruleta a una parte de la población con mayor fitness
        # En este caso, si no cae en posibilidad de crossover, pasan directamente como hijos a la nueva generación

        for i in range(missingIndividuals):
                maxFitness: float = max(FITNESSES);
                maxIndex = FITNESSES.index(maxFitness);
                nextGeneration.append(POPULATION[maxIndex]);
                FITNESSES[maxIndex] = 0.0 #Lo saco del arreglo para que no moleste, este metodo es destructivo y no se que tan bien está, pero entiendo que como las Fitnesses son de la generacion previa ya no me interesan

    #MUTATION ROULETTE
    for i in range(POPULATION_SIZE): #si bien POPULATION_SIZE coincide con el tamaño de nextGeneration, quizas sea mas claro poner len(nextGeneration) como limite superior
        if(random.uniform(0.0, 1.0) <= MUTATION_CHANCE):
            mutant: Individual = mutate(nextGeneration[i]);
            nextGeneration[i] = mutant;

    #finally replace current pop with next gen
    POPULATION = nextGeneration;
    
    #TEST FITNESS FOR EACH INDIVIDUAL
    newFitnesses: list[float] = [];

    for individual in POPULATION:
        fitnessResult:float = testFitness(individual);
        newFitnesses.append(fitnessResult); 
        
    FITNESSES = newFitnesses;

    GENERATION += 1;
    printCurrentGen(GENERATION, POPULATION, FITNESSES); #Imprimo la generacion actual y la poblacion con sus fitnesses

    

