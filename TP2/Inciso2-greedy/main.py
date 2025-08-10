from model.Backpack import Backpack
from model.Object import Object
import time
import sys 

# Redirigir la salida estándar a un archivo
sys.stdout = open("resultado_inciso2.txt", "w")

BACKPACK_MAX_VOLUME: int = 4200

OBJECT_ROOSTER: list[Object] = [
    Object(150, 20),
    Object(325, 40),
    Object(600, 50),
    Object(805, 36),
    Object(430, 25),
    Object(1200, 64),
    Object(770, 54),
    Object(60, 18),
    Object(930, 46),
    Object(353, 28)
]

OBJECT_ROOSTER_SIZE: int = len(OBJECT_ROOSTER)

BACKPACK: Backpack = Backpack(BACKPACK_MAX_VOLUME)



#PROGRAMA
startTime: float = time.time()

#Ordeno el rooster de objetos por su relación valor/volumen
OBJECT_ROOSTER = sorted(OBJECT_ROOSTER, key = lambda object: object.valToVolRatio, reverse = True)

print('-------------------------------------------\nListado de objetos ordenados:\n')
for object in OBJECT_ROOSTER:
    print(object)

combination: int = 0

for i in range(0, OBJECT_ROOSTER_SIZE - 1):
    succesfullyAdded: bool = BACKPACK.addObject(OBJECT_ROOSTER[i])

    if(succesfullyAdded):
        combination |= (1 << i)

endTime: float = time.time()
BACKPACK.combination = combination

print(f'-------------------------------------------\nMochila armada en {endTime - startTime:5f} Segundos:\n')
print(BACKPACK)
print('\nContenidos:\n')
contents: list[Object] = BACKPACK.contents
for object in contents:
    print(object)
