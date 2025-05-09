class Pilha:
    def __init__(self):
        self.items = []  # Lista usada para armazenar os elementos da pilha

    def isEmpty(self):
        return self.items == []  # Retorna True se a pilha estiver vazia

    def push(self, item):
        self.items.append(item)  # Adiciona um item no topo da pilha

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()  # Remove e retorna o item do topo
        return None  # Retorna None se a pilha estiver vazia

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]  # Retorna o item do topo sem remover
        return None

    def size(self):
        return len(self.items)  # Retorna a quantidade de itens na pilha
