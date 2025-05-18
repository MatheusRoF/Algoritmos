package Busca.Java;
public class B_Binária {

    /**
     * Implementação do algoritmo de busca binária que retorna tanto o índice quanto o valor encontrado.
     *
     * @param lista Um array ORDENADO onde a busca será realizada
     * @param item O valor que está sendo buscado no array
     * @return Um array de Object contendo {índice, valor} se encontrado, ou {null, null} se não encontrado
     */
    public static Object[] buscaBinaria(int[] lista, int item) {
        int baixo = 0;
        int alto = lista.length - 1;

        while (baixo <= alto) {
            int meio = (baixo + alto) / 2;
            int chute = lista[meio];

            if (chute == item) {
                return new Object[]{meio, chute};  // Retorna índice e valor
            }

            if (chute > item) {
                alto = meio - 1;
            } else {
                baixo = meio + 1;
            }
        }

        return new Object[]{null, null};  // Retorna null para ambos se não encontrado
    }

    // Versão genérica para outros tipos comparáveis (como String)
    public static <T extends Comparable<T>> Object[] buscaBinaria(T[] lista, T item) {
        int baixo = 0;
        int alto = lista.length - 1;

        while (baixo <= alto) {
            int meio = (baixo + alto) / 2;
            T chute = lista[meio];

            int comparacao = chute.compareTo(item);
            
            if (comparacao == 0) {
                return new Object[]{meio, chute};
            }

            if (comparacao > 0) {
                alto = meio - 1;
            } else {
                baixo = meio + 1;
            }
        }

        return new Object[]{null, null};
    }

    public static void main(String[] args) {
        // Exemplo com números inteiros
        int[] numeros = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
        
        Object[] resultado = buscaBinaria(numeros, 10);
        System.out.println("Para o valor 10: Índice = " + resultado[0] + ", Valor = " + resultado[1]);
        
        resultado = buscaBinaria(numeros, 16);
        System.out.println("Para o valor 16: Índice = " + resultado[0] + ", Valor = " + resultado[1]);
        
        resultado = buscaBinaria(numeros, 5);
        System.out.println("Para o valor 5: Índice = " + resultado[0] + ", Valor = " + resultado[1]);

        // Exemplo com Strings
        String[] nomes = {"Alice", "Bruno", "Clara", "Daniel", "Eduarda", "Felipe"};
        
        resultado = buscaBinaria(nomes, "Clara");
        System.out.println("Para o nome 'Clara': Índice = " + resultado[0] + ", Valor = " + resultado[1]);
        
        resultado = buscaBinaria(nomes, "Zeca");
        System.out.println("Para o nome 'Zeca': Índice = " + resultado[0] + ", Valor = " + resultado[1]);
    }
}