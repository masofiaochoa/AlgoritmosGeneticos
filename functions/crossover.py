import random

from config import *
from individual import Individual


def crossover( parents: list[Individual] ) -> list[Individual]:
    children: list[Individual] = [];
    
    crossoverPoint: int = random.randint(1, CHROMOSOME_LEN - 1);  #El limite inferior siendo 0 es medio raro porque te puede dar hijos identicos al padre, evaluar cambiarlo a 1
    
    #todo esto es manipulacion de bits, en un comentario es dificil de explicar
    bitMask: int = ( 1 << crossoverPoint ) - 1;

    chrm1: int = ((parents[0].chromosome & bitMask) | (parents[1].chromosome & ~bitMask));
    chrm2: int = ((parents[1].chromosome & bitMask) | (parents[0].chromosome & ~bitMask));

    children.append(Individual(chrm1, None, None));
    children.append(Individual(chrm2, None, None));

    return children;