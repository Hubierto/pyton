from abc import ABC, abstractmethod
import os

os.system("cls || clear")


class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return(
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCep: {self.cep}"
            f"\nCidade: {self.cidade}"

        ) 
    
class Funcionario(ABC):

    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco ) -> None:
       self.nome = nome 
       self.telefone = telefone
       self.email = email
       self.endereco = endereco 

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}" 
            f"\nE-mail: {self.email}" 
            f"\nEndereço: {self.endereco}" 
        )
    
    #@abstractmethod
    #def salarioFinal(ABC) -> float:
    #    pass

class Engenheiro:

    #BONIFICACAO = 1.5

    def __init__(self, crea: float) -> None:
        self.crea = crea

    #def salarioFinal(self) -> float:
    #    resultado = self.salario * self.BONIFICACAO
    #    return resultado

    def __str__(self) -> float:
        return(
            f"\nCrea: {self.crea}"
        )
    
class Medico:

    #BONIFICACAO = 2.0

    def __init__(self, crm: float) -> None:
        self.crm = crm

    #def salarioFinal(self) -> float:
    #    resultado = self.salario * self.BONIFICACAO
    #    return resultado

    def __str__(self) -> float:
        return(
            f"\nCrm: {self.crm}"
        )    

funcionario = Funcionario("JJ","71966554433", "JJ@gmail.com", Endereco("...", "07", "E", "345123456", "Salvador"))

engenheiro = Engenheiro(1000)

medico = Medico(2000)

print(funcionario)
print(engenheiro)
print(medico)

 



   
   
