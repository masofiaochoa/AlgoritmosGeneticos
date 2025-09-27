from config import *
from capitalRoute import CapitalRoute

#Función objetivo, lo tomamos como la distancia total que conlleva recorrer la ruta
def targetFunction(capRoute: CapitalRoute) -> float:
    return capRoute.distance;