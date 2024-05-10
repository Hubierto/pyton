import os
os.system("cls || clear")

soma = 0

for i in range(3):
    notas = float(input(f"Digite a {i+1} nota: "))
    soma += notas

media = soma/3

print(f"Sua média: {media}")

if media >= 7:
    print(f"Aprovado!")
elif media < 7 and media > 4:
    print(f"Recuperação!")
else:
    print(f"Reprovado!")        