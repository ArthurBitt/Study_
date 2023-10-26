#Procurando uma string dentro de outra

nome = str(input("Digite seu nome: ")).upper().strip()

# Operador in
print("SILVA" in nome)


#usando fatiamento
print(f'Tem Silva no seu nome: {nome[:6] == "SILVA"}')