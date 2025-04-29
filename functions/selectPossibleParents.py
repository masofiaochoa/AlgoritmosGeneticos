from individual import Individual
import math
import random
def selectPossibleParents(population: list[Individual], fitnesses: list[float]) -> list[Individual]:
    selectedPossibleParents: list[Individual] = []; #Contendra los individuos elegidos para posibilidad de cruza
    totalFitness: float = sum(fitnesses);
    roulette: list[Individual] = []; #Simulo una ruleta de 100 elementos (100% de probabilidad)
    
    for i, individual in enumerate(population):
        roulette.extend([individual] * math.ceil(100 * fitnesses[i]));
    
    for _ in range(len(population)):
        selectedIndividual: Individual = random.choice(roulette);
        selectedPossibleParents.append(selectedIndividual);

    return selectedPossibleParents;