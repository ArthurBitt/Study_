# condicionais para imprimir par ou ímpar
import colorama, time

num = int(input(colorama.Fore.GREEN +"Digite um número qualquer: "))
time.sleep(2)
if num%2 == 0 :
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")