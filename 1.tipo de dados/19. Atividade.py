import os
os.system("cls || clear")

soma = 0

for i in range(4):
    notas = float(input(f"Digite o valor da {i + 1}ª nota: "))
    soma += notas

media = soma/4

print(f"Sua média: {media}")