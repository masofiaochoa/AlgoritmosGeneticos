# targetFunction.py

# Para poder importar model se necesita un path absoluto
import sys
from pathlib import Path

from numpy import floor

from AG.individual import Individual
sys.path.append(str(Path(__file__).parent.parent.parent))

from typing import Tuple
from mainML import Model
from config import WIND_SPEED, GRID_CELL_SIZE, WIND_ANGLE

def targetFunction(ind: Individual, model: Model) -> float:
    #print("\nPATH DISTANCE Y TOTAL TIME\n")
    #print(ind.pathDistance)
    total_time = model.predictTime(WIND_SPEED, WIND_ANGLE, floor(ind.pathDistance))
    #print(total_time)
    return float(total_time)
