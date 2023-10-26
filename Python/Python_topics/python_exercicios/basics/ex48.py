# somando numeros divisiveis de um numero dado intervalo
import time

soma = 0
for i in range (1, 501):
    if i % 3 == 0 and i%2 !=0:
        time.sleep(0.1)
        print(i, end =",")
        soma += i
print(f"A soma é: {soma} ")
