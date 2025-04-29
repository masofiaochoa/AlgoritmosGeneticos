#IMPORTS
import math
import random
from typing import List

#INDIVIDUAL
class Individual:
    def __init__(self, chromosome: int): #Para python los binarios son ints, no tiene tipo aparte, pero el 99% de las veces voy a trabajar con bitwise operators como si fuera un binario
        self.chromosome = chromosome;
        pass;

    def __str__(self) -> str:
        return f"Chromosome: {bin(self.chromosome)}" #Bin solamente hace que el int se imprima como binario
        

#CONSTANTS
POPULATION_SIZE: int = 4; #poblacion
CHROMOSOME_LEN: int = 5; #Cantidad de genes en cromosoma del individual
MUTATION_CHANCE: float = 0.001; #probabilidad de mutacion
CROSSOVER_CHANCE: float = 0.95; #probabilidad de cruza

#GLOBAL VARIABLES
POPULATION: List[Individual] = [];
FITNESSES: List[float] = [];
GENERATION: int = 0;

#COMMON FUNCTIONS
def testFitness(individual: Individual) -> float:
    """ Esta es la funcion fitness del ej, el tema es que si los 4 individuos toman valor 31(Valor maximo) el fitness retorna 0.25 y termina haciendo un bardo barbaro
    total: int = 0;
    for i in POPULATION:
        total += i.chromosome ** 2;
    
    if(total == 0.0):
        return 0.0
    else:
        return ( individual.chromosome ** 2 ) / total;
    """

    return (individual.chromosome**2 / 31 ** 2);
 
def selectPossibleParents(population: List[Individual], fitnesses: List[float]) -> List[Individual]:
    selectedPossibleParents: List[Individual] = []; #Contendra los individuos elegidos para posibilidad de cruza
    totalFitness: float = sum(fitnesses);
    roulette: List[Individual] = []; #Simulo una ruleta de 100 elementos (100% de probabilidad)
    
    for i, individual in enumerate(population):
        roulette.extend([individual] * math.ceil(100 * fitnesses[i]));
    
    for _ in range(len(population)):
        selectedIndividual: Individual = random.choice(roulette);
        selectedPossibleParents.append(selectedIndividual);

    return selectedPossibleParents;



    
    """
    Asi se implementa una ruleta 'prolija' con lenguaje base en python, no lo uso porque me parece sintacticamente mas jodido de leer y entender

    probs = [f / total_fitness for f in fitnesses]
    return random.choices(population, weights=probs, k=2)
    """

def crossover( parents: List[Individual] ) -> List[Individual]:
    children: List[Individual] = [];
    
    crossoverPoint:int = random.randint(0, CHROMOSOME_LEN - 1);  #El limite inferior siendo 0 es medio raro porque te puede dar hijos identicos al padre, evaluar cambiarlo a 1
    
    #todo esto es manipulacion de bits, en un comentario es dificil de explicar
    bitMask: int = ( 1 << crossoverPoint ) - 1;

    chrm1: int = ((parents[0].chromosome & bitMask) | (parents[1] & ~bitMask));
    chrm2: int = ((parents[1].chromosome & bitMask) | (parents[0] & ~bitMask));

    children.append(Individual(chrm1));
    children.append(Individual(chrm2));

    return children;

#estrategia de mutacion: complemento del gen (0 a 1 y 1 a 0)
#Creo que aca se podría agregar un parametro 'strategy' y un parametro 'geneAmount' para hacerlo mas general (estrategias de mutacion y cantidad de genes a mutar)
def mutate(individual: Individual) -> Individual:
    mutatedGen = random.randint(0, CHROMOSOME_LEN - 1);
    individual.chromosome = individual.chromosome ^ (1 << mutatedGen);
    return individual;

def printCurrentGen():
    print(f"Generation: {GENERATION}\n\n");
    for i in range(POPULATION_SIZE):
        print(f"\tIndividual:\n\t\t{ POPULATION[i] }\n\t\tFitness: { FITNESSES[i] }\n\n");
    print("-------------------------------");

#PROGRAM
#GENERATE INITIAL POPULATION
for _ in range(POPULATION_SIZE):
    newChromosome: int = random.randint(0, 2**CHROMOSOME_LEN - 1) #genero un numero binario que como maximo sea 2 elevado a el largo del cromosoma - 1 (Ej si es un cromosoma de 3, el maximo numero representable es 2^2 + 2^1 + 2^0 = 2^3 - 1)
    POPULATION.append(Individual(newChromosome));

for individual in POPULATION:
    fitnessResult:float = testFitness(individual);
    FITNESSES.append(fitnessResult); 

#LOOP PRINCIPAL
while(max(FITNESSES) < 0.95):
    #SELECT POSSIBLE PARENTS
    possibleParents: List[Individual] = selectPossibleParents(POPULATION, FITNESSES);

    #CROSSOVER ROULETTE
    nextGeneration: List[Individual] = [];

    for i in range(POPULATION_SIZE, 2): #si bien POPULATION_SIZE coincide con el tamaño de possibleParents, quizas sea mas claro poner len(possibleParents) como limite superior
        if(random.uniform(0.0, 1.0) <= CROSSOVER_CHANCE):
            parents: List[Individual] = [possibleParents[i], possibleParents[i + 1]];
            children: List[Individual] = crossover(parents);
            nextGeneration.extend(children);

    #Checkeo si hace falta añadir individuos extras para que la poblacion nueva mantenga el tamaño, uso elitismo en caso de haber faltantes (Elijo miembros de la poblacion anterior con el mayor fitness)
    if(len(nextGeneration) < POPULATION_SIZE):
        missingIndividuals: int = POPULATION_SIZE - len(nextGeneration);



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
    newFitnesses: List[float] = [];

    for individual in POPULATION:
        fitnessResult:float = testFitness(individual);
        newFitnesses.append(fitnessResult); 
        
    FITNESSES = newFitnesses;

    GENERATION += 1;
    printCurrentGen();

    

