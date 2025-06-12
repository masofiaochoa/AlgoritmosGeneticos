from config import *

#Función objetivo del enunciado
def targetFunction(chromosome: int) -> float:
    value: float = round((chromosome / COEF) ** 2, 6)
    
    return value