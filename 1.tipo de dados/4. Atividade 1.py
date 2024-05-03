import os
os.system("cls || clear")

print("Solicitando dados")
nome = input("Digite seu nome: ")
idade = int(input("digite sua idade: ")) 
nota1 = float(input("Digite sua 1ª nota: "))
nota2 = float(input("Digite sua 2ª nota: "))
 

media = (nota1 + nota2)/2

os.system("cls||clear")
print("=== Exibindo o resultado ===")
print(f"Seu nome: {nome}")
print(f"Sua idade: {idade}")
print(f"Sua 1ª nota: {nota1}")
print(f"Sua 2ª nota: {nota2}")
print(f"Sua media: {media}")


 