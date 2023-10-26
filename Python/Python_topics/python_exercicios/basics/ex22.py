nome = input("Digite seu nome: ").strip() #.stri() tira os espaços do início e do fim
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' ')) #len() - .count(" ") tira os espaços repetidos dentro da string
print(nome.find(" ")) #retorna o índice em que se encontra o primeiro espaço