#gerenciador de pagamentos

import time, colorama
print(colorama.Fore.GREEN)

preco = preco2 = float(input("Qual o valor do produto: "))
condicaoPgto = int(input(
"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[1] À VISTA - 10% DESCONTO
[2] À VISTA NO CARTÃO - 5% DESCONTO
[3] ATÉ 2X - SEM DESCONTO
[4] 3X OU MAIS - 20% JUROS 
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Sua opção:
"""))

if(condicaoPgto == 1):
    preco -= preco*0.1
    print(f"à vista {preco2}R$ sai por {preco}R$")
elif(condicaoPgto == 2):
    preco -= preco*0.05
    print(f"à vista no cartão {preco2}R$ sai por {preco}R$")
elif(condicaoPgto ==3):
    preco
    print(f"O valor {preco}R$ não possui descontos em 2x")
    print(f"Ficam 2x de {preco/2}R$")
elif(condicaoPgto == 4):
    preco += preco*0.2
    parcelas = int(input("Quantas parcelas: "))
    print(f"O valor {preco2}R$ sai por {preco}R$ - 20% de juros pagando em 3x ou mais")
    print(f"Ficam {parcelas}x de {preco/parcelas:.2f}R$")
else:
    print("Opção inválida")
