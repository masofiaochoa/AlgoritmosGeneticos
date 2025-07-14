from model.Backpack import Backpack
from model.Object import Object

BACKPACK_BASE_VOLUME: int = 4200

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

BACKPACKS: list[Backpack] = []


for i in range(1, 2**OBJECT_ROOSTER_SIZE): #Loop que corre n veces donde n es la cantidad de combinaciones posibles con la cantidad de objetos del listado
    backpack: Backpack = Backpack(BACKPACK_BASE_VOLUME)

    for j in range(OBJECT_ROOSTER_SIZE):
        if (i >> j) & 1:  # i representa en binario los objetos a cargar, ej 10010101 nos dice que se cargan los objetos con indice 10, 4, 2 y 0
                        #Hago esto para checkear que indices estan 'encendidos' y despues cargo con dicho indice
            backpack.addObject(OBJECT_ROOSTER[j])

    BACKPACKS.append(backpack)


BACKPACKS = sorted(BACKPACKS, key = lambda backpack: backpack.value, reverse = True)

for i in range (0, len(BACKPACKS)):
    print(BACKPACKS[i])