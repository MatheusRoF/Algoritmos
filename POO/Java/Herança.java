package POO.Java;

public class Herança {
    // Classe base
class Animal {
    void fazerSom() {
        System.out.println("O animal faz um som.");
    }
}

// Classe filha herda de Animal
class Cachorro extends Animal {
    void abanarRabo() {
        System.out.println("O cachorro abana o rabo.");
    }
}
    
}

// Explicação: Cachorro herda o método fazerSom() 
// da classe Animal, e pode adicionar seus próprios 
// comportamentos (abanarRabo()).