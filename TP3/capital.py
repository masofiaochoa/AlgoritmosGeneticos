#Capital
from typing import Dict

class Capital:
    def __init__(self, name: str, index: int) -> None:
        self.name: str = name
        self.index: int = index
        self.visited: bool = False
        self.isOrigin: bool = False
        self.distances: Dict[str, float] = {}

    def getDistanceTo(self, otherCapital: str) -> float:
        return self.distances.get(otherCapital, float('inf'))
    
    #Devuelve el nombre de la capital más cercana no visitada.
    def nearestUnvisited(self, capitals: Dict[str, 'Capital']) -> str | None:
        nearest = None
        min_dist = float('inf')
        for city_name, city_obj in capitals.items():
            if not city_obj.visited:
                dist = self.getDistanceTo(city_name)
                if dist < min_dist:
                    min_dist = dist
                    nearest = city_name
        return nearest

    def __repr__(self) -> str:
        return f"Capital(Nombre='{self.name}', Visitada?={self.visited}, Origen del viaje?={self.isOrigin})"
