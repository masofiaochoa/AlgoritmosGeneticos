import math
import random

from individual import Individual

# Función que solo se usa en ruleta
def accumulateProportions(proportions: list[float]) -> list[float]:
  cumulativeProportions: list[float] = []

  acc = 0
  for p in proportions:
    acc += p
    cumulativeProportions.append(acc)

  return cumulativeProportions

def roulette(population: list[Individual], fitnesses: list[float]) -> list[Individual]:
    selectedPossibleParents: list[Individual] = []; #Contendra los individuos elegidos para posibilidad de cruza
    totalFitness: float = sum(fitnesses);

    # Construyo la ruleta
    proportions: list[float] = map(lambda x: x/totalFitness, fitnesses) # Se definen las proporciones dependiendo del fitness y el fitnessTotal.
    cumulativeProportions: list[float] = accumulateProportions(proportions) # Se acumulan las proporciones de modo de delimitar el espacio del 0 al 1 para cada uno de los cromosomas.

    while len(selectedPossibleParents) < len(population):
      r = random.random()
      for i, cp in enumerate(cumulativeProportions):
        if r <= cp:
          selectedPossibleParents.append(population[i])
          break

    return selectedPossibleParents;