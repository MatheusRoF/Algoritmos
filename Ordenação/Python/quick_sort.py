def quick_sort(arr, inicio=0, fim=None):
    if fim is None:
        fim = len(arr) - 1
    if inicio < fim:
        # Particiona o array e obtém o índice do pivô
        p = particao(arr, inicio, fim)
        # Ordena recursivamente os elementos antes e depois do pivô
        quick_sort(arr, inicio, p - 1)
        quick_sort(arr, p + 1, fim)
        print(f"Passo: {arr}")  # Mostra o estado atual

def particao(arr, inicio, fim):
    pivô = arr[fim]  # Escolhe o último elemento como pivô
    i = inicio - 1    # Índice do menor elemento
    
    for j in range(inicio, fim):
        # Se o elemento atual é menor ou igual ao pivô
        if arr[j] <= pivô:
            i += 1
            # Troca arr[i] e arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Coloca o pivô na posição correta
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

# Teste
arr = [10, 7, 8, 9, 1, 5]
print("Array original:", arr)
quick_sort(arr)
print("Array ordenado:", arr)

# Portugol

# algoritmo quick_sort
#     procedimento particao(vetor[], inicio, fim)
#         pivô ← vetor[fim]
#         i ← inicio - 1
        
#         para j de inicio até fim-1 faça
#             se vetor[j] <= pivô então
#                 i ← i + 1
#                 troca(vetor[i], vetor[j])
#             fimse
#         fimpara
        
#         troca(vetor[i + 1], vetor[fim])
#         retorne i + 1
#     fimprocedimento

#     procedimento quick_sort(vetor[], inicio, fim)
#         se inicio < fim então
#             p ← particao(vetor, inicio, fim)
#             quick_sort(vetor, inicio, p - 1)
#             quick_sort(vetor, p + 1, fim)
#         fimse
#     fimprocedimento
# fimalgoritmo