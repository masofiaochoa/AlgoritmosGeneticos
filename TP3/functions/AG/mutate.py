import random

from config import *
from capital import Capital
from capitalRoute import CapitalRoute

#Muta una ruta haciendo un intercambio entre dos posiciones del recorrido de capitales sin incluir la capital de origen ni de destino
def mutate(capRoute: CapitalRoute) -> CapitalRoute:
    
    indexsToSwap: tuple[int, int] = [random.sample(range(1, len(capRoute.route) - 1), 2)] #Elige dos indices aleatorios para swapear capitales en la ruta SIN incluir origen ni final

    auxCap: Capital = capRoute.route[indexsToSwap[0]]
    capRoute.route[indexsToSwap[0]] = capRoute.route[indexsToSwap[1]]
    capRoute.route[indexsToSwap[1]] = auxCap
    capRoute.recalcuteRouteDistance()
    return capRoute
