# Analise de Triângulos com condicionais

a = float(input("Digite o primeiro segmentos: "))
b = float(input("Digite o segundo segmentos: "))
c = float(input("Digite o terceiro segmentos: "))

if (b < (a + c)) and (a < (b + c)) and (c < (a + b)):
   print("é um triângulo")
else:
   print("Não é triângulo")