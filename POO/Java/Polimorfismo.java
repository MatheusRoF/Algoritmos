package POO.Java;

public class Polimorfismo {
    class Animal {
        void fazerSom() {
            System.out.println("Som genérico de animal.");
        }
    }
    
    class Gato extends Animal {
        @Override
        void fazerSom() {
            System.out.println("Miau!");
        }
    }
    
    class Vaca extends Animal {
        @Override
        void fazerSom() {
            System.out.println("Muuu!");
        }
    }
    
}

// Explicação: Mesmo que você chame fazerSom() 
// a partir de uma referência Animal, o som emitido 
// depende da classe real do objeto (Gato, Vaca, etc).