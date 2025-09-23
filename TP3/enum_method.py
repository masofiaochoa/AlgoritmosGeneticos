from enum import Enum

#Contiene los posibles metodos de selección de padre a elegir. Es una clase 100% utilititaria y para mayor facilidad de modularización del código 
class AG_Method(Enum):
    ROULETTE: int = 1
    TOURNAMENT: int  = 2
    
class Routing_Method(Enum):
    NEAREST_TO_START_CITY: int = 1
    SHORTEST_PATH_TO_ALL: int = 2
    GENETIC_ALGORITHM: int = 3