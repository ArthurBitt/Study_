# Leitor de velocidade  - utilizando if, elif e else

import colorama, time
vel = int(input(colorama.Fore.RED + "Digite a velocidade do carro: "))
multa = 7.00 * (vel - 80)

time.sleep(2)

if (vel > 80):
    print(f"Você será multado {multa:.2f}R$")

elif (vel < 40):
    print("Velocidade abaixo do permitido na via. Mínima é de 40")

else:
    ("Velocidade dentro do limite. Boa viagem!")