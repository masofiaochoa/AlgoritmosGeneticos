import random

from config import *
from capital import Capital
from capitalRoute import CapitalRoute

#Genera dos hijos a partir de dos padres cruzando sus caminos en un punto aleatorio sin incluir origen (CAPITALS[0]) ni destino (Vuelta al origen) CAPITALS[len(CAPITALS) - 1])
def crossover(parents: list[CapitalRoute]) -> list[CapitalRoute]:
    parent1, parent2 = parents
    
    # Elegimos punto de corte aleatorio evitando el capital de inicio (indice 0) y capital de fin (indice len(parent1.route) - 1)
    start = 1
    end = len(parent1.route) - 2
    cut = random.randint(start, end)
    
    # Hijo 1
    child1Route = parent1.route[:cut] #copio mitad inferior de parent1
    for cap in parent2.route[1:-1]:  # por cada capital de la ruta de parent2, ignorando primera y ultima capital
        if cap not in child1Route: #agrego solamente los no duplicados
            child1Route.append(cap)
    child1Route.append(parent1.startCapital)  #Cerramos el trayecto agregando la startCapital como ultima capital
    
    # Hijo 2:
    child2Route = parent2.route[:cut] #copio mitad inferior de parent2
    for cap in parent1.route[1:-1]: #por cada capital de la ruta de parent1, ignorando primera y ultima capital
        if cap not in child2Route:
            child2Route.append(cap)
    child2Route.append(parent2.startCapital)
    
    # Creamos CapitalRoute para devolverlos
    child1 = CapitalRoute(parent1.startCapital)
    child1.route = child1Route
    child1.recalcuteRouteDistance()
    
    child2 = CapitalRoute(parent2.startCapital)
    child2.route = child2Route
    child2.recalcuteRouteDistance()
    
    return [child1, child2]
