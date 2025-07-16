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