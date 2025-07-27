#Objeto, tiene un valor ($), un peso y una relación valor/peso
class Object:
    def __init__(self, volume: int, value: int):
        self.value: int = value
        self.volume: int = volume
        self.valToVolRatio: float = value / volume
        pass;

    def __str__(self) -> str:
        return f"Objeto:\n\t\tValor:{self.value}\n\t\tVolumen: {self.volume}\n\t\tValor / Volumen: {self.valToVolRatio}"
