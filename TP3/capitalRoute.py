from typing import List
from capital import Capital

#Describe una ruta que recorre todas las capitales argentinas desde una capital de origen definida 
#y, que al finalizar de visitar todas las demas capitales, vuelve a la capital de origen
class CapitalRoute:
    def __init__(self, startCapital: Capital) -> None:
        self.route: List[Capital] = [startCapital]   #Ruta, inicia siempre en la capital de origen y termina tambien en dicha capital
        self.distance: float = 0.0 #Coindide con el valor de la función objetivo de la ruta en el caso de utilizar algoritmos geneticos
        self.startCapital: Capital = startCapital
        self.fitness: float = 0.0 #Distancia dividido la sumatoria de distancias de todas las rutas. Solo se usa para metodo de Algoritmos geneticos

    #Agrega una capital a la ruta y acumula la distancia recorrida.
    def addCapital(self, nextCapital: Capital) -> None:
        distanceToNextCapital: float = self.route[-1].getDistanceTo(nextCapital.name)
        self.route.append(nextCapital)
        self.distance += distanceToNextCapital

    #Cierra el ciclo volviendo a la ciudad de inicio.
    def returnToStartCapital(self) -> None:   
        if self.route[-1] != self.startCapital:
            self.addCapital(self.startCapital)


    #Devuelve los nombres de las ciudades en la ruta.
    def getCapitalNames(self) -> List[str]:
        return [c.name for c in self.route]

    
    #Recalcula la distancia total de la ruta, se usa solamente en el metodo de AG cuando la ruta sufre alteraciones como una mutación o un crossover
    def recalcuteRouteDistance(self):
        self.distance = 0.0
        for i in range(0, len(self.route) - 1): #Range no incluye el extremo superior por ende no es necesario usar len(self.route) - 2
            self.distance += self.route[i].getDistanceTo(self.route[i + 1].name)
            

    def __len__(self) -> int:
        return len(self.route)

    def __repr__(self) -> str:
        names = " -> ".join(self.get_cities_names())
        return f"CapitalRoute(start={self.startCapital.name}, distance={self.distance:.1f} KMs, route={names})"
