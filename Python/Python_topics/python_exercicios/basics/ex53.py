#verificando palíndromos

import colorama,time

print(colorama.Fore.GREEN)
palavra = input("Digite sua palvra: ").strip().upper()

novaPalavra = palavra[::-1]

if (novaPalavra == palavra):
    print("PALÍNDROMO")
else:
    print("NÃO É PALÍNDROMO")


# usando o for é preciso fazer com que a palavra não tenha espaços entre as letras
print(colorama.Fore.GREEN)
palavra = input("Digite sua palvra: ").strip().upper()
palavra.split()
palavra =''.join(palavra)
novaPalavra = ''
for i in range(len(palavra)-1, -1, -1):
    novaPalavra += palavra[i]

if(novaPalavra == palavra):
    print("Palíndromo")
else:
    print("Não é palíndromo")