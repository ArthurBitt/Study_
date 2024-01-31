from modelos_heranca.avaliacao import Avaliacao
class Restaurante:
    # encapsulando os atributos, alterações diretas objeto.atributo ficam indisponíveis
    restaurantes = list()


    def __init__(self, _nome, _especialidade):
        self._nome = _nome.title()
        self._especialidade = _especialidade.title()
        self._ativo = False
        Restaurante.restaurantes.append(self) 
        self._avaliacao = list() #*composicao  


    def __str__(self):
        return f'''
        Restaurante: {self._nome}
        Especialidade: {self._especialidade} 
        Ativo: {self._ativo}
        media: {self.media_avaliacoes}'''
        
    @classmethod # boa prática anotar métodos utilizados pela classe
    def listar_restaurantes(cls): # pedem parâmetro cls -//self
        lista = cls.restaurantes # cls.restaurantes // self.nome
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')

        for restaurante in lista:
            # ljust(int) aplica espaçamento   
            print(f'{restaurante._nome.ljust(25)} | {restaurante._especialidade.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')    

    @property
    def ativo(self):
        return "Ativo" if self._ativo == True else "Desativado"

    def ativar(self):
        self._ativo = not self._ativo # not inverte o False
        return self._ativo
     
    def receber_avaliacao(self,cliente, nota):
        if 0 <= nota <=5:
            print("Por favor, avalia de 1 a 5 estrelas")
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao) # lista _avaliacao esta apendando um objeto avaliacao// quant clientes = quant notas
        else:
            print("Nota inválida")          
            
                
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem Avaliações'
        else:
            soma_notas = sum(avaliacao.nota for avaliacao in self._avaliacao) # itera a lista _avaliacao - separa nota de cliente
            quant_notas = len(self._avaliacao)
            media = soma_notas/quant_notas
            return round(media, 1)