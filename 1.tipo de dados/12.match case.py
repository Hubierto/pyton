import os
os.system("cls || clear")

resultado = 0
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
opcao = input("Digite o símbolo da operação matemática: ")

match(opcao):
    case "+":
        resultado = a + b  
    case "-":
        resultado = a - b
    case "*":
        resultado = a * b
    case "/":
        resultado = a / b
    case _: 
        print("Opção inválida")           

print(f"Resultado = {resultado}")

