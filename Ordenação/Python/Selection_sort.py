def selection_sort(arr): #Troca de o menor de lugar
    n = len(arr) #Pega o tamanho do array

    #Complexidade de tempo O(n²):O algoritmo sempre faz o mesmo 
    # número de comparações, independentemente da entrada estar ordenada ou não.
    #Complexidade de Espaço O(1): Não precisa de espaço extra

    #Percorre toda a lista
    for i in range(n):
        #Encontra o valor minimo na lista
        min_index = i

        #Procura menor elemento no restante da lista
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        #Troca o menor encontrado com o primeiro elemento
        arr[i], arr[min_index] = arr[min_index], arr[i]

        #Mostra o estado do array após cada iteração
        print(f"Passo{i + 1}:{arr}")

# Testando com seu exemplo
arr = [64, 25, 12, 22, 11]
print("Array original:", arr)
selection_sort(arr)
print("Array ordenado:", arr)

#PORTUGOL
# função selection_sort(lista[inteiro], tamanho)
#     para i de 0 até tamanho - 1 faça
#         min_indice ← i

#         // Procura o menor valor no restante da lista
#         para j de i + 1 até tamanho - 1 faça
#             se lista[j] < lista[min_indice] então
#                 min_indice ← j
#             fimse
#         fimpara

#         // Troca os valores
#         temp ← lista[i]
#         lista[i] ← lista[min_indice]
#         lista[min_indice] ← temp

#         // Mostra a lista (opcional)
#         escreva("Passo ", i + 1, ": ")
#         para k de 0 até tamanho - 1 faça
#             escreva(lista[k], " ")
#         fimpara
#         escreval()
#     fimpara
# fimfunção

# // Programa principal
# variável lista[7] ← {5, 15, 77, 21, 5, 25, 2}
# escreva("Lista original: ")
# para i de 0 até 6 faça
#     escreva(lista[i], " ")
# fimpara
# escreval()

# selection_sort(lista, 7)

# escreva("Lista ordenada: ")
# para i de 0 até 6 faça
#     escreva(lista[i], " ")
# fimpara
