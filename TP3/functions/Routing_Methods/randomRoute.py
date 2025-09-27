

import random
from typing import Dict

from capital import Capital
from capitalRoute import CapitalRoute


def randomRoute(start: str, capitals: Dict[str, Capital]) -> CapitalRoute:
    #Reiniciamos el estado 'visitado' en todas las capitales
    for c in capitals.values():
        c.visited = False

    startCapital = capitals[start]
    capRoute = CapitalRoute(startCapital)
    startCapital.visited = True

    while len(capRoute.route) < len(capitals):
        # Generamos lista de capitales no visitadas
        unvisited = [c for c in capitals.values() if not c.visited]
        if not unvisited:  # Si no hay más capitales sin visitar, salimos
            break
        # Elegimos una capital aleatoria de la lista
        nextCapital = random.choice(unvisited)

        capRoute.addCapital(nextCapital)
        nextCapital.visited = True
        
    return capRoute