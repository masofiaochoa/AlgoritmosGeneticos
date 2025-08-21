# targetFunction.py

# Para poder importar model se necesita un path absoluto
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import math
from individual import Individual
from mainML import Model
from config import WIND_SPEED, GRID_CELL_SIZE

def compute_angle(a: tuple[int, int], b: tuple[int, int]) -> float:
    """
    Calcula el ángulo (en grados) entre dos celdas a -> b.
    Convención (como el viento viene de derecha a izquierda por como se cruza el río):
        (0,0)->(0,1) => 0° (derecha)
        (0,0)->(1,0) => 90° (abajo)
        (0,0)->(0,-1)=> 180° (izquierda)
        (0,0)->(-1,0)=> 270° (arriba)
    Soporta diagonales también.
    """
    dx = b[1] - a[1]  # diferencia en columnas
    dy = b[0] - a[0]  # diferencia en filas
    ang_rad = math.atan2(dy, dx)
    ang_deg = math.degrees(ang_rad)
    return ang_deg % 360

def targetFunction(individual: Individual, model: Model) -> float:
    path = individual.path
    total_time = 0.0

    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        angle = compute_angle(a, b)
        # cada paso mide GRID_CELL_SIZE metros
        print(f"Paso de {a} a {b}: ángulo = {angle}°")
        step_time = model.predict(WIND_SPEED, angle, GRID_CELL_SIZE)
        total_time += float(step_time)

    return total_time
