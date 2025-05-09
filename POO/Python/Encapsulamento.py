class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def get_saldo(self):
        return self.__saldo

# Explicação: __saldo é um atributo privado 
#   (Python usa dois underlines). O acesso é feito 
#   apenas por métodos depositar, sacar e get_saldo.