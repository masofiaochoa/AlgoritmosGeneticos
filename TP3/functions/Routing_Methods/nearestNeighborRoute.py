from typing import Dict
from capital import Capital

def nearestNeighborRoute(start: str, capitals: Dict[str, Capital]) -> tuple[list[str], float]:
    # Reiniciamos visitados
    for c in capitals.values():
        c.visited = False

    route = [start]
    capitals[start].visited = True
    total_distance = 0.0
    current_city = start

    while len(route) < len(capitals):
        next_city = capitals[current_city].nearestUnvisited(capitals)
        if next_city is None:
            break  # por si hay algún problema
        total_distance += capitals[current_city].getDistanceTo(next_city)
        capitals[next_city].visited = True
        route.append(next_city)
        current_city = next_city

    # Regresar a la ciudad de inicio
    total_distance += capitals[current_city].getDistanceTo(start)
    route.append(start)

    return route, total_distance