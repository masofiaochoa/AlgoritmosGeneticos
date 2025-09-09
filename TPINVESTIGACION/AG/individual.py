# Individuo, contiene path (lista de (r,c)), valor de función objetivo, fitness.
# Se redefine la función __str__ para poder printearlo de mejor manera

import matplotlib.pyplot as plt

from config import GRID_ROWS, GRID_COLS, DISTANCE_TRAVELED_TO_DRIFT_RATIO, GRID_CELL_SIZE
from typing import List, Tuple
from functions.helpers.calculatePathLength import calculatePathLength


class Individual:
    def __init__(self, path: List[Tuple[int, int]], pathDistance: int, targetFunctionValue: float, fitness: float):
        self.path = path                          # [(r,c), (r,c), ..., goal]
        self.targetFunctionValue = targetFunctionValue #coincide con el tiempo que toma recorrer el camino elegido
        self.fitness = fitness
        self.pathDistance = 0
        self.partialDrift = 0
        self.outOfBounds = False

    def __str__(self) -> str:  
        path_matrix = [[1 if (j, i) in self.path else 0 for i in range(GRID_COLS)] for j in range(GRID_ROWS)]
        
        return (
            "Individual:\n"
            f"\tCamino: {self.path}\n"
            f"\tDistancia del camino: {self.pathDistance}\n"
            f"\tTiempo que toma recorrer el camino (Funcion objetivo): {self.targetFunctionValue:.6f}\n"
            f"\tFitness: {self.fitness:.6f}\n"
            f"Matriz de viaje:\n" + "\n".join([f"Fila {i:2d}: {row}" for i, row in enumerate(path_matrix)])
            )
    
    def plot(self, show_grid: bool = True):
        fig, ax = plt.subplots(figsize=(6, 6))


        # Configuración de los límites
        ax.set_xlim(-0.5, GRID_COLS - 0.5)
        ax.set_ylim(-0.5, GRID_ROWS - 0.5)
        ax.set_aspect('equal')


        if show_grid:
            ax.set_xticks(range(GRID_COLS))
            ax.set_yticks(range(GRID_ROWS))
            ax.grid(True, which='both', color='lightgrey', linewidth=0.5)


        # Extraer filas y columnas del path
        rows = [p[0] for p in self.path]
        cols = [p[1] for p in self.path]


        # Dibujar el camino
        ax.plot(cols, rows, color='red', linewidth=2, marker='o', markersize=4)


        # Marcar inicio y fin
        ax.scatter(cols[0], rows[0], color='green', s=100, label='Inicio')
        ax.scatter(cols[-1], rows[-1], color='blue', marker='x', s=100, label='Fin')


        # Invertir eje Y (para que fila 0 esté arriba como en matrices)
        ax.invert_yaxis()


        ax.legend()
        plt.title("Representación del Individuo")
        plt.show()
    
    def addPathStep(self, nextStep: Tuple[int, int]):
        partialDistanceTraveled = calculatePathLength([self.path[-1], nextStep]) #Distancia del ultimo paso al proximo paso
        self.path.append(nextStep)
        self.partialDrift += DISTANCE_TRAVELED_TO_DRIFT_RATIO * partialDistanceTraveled
        self.drift()
        self.pathDistance = calculatePathLength(self.path)
        
        
    #para mutacion. no aplica drift
    def replaceStepAtPos(self, newStep: Tuple[int, int], stepToReplaceIndex: int):
        self.path[stepToReplaceIndex] = newStep
        self.pathDistance = calculatePathLength(self.path)
        
        
        
    def drift(self):
    #    return #Funcionalidad anulada pues los algoritmos usados para elegir caminos no lograron adaptarse  correctamente
         
        if(self.partialDrift >= GRID_CELL_SIZE):
            self.partialDrift -= GRID_CELL_SIZE;
            lastPos = self.path[-1]
            drift = (1, 0)
            driftedPos = (lastPos[0] + drift[0], lastPos[1] + drift[1])
            driftedRow, driftedCol = driftedPos
            
            #si la posicion derivada por la corriente no esta fuera del grid, la deriva. Sino simplemente lo deja en el fondo del grid
            if(0 <= driftedRow < GRID_ROWS and 0 <= driftedCol < GRID_COLS):
                self.path.append(driftedPos) 
    


                
        
        