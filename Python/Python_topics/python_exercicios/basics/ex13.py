#reajuste de salário

salario = float(input("Digite o valor do sálario que receberá o reajuste: "))
reajuste = salario + (salario*0.15)
novoSalario = reajuste

print(f'O valor do salário era de {salario}R$ '
      f'Após o reajuste, o valor será {novoSalario:.2f}R$')