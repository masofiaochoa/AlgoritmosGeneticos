from CapitalRoute import capitalRoute
from config import *

#Formatea e imprime los datos de la generación actual de individuos.
def printCurrentGen(GENERATION: int, POPULATION: list[CapitalRoute], maxTargetFunctionValue: float, minTargetFunctionValue: float) -> None:
    print(f"Generation: {GENERATION}");
    for i in range(0, POPULATION_SIZE):
        print(f"\n\t{ POPULATION[i] }");
    print(f"Minimo de la generación: {minTargetFunctionValue}")
    print(f"Maximo de la generación: {maxTargetFunctionValue}")
    print("-------------------------------");