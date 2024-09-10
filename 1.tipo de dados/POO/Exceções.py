import os

os.system("cls ||clear")

#Criando minha propria excessão
class SaldoInsuficienteError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo Protgido

    #Semelhante ao getSaldo() 
    @property
    def saldo(self):
        return self._saldo 

    def sacar(self) -> str:
        valor_saque = float(input("Digite o valor que deseja sacar: "))


        try:
            self.__verificar_sacar(valor_saque)
            self.__verificar_valor_negativo(valor_saque)
        except (SaldoInsuficienteError,ValorNegativoError) as erro:
            return f"Prezado cliente: {erro}"
        
        self._saldo -= valor_saque
        return f"Saque realizado com sucesso"


    def __verificar_sacar(self, valor) -> None: #Método privado
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo Insuficiente.")
        

    def __verificar_valor_negativo(self, valor):
        if valor < 0:
            raise valorNegativoError("valor negativo")  
         

    def depositar(self):
        valor_deposito = float(input("Digite o valor que deseja depositar"))
        try:
            
        self._saldo += valor
        return self._saldo

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instanciando classe
Conta_corrente = ContaCorrente(234, 567)
Conta_poupanca = ContaPoupanca(121, 343)

 
print(f"Número da conta: {Conta_corrente.numero_conta}")
print(f"Saldo: {Conta_corrente.saldo}")

#Sacar com saldo insuficiente

print("Conta corrente")
print(Conta_corrente.sacar())
print(f"Saldo: {Conta_corrente.saldo}")

print("Conta poupança")
print(Conta_poupanca.sacar())
print(f"Saldo: {Conta_poupanca.saldo}")


