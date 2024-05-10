import os
os.system("cls || clear")

produtoNome = str(input("Digite o nome do produto: "))
produtoQte = int(input("Digite a quantidade de unidades compradas: "))
produtoPreco = float(input("Digite o preço por unidade: "))

if produtoQte <= 5:
    desconto = 0.02
elif produtoQte > 5 and produtoQte <= 10:
    desconto = 0.03
else:
    desconto = 0.05


subTotal = produtoQte * produtoPreco
totalAPagar = subTotal -(subTotal * desconto)


print(f"Produto: {produtoNome}")
print(f"Quantidade: {produtoQte}")
print(f"Preco: {produtoPreco}")
print(f"Totala pagar: {totalAPagar}")
