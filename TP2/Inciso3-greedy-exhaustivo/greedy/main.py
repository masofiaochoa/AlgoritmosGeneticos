from model.Backpack import Backpack
from model.Object import Object
import time

BACKPACK_MAX_WEIGHT: int = 3000

OBJECT_ROOSTER: list[Object] = [
    Object(1800, 72),
    Object(600, 36),
    Object(1200, 60),
]

OBJECT_ROOSTER_SIZE: int = len(OBJECT_ROOSTER)

BACKPACK: Backpack = Backpack(BACKPACK_MAX_WEIGHT)



#PROGRAMA GREEDY
startTime: float = time.time()
#Ordeno el rooster de objetos por su relación valor/peso
OBJECT_ROOSTER = sorted(OBJECT_ROOSTER, key = lambda object: object.valToWeightRatio, reverse = True)

print('-------------------------------------------\nListado de objetos ordenados:\n')
for object in OBJECT_ROOSTER:
    print(object)

combination: int = 0

for i in range(0, OBJECT_ROOSTER_SIZE - 1):
    succesfullyAdded: bool = BACKPACK.addObject(OBJECT_ROOSTER[i])
    if(succesfullyAdded):
        combination |= (1 << i)

endTime: float = time.time() #Contamos con solucion obtenida en este momento

BACKPACK.combination = combination

print(f'-------------------------------------------\nMochila armada en {endTime - startTime:.5f} segundos:\n')
print(BACKPACK)
print('\nContenidos:\n')
contents: list[Object] = BACKPACK.contents
for object in contents:
    print(object)
