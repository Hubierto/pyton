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

os.system("cls || clear")
print("Exibindo dados\n")
print(f"Primeiro número: {primeiroNumero}")
print(f"Segundo número: {segundoNumero}")
print(f"Soma: {soma}")
print(f"Subtração: {subtração}")
print(f"produto: {produto}")
print(f"Média: {media}")
print(f"Maior número: {maior}")
print(f"menor número: {menor}")