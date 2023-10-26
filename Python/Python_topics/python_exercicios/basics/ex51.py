# Calculando os 10 primeiros termos da PA
razao = int(input("Razão da PA: "))
an = int(input("Primeiro Termo: "))
decimo = (10-1)*razao
for i in range(an,decimo,razao):
    print(i, end= '➡️')