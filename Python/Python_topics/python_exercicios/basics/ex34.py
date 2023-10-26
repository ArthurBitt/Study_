# aplicando condicionais para aumentar salário
salario = float(input("Digite seu salário: "))

perct1 = 0.1
perct2 = 0.15

if (salario <= 1250.00):
    salario += (salario * perct2)

else:
    salario += (salario * perct1)

print(f"Seu novo salário será de {salario:.2f} R$")
