#Mochila, tiene un Peso total (cm3), Peso restante, valor total y una lista de objetos que contiene

from model.Object import Object

class Backpack:
    def __init__(self, maxWeight: int, combination: int):
        self.combination: int = combination
        self.maxWeight: int = maxWeight
        self.currentWeight: int = 0;
        self.value: int = 0;
        self.contents: list[Object] = [] 
        pass;
    
    def addObject(self, newObj: Object):
        self.currentWeight += newObj.weight
        self.value += newObj.value
        self.contents.append(newObj)
        self.contents = sorted(self.contents, key = lambda object: object.valToWeightRatio, reverse = True) #Ordeno por la relacion valor / Peso de cada objeto
        
    def isValidBackpack(self) -> bool:
        if(self.currentWeight > self.maxWeight):
            return False
        else:
            return True
    
    def __str__(self) -> str:
        formatted_combination_bin = f"{self.combination:03b}" #formateo para que siempre imprima la misma cantidad de digitos y saque el 0b
        if(self.isValidBackpack()):
            return f"Mochila Nro {self.combination}\n\t\tCombinación: {formatted_combination_bin}\n\t\tValor:{self.value}\n\t\tPeso ocupado: {self.currentWeight}\n\t\tValor / Peso: {self.value / self.currentWeight}"
        else:
            return f"Mochila Nro {self.combination} NO VALIDA:\n\t\tCombinación: {formatted_combination_bin}\n\t\tValor:{self.value}\n\t\tPeso ocupado: {self.currentWeight}"