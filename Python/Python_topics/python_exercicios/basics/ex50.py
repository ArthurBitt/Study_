#
soma = 0
for i in range(1,3):
    num = int(input("Digite um numero: "))
    if (num % 2 == 0):
        soma += num
    else:
        break

print(f"A soma dos pares é: {soma}")
