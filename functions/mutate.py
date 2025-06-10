import random

from config import *
from individual import Individual

#Muta un individuo haciendo una mutación inversa sobre un gen aleatorio del mismo
def mutate(individual: Individual) -> Individual:
    #Mascara de bits
    mutatedGen: int = random.randint(0, CHROMOSOME_LEN - 1);
    #Operacion binaria sobre el cromosoma original para generar el cromosoma mutado
    mutatedChromosome: int = individual.chromosome ^ (1 << mutatedGen);

    #asignación del cromosoma mutado al individuo original para generar el cromosoma mutado
    individual.chromosome = mutatedChromosome
    individual.targetFunctionValue = None
    individual.fitness = None

    return individual
