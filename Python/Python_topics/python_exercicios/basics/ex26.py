# quantas vezes uma letra aparece, a primeira posição e a última

stringFrase = str(input("Digite uma frase: ")).upper()

quantidade = stringFrase.count("A")
index = stringFrase.find("A") +1  # find() pega a primeira posição que aparece. o +1 inicia o index em 1
indexr = stringFrase.rfind("A") +1 # rfind() pega a última posição que aparece

print(quantidade)
print(index)
print(indexr)