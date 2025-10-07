from enum_method import *
#Contiene constantes globales que sirven para configurar la corrida a realizarce

#PARAMETROS
START_CAPITAL = Capital_Names.USHUAIA.value #IMPORTANTE EL .VALUE

#METODO DE GENERACION DE RUTA
ROUTING_METHOD = Routing_Method.GENETIC_ALGORITHM

#VARIABLES ESPECIFICAS DE AG
SELECTION_METHOD = AG_Method.TOURNAMENT
#Determinan el porcentaje de la poblacion inicial que se genera utilizando el metodo de ir a la capital mas cercana primero
#Y el porcentage que elige aleatoriamente el camino
TARGET_GENERATION = 200
POPULATION_SIZE = 50; #Cantidad de poblacion

RANDOM_ROUTE_GENERATED = 25; #Cantidad de poblacion inicial que se genera con una ruta random
NEAREST_NEIGHBOR_ROUTE_GENERATED = 25 #Cantidad de poblacion inicial que se genera con una ruta que elige primero la capital mas cercana sin retornar al origen

MUTATION_CHANCE: float = 0.3; #probabilidad de mutacion
CROSSOVER_CHANCE: float = 0.7; #probabilidad de cruza
PRINT_GENERATIONS = [1, 2, 50, 100, 150, 199] # Generaciones en las que se imprimira el estado actual de la poblacion

ELITISM_PERCENTAGE: float = 0.0 #Porcentaje de elitismo (Ej: si 0.2 y tamaño de poblacion = 10 entonces 10 * 0.2 = 2 -> 2 individuos seran elegidos via elitismo)
ELITISM_CHOSEN_INDIVIDUAL_AMOUNT: int = int(POPULATION_SIZE * ELITISM_PERCENTAGE)
REMAINDER_POPULATION: int = POPULATION_SIZE - ELITISM_CHOSEN_INDIVIDUAL_AMOUNT #Cantidad de poblacion restante luego de aplicar elitismo a la que se aplicaran los metodos (crossover y mutacion)