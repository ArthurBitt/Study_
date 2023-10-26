# # 01 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
# print("Alo mundo")
# # 02 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# num = float(input("Digite um número: "))
# print(f'número informado foi {num}')
# # # 03 Faça um Programa que peça dois números e imprima a soma.
# def soma():
#     num = (input("Digite dois números. Separe-os por vírgula: "))
#     num =tuple(num.split(","))

#     print(float(num[0]) + float(num[1]))
# soma()


#  04 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media(lista = list()):
    total_notas = int(input("Quantas notas no total: "))
    
    for i in range((total_notas)):
        nota = float(input(f"Digite a {i+1}° nota: "))
        lista.append(nota)
    soma = sum(lista)
    media = (soma)/(total_notas)

    return f'media: {round(media, 1)}'

print(media())