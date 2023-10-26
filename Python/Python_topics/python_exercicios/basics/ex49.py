# tabuada com loop
import colorama, time
print(colorama.Fore.GREEN)
tabuada = int(input("Digite o número para ver a tabuada: "))
for i in range(0,11):
    print(colorama.Fore.RED + f"""{tabuada} x""" + colorama.Fore.BLUE + f""" {i} = {tabuada * i}""")