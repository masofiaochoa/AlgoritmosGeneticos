from config import *

#Función objetivo del enunciado
def targetFunction(chromosome: int) -> float:
    value: float = (chromosome / COEF) ** 2
    
    return value