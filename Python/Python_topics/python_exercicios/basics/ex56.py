# iterando, operando e verificando
import colorama

idade = 0
soma = 0
totMComMenosDe20 = 0
nomeHomemMaisVelho = ""
for i in range(1,3):
    maior = idade
    print(colorama.Fore.GREEN + f"--------------{i}° PESSOA----------")
    nome = input("Digite seu nome: ").title()
    idade = int(input("Digite sua idade: "))
    sexo = input("[M/F]").upper()
    soma+= idade

    if (sexo == "M"):
        if (idade > maior):
            nomeHomemMaisVelho = nome
            maior = idade

    else:
        if(idade < 20):
            totMComMenosDe20 +=1



media = soma/4
print(f"Média idade do grupo: {media}")
print(f"NOME: {nomeHomemMaisVelho} IDADE: {maior}" )
print(f"TOTAL F < 20 {totMComMenosDe20}")