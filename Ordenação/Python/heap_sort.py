def heap_sort(arr):
    n = len(arr)
    
    # Constrói um max-heap (Complexidade: O(n))
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extrai elementos um por um (Complexidade: O(n log n))
    for i in range(n - 1, 0, -1):
        # Move a raiz (maior elemento) para o final
        arr[0], arr[i] = arr[i], arr[0]
        # Reconstroi o heap no array reduzido
        heapify(arr, i, 0)
        print(f"Passo {n - i}: {arr}")  # Mostra o estado atual

def heapify(arr, n, i):
    maior = i  # Inicializa o maior como raiz
    esq = 2 * i + 1
    dir = 2 * i + 2
    
    # Verifica se o filho esquerdo é maior que a raiz
    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    
    # Verifica se o filho direito é maior que a raiz
    if dir < n and arr[dir] > arr[maior]:
        maior = dir
    
    # Troca se necessário e faz heapify recursivamente
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

# Teste
arr = [12, 11, 13, 5, 6, 7]
print("Array original:", arr)
heap_sort(arr)
print("Array ordenado:", arr)

# Portugol

# algoritmo heap_sort
#     procedimento heapify(vetor[], tamanho, indice)
#         maior ← indice
#         esquerda ← 2 * indice + 1
#         direita ← 2 * indice + 2
        
#         se esquerda < tamanho e vetor[esquerda] > vetor[maior] então
#             maior ← esquerda
#         fimse
        
#         se direita < tamanho e vetor[direita] > vetor[maior] então
#             maior ← direita
#         fimse
        
#         se maior ≠ indice então
#             troca(vetor[indice], vetor[maior])
#             heapify(vetor, tamanho, maior)
#         fimse
#     fimprocedimento

#     procedimento heap_sort(vetor[], n)
#         // Construir heap máximo
#         para i de n div 2 - 1 até 0 passo -1 faça
#             heapify(vetor, n, i)
#         fimpara
        
#         // Extrair elementos do heap
#         para i de n-1 até 1 passo -1 faça
#             troca(vetor[0], vetor[i])
#             heapify(vetor, i, 0)
#         fimpara
#     fimprocedimento
# fimalgoritmo