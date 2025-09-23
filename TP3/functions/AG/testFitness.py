from individual import Individual

#Funcion fitness del enunciado (Función objetivo del individuo dividido el total de la suma de todas las funciones objetivos de la población)
def testFitness(individual: Individual, TARGET_FUNCTION_TOTAL: float) -> float:

    fitnessFunction: float = individual.targetFunctionValue / TARGET_FUNCTION_TOTAL

    return fitnessFunction