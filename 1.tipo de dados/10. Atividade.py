import os
os.system("cls || clear")

valorA = int(input("Digite um número: "))
valorB = int(input("Digite outro número: "))
valorC = int(input("Digite um último valor: \n"))

if valorA + valorB < valorC:
    print("ValorA + valorB é menor que valorC")
elif valorA + valorB > valorC:
    print("valorA + valorB é maior que valorC")
else:
    print("os valores são iguais!")        