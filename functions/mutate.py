import random

from config import *
from individual import Individual
from functions import testFitness


def mutate(individual: Individual) -> Individual:
    mutatedGen: int = random.randint(0, CHROMOSOME_LEN - 1);
    mutatedChromosome: int = individual.chromosome ^ (1 << mutatedGen);

    mutatedFitness: float = testFitness(mutatedChromosome)

    individual.chromosome = mutatedChromosome
    individual.fitness = mutatedFitness

    return individual
