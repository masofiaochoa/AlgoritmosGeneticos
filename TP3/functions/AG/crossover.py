import random

from config import *
from individual import Individual

#Genera dos hijos a partir de dos padres cruzando sus cromosomas a partir de punto de corte aleatorio
def crossover( parents: list[Individual] ) -> list[Individual]:
    children: list[Individual] = [];
    
    crossoverPoint: int = random.randint(1, CHROMOSOME_LEN - 1);
    
    #Generacion de la mascara y operaciones binarias entre los cromosomas y la mascara para generar los hijos
    bitMask: int = ( 1 << crossoverPoint ) - 1;

    chrm1: int = ((parents[0].chromosome & bitMask) | (parents[1].chromosome & ~bitMask));
    chrm2: int = ((parents[1].chromosome & bitMask) | (parents[0].chromosome & ~bitMask));

    children.append(Individual(chrm1, None, None));
    children.append(Individual(chrm2, None, None));

    return children;