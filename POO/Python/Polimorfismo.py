class Animal:
    def fazer_som(self):
        print("Som genérico de animal.")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

class Vaca(Animal):
    def fazer_som(self):
        print("Muuu!")

# Explicação: Várias classes usam o mesmo método 
# (fazer_som), mas com comportamentos diferentes. 
# Isso é polimorfismo.

