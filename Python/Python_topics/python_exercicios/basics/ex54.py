# Iterando inputs
import datetime
anoAtual = datetime.datetime.now().year
menor = 0
maior = 0
for i in range(1,8):
    ano = int(input("Digite seu ano de nascimento: "))
    idade = anoAtual - ano
    if (idade > 18):
        maior+=1
    else:
        menor+=1

print(f"Maiores de idade {maior}")
print(f"Menores de idade {menor}")