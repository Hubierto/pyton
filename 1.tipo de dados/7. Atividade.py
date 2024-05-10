import os
os.system("cls || clear")

primeiroNumero = int(input("Digite seu primeiro número: "))
segundoNumero = int(input("Digite outro número: "))

soma = primeiroNumero + segundoNumero
subtração = primeiroNumero - segundoNumero
produto = primeiroNumero * segundoNumero 
media = soma/2
maior = max( primeiroNumero, segundoNumero)
menor = min( primeiroNumero, segundoNumero)

print("Exibindo dados")
print(f"Primeiro número: {primeiroNumero}")
print(f"")