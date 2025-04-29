import random
from individual import Individual
from config import *

def mutate(individual: Individual) -> Individual:
    mutatedGen = random.randint(0, CHROMOSOME_LEN - 1);
    individual.chromosome = individual.chromosome ^ (1 << mutatedGen);
    return individual;
