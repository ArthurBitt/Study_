#verificando se é primo

num = int(input("Digite um numero: "))

for i in range(2, round(num/2)+1):

    if (num%i != 0):
        print("é primo")
        break
    else:
        print("Não é primo")



