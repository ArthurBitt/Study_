#usando condicionais, Colorama e Sleep para imprimir um rando.choice()

import random, time
from colorama import init, Fore

init()

print(Fore.BLUE + "-=-"*20) # usando init() e Fore.COR dqui para baixo fica tudo na cor especificada
print("Vou pensar em um número entre 0 e 10")
print("-=-"*20)
lista = list(range(0,5))
result = random.choice(lista)

x = int(input("Em que número pensei: "))

while (x != result):

    print("Número incorreto, tente outra vez!")
    x = int(input("Em que número pensei: "))
    print(Fore.GREEN + "Loading...")
    time.sleep(1)  # segundos

    if (x == result):
        print("Acertou!")
        break
