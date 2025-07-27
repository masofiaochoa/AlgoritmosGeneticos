#Mochila, tiene un peso total (cm3), peso restante, valor total y una lista de objetos que contiene

from model.Object import Object

class Backpack:
    def __init__(self, maxWeight: int):
        self.combination: int = None
        self.maxWeight: int = maxWeight
        self.currentWeight: int = 0;
        self.value: int = 0;
        self.contents: list[Object] = [] 
        pass;
    
    def addObject(self, newObj: Object) -> bool:
        if(self.currentWeight + newObj.weight <= self.maxWeight):
            self.currentWeight += newObj.weight
            self.value += newObj.value
            self.contents.append(newObj)
            self.contents = sorted(self.contents, key = lambda object: object.valToWeightRatio, reverse = True) #Ordeno por la relacion valor / peso de cada objeto
            return True
        else:
            return False

    def __str__(self) -> str:
        formatted_combination_bin = f"{self.combination:03b}" #formateo para que siempre imprima la misma cantidad de digitos y saque el 0b
        return f"Mochila: \n\t\tCombinación: {formatted_combination_bin}\n\t\tValor:{self.value}\n\t\tPeso ocupado: {self.currentWeight}\n\t\tValor / peso: {self.value / self.currentWeight}"
  
    # Se redefine el método __eq__ para comparar mochilas basándose en su valor, peso restante y contenidos
    def __eq__(self, other) -> bool:
        if not isinstance(other, Backpack):
            return False
        return (self.value == other.value and 
                self.currentWeight == other.currentWeight and
                len(self.contents) == len(other.contents) and
                all(obj in other.contents for obj in self.contents))
# Se recomienda implementar __hash__ si se implementa __eq__ pero no es estrictamente necesario