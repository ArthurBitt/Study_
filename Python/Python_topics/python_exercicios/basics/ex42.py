# mesmo que o exercício 35 mas aninhando o if

# Analise de Triângulos com condicionais

a = float(input("Digite o primeiro segmentos: "))
b = float(input("Digite o segundo segmentos: "))
c = float(input("Digite o terceiro segmentos: "))

if (b < (a + c)) and (a < (b + c)) and (c < (a + b)):
    if (a != b and b != c):
        print(f"Os segmentos {a}, {b}, {c} forma um triângulo Escaleno")
    elif (a == b == c):
        print(f"Os segmentos {a}, {b}, {c} forma um triângulo Equilátero")
    else:
        print(f"Os segmentos {a}, {b}, {c} forma um triângulo Isóceles")
else:
    print(f"As medidas {a}, {b}, {c} não formam triângulos")

