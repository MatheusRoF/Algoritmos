from abc import ABC, abstractmethod

# Classe abstrata (modelo genérico)
class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def mover(self):
        pass

# Classe concreta com implementação específica
class Carro(Veiculo):
    def mover(self):
        print(f"{self.modelo} está dirigindo na estrada.")

# Explicação: A classe Veiculo define um 
#   método abstrato mover() que cada veículo 
#   deve implementar. Carro implementa esse comportamento 
#   específico.