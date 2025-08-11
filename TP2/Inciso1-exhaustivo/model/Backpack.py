#Mochila, tiene un volumen total (cm3), volumen restante, valor total y una lista de objetos que contiene

from model.Object import Object

class Backpack:
    def __init__(self, maxVolume: int, combination: int):
        self.combination: int = combination
        self.maxVolume: int = maxVolume
        self.currentVolume: int = 0;
        self.value: int = 0;
        self.contents: list[Object] = [] 
        pass;
    
    def addObject(self, newObj: Object):
        self.currentVolume += newObj.volume
        self.value += newObj.value
        self.contents.append(newObj)
        self.contents = sorted(self.contents, key = lambda object: object.valToVolRatio, reverse = True) #Ordeno por la relacion valor / volumen de cada objeto
        
    def isValidBackpack(self) -> bool:
        if(self.currentVolume > self.maxVolume):
            return False
        else:
            return True
    
    def __str__(self) -> str:
        formatted_combination_bin = f"{self.combination:010b}" #formateo para que siempre imprima la misma cantidad de digitos y saque el 0b
        if(self.isValidBackpack()):
            return f"Mochila Nro {self.combination}\n\t\tCombinación: {formatted_combination_bin}\n\t\tValor:{self.value}\n\t\tVolumen ocupado: {self.currentVolume}\n\t\tValor / Volumen: {self.value / self.currentVolume}"
        else:
            return f"Mochila Nro {self.combination} NO VALIDA:\n\t\tCombinación: {formatted_combination_bin}\n\t\tValor:{self.value}\n\t\tVolumen ocupado: {self.currentVolume}"