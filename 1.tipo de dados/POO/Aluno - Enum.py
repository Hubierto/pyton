from enum import Enum
import os

os.system("cls ||clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Aluno: 
    def __init__(self, nome: str, idade: int, sexo = Sexo) -> None:
        self.nome = nome    
        self.idade = idade    
        self.sexo = sexo 

    def __str__(self) -> str:
        return(f"\nNome: {self.nome}"       
               f"\nIdade: {self.idade}"       
               f"\nSexo: {self.sexo.value}")       

#Instanciando classe
aluno1 = Aluno("Marta",22, Sexo.FEMININO)

print(aluno1)