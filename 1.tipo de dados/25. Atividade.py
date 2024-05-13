import os
os.system("cls||clear")

soma = 0
quantidadeNotas = 0

while True:
    nota = float(input("Digite uma nota: "))

    resposta = input("Deseja digitar mais uma nota? S ou N: ")
    resposta = resposta.upper()

    soma += nota
    quantidadeNotas += 1

    if resposta == "N":
        break

media = soma/quantidadeNotas

print(f"Media: {media}")
    
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperaçãp")
else:
    print("Reprovado")        

