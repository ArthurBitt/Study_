# Lendo um ano bissexto

# minha lógica
x = range(0, 9999, 4)

anoConsultado = int(input("Digite o ano que gostaria de consultar se é bissexto: "))

if (anoConsultado in x ):
        print(f" O ano {anoConsultado} é bissexto")

else:
    print(f"o Ano {anoConsultado} não é bissexto")


    # aparentemente existem mais regras do que a penas ser de 4 em 4 anos

anoConsultado = int(input("Digite o ano que gostaria de consultar se é bissexto: "))

if (anoConsultado % 4 == 0 and (anoConsultado % 100 != 0 or anoConsultado % 400 == 0)):
    print(f"O ano {anoConsultado} é bissexto")
else:
    print(f"O ano {anoConsultado} não é bissexto")

