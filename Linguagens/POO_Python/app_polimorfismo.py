from modelos_polimorfismo.restaurante import Restaurante # __inicia pycache__ bytecode do código
from modelos_polimorfismo.cardapio.bebida import Bebida
from modelos_polimorfismo.cardapio.prato  import Prato


# restaurante recebe nome, especialização, status de atividade, nota e é adicionado em uma lista de restaurantes da classe
restaurante = Restaurante("Padaria","Panificadora")    
restaurante.receber_avaliacao("Arthur", 4)
restaurante.listar_restaurantes()

# Pratos e Bebidas possuem nome, preco - descricao e tamnho
p1 = Prato("Feijoada", 30.5, "Melhor Feijoada da cidade")
b1 = Bebida("Suco de Limão", 8.5, "Grande")

# restaurantes adicionam ao seu cardapio bebidas e pratos
restaurante.adicionar_no_cardapio(b1)
restaurante.adicionar_no_cardapio(p1)


    
def main():
    restaurante.exibir_cardapio

if __name__ == '__main__':
    main()