def insertion_sort(arr):  # Insere o valor no lugar certo
    n = len(arr)  # Pega o tamanho do array

    # Complexidade de tempo O(n²) no pior caso (lista inversamente ordenada)
    # Melhor caso: O(n) se a lista já estiver ordenada
    # Complexidade de Espaço O(1): algoritmo in-place (não usa espaço extra)

    # Começa da segunda posição (índice 1), pois o primeiro já está "ordenado"
    for i in range(1, n):
        chave = arr[i]  # A "chave" é o valor que queremos inserir na parte ordenada
        j = i - 1       # Começamos comparando com o elemento anterior

        # Enquanto o elemento anterior for maior que a chave,
        # vamos deslocando os elementos para a direita
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]  # Move o elemento maior uma posição à frente
            j -= 1              # Vai para o próximo elemento à esquerda

        # Quando encontramos a posição correta, inserimos a chave
        arr[j + 1] = chave

        # Mostra o estado do array após cada passo da ordenação
        print(f"Passo {i}: {arr}")

# Testando com seu exemplo
arr = [64, 25, 12, 22, 11]
print("Array original:", arr)
insertion_sort(arr)
print("Array ordenado:", arr)

#PORTUGOL
# função insertion_sort(lista[inteiro], tamanho)
#     para i de 1 até tamanho - 1 faça
#         chave ← lista[i]
#         j ← i - 1

#         // Move os elementos maiores que a chave
#         enquanto j ≥ 0 e lista[j] > chave faça
#             lista[j + 1] ← lista[j]
#             j ← j - 1
#         fimenquanto

#         lista[j + 1] ← chave

#         // Mostra o estado da lista após cada iteração
#         escreva("Passo ", i, ": ")
#         para k de 0 até tamanho - 1 faça
#             escreva(lista[k], " ")
#         fimpara
#         escreval()
#     fimpara
# fimfunção

# // Programa principal
# variável lista[5] ← {64, 25, 12, 22, 11}
# escreva("Lista original: ")
# para i de 0 até 4 faça
#     escreva(lista[i], " ")
# fimpara
# escreval()

# insertion_sort(lista, 5)

# escreva("Lista ordenada: ")
# para i de 0 até 4 faça
#     escreva(lista[i], " ")
# fimpara
