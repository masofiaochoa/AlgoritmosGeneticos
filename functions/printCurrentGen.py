from individual import Individual
from config import *

def printCurrentGen(GENERATION: int, POPULATION: list[Individual]) -> None:
    print(f"Generation: {GENERATION}\n\n");
    for i in range(POPULATION_SIZE):
        print(f"\tIndividual:\n\t\t{ POPULATION[i] }\n\n");
    print("-------------------------------");