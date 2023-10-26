#aluguel de carros

dias = int(input("Quantos dias será alugado o veículo: "))
km = int(input("Quantos Km serão rodados: "))

total = (km * 0.15) + 60 * 8

print(f'O total a ser pago pelo aluguel é de {total}R$')