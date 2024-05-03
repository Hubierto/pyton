import os
os.system("cls || clear")

primeiroNumero = int(input("Digite um número inteiro"))
segundoNumero = int(input("Digite outro número inteiro"))

soma = primeiroNumero + segundoNumero
subtração = primeiroNumero - segundoNumero
produto = primeiroNumero * segundoNumero 
media = soma/2
maior = max( primeiroNumero, segundoNumero)
menor = min( primeiroNumero, segundoNumero)

'''
if primeiroNumero > segundoNumero:
    maior = primeiroNumero
else: 
    maior = segundoNumero  

if primeiroNumero > segundoNumero:
    maior = primeiroNumero
else: 
    maior = segundoNumero 
'''

print(f"primeiro número: {primeiroNumero}")
print(f"segundo número: {segundoNumero}")
print(f"soma: {soma}")
print(f"subtração: {subtração}")
print(f"produto: {produto}")
print(f"maior número: {maior}")
print(f"menor número: {menor}")
print(f"media: {media}")