# alistamento 18 anos com condicionais e datime
from datetime import datetime

anoNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = datetime.now().year

idade = anoAtual - anoNascimento

if (idade == 18):
    print(f"Seu ano de alistamento é {anoAtual}")

elif (idade < 18 ):
    print(f"Seu ano de alistamento é {anoAtual + (abs(idade - 18) )}")

else:
    print(f"Seu alistamento já passou, foi em {(anoAtual - (idade - 18))}")



