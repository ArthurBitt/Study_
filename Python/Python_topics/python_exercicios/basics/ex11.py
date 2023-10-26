#pintando area - 1litro pinta 2m²

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
area = altura*largura
litrosTinta = area/2


print(f""" 
A área que será pintada possui {area}m²
Será gasto um total de {litrosTinta}L para pinta-la
""")


