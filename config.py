from enum_method import Method
#Contiene constantes globales que sirven para configurar la corrida a realizarce

#CONSTANTS
POPULATION_SIZE: int = 10; #Cantidad de poblacion
CHROMOSOME_LEN: int = 30; #Cantidad de genes en cromosoma de cada individuo
MUTATION_CHANCE: float = 0.05; #probabilidad de mutacion
CROSSOVER_CHANCE: float = 0.75; #probabilidad de cruza
ELITISM_PERCENTAGE: float = 0.2 #Porcentaje de elitismo (Ej: si 0.2 y tamaño de poblacion = 10 entonces 10 * 0.2 = 2 -> 2 individuos seran elegidos via elitismo)
ELITISM_CHOSEN_INDIVIDUAL_AMOUNT: int = int(POPULATION_SIZE * ELITISM_PERCENTAGE)
REMAINDER_POPULATION: int = POPULATION_SIZE - ELITISM_CHOSEN_INDIVIDUAL_AMOUNT #Cantidad de poblacion restante luego de aplicar elitismo a la que se aplicaran los metodos (crossover y mutacion)
SELECTION_METHOD: Method = Method.TOURNAMENT; #Metodo de selección de padres
TOURNAMENT_PERCENTAGE: float = 0.4 #Porcentaje de individuos que participaran en torneo, funciona de la misma manera que el porcentaje de elitismo
COEF: int = 2**30 - 1 #Coeficiente de la funcion objetivo del enunciado