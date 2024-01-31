from abc import ABC, abstractmethod

class itemCardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco


    def __str__(self):
        return self._nome
    
    # Aplicação desse método passa ser obrigatória nas classes filhas - polimorfismo no modo como cada classe aplica o desconto
    @abstractmethod
    def aplicar_descont(self):
        pass


