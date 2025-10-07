from typing import Dict, List
import pandas as pd

from capitalRoute import CapitalRoute
from config import *
from enum_method import *

from capital import Capital
from functions.Routing_Methods.geneticAlgorithmRoute import geneticAlgorithmRoute
from functions.Routing_Methods.nearestNeighborRoute import nearestNeighborRoute
from functions.Routing_Methods.shortestPathToVisitAllRoute import shortestPathToVisitAllRoute
from functions.AG.plot_utils import plot_route_cartopy

#VARIABLES
CAPITALS: Dict[str, Capital] = {}

#CARGA DE CSV
df: pd.DataFrame = pd.read_csv("capitales.csv")

#Esta columna no nos sirve de mucho por eso la renombramos
df = df.rename(columns={df.columns[0]: 'Capital'})

df.set_index('Capital', inplace=True)

#Reemplazo los espacios vacios con 0 (Distancia a una misma capital desde esa capital es 0) lo hago para que no figure como NaN
df = df.fillna(0)

#Nos aseguramos que las filas y columnas coincidan (En una matriz de distancias debería ser asi)
assert set(df.index) == set(df.columns), "Fila y columnas no coinciden"


# CREAMOS LAS CAPITALES
CAPITALS = {name: Capital(name, i) for i, name in enumerate(df.index)}
print([capital.name for capital in CAPITALS.values()])

# CARGAMOS LAS DISTANCIAS DE CADA CAPITAL A TODAS LAS DEMAS CAPITALES
for origin in df.index:
    for dest in df.columns:
        if pd.notna(df.at[origin, dest]):
            CAPITALS[origin].distances[dest] = float(df.at[origin, dest])



#PROGRAMA PRINCIPAL

# INCISO A
if ROUTING_METHOD == Routing_Method.NEAREST_TO_START_CAPITAL:
    route = nearestNeighborRoute(START_CAPITAL, CAPITALS)
    print("Metodo de elección de ruta: “Desde cada ciudad ir a la ciudad más cercana no visitada. Con una ciudad de partida definida por el usuario")
    print("Ciudad de partida:", route.startCapital.name)
    print("Recorrido completo:", " -> ".join(route.getCapitalNames()))
    print(f"Longitud total del trayecto: {route.distance:.1f} km")

# INCISO B    
elif ROUTING_METHOD == Routing_Method.SHORTEST_PATH_TO_ALL:
    route = shortestPathToVisitAllRoute(CAPITALS)
    print("Metodo de elección de ruta: “Recorrido mínimo para visitar todas las capitales de las provincias de la República Argentina yendo siempre a la ciudad sin visitar más cercana")
    print("Ciudad de partida:", route.startCapital.name)
    print("Recorrido completo:", " -> ".join(route.getCapitalNames()))
    print(f"Longitud total del trayecto: {route.distance:.1f} km")

# NO IMPLEMENTADO (placeholder)
elif ROUTING_METHOD == Routing_Method.GENETIC_ALGORITHM:
    finalPopulation: list[CapitalRoute] = geneticAlgorithmRoute(CAPITALS)
    
    # Se muestran los cromosomas de la población final
    # for i, cp in enumerate(finalPopulation):
    #     print(f"Cromosoma:{i}\n\t{cp}\n")

    plot_route_cartopy(finalPopulation[0])