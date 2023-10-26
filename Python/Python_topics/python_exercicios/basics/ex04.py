#Verificações de uma variável - função is()

variavel = input("Digete algo: ")

#verifica o tipo primitivo
print(f"tipo: {type(variavel)} ")

#verifica se tem espaços
print(f"tem espaços: {variavel.isspace()} ")

#verifica se é numerico - obs. uma str pode ser numérica, mas seu tipo ainda seria str
print(f"é um número: {variavel.isnumeric()} ")

#verifica se é letra
print(f"é uma letra: {variavel.isalpha()}" )

##verifica se é alfanumérico
print(f"é alfanum: {variavel.isalnum()}")

#verifica maiúsculas
print(f"esta em maiúsculo: {variavel.isupper()}")

#verifica minúsculas
print(f"esta em minúsculo: {variavel.islower()}")

#verifica se a primeira letara é maiúscula
print(f"a primeira letra é maiúscula {variavel.istitle()} ")