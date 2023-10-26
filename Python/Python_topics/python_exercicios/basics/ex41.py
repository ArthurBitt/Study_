# Usando condicionais para classificar atletas
from datetime import datetime
import colorama, time

anoAtual = datetime.now().year
anoNascimento = int(input(colorama.Fore.LIGHTMAGENTA_EX + "Digite seu ano de Nascimento: "))
idade = anoAtual - anoNascimento
time.sleep(1)
print("A idade do atleta pertence a categoria: ")
if (idade <= 9):
    print("Mirim")
elif (idade <=14):
    print("Infantil")
elif(idade <= 25):
    print("Junior")
else:
    print("Master")


