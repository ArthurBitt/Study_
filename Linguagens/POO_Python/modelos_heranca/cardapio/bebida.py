from modelos_heranca.cardapio.itemcardapio import itemCardapio
class Bebida(itemCardapio):
    def __init__(self, _nome, _preco, tamanho):
        super().__init__(_nome,_preco)
        self._tamanho = tamanho

    def __str__(self):
            return self._nome