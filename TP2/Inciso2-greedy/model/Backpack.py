#Mochila, tiene un volumen total (cm3), volumen restante, valor total y una lista de objetos que contiene

from model.Object import Object

class Backpack:
    def __init__(self, maxVolume: int):
        self.combination: int = None
        self.maxVolume: int = maxVolume
        self.currentVolume: int = 0;
        self.value: int = 0;
        self.contents: list[Object] = [] 
        pass;
    
    def addObject(self, newObj: Object) -> bool:
        if(self.currentVolume + newObj.volume <= self.maxVolume):
            self.currentVolume += newObj.volume
            self.value += newObj.value
            self.contents.append(newObj)
            self.contents = sorted(self.contents, key = lambda object: object.valToVolRatio, reverse = True) #Ordeno por la relacion valor / volumen de cada objeto
            return True
        else:
            return False

    def __str__(self) -> str:
        formatted_combination_bin = f"{self.combination:010b}" #formateo para que siempre imprima la misma cantidad de digitos y saque el 0b
        return f"Mochila: \n\t\tCombinación: {formatted_combination_bin}\n\t\tValor:{self.value}\n\t\tVolumen ocupado: {self.currentVolume}\n\t\tValor / Volumen: {self.value / self.currentVolume}"
  
    # Se redefine el método __eq__ para comparar mochilas basándose en su valor, volumen restante y contenidos
    def __eq__(self, other) -> bool:
        if not isinstance(other, Backpack):
            return False
        return (self.value == other.value and 
                self.currentVolume == other.currentVolume and
                len(self.contents) == len(other.contents) and
                all(obj in other.contents for obj in self.contents))
# Se recomienda implementar __hash__ si se implementa __eq__ pero no es estrictamente necesario