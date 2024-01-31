from modelos_heranca.restaurante import Restaurante # __inicia pycache__ bytecode do código
from modelos_heranca.cardapio.bebida import Bebida
from modelos_heranca.cardapio.prato  import Prato

    
p1 = Prato("Feijoada", 30.5, "Melhor Feijoada da cidade")
b1 = Prato("Suco de Limão", 8.5, "Grande")
    
def main():
    print(p1)
    print(b1)

if __name__ == '__main__':
    main()