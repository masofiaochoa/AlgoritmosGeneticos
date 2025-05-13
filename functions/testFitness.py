from individual import Individual

def testFitness(individual: Individual, TARGET_FUNCTION_TOTAL: float) -> float:

    fitnessFunction: float = individual.targetFunctionValue / TARGET_FUNCTION_TOTAL

    return fitnessFunction