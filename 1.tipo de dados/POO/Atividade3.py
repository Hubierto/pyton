from abc import ABC, abstractmethod
import os

os.system("cls || clear")

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

        



   
   
