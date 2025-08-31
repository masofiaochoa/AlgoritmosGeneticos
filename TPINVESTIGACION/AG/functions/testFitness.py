from individual import Individual

#Funcion fitness del enunciado (Función objetivo del individuo dividido el total de la suma de todas las funciones objetivos de la población)
def testFitness(individual: Individual, target_function_total: float) -> float:

    fitnessFunction: float = (target_function_total - individual.targetFunctionValue) / target_function_total

    return fitnessFunction