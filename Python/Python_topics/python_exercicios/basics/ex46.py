# Contagem regressiva com loop
import time, colorama
print(colorama.Fore.GREEN)
for i in range(10,-1,-1):
    time.sleep(1)
    print(i, end = ",")
