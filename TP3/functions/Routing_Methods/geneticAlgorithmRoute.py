import random
from typing import Dict, List
from capital import Capital
from capitalRoute import CapitalRoute
from config import *

def geneticAlgorithmRoute(start: str, capitals: Dict[str, Capital]) -> tuple[list[str], float]:
    # ---- INICIALIZACIÓN ----
    all_capitals_except_start: List[Capital] = [c for name, c in capitals.items() if name != start]
    population: List[CapitalRoute] = []

    for _ in range(POPULATION_SIZE):
        route = CapitalRoute(capitals[start])
        shuffled_caps = all_capitals_except_start[:]
        random.shuffle(shuffled_caps)
        for cap in shuffled_caps:
            route.addCapital(cap)
        route.returnToStartCapital()
        population.append(route)

    # ---- LOOP PRINCIPAL DEL AG ----
    for generation in range(MAX_GENERATIONS):
        # Calcular fitness relativo
        total_distance = sum(route.getRouteDistance() for route in population)
        for route in population:
            route.fitness = (total_distance - route.getRouteDistance()) / total_distance

        # ---- SELECCIÓN ----
        new_population: List[CapitalRoute] = []
        for _ in range(POPULATION_SIZE // 2):
            # Roulette wheel selection
            parents = random.choices(
                population,
                weights=[route.fitness for route in population],
                k=2
            )
            # ---- CROSSOVER ----
            child1, child2 = crossover(parents[0], parents[1])
            # ---- MUTACIÓN ----
            if random.random() < MUTATION_RATE:
                child1 = mutate(child1)
            if random.random() < MUTATION_RATE:
                child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

    # ---- SELECCIONAR MEJOR INDIVIDUO ----
    best_route = min(population, key=lambda r: r.getRouteDistance())
    return best_route.getCapitalNames(), best_route.getRouteDistance()