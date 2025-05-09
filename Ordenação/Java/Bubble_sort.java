package Ordenação.Java;

public class Bubble_sort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean trocou;

        for (int i = 0; i < n; i++) {
            trocou = false;

            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Troca os elementos
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    trocou = true;
                }
            }

            // Mostra o estado após cada passagem
            System.out.print("Passo " + (i + 1) + ": ");
            imprimirArray(arr);

            if (!trocou) break; // Otimização: para se já estiver ordenado
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
        bubbleSort(arr);
        System.out.print("Array ordenado: ");
        imprimirArray(arr);
    }
    
}
