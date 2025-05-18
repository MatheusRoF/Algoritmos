def busca_binaria(lista, item):
    """
    Implementação do algoritmo de busca binária que retorna tanto o índice quanto o valor encontrado.
    
    Args:
        lista: Uma lista ORDENADA onde a busca será realizada.
        item: O valor que está sendo buscado na lista.
    
    Returns:
        Uma tupla contendo (índice, valor) se o item for encontrado, ou (None, None) se não encontrado.
    """
    
    # Inicializa os ponteiros para o início e fim da lista
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        # Encontra o elemento do meio
        meio = (baixo + alto) // 2
        chute = lista[meio]
        
        # Verifica se o chute é igual ao item buscado
        if chute == item:
            return meio, chute  # Retorna tanto o índice quanto o valor
        
        # Se o chute for maior que o item, ajusta o limite superior
        if chute > item:
            alto = meio - 1
        # Se o chute for menor que o item, ajusta o limite inferior
        else:
            baixo = meio + 1
    
    # Retorna None para ambos se o item não for encontrado
    return None, None

# Exemplo de uso
if __name__ == "__main__":
    # Lista ordenada de números
    numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    # Testando a busca
    indice, valor = busca_binaria(numeros, 10)
    print(f"Para o valor 10: Índice = {indice}, Valor = {valor}")
    # Saída: Para o valor 10: Índice = 4, Valor = 10
    
    indice, valor = busca_binaria(numeros, 16)
    print(f"Para o valor 16: Índice = {indice}, Valor = {valor}")
    # Saída: Para o valor 16: Índice = 7, Valor = 16
    
    indice, valor = busca_binaria(numeros, 5)
    print(f"Para o valor 5: Índice = {indice}, Valor = {valor}")
    # Saída: Para o valor 5: Índice = None, Valor = None
    
    # Lista ordenada de strings
    nomes = ['Alice', 'Bruno', 'Clara', 'Daniel', 'Eduarda', 'Felipe']
    
    indice, valor = busca_binaria(nomes, 'Clara')
    print(f"Para o nome 'Clara': Índice = {indice}, Valor = {valor}")
    # Saída: Para o nome 'Clara': Índice = 2, Valor = Clara
    
    indice, valor = busca_binaria(nomes, 'Zeca')
    print(f"Para o nome 'Zeca': Índice = {indice}, Valor = {valor}")
    # Saída: Para o nome 'Zeca': Índice = None, Valor = None