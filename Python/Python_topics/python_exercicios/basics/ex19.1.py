#random

import random

# Gerando um número aleatório entre 0 e 1
print(random.random())

# Gerando um número inteiro aleatório entre 1 e 10
print(random.randint(1, 10))

# Gerando um número de ponto flutuante aleatório entre 0 e 1
print(random.uniform(0, 1))

# Selecionando um elemento aleatório de uma lista
lista = [1, 2, 3, 4, 5]
print(random.choice(lista))

# Embaralhando os elementos de uma lista
random.shuffle(lista)
print(lista)

# Selecionando 3 elementos únicos aleatórios de uma lista
print(random.sample(lista, 3))
