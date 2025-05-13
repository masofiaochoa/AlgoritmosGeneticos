import random

from config import *
from individual import Individual


def mutate(individual: Individual) -> Individual:
    mutatedGen: int = random.randint(0, CHROMOSOME_LEN - 1);
    mutatedChromosome: int = individual.chromosome ^ (1 << mutatedGen);

    individual.chromosome = mutatedChromosome
    individual.targetFunctionValue = None
    individual.fitness = None

    return individual
