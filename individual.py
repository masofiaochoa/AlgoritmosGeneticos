class Individual:
    def __init__(self, chromosome: int, fitness: float): #Para python los binarios son ints, no tiene tipo aparte, pero el 99% de las veces voy a trabajar con bitwise operators como si fuera un binario
        self.chromosome = chromosome
        self.fitness = fitness
        pass;

    def __str__(self) -> str:
        return f"Chromosome: {bin(self.chromosome)} - Fitness: {self.fitness}" #Bin solamente hace que el int se imprima como binario
    
