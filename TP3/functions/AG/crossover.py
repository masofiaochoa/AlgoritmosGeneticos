import random
from typing import List
from config import *
from capital import Capital
from capitalRoute import CapitalRoute

# función auxiliar: aplica CX entre dos padres y devuelve un hijo
def cycleCrossover(p1: CapitalRoute, p2: CapitalRoute, size: int) -> CapitalRoute:
    # Inicializamos la ruta del hijo con None
    childRouteNames = [None] * size
    visited = set()
    index = random.randint(0, size - 1)  # índice inicial aleatorio

    # Creamos listas de nombres de capitales en los padres. Trabajo con nombres para evitar problemas con el deepcopy
    p1_names = [c.name for c in p1.route]
    p2_names = [c.name for c in p2.route]

    # Construimos el ciclo usando los nombres. Este ciclo termina cuando pasas por un índice que ya completaste
    #! Por qué es un número aleatorio? Según el crossover cícclico se arranca en la primera posición
    while index not in visited:
        visited.add(index)
        childRouteNames[index] = p1_names[index]  # copiamos la capital desde p1 (por nombre)
        capitalName = p2_names[index]             # tomamos la capital correspondiente de p2
        index = p1_names.index(capitalName)       # siguiente índice del ciclo será donde está esa capital en p1

    # Completamos los huecos con capitales de p2 (por nombre)
    for i in range(size):
        if childRouteNames[i] is None:
            childRouteNames[i] = p2_names[i]

    # Reconstruimos los objetos Capital a partir de los nombres
    # Usamos la lista combinada de p1 + p2 para asegurarnos de tomar los objetos correctos
    child = CapitalRoute(p1.startCapital)
    child.route = [next(c for c in p1.route + p2.route if c.name == name) for name in childRouteNames]

    # Recalculamos la distancia de la ruta del hijo
    child.recalculateRouteDistance()
    return child


def crossover(parents: List[CapitalRoute]) -> List[CapitalRoute]:
    parent1, parent2 = parents
    size = len(parent1.route)
    # generar los dos hijos (Notar que el orden de los padres se invierte)
    child1 = cycleCrossover(parent1, parent2, size)
    child2 = cycleCrossover(parent2, parent1, size)
    return [child1, child2]


