package Ordenação.Java;

public class Selection_sort {
    public static void selectionSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            int minIndex = i;

            // Encontra o menor elemento do restante da lista
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            // Troca o menor encontrado com o primeiro da parte não ordenada
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;

            // Mostra o estado após cada iteração
            System.out.print("Passo " + (i + 1) + ": ");
            imprimirArray(arr);
        }
    }

    public static void imprimirArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11};
        System.out.print("Array original: ");
        imprimirArray(arr);
        selectionSort(arr);
        System.out.print("Array ordenado: ");
        imprimirArray(arr);
    }
    
}
