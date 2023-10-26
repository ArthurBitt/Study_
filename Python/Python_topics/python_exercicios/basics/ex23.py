#trabalhando com leitura e fragmentação de um input numerico

numero = int(input("Digite um numero entre 0 e 9999: "))
print(f"Seu numero : {numero}")
u = numero // 1%10 #divide numero por e pega o resto da divisão por 10
d = numero // 10%10
c = numero // 100%10
m = numero // 1000%10

print(f"Unidade: {u}")
print(f"Unidade: {d}")
print(f"Unidade: {c}")
print(f"Unidade: {m}")