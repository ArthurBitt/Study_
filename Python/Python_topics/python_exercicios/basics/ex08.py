#conversor de medidas km, hm, dam,dm, cm, mm
valor = int(input("Digite a medida em metros: "))

Km = valor/1000
Hm = valor/100
Dam = valor/10
Dm = valor * 10
Cm = valor * 100
Mm = valor * 1000

#.1 formata em uma casa decimal, e - adiciona a potencia de base dez na formatação.
print(f"""
{Km:.1e} km
{Hm:.1e} hm
{Dam:.1e} dam
{Dm:.1e} dm
{Cm:.1e} cm
{Mm:.1e} mm
        """)