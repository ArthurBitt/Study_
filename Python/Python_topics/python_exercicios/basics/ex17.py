#hipotenusa de um triângulo

import math
catOP = float(input("Digite o valor do cateto oposto: "))
catADJ = float(input("Digite o valor do cateto adjacente: "))
Hipo = math.sqrt((catADJ**2) + (catOP**2))

print(f'Hipotenusa: {Hipo:.2f}')

