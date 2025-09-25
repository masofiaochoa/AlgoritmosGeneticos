from typing import Dict

#Genera una solucion por cada ciudad de inicio utilizando la función del inciso A (Ir siempre a la ciudad mas cercana no visitada)
#Compara todas las soluciones y elige la mejor
from capital import Capital
from capitalRoute import CapitalRoute
from functions.Routing_Methods.nearestNeighborRoute import nearestNeighborRoute

def shortestPathToVisitAllRoute(capitals: Dict[str, Capital]) -> CapitalRoute:
    bestRoute: CapitalRoute | None = None

    #Probamos cada capital como capital inicial a ver cual da el mejor resultado con el metodo de nearestNeighborRoute
    for startCapital in capitals.keys():
        possibleBestRoute = nearestNeighborRoute(startCapital, capitals)
        if bestRoute is None or possibleBestRoute.distance < bestRoute.distance: #El None se da solamente en la primera iteración
            bestRoute = possibleBestRoute

    return bestRoute
