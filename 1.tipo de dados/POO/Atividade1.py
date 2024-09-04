import os

os.system("cls ||clear")

class Pet:

    def __init__(self, nome: str, idade: int, raca: str, porte: str, alimentacao: str) -> None:
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \n Idade: {self.idade} \n Raça: {self.raca} \n Porte: {self.porte} \n Alimentação: {self.alimentacao}"

pet = Pet("pop ", 12, "poodle", "pequeno", "ração")

print(pet.exibir_dados())