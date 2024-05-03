import os
os.system("cls || clear")

print("Solicitando dados")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3



os.system("cls||clear")
print("=== Exibindo o resultado ===")
print(f"Seu nome: {nome}")
print(f"Sua idade: {idade}")
print(f"Sua 1ª nota: {nota1}")
print(f"Sua 2ª nota: {nota2}")
print(f"Sua 3ª nota: {nota3}")
print(f"Sua media: {media}")

if media >= 7:
    print("Aprovado")
else: 
    print("reprovado")

         
