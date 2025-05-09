package POO.Java;

public class Encapsulamento {
    class ContaBancaria {
        private double saldo; // Protegido: só acessado por métodos
    
        public ContaBancaria(double saldoInicial) {
            this.saldo = saldoInicial;
        }
    
        public void depositar(double valor) {
            saldo += valor;
        }
    
        public void sacar(double valor) {
            if (valor <= saldo) {
                saldo -= valor;
            } else {
                System.out.println("Saldo insuficiente.");
            }
        }
    
        public double getSaldo() {
            return saldo;
        }
    }
    
}

// Explicação: O saldo está protegido (private). 
// O acesso e modificação só podem ser feitos com 
// getSaldo(), depositar() ou sacar() — isso é encapsulamento.