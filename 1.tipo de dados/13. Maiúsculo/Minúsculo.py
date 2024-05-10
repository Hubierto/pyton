import os
os.system("cls || clear")

nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo(M ou F): ")
estadoCivil = input("Digite o seu estado civil(CASADA ou SOLTEIRA): ")

#sexo = sexo.upper()
#estadoCivil = estadoCivil.upper()

#if sexo == "F" and estadoCivil == "CASADA":

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == "f" and estadoCivil == "casada":
    anos = input("Digite há quantos anos voçê está casada: ")

print(f"Seu nome: {nome}")  
print(f"Seu sexo: {sexo}")  
print(f"Seu estado civil: {estadoCivil}")  
  
if sexo == "f" and estadoCivil == "casada":
    print(f"Anos de casada: {anos}")
  


