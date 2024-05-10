import os

os.system("cls |clear")

#inicializando variável
numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")