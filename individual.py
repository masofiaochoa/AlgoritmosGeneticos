class Individual:
    def __init__(self, chromosome: int, targetFunctionValue: float,fitness: float): #Para python los binarios son ints, no tiene tipo aparte, pero el 99% de las veces voy a trabajar con bitwise operators como si fuera un binario
        self.chromosome = chromosome
        self.targetFunctionValue = targetFunctionValue
        self.fitness = fitness
        pass;

    def __str__(self) -> str:
        binary_value = bin(self.chromosome).lstrip("0b")
        return f"Individual:\n\t\tValor real:{self.chromosome}\n\t\tChromosome: {binary_value}\n\t\tValor Objetivo: {self.targetFunctionValue}\n\t\tFitness: {self.fitness}" #Bin solamente hace que el int se imprima como binario
    
    #{bin(self.chromosome)}
    
