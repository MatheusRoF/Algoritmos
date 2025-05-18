def merge_sort(arr):
    # Função principal que implementa o Merge Sort
    # Complexidade de Tempo: O(n log n) - Sempre divide pela metade e depois combina
    # Complexidade de Espaço: O(n) - Precisa de espaço auxiliar para mesclar

    if len(arr) > 1:
        print(f"Dividindo: {arr}")
        mid = len(arr) // 2  # Encontra o meio do array
        left_half = arr[:mid]  # Divide a primeira metade
        right_half = arr[mid:]  # Divide a segunda metade

        # Chama recursivamente para cada metade
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0  # Inicializa índices para percorrer os arrays

        # Mescla as duas metades ordenadas
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copia os elementos restantes de left_half, se houver
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copia os elementos restantes de right_half, se houver
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print(f"Mesclando: {arr}")

# Testando com seu exemplo
arr = [64, 25, 12, 22, 11]
print("Array original:", arr)
merge_sort(arr)
print("Array ordenado:", arr)

# algoritmo merge_sort

# // Complexidade de Tempo: O(n log n) - Sempre divide pela metade e depois combina
# // Complexidade de Espaço: O(n) - Precisa de espaço auxiliar para mesclar

# função merge(lista[inteiro], esquerda[inteiro], meio[inteiro], direita[inteiro])
#     tamanho_esq ← meio - esquerda + 1
#     tamanho_dir ← direita - meio
    
#     // Cria arrays temporários
#     lista_esq[inteiro:tamanho_esq]
#     lista_dir[inteiro:tamanho_dir]
    
#     // Copia dados para os arrays temporários
#     para i de 0 até tamanho_esq - 1 faça
#         lista_esq[i] ← lista[esquerda + i]
#     fimpara
    
#     para j de 0 até tamanho_dir - 1 faça
#         lista_dir[j] ← lista[meio + 1 + j]
#     fimpara
    
#     // Mescla os arrays temporários
    
#     i ← 0  // Índice inicial do primeiro subarray
#     j ← 0  // Índice inicial do segundo subarray
#     k ← esquerda  // Índice inicial do array mesclado
    
#     enquanto i < tamanho_esq e j < tamanho_dir faça
#         se lista_esq[i] <= lista_dir[j] então
#             lista[k] ← lista_esq[i]
#             i ← i + 1
#         senão
#             lista[k] ← lista_dir[j]
#             j ← j + 1
#         fimse
#         k ← k + 1
#     fimenquanto
    
#     // Copia os elementos restantes de lista_esq, se houver
#     enquanto i < tamanho_esq faça
#         lista[k] ← lista_esq[i]
#         i ← i + 1
#         k ← k + 1
#     fimenquanto
    
#     // Copia os elementos restantes de lista_dir, se houver
#     enquanto j < tamanho_dir faça
#         lista[k] ← lista_dir[j]
#         j ← j + 1
#         k ← k + 1
#     fimenquanto
# fimfunção

# função merge_sort_recursivo(lista[inteiro], esquerda[inteiro], direita[inteiro])
#     se esquerda < direita então
#         escreva("Dividindo: ")
#         para i de esquerda até direita faça
#             escreva(lista[i], " ")
#         fimpara
#         escreval()
        
#         meio ← esquerda + (direita - esquerda) / 2
        
#         // Ordena primeira e segunda metades
#         merge_sort_recursivo(lista, esquerda, meio)
#         merge_sort_recursivo(lista, meio + 1, direita)
        
#         // Mescla as metades ordenadas
#         merge(lista, esquerda, meio, direita)
        
#         escreva("Mesclando: ")
#         para i de esquerda até direita faça
#             escreva(lista[i], " ")
#         fimpara
#         escreval()
#     fimse
# fimfunção

# função merge_sort(lista[inteiro], tamanho[inteiro])
#     merge_sort_recursivo(lista, 0, tamanho - 1)
# fimfunção

# // Programa principal
# variável lista[5] ← {64, 25, 12, 22, 11}
# escreva("Array original: ")
# para i de 0 até 4 faça
#     escreva(lista[i], " ")
# fimpara
# escreval()

# merge_sort(lista, 5)

# escreva("Array ordenado: ")
# para i de 0 até 4 faça
#     escreva(lista[i], " ")
# fimpara
# escreval()
# fimalgoritmo