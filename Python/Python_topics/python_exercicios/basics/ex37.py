# Convertendo decimais para outros formatos usando condicionais
import colorama, time
print(colorama.Fore.GREEN)

num = int(input("Digite um numero inteiro: "))
print("Escolha uma das alternativas para conversão: ")
escolha = int(input("""
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL

Sua opção: """))

print(colorama.Fore.LIGHTRED_EX + "Covertendo...")
time.sleep(2)

if (escolha == 3):
    num = hex(num)

elif (escolha == 2):
    num = oct(num)
else:
    num = bin(num)
print(num)