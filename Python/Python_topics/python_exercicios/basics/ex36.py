# Condicionais para pagar empréstimo
valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do seu salário: "))
pagtoQtsAnos = int(input("Digite em quantos anos deseja pagar o empréstimo: "))

mensalidaEmprestimo = valorCasa/ (pagtoQtsAnos * 12)
perctMax = salario * 0.3

if(mensalidaEmprestimo > perctMax):
    print(f"O valor das parcelas excedem 30% do seu salário. Ficariam em {pagtoQtsAnos*12}X de "
          f"{mensalidaEmprestimo:.2f} R$")
    print("Empréstimo negado")
else:
    print(
        f"O valor das ficam em {pagtoQtsAnos * 12}X de {mensalidaEmprestimo:.2f} R$")
    print("O empréstimo será depositado na sua conta")