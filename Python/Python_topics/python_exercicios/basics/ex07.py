# Média Aritmética
media = 0
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = ((nota1 + nota2)/2)

print("Media: {}".format(media))

#media arredondada com func round()
print("Media arredondada: {}".format(round(media)))

#media formatada
print(f"Media formatada: {media:.1f}")