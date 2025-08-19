from ..individual import Individual

def printCurrentGen(gen: int, population: list[Individual], max_fitness: float, min_fitness: float) -> None:
    print(f"\nGeneration {gen}:")
    print(f"  Max Fitness: {max_fitness}")
    print(f"  Min Fitness: {min_fitness}")