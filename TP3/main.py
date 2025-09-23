from typing import Dict
import pandas as pd

from config import *
from enum_method import *

from capital import Capital
from functions.Routing_Methods.nearestNeighborRoute import nearestNeighborRoute
from functions.Routing_Methods.shortestPathToVisitAllRoute import shortestPathToVisitAllRoute

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

# CARGAMOS LAS DISTANCIAS DE CADA CAPITAL A TODAS LAS DEMAS CAPITALES
for origin in df.index:
    for dest in df.columns:
        if pd.notna(df.at[origin, dest]):
            CAPITALS[origin].distances[dest] = float(df.at[origin, dest])




#PROGRAMA PRINCIPAL INCISO A
if(ROUTING_METHOD == Routing_Method.NEAREST_TO_START_CITY):
    route, distance = nearestNeighborRoute(START_CITY, CAPITALS)
    print("Metodo de elección de ruta: “Desde cada ciudad ir a la ciudad más cercana no visitada. Con una ciudad de partida definida por el usuario")
    print("Ciudad de partida:", START_CITY)
    print("Recorrido completo:", " -> ".join(route))
    print(f"Longitud total del trayecto: {distance:.1f} km")
    
elif(ROUTING_METHOD == Routing_Method.SHORTEST_PATH_TO_ALL):
    route, distance = shortestPathToVisitAllRoute(CAPITALS)
    print("Metodo de elección de ruta: “Recorrido mínimo para visitar todas las capitales de las provincias de la República Argentina yendo siempre a la ciudad sin visitar mas cercana")
    print("Ciudad de partida:", route[0])
    print("Recorrido completo:", " -> ".join(route))
    print(f"Longitud total del trayecto: {distance:.1f} km")
    
elif(ROUTING_METHOD == Routing_Method.GENETIC_ALGORITHM):
    print("A implementar")