from enum import Enum
import os

os.system("cls ||clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:

    def __init__(self, id: str, nome: str, salario: float, setor: Setor, sexo: Sexo, idade: int) -> None:
       self.id = id
       self.nome = nome 
       self.salario = salario
       self.setor = setor
       self.sexo = sexo
       self.idade = idade

    def __str__(self) -> str:
        return(
            f"\nId: {self.id}"
            f"\nNome: {self.nome}"
            f"\nSalario: {self.salario}"
            f"\nSetor: {self.setor}"
            f"\nSexo: {self.sexo}"
            f"\nIdade: {self.idade}"
        )  
    
funcionario1 = Funcionario("092738374", "Mario", 12000, Setor.FINANCEIRO.value, Sexo.MASCULINO.value, 22)    

print(funcionario1)
       