package Estrutura_Dados.Java;

import java.util.LinkedList;

public class Fila {
    private LinkedList<Object> items;

    // Construtor: inicializa a fila como uma lista encadeada vazia
    public Fila() {
        items = new LinkedList<>();
    }

    // Verifica se a fila está vazia
    public boolean isEmpty() {
        return items.isEmpty();
    }

    // Insere um item no final da fila
    public void enqueue(Object item) {
        items.addLast(item);  // adiciona no final da lista
    }

    // Remove o primeiro item da fila (o mais antigo)
    public Object dequeue() {
        if (!isEmpty()) {
            return items.removeFirst();  // remove e retorna o primeiro da fila
        }
        return null;  // retorna null se a fila estiver vazia
    }

    // Retorna o tamanho da fila
    public int size() {
        return items.size();
    }

    // Exibe a fila (opcional)
    public void printQueue() {
        System.out.println(items);
    }
    
}
