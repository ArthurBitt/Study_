#usando condicionais, Colorama e Sleep para imprimir um rando.choice()

import random, time
from colorama import init, Fore

init()

print(Fore.BLUE + "-=-"*20) # usando init() e Fore.COR dqui para baixo fica tudo na cor especificada
print("Vou pensar em um número entre 0 e 5")
print("-=-"*20)
lista = list(range(0,5))
result = random.choice(lista)

x = int(input("Em que número pensei: "))
print(Fore.GREEN + "Loading...")
time.sleep(3)#segundos
if (x == result):
    print(f"Correto, o numero era {result}")
else:
    print(f"errou, o numero correto era {result}")
