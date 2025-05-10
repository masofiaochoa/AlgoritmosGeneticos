from individual import Individual
from config import *

def printCurrentGen(GENERATION: int, POPULATION: list[Individual]) -> None:
    print(f"Generation: {GENERATION}");
    for i in range(0, POPULATION_SIZE):
        print(f"\n\t{ POPULATION[i] }");
    print("-------------------------------");