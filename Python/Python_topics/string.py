
#Para saber o comprimento de uma string, você pode usar a função len():
minha_string = "Olá, mundo!"
tamanho = len(minha_string)
print(tamanho)  # Saída: 12

#Você pode acessar caracteres individuais de uma string usando índices entre colchetes
minha_string = "Olá, mundo!"
primeiro_caracter = minha_string[0]
print(primeiro_caracter)  # Saída: 'O'

#Para concatenar duas strings, você pode usar o operador de adição (+) ou o método join():
string1 = "Olá"
string2 = "mundo"
concatenada1 = string1 + ", " + string2 + "!"
print(concatenada1)  # Saída: "Olá, mundo!"

concatenada2 = ", ".join([string1, string2, "!"])
print(concatenada2)  # Saída: "Olá, mundo!"

#Você pode converter uma string para maiúsculas ou minúsculas usando os métodos upper() e lower():
minha_string = "Olá, mundo!"
maiuscula = minha_string.upper()
print(maiuscula)  # Saída: "OLÁ, MUNDO!"

minuscula = minha_string.lower()
print(minuscula)  # Saída: "olá, mundo!"


#Para verificar se uma string começa ou termina com um determinado texto, você pode usar os métodos startswith() e endswith():
minha_string = "Olá, mundo!"
começa_com_ola = minha_string.startswith("Olá")
print(começa_com_ola)  # Saída: True

termina_com_ponto = minha_string.endswith(".")
print(termina_com_ponto)  # Saída: False

#Para dividir uma string em partes com base em um separador, você pode usar o método split():
minha_string = "Olá, mundo!"
partes = minha_string.split(", ")
print(partes)  # Saída: ['Olá', 'mundo!']

#Para substituir parte de uma string por outra, você pode usar o método replace():
minha_string = "Olá, mundo!"
substituida = minha_string.replace("Olá", "Oi")
print(substituida)  # Saída: "Oi, mundo!"

#Você pode verificar se uma determinada substring está presente em uma string usando o operador in:
minha_string = "Olá, mundo!"
contem_ola = "Olá" in minha_string
print(contem_ola)  # Saída: True

#Você pode formatar strings usando o método format() ou f-strings
nome = "João"
idade = 25
mensagem1 = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem1)  # Saída: "Meu nome é João e eu tenho 25 anos."

mensagem2 = f"Meu nome é {nome} e eu tenho {idade} anos."
print(mensagem2)  # Saída: "Meu nome é João e eu tenho 25 anos."

#Para remover espaços em branco do início e do final de uma string, você pode usar os métodos strip(), lstrip() e rstrip():
minha_string = "   Olá, mundo!   "
sem_espacos = minha_string.strip()
print(sem_espacos)  # Saída: "Olá, mundo!"

#Para encontrar a posição de uma substring dentro de uma string, você pode usar o método find() ou index(). Ambos retornam o índice da primeira ocorrência da substring encontrada
minha_string = "Olá, mundo!"
posicao1 = minha_string.find("mundo")
print(posicao1)  # Saída: 5

posicao2 = minha_string.index("mundo")
print(posicao2)  # Saída: 5


#Para contar quantas vezes uma substring ocorre em uma string, você pode usar o método count():
minha_string = "Olá, mundo!"
ocorrencias = minha_string.count("o")
print(ocorrencias)  # Saída: 2

#Você pode verificar se todos os caracteres em uma string são letras, dígitos, espaços em branco, etc., usando métodos como isalpha(), isdigit(), isspace()
string1 = "Olá"
string2 = "123"

print(string1.isalpha())   # Saída: True
print(string1.isdigit())   # Saída: False
print(string2.isdigit())   # Saída: True

#além do método split() mencionado anteriormente, você também pode usar o método join() para unir uma lista de strings
# em uma única string:
lista = ["Olá", "mundo", "!"]
unida = " ".join(lista)
print(unida)  # Saída: "Olá mundo !"

