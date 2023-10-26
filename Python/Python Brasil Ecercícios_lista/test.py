# try:
#     a = float(input(":"))
#     b = float(input(":"))
#     r = a/b
    
# except Exception as error:
#     print(f"Houston, we got problem!, we found an error {error.__class__}")
# except Exception as error:
#     print(f"Houston, we got problem!, we found an error {error.__cause__}")


# except (ValueError):
#     print(f"Houston, we got problem!, we found an value error")

# except (TypeError):
#     print(f"Houston, we got problem!, we found an typer error ")

# except (ZeroDivisionError):
#     print(f"Houston, we got problem!, we found an zero division error ")

# except (KeyboardInterrupt):
#     print(f"Houston, we got problem!, we found an keybord interrupt error ")

# else:
#     print(r)

# finally:
#     print("Try again!")


# def leiaint():
#     try:
#         num = int(input("Digite um inteiro: "))
#     except (ValueError,TypeError)  as error :
#             print(error.__class__)
#             print("Digite um inteiro válido")
    
#     except(KeyboardInterrupt):
#          print("Entrada de dados interronpida")

#     else:
#         print(f"O número fornecido foi {num}") 

# def leiafloat():
#     try:
#         num = float(input("Digite um inteiro: "))
        
#     except (ValueError,TypeError)  as error :
#             print(error.__class__)
#             print("Digite um Real válido")
#             continue
#     except(KeyboardInterrupt):
#          print("Entrada de dados interronpida")

#     else:
#         print(f"O número fornecido foi {num}") 

# # leiaint()
# leiafloat()

import urllib
import urllib.request

site = urllib.request.urlopen("https://www.google.com.br/?hl=pt-BR")


try:
    site
except (urllib.error.URLError):
    print("ERRO")
else:
    print("OK")
    print(site.read())