import os
os.system("cls || clear")

print("Solicitando dados para o usuário")
login = input("Digie o login: ")
senha = input("Digite sua senha: ")


if login == "Marta" and senha == "123":
    print("Bem vindo")
else:
    print("Acesso negado")
