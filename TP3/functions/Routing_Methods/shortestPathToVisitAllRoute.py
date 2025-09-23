from typing import Dict

#Genera una solucion por cada ciudad de inicio utilizando la función del inciso A (Ir siempre a la ciudad mas cercana no visitada)
#Compara todas las soluciones y elige la mejor
from capital import Capital
from functions.Routing_Methods.nearestNeighborRoute import nearestNeighborRoute

def shortestPathToVisitAllRoute(capitals: Dict[str, Capital]) -> tuple[list[str], float]:
    best_route: list[str] = []
    best_distance: float = float("inf")

    # Probar desde cada ciudad como ciudad inicial
    for start_city in capitals.keys():
        route, distance = nearestNeighborRoute(start_city, capitals)

        if distance < best_distance:
            best_distance = distance
            best_route = route

    return best_route, best_distance
