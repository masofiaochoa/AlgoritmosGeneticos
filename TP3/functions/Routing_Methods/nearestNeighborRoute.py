from typing import Dict
from capital import Capital
from capitalRoute import CapitalRoute

#Encuentra una ruta desde una determinada capital de inicio recorriendo todas las demas capitales no visitadas
#Recorre siempre primero la capital no visitada mas cercana a la capital actual, y al final retorna a la capital de inicio
def nearestNeighborRoute(start: str, capitals: Dict[str, Capital]) -> CapitalRoute:
    #Reiniciamos el estado 'visitado' en todas las capitales
    for c in capitals.values():
        c.visited = False

    startCapital = capitals[start]
    capRoute = CapitalRoute(startCapital)
    startCapital.visited = True
    currentCapital = startCapital

    while len(capRoute.route) < len(capitals):
        nearestCapitalToCurrent = currentCapital.nearestUnvisited(capitals)
        if nearestCapitalToCurrent is None: #Si no hay mas capitales sin visitar, volvemos (No debería cumplirse nunca esta condicion dada la condicion del while)
            break
        nextCapital = capitals[nearestCapitalToCurrent] #Lo buscamos en el diccioanrio de capitales por nombre para obtener el objeto
        capRoute.addCapital(nextCapital)
        nextCapital.visited = True
        currentCapital = nextCapital

    capRoute.returnToStartCapital()
    return capRoute