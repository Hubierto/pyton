import os
os.system("cls || clear")

pares = 0
impares = 0

for i in range(5):
    numeros = int(input(f"Digite o {i + 1} número: "))
    if numeros %2 == 0:
        pares += 1
    else:
        impares += 1    
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números impares: {impares}")