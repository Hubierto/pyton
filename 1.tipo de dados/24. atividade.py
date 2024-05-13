import os

os.system("cls || clear")

soma = 0
nota = float

for i in range(3):
    while True:
        nota = float(input(f"Digite sua {i + 1}ª nota: "))
        if nota < 0 or nota > 10:
            print("Nota invalida")
        else:
            soma += nota
            media = soma / 3
            break

print(f"Sua media: {media}")                