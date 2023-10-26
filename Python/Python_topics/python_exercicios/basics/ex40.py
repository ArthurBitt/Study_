nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/ 2

if (media >= 7.0):
    print("APROVADO")
elif (media < 5.0):
    print("REPROVADO")
else:
    print("RECUPERAÇÃO")