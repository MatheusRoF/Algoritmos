package Estrutura_Dados.Java;

import java.util.LinkedList;

public class Pilha {
    private LinkedList<Object> items;

    // Construtor: inicializa a pilha como uma lista vazia
    public Pilha() {
        items = new LinkedList<>();
    }

    // Verifica se a pilha está vazia
    public boolean isEmpty() {
        return items.isEmpty();
    }

    // Adiciona um item no topo da pilha
    public void push(Object item) {
        items.addLast(item);
    }

    // Remove e retorna o item do topo
    public Object pop() {
        if (!isEmpty()) {
            return items.removeLast();
        }
        return null;
    }

    // Retorna o item do topo sem remover
    public Object peek() {
        if (!isEmpty()) {
            return items.getLast();
        }
        return null;
    }

    // Retorna o tamanho da pilha
    public int size() {
        return items.size();
    }

    // Exibe o conteúdo da pilha
    public void printStack() {
        System.out.println(items);
    }
    
}
