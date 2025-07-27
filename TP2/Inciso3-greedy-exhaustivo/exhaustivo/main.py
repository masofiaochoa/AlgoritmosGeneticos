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


BACKPACKS: list[Backpack] = []

#PROGRAMA
startTime: float = time.time()

for i in range(1, 2**OBJECT_ROOSTER_SIZE): #Loop que corre n veces donde n es la cantidad de combinaciones posibles con la cantidad de objetos del listado
    backpack: Backpack = Backpack(BACKPACK_MAX_WEIGHT, combination=i)

    for j in range(OBJECT_ROOSTER_SIZE):
        if (i >> j) & 1:  # i representa en binario los objetos a cargar, ej 10010101 nos dice que se cargan los objetos con indice 10, 4, 2 y 0
                        #Hago esto para checkear que indices estan 'encendidos' y despues cargo con dicho indice
            backpack.addObject(OBJECT_ROOSTER[j])
    
    BACKPACKS.append(backpack)

BACKPACKS = sorted(BACKPACKS, key = lambda backpack: backpack.value, reverse = True)

print('-------------------------------------------\nLISTADO TOTAL DE MOCHILAS:\n')
for backpack in BACKPACKS:
    print(backpack)

print('-------------------------------------------\nMOCHILAS ELIMINADAS:\n')
for i in range(len(BACKPACKS) - 1, -1, -1): #Recorro el arreglo de el final hacia el principio porque sino se bugean los indices al hacer .pop
    if BACKPACKS[i].isValidBackpack():
        continue
    else:
        print(BACKPACKS[i])
        BACKPACKS.pop(i)

endTime: float = time.time() #En este momento ya se encontro la solucion

print('-------------------------------------------\nLISTADO FINAL DE MOCHILAS:\n')
for backpack in BACKPACKS:
    print(backpack)

print(f'-------------------------------------------\nMEJOR SOLUCION OBTENIDA EN {endTime-startTime:.5f} segundos:\n')
print(BACKPACKS[0])