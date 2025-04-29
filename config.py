from enum_method import Method

#CONSTANTS
POPULATION_SIZE: int = 4; #poblacion
CHROMOSOME_LEN: int = 5; #Cantidad de genes en cromosoma del individual
MUTATION_CHANCE: float = 0.001; #probabilidad de mutacion
CROSSOVER_CHANCE: float = 0.95; #probabilidad de cruza
ELITISM_RATE: float = 0.0;
SELECTION_METHOD: Method = "Roulette"; #CORREGIR