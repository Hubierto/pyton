import os
os.system
"""
Descrição das variáveis:
  - quantidade_pares: Quantidade de números pares.
  - quantidade_impares: Quantidade de números ímpares.
  - quantidade_positivos: Quantidade de números positivos.
  - quantidade_negativos: Quantidade de números negativos.
  - quantidade_de_numeros: Qquantidade de números
  - maior_numero: O maior número.
  - menor_numero: O menor número.
  - media_pares: Média dos números pares.
  - media_impares: Média dos números ímpares.
  - media_geral: Média de todos os números.
  - numeros_invertidos: Os números na ordem inversa.
"""

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0  
quantidade_negativos = 0
quantidade_de_numeros = 5
maior_numero = 0
menor_numero = 0 
soma_pares  = 0
soma_impares = 0
soma_geral = 0

#Declarando vetor
numeros = []

# Variáveis para armazenar os números
for i in range(5):
    numero = int(input(f"Digite um numero: "))
    numeros.append(numero)
    if numeros[i] % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero

    if numeros[i] > 0:
        quantidade_positivos += 1
    elif numeros[i] < 0:
        quantidade_negativos += 1
   
maior_numero = max(numeros)
menor_numero = min(numeros)

media_geral = sum(numeros)/5

media_pares = soma_pares/quantidade_pares
media_impares = soma_impares/quantidade_impares



print("\nEstatísticas dos números:")
print(f'Quantidade de pares: {quantidade_pares}')
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Quantidade de numeros inseridos: {quantidade_de_numeros}")
print(f"O maior número: {maior_numero}")
print(f"O menor número: {menor_numero}")
print(f"Média de números pares: {media_pares}")
print(f"Média de números impares: {media_impares}")
print(f"Média geral: {media_geral}")
print(f"Numero: {numeros[::-1]}")











