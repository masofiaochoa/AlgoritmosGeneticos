import copy
import random
from typing import Dict

from capital import Capital
from .getPopulationFitness import getPopulationFitness
from functions.Routing_Methods.randomRoute import randomRoute
from functions.Routing_Methods.nearestNeighborRoute import nearestNeighborRoute
from config import *
from capitalRoute import CapitalRoute

#Genera la población inicial iterando una generación de cromosomas aleatorios por la cantidad de población y luego evaluando el fitness para cada uno de ellos
def generateInitialPopulation(capitals: Dict[str, Capital]):
    
    initialPopulation: list[CapitalRoute] = []
    
    for _ in range(RANDOM_ROUTE_GENERATED):
        randomStartCapital = random.choice(list(capitals.keys()));
        # Creamos una copia independiente de las capitales para esta ruta
        localCapitals = copy.deepcopy(capitals)
        capRoute: CapitalRoute = randomRoute(randomStartCapital, localCapitals)
        initialPopulation.append(capRoute)
        
        
    for _ in range(NEAREST_NEIGHBOR_ROUTE_GENERATED):
        randomStartCapital = random.choice(list(capitals.keys()));
        # Creamos una copia independiente de las capitales para esta ruta
        localCapitals = copy.deepcopy(capitals)
        capRoute: CapitalRoute = nearestNeighborRoute(randomStartCapital, localCapitals, returnToStart=False)
        initialPopulation.append(capRoute)
    initialPopulation = getPopulationFitness(initialPopulation)

    return initialPopulation
