import random

from individual import Individual
from config import *

#Acumula las proporciones para contar con valores proporcionales para cada participante de la ruleta
def accumulateProportions(proportions: list[float]) -> list[float]:
  cumulativeProportions: list[float] = []

  acc = 0
  for p in proportions:
    acc += p
    cumulativeProportions.append(acc)

  return cumulativeProportions

#Genera una ruleta a partir de la población en la cual la probabilidad de ser elegido de cada individuo es directamente proporcional a su fitness
def roulette(population: list[Individual]) -> list[Individual]:
    selectedPossibleParents: list[Individual] = []; #Contendra los individuos elegidos para posibilidad de cruza

    # Construyo la ruleta
    proportions: list[float] = [x.fitness for x in population]

    cumulativeProportions: list[float] = accumulateProportions(proportions) # Se acumulan las proporciones de modo de delimitar el espacio del 0 al 1 para cada uno de los cromosomas.

    while len(selectedPossibleParents) < (REMAINDER_POPULATION):
      r = random.random() #genera un numero real aleatorio del 0 al 1
      for i, cp in enumerate(cumulativeProportions):
        if r <= cp: 
          selectedPossibleParents.append(population[i])
          break #sale del for, vuelve a calcular un r

    return selectedPossibleParents;