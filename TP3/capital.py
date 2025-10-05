#Capital
from typing import Dict

class Capital:
    def __init__(self, name: str, index: int) -> None:
        self.name: str = name
        self.index: int = index
        self.visited: bool = False
        self.isOrigin: bool = False
        self.distances: Dict[str, float] = {}

    #Obtiene la distancia de la capital actual hacia la otra capital, lo hace buscando con el nombre de la otra capital la entrada en el diccionario generado a partir del CSV
    def getDistanceTo(self, otherCapitalName: str) -> float:
        return self.distances.get(otherCapitalName, float('inf'))
    
    #Devuelve el nombre de la capital más cercana no visitada.
    def nearestUnvisited(self, capitals: Dict[str, 'Capital']) -> str:
        nearest = None
        min_dist = float('inf')
        for capitalName, capitalObject in capitals.items():
            if not capitalObject.visited:
                dist = self.getDistanceTo(capitalName)
                if dist < min_dist:
                    min_dist = dist
                    nearest = capitalName
        return nearest

    def __repr__(self) -> str:
        return f"Capital(Nombre='{self.name}', Visitada?={self.visited}, Origen del viaje?={self.isOrigin})"
