from enum import Enum

#Contiene los posibles metodos de selección de padre a elegir. Es una clase 100% utilititaria y para mayor facilidad de modularización del código 
class Method(Enum):
    ROULETTE: int = 1
    TOURNAMENT: int  = 2