#embaralhando uma coleçãp com random

import random

aluno1 = input("Digite o nome do aluno(a): ")
aluno2 = input("Digite o nome do aluno(a): ")
aluno3 = input("Digite o nome do aluno(a): ")
aluno4 = input("Digite o nome do aluno(a): ")

lista =[aluno1,aluno2,aluno3,aluno4]

random.shuffle(lista)

print(lista)