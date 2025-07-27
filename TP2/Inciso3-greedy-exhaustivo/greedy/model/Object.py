#Objeto, tiene un valor ($), un peso y una relación valor/peso
class Object:
    def __init__(self, weight: int, value: int):
        self.value: int = value
        self.weight: int = weight
        self.valToWeightRatio: float = value / weight
        pass;

    def __str__(self) -> str:
        return f"Objeto:\n\t\tValor:{self.value}\n\t\tPeso: {self.weight}\n\t\tValor / Peso: {self.valToWeightRatio}"
