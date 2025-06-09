from enum_method import Method

#CONSTANTS
POPULATION_SIZE: int = 10; #poblacion
CHROMOSOME_LEN: int = 30; #Cantidad de genes en cromosoma del individual
MUTATION_CHANCE: float = 0.05; #probabilidad de mutacion
CROSSOVER_CHANCE: float = 0.75; #probabilidad de cruza
ELITISM_PERCENTAGE: float = 0.2
ELITISM_CHOSEN_INDIVIDUAL_AMOUNT: int = int(POPULATION_SIZE * ELITISM_PERCENTAGE)
REMAINDER_POPULATION: int = POPULATION_SIZE - ELITISM_CHOSEN_INDIVIDUAL_AMOUNT #Cantidad de poblacion restante luego de aplicar elitismo a la que se aplicaran los metodos (crossover y mutacion)
SELECTION_METHOD: Method = Method.TOURNAMENT;
COEF: int = 2**30 - 1
TOURNAMENT_PERCENTAGE: float = 0.4