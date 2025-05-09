def bubble_sort(arr):  # Função que ordena o array usando Bubble Sort
    n = len(arr)  # Pega o tamanho do array

    # Complexidade de tempo:
    # - Pior caso: O(n²), quando a lista está invertida.
    # - Melhor caso: O(n), se estiver ordenada e com otimização (flag).
    # Complexidade de espaço: O(1) → algoritmo in-place

    # Percorre todo o array
    for i in range(n):
        trocou = False  # Flag para detectar se houve troca nessa passagem

        # A cada passada, o maior elemento "borbulha" para o final
        for j in range(0, n - 1 - i):  # n-1-i evita reavaliar o fim já ordenado
            if arr[j] > arr[j + 1]:
                # Troca os elementos se estiverem fora de ordem
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True  # Marca que houve troca

        # Mostra o estado do array após cada passagem
        print(f"Passo {i + 1}: {arr}")

        # Se não houve troca, a lista já está ordenada
        if not trocou:
            break

arr = [64, 25, 12, 22, 11]
print("Array original:", arr)
bubble_sort(arr)
print("Array ordenado:", arr)

#PORTUGOL
# função bubble_sort(lista[inteiro], tamanho)
#     para i de 0 até tamanho - 1 faça
#         trocou ← falso

#         // Percorre até o último elemento não ordenado
#         para j de 0 até tamanho - 2 - i faça
#             se lista[j] > lista[j + 1] então
#                 // Troca os elementos
#                 temp ← lista[j]
#                 lista[j] ← lista[j + 1]
#                 lista[j + 1] ← temp
#                 trocou ← verdadeiro
#             fimse
#         fimpara

#         // Mostra o estado da lista
#         escreva("Passo ", i + 1, ": ")
#         para k de 0 até tamanho - 1 faça
#             escreva(lista[k], " ")
#         fimpara
#         escreval()

#         // Se nenhuma troca foi feita, já está ordenado
#         se não trocou então
#             pare
#         fimse
#     fimpara
# fimfunção

# // Programa principal
# variável lista[5] ← {64, 25, 12, 22, 11}
# escreva("Lista original: ")
# para i de 0 até 4 faça
#     escreva(lista[i], " ")
# fimpara
# escreval()

# bubble_sort(lista, 5)

# escreva("Lista ordenada: ")
# para i de 0 até 4 faça
#     escreva(lista[i], " ")
# fimpara
