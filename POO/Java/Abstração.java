package POO.Java;

public class Abstração {
    abstract class Veiculo {
        String modelo;
    
        Veiculo(String modelo) {
            this.modelo = modelo;
        }
    
        // Método abstrato: cada veículo vai implementar de forma diferente
        abstract void mover();
    }
    
    // Classe concreta implementa os detalhes
    class Carro extends Veiculo {
        Carro(String modelo) {
            super(modelo);
        }
    
        // Implementação do comportamento mover()
        @Override
        void mover() {
            System.out.println(modelo + " está dirigindo na estrada.");
        }
    }
    
}

// Explicação: Veiculo é uma abstração genérica. 
//  O usuário usa mover() sem saber os detalhes 
//  de como um carro se move internamente.

