# IMC
import colorama, time

print(colorama.Fore.MAGENTA)
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso/(altura * altura)

print(f"Dado seu imc de {round(imc)} você possui:  ")
time.sleep(1)
if(imc < 18.5):
    print("peso abaixo do ideal")
elif(18.5 <= imc < 25):
    print("Peso ideal")
elif(25 <= imc < 30):
    print("sobrepeso")
elif(30 <= imc < 40):
    print("Obesidade")
else:
    print("Obesidade Mórbida")