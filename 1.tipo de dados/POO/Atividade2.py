import os

os.system("cls||clear")

class Conta_bancaria:

    def __init__(self, banco: str, agencia: str, numero_da_conta: int, tipo_da_conta: str, saldo_atual, limite_disponivel) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.tipo_da_conta = tipo_da_conta
        self.saldo_atual = saldo_atual
        self.limite_disponivel = limite_disponivel

    def __str__(self) -> str:
        return (
            f"\nBanco: {self.banco}"
            f"\nAgencia: {self.agencia}"
            f"\nNúmero da conta: {self.numero_da_conta}"
            f"\nTipo da conta: {self.tipo_da_conta}"
            f"\nSaldo atual: {self.saldo_atual}"
            f"\nLimite Disponível: {self.limite_disponivel}") 
    
class Funcionario:

    def __init__(self, codigo_do_funcionario: str, nome: str, endereco: str, telefone: str, email: str, contaDoBanco: Conta_bancaria) -> None:
        self.codigo_do_funcionario = codigo_do_funcionario
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone 
        self.email = email
        self.contaDoBanco = contaDoBanco

    def __str__(self) -> str:
        return (
            f"\nCódigo do funcionário: {self.codigo_do_funcionario}"
            f"\nNome: {self.nome}"
            f"\nEndereço: {self.endereco}" 
            f"\nTelefone: {self.telefone}" 
            f"\nE-mail: {self.email}" 
            f"\nConta do banco: {self.contaDoBanco}"
             )

funcionario = Funcionario("010203", "Rogério", "rua Almeida", "719-96754433","kkk@gmail.com",
                          Conta_bancaria("Caixa", "01", 2, "corrente", "1000","5000" ))            

print(funcionario)    
        

