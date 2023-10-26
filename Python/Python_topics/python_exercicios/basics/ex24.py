#verificando uma string dentro da outra.

city = input("Digite o nome da cidade em que nasceu: ").strip()

# find retornará o index da primeira letra da string buscada
index = city.upper().find("SANTO")
print(index)

# O operador lógico verifica se os primeiros 5 index são SANTO retornando True or False
print(city[:5].upper() == "SANTO")