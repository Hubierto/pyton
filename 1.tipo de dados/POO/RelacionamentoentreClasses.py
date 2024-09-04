import os

os.system("cls ||clear")#Limpa o terminal

#Criando a classe endereco.
class Endereco: 
    #Criando um contrutor.
    def __init__(self, logradouro: str, numero: str) -> None:
        self.logradouro = logradouro
        self.numero = numero

    #Semelhante ao toString()
    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\n Numero: {self.numero}")
        

# Criando a classe aluno.
class Aluno:
    # Criando um construtor.
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    #Semelhante ao toString()
    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}"
            f"\n Idade: {self.idade} "
            f"\n Endereco: {self.endereco}")
               

#instanciar Classe.
#endereco1 = Endereco("Nenhum","23")
#aluno = Aluno("Marta", 22, endereco1)

aluno = Aluno("Mario",22,
               Endereco("Algum", 10))

print(aluno)
