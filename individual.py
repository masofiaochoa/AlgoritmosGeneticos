class Individual:
    def __init__(self, chromosome: int, targetFunctionValue: float,fitness: float): #Para python los binarios son ints, no tiene tipo aparte, pero el 99% de las veces voy a trabajar con bitwise operators como si fuera un binario
        self.chromosome = chromosome
        self.targetFunctionValue = targetFunctionValue
        self.fitness = fitness
        pass;

    def __str__(self) -> str:
        return f"Individual:\n\t\tChromosome: {bin(self.chromosome)}\n\t\tFitness: {self.fitness}" #Bin solamente hace que el int se imprima como binario
    
