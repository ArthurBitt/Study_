#Menu matemático com while


n1  = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
sair = False



while (sair == False):
    option = int(input("""
    [1] Somar
    [2] Multiplicar
    [3] Maior 
    [4] Novos Números
    [5] Sair do Programa
    >>>> Sua opção: """))

    if(option == 1):
        print(f'{n1} + {n2} = {n1+n2}')
        continue
    elif(option == 2):
        print(f'{n1} * {n2} = {n1 * n2}')
        continue
    elif(option == 3):
        if (n1 > n2):
            print(f'{n1} > {n2}')
        else:
            print(f'{n2} > {n1}')
            continue
    elif(option == 4):
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        continue
    elif(option == 5):
        sair = True
        print("...Saindo")
    else:
        print("Opção inválida")
        continue
