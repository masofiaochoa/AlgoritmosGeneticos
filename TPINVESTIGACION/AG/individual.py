# Individuo, contiene path (lista de (r,c)), valor de función objetivo, fitness.
# Se redefine la función __str__ para poder printearlo de mejor manera

from config import GRID_ROWS, GRID_COLS
from typing import List, Tuple

class Individual:
    def __init__(self, path: List[Tuple[int, int]], targetFunctionValue: float, fitness: float):
        self.path = path                          # [(r,c), (r,c), ..., goal]
        self.targetFunctionValue = targetFunctionValue
        self.fitness = fitness

    def __str__(self) -> str:  
        path_matrix = [[1 if (j, i) in self.path else 0 for i in range(GRID_COLS)] for j in range(GRID_ROWS)]
        
        return (
            "Individual:\n"
            f"\tPath len: {len(self.path)}\n"
            f"\tPath: {self.path}\n"
            f"\tValor Objetivo: {self.targetFunctionValue:.6f}\n"
            f"\tFitness: {self.fitness:.6f}\n"
            f"Matriz de viaje:\n" + "\n".join([f"Fila {i:2d}: {row}" for i, row in enumerate(path_matrix)])
            )
