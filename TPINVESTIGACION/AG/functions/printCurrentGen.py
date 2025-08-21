from individual import Individual

def printCurrentGen(gen: int, population: list[Individual], max_fitness: float, min_fitness: float) -> None:
    print(f"------------------------------------------------------\n\tGeneration {gen}:")
    print(f"\n\tCromosoma con el máximo fitness: {population[-1]}\n")
    print(f"\n\tCromosoma con el mínimo fitness: {population[0]}")