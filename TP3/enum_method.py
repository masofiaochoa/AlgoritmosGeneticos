from enum import Enum

#Contiene los posibles metodos de selección de padre a elegir. Es una clase 100% utilititaria y para mayor facilidad de modularización del código 
class AG_Method(Enum):
    ROULETTE: int = 1
    TOURNAMENT: int  = 2
    
class Routing_Method(Enum):
    NEAREST_TO_START_CAPITAL: int = 1
    SHORTEST_PATH_TO_ALL: int = 2
    GENETIC_ALGORITHM: int = 3

class Capital_Names(Enum):
    CIDAD_DE_BS_AS = "CIDAD DE BS AS"
    CORDOBA = "CORDOBA"
    CORRIENTES = "CORRIENTES"
    FORMOSA = "FORMOSA"
    LA_PLATA = "LA PLATA"
    LA_RIOJA = "LA RIOJA"
    MENDOZA = "MENDOZA"
    NEUQUEN = "NEUQUEN"
    PARANA = "PARANA"
    POSADAS = "POSADAS"
    RAWSON = "RAWSON"
    RESISTENCIA = "RESISTENCIA"
    RIO_GALLEGOS = "RIO GALLEGOS"
    SFDV_DE_CATAMARCA = "SFDV DE CATAMARCA"
    SM_DE_TUCUMAN = "SM DE TUCUMAN"
    SS_DE_JUJUY = "SS DE JUJUY"
    SALTA = "SALTA"
    SAN_JUAN = "SAN JUAN"
    SAN_LUIS = "SAN LUIS"
    SANTA_FE = "SANTA FE"
    SANTA_ROSA = "SANTA ROSA"
    SGO_DEL_ESTERO = "SGO DEL ESTERO"
    USHUAIA = "USHUAIA"
    VIEDMA = "VIEDMA"
