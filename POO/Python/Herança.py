class Animal:
    def fazer_som(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def abanar_rabo(self):
        print("O cachorro abana o rabo.")

# Explicação: Cachorro herda o método fazer_som() da 
#   classe Animal, e ainda adiciona seu próprio 
#   comportamento.