import os

os.system("cls ||clear")#Limpa o terminal

# Criando aclasse aluno.
class Aluno:
    # Criando um construtor.
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \n Idade: {self.idade}"
               

#instanciar Classe.
aluno = Aluno("Marta", 22)

# print(aluno.nome)
# print(aluno.idade)

print(aluno.exibir_dados())
