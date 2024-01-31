from modelos_heranca.cardapio.itemcardapio import itemCardapio
class Prato(itemCardapio):
    def __init__(self, _nome, _preco, descricao):
        super().__init__(_nome, _preco)
        self._descricao = descricao

    def __str__(self):
            return self._nome