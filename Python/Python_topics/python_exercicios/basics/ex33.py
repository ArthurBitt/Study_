#Exgerando nos if's

num = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

menor = num
maior = num3

if (num2 < num and num2 < num3):
    menor = num2

if (num3 < num and num3 < num2):
    menor = num3

if (num > num3 and num > num2):
    maior = num

if (num2 > num3 and num2 > num):
    maior = num2


# dentro dos blocos os if's não foram ativados. ???
print("Menor: ", menor)
print("Maior: ", maior)