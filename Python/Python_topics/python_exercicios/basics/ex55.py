#maior e menor pesos

peso = 0
maior = 0
for i in range(1,6):
    menor = peso
    peso = float(input("Digite seu peso: "))
    if (peso > maior):
        maior = peso

    if (peso < menor):
        menor = peso



print(f"Maior peso registrado: {maior:.1f}KG")
print(f"Menor peso registrado> {menor:.1f}KG")