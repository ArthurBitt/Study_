print("ASSOCIAÇÕES - HERANÇA")
# superclasse contém o que é comum as subclasses, a essas cabe a tarefa de especializar as características e
# comportamentos.

class Titulo:
    def __init__(self, nome, ano):
        self._nome = nome
        # self.__nome = nome.title()
        self._ano = ano
        # self.__ano = ano
        self.likes = 0
        # self.__likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def altera_nome(self, nome):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, like):
        if like:
            self._likes += 1


# AS SUBCLASSES NÃO HERDAM DIRETAMENTE OS ATRIBUTOS PRIVADOS DA CLASSE MÃE. É NECESSÁRIO DECLARAR OS ATRIBUTOS
# PRIVADOS QUE FORAM HERDADOS USANDO A NOTAÇÃO DE __class__.atributo OU _atributo NA CLASSE MÃE.
# LEMBRANDO, _ PROTEGE MAS NÃO PRIVA O ATRIBUTO
# AINDA QUE USAR SOMENTE _ NOS ATRIBUTOS PERMITA QUE AS SUBCLASSES HERDEM OS ATRIBUTOS ANTES PRIVADOS, AINDA HÁ O
# PROBLEMA DE MANUTENÇÃO DO CÓDIGO, É PRECISO ALTERAR TODAS REFERÊNCIAS self.atributo PARA _
# PENSANDO EM OTIMIZAR,
class Filme(Titulo):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0

class Serie(Titulo):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0


filme1 = Filme("FILME", 1990, 120)
filme1.likes = True
filme1.likes = True
filme1.likes = True
print(f"Nome: {filme1.nome} - Likes: {filme1.likes}")

serie1 = Serie("SERIE", 1990, 7)
serie1.likes = True
serie1.likes = True
print(f"Nome: {serie1.nome} - Likes: {serie1.likes}")

# PROBLEMA DE MANUTENÇÃO DO CÓDIGO, É PRECISO ALTERAR TODAS REFERÊNCIAS self.atributo PARA _
# PENSANDO EM OTIMIZAR,REDUZIMOS AS CLASSES FILHAS E UTILIZAMOS EXTENSÃO super(). PARA USAR O de __init__() da classemãe
# O super(). CHAMA QUALQUER MÉTODO DA CLASSE MÃE
print("HERANÇA - super()")

class Titulo1:
    def __init__(self, nome, ano):
        self._nome = nome
        # self.__nome = nome.title()
        self.ano = ano
        # self.__ano = ano
        self._likes = 0
        # self.__likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def altera_nome(self, nome):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, like):
        if like:
            self._likes += 1

class Filme(Titulo1):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # passado o super().__init__ com os atributos protegidos da mae
        self.duracao = duracao #criado atributo especializado da classe filha e passado o parâmtro correspondente

class Serie(Titulo1):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

filme1 = Filme("FILME", 1990, 120)
filme1.likes = True
filme1.likes = True
filme1.likes = True
print(f"Nome: {filme1.nome} - Likes: {filme1.likes}")

serie1 = Serie("SERIE", 1990, 7)
serie1.likes = True
serie1.likes = True
print(f"Nome: {serie1.nome} - Likes: {serie1.likes}")


print("QUANDO NÃO USAR HERANÇA")
#OBS. CLASSE Titulo4 ESTÁ MONTADA COM TÓPICOS DE POLIMORFISMO, NA DÚVIDA CONSULTAR DOCUMENTAÇÃO.
class Titulo4:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0


    def __str__(self):
        f"{self._nome} - {self.ano} - {self.likes}"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def altera_nome(self, nome):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, like):
        if like:
            self._likes += 1

class Filme(Titulo4):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} -{self._duracao} - {self.likes} Likes"

class Serie(Titulo4):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._temporadas}- {self.likes} Likes"

class Playlist:
    def __init__(self, nome, titulos):
        self._nome = nome
        self._titulos = titulos

    @property
    def tamanho(self):
        return len(self._titulos)

filme1 = Filme("FILME", 1990, 120)
filme1.likes = True
filme1.likes = True
filme1.likes = True
serie1 = Serie("SERIE", 1990, 7)
serie1.likes = True
serie1.likes = True

filmesSeries = [filme1, serie1]
print(type(filmesSeries))
print(type(filme1))
print(type(serie1))

playlistobj = Playlist("MinhaPlaylist", filmesSeries)

#É PASSADO PARA playlistobj UMA LISTA filmesSeries, MAS PARA ITERAR, ACESSAR A LISTA DIRETAMENTE NÃO FUNCIONA (# playlistobj.filmesSeries), É NECESSÁRIO ACESSAR O QUE ELA GUARDA, Titulos
for titulo in playlistobj._titulos:
    print(titulo) # titulo impresso é um objeto, guardado pela lista filmesSeries que foi passada como parâmetro para
    # o playlistobj

class Titulo5:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0


    def __str__(self):
        f"{self._nome} - {self.ano} - {self.likes}"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def altera_nome(self, nome):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, like):
        if like:
            self._likes += 1

class Filme(Titulo5):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} -{self._duracao} - {self.likes} Likes"

class Serie(Titulo5):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._temporadas}- {self.likes} Likes"

class Playlist(list): # FAÇO Playlist HERDAR DE LIST
    def __init__(self, nome, titulos):
        self._nome = nome
        super().__init__(titulos)# CHAMO CONSTRUTUTOR DE List E DIGO QUE O PARÂMETRO titulos É UMA LISTA




filme1 = Filme("FILME", 1990, 120)
filme1.likes = True
filme1.likes = True
filme1.likes = True
serie1 = Serie("SERIE", 1990, 7)
serie1.likes = True
serie1.likes = True

filmesSeries = [filme1, serie1]
print(type(filmesSeries))
print(type(filme1))
print(type(serie1))

playlistobj = Playlist("MinhaPlaylist", filmesSeries) #INSTANCIO UM OBJ DE Playlist E PASSO filmesSeries COMO PARÂMETRO

print("Tamanho: ", len(playlistobj))
for titulo in playlistobj:
    print(titulo)



