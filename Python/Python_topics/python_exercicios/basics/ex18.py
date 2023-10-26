#seno, cosseno e tangente com conversão para radianos e importando math

import math

graus = float(input("Digite quantos graus: "))

print(f"""
SENO: {math.sin(math.radians(graus)):.2f}
COSSENO: {math.cos(math.radians(graus)):.2f}
TANGENTE: {math.tan(math.radians(graus)):.2f}
            """)