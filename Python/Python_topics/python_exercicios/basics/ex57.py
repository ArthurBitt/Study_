#Usando o loop while

# sexo = input("Digite seu sexo [M/F]|: ")
#
# while sexo != "M" and sexo != "F":
#     sexo = input("Digite seu sexo [M/F]: ")

sexo = input("Digite seu sexo [M/F]: ")
while sexo not in "MmFf":
    sexo = input("Digite seu sexo [M/F]: ")