from modelos_polimorfismo.cardapio.itemcardapio import itemCardapio
class Bebida(itemCardapio):
    def __init__(self, _nome, _preco, tamanho):
        super().__init__(_nome,_preco)
        self._tamanho = tamanho

    def __str__(self):
            return self._nome
    
    # método abstrato reescrito na filha
    def aplicar_descont(self):
         self._preco -= self._preco *0.5
