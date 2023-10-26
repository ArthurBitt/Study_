#JOKENPO
import random, time, colorama
choiceRamdon = random.randint(1,3)
escolha = int(input("""

[1] PEDRA
[2] PAPEL
[3] TESOURA

SUA ESCOLHA: """))
time.sleep(1)

if (choiceRamdon == 1):
    print("PC ESCOLHE: PEDRA")
if (choiceRamdon == 2):
    print("PC ESCOLHE: PAPEL")
if (choiceRamdon == 3):
    print("PC ESCOLHE: TESOURA")


if (choiceRamdon == escolha):
    print("DRAW")

elif (escolha!=choiceRamdon):
    if (choiceRamdon == 1 and escolha == 2):
        print("WIN - Papel embrulha pedra")

    elif (choiceRamdon == 3 and escolha == 1):
        print("WIN - Pedra quebra tesoura")

    elif(choiceRamdon == 2 and escolha == 3):
        print("WIN -  Tesoura Corta Papel")

    else:
        print("Lose")