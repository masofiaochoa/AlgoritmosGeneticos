#Mochila, tiene un volumen total (cm3), volumen restante, valor total y una lista de objetos que contiene

from model.Object import Object

class Backpack:
    def __init__(self, baseVolume: int):
        self.baseVolume: int = baseVolume
        self.remainderVolume: int = baseVolume
        self.value: int = 0;
        self.contents: list[Object] = [] 
        pass;
    
    def addObject(self, newObj: Object) -> bool:
        if(newObj.volume > self.remainderVolume): #Checkeo que haya espacio
            return False
        else:
            self.remainderVolume -= newObj.volume
            self.value += newObj.value
            self.contents.append(newObj)
            self.contents = sorted(self.contents, key = lambda object: object.valToVolRatio, reverse = True) #Ordeno por la relacion valor / volumen de cada objeto
            return True   
        
    def __str__(self) -> str:
        return f"Mochila:\n\t\tValor:{self.value}\n\t\tVolumen restante: {self.remainderVolume}\n\t\tValor / Volumen: {self.value / (self.baseVolume - self.remainderVolume)}"
    
    # Se redefine el método __eq__ para comparar mochilas basándose en su valor, volumen restante y contenidos
    def __eq__(self, other) -> bool:
        if not isinstance(other, Backpack):
            return False
        return (self.value == other.value and 
                self.remainderVolume == other.remainderVolume and
                len(self.contents) == len(other.contents) and
                all(obj in other.contents for obj in self.contents))
# Se recomienda implementar __hash__ si se implementa __eq__ pero no es estrictamente necesario