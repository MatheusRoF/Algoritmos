package Ordenação.Java;

public class Insertion_sort {
    public static void insertionSort(int[] arr) {
        int n = arr.length;

        for (int i = 1; i < n; i++) {
            int chave = arr[i];
            int j = i - 1;

            // Move os elementos maiores que a chave uma posição à frente
            while (j >= 0 && arr[j] > chave) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = chave;

            // Mostra o estado após cada iteração
            System.out.print("Passo " + i + ": ");
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
        insertionSort(arr);
        System.out.print("Array ordenado: ");
        imprimirArray(arr);
    }
    
}
