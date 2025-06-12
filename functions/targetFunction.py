from config import *

#Función objetivo del enunciado, redondeamos a 6 decimales
def targetFunction(chromosome: int) -> float:
    value: float = round((chromosome / COEF) ** 2, 6)
    
    return value