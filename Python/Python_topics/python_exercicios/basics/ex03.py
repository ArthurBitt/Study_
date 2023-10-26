#operação de soma

#os inputs() transformam automaticamente o dado recebido em string, portanto,
# é preciso realizar um casting para o tipo de dados desejado

n1 = int(input("Digite uma valor: "))
n2 = int(input("Digite outro valor: "))

soma = n1+n2
print(f'{n1} + {n2} = {soma}')