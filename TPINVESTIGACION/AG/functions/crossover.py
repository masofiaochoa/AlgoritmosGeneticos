# crossover.py
# Se dan dos individuos, se cruzan y se devuelve una nueva pareja.
# La cruza se realiza a traves de los paths de cada uno. Se busca los posibles puntos de intersección, se elige uno aleatoriamente y se intercambia

import random

from individual import Individual

#? Siendo que los padres son unicamente dos individuos, podriamos usar tuplas. Debatir.
def crossover(parents: list[Individual]) -> list[Individual]:
    
    children: list[Individual] = [];
    
    # Buscar puntos de intersección
    intersection_points = set(parents[0].path) & set(parents[1].path)
    if not intersection_points:
        # Si no hay intersección, retornar los padres
        return parents

    # Elegir un punto de intersección aleatorio
    crossover_point = random.choice(list(intersection_points))

    # Crear nuevos individuos cruzando los paths
    new_first_path = parents[0].path[:parents[0].path.index(crossover_point)] + parents[1].path[parents[1].path.index(crossover_point):]
    new_second_path = parents[1].path[:parents[1].path.index(crossover_point)] + parents[0].path[parents[0].path.index(crossover_point):]

    children.append(Individual(path=new_first_path, pathDistance=None, targetFunctionValue=None, fitness=None))
    children.append(Individual(path=new_second_path, pathDistance=None, targetFunctionValue=None, fitness=None))

    # Retornar los nuevos individuos
    return children