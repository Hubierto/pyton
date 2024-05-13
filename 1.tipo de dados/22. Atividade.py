import os
os.system("cls||clear")

primeiraNota: float = -1
segundaNota: float = -1

while (primeiraNota < 0 or primeiraNota > 10) :
    primeiraNota = float(input("Digite a primeira nota: "))
    
while (segundaNota < 0 or segundaNota > 10) :
    segundaNota = float(input("Digite a segunda nota: "))
        
media = (primeiraNota + segundaNota) / 2   

print(f"Média: {media} ")


