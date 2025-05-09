# Definição da classe Fila
class Fila:
    
    # Método construtor: inicializa a fila como uma lista vazia
    def __init__(self):
        self.items = []  # 'items' será a estrutura que armazena os elementos da fila

    # Verifica se a fila está vazia
    def isEmpty(self):
        return self.items == []  # Retorna True se a lista estiver vazia, ou False caso contrário

    # Insere um item no início da fila (posição 0)
    def enqueue(self, item):
        self.items.insert(0, item)  # 'insert(0, item)' insere o elemento no início da lista

    # Remove o último item da fila (que é o primeiro a ter sido inserido)
    def dequeue(self):
        return self.items.pop()  # 'pop()' sem índice remove e retorna o último item da lista

    # Retorna o tamanho atual da fila
    def size(self):
        return len(self.items)  # 'len' retorna a quantidade de elementos na lista
    
    # Adiciona um método __str__ para representar a fila como uma string
    def __str__(self):
        return str(self.items)  # Exibe a fila como uma lista

#USANDO A FILA
fila = Fila()
fila.enqueue("Koda")
fila.enqueue(2)
fila.enqueue(3)
print(fila.size())  # Imprime o tamanho da fila
print(fila)

fila.dequeue()
print(fila.size())  # Imprime o tamanho da fila
print(fila)  # Imprime a fila atualizada

