#O POLIMORFISMO É ALCANÇADO ATRAVÉS DA HERANÇA. QUANDO UMA CLASSE QUE HERDA OU QUE É HERDADA REPRESENTA A MESMA
# INSTÂNCIA O POLIMORFISMO FOI ALCANÇADO
print("POLIMORFISMO")
class Titulo2:
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

class Filme(Titulo2):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # passado o super().__init__ com os atributos protegidos da mae
        self.duracao = duracao #criado atributo especializado da classe filha e passado o parâmtro correspondente

class Serie(Titulo2):
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

filmesSeries = [filme1, serie1]

#AQUI ACONTECE O POLIMORFISMO, NÃO IMPORTA A CLASSE QUE ESTÁ SENDO UTILIZADA, DENTRO DO FOR É VERIFICADO E IMPRESSO
# TEMPORADAS OU DURACAO MIN
for titulo in filmesSeries:
    detalhes = titulo.duracao if hasattr(titulo, "duracao") else titulo.temporadas #IF TERNÁRIO - ÚNICA LINHA

for titulo in filmesSeries:
    if hasattr(titulo, "duracao"):
        detalhes = titulo.duracao
    else:
        detalhes = titulo.temporadas
    # Faça algo com a variável detalhes aqui

print("POLIMORFISMO - SOBREESCRITA DE MÉTODOS")
#A SOBREESCRITA AUXÍLIA O POLIMORFISMO VERICAR MENOS, ISTO É, DIMINUI A COMPLEXIDADE DO CÓDIGO, NA MEDIDA EM QUEPARA
# IMPRIMNIR DURACAO EM MINUTOS PARA FILMES E TEMPORADAS PARA SERIES, BASTA FAZER UM MÉTODO QUE IMPRIME A FICHA
# TÉCNICA DO TÍTULO, COPIA-LO E ESCREVE-LO NAS CLASSES FILHAS, MAS ADICIONANDO AS ESPECIALIZAÇÕES.


class Titulo3:
    def __init__(self, nome, ano):
        self._nome = nome
        # self.__nome = nome.title()
        self.ano = ano
        # self.__ano = ano
        self._likes = 0
        # self.__likes = 0

    def exibeFichaTecnica(self):
        print(f"{self._nome} - {self.ano} - {self.likes}") #método genérico

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

class Filme(Titulo3):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    def exibeFichaTecnica(self):
        print(f"{self._nome} - {self.ano} -{self._duracao} - {self.likes}")  # método sobreescrito

class Serie(Titulo3):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def exibeFichaTecnica(self):
        print(f"{self._nome} - {self.ano} - {self._temporadas}- {self.likes} Likes")  # método sobreescrito

filme1 = Filme("FILME", 1990, 120)
filme1.likes = True
filme1.likes = True
filme1.likes = True
serie1 = Serie("SERIE", 1990, 7)
serie1.likes = True
serie1.likes = True

filmesSeries = [filme1, serie1]

#AQUI OCORRE O POLIMORFISMO, COM A CHAMADA DO MÉTODO REESCRITO, NÃO IMPORTA QUAL INSTÂNCIA, FILME, OU SERIE.
for titulo in filmesSeries:
    titulo.exibeFichaTecnica()


print("DUNDER METHODS - __str__")
#__str__ RETORNA UMA REPRESENTAÇÃO VISUAL DO MEU MÉTODO, QUANDO PRINTADA A VARIÁVEL TEMPORÁRIA DO LOOP, IRÁ EXIBIR A
# STRING DO RETURN.

class Titulo4:
    def __init__(self, nome, ano):
        self._nome = nome
        # self.__nome = nome.title()
        self.ano = ano
        # self.__ano = ano
        self._likes = 0
        # self.__likes = 0

    def __str__(self):
        f"{self._nome} - {self.ano} - {self.likes}" #método genérico

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
        return f"{self._nome} - {self.ano} -{self._duracao} - {self.likes} Likes" # método sobreescrito

class Serie(Titulo4):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self._temporadas}- {self.likes} Likes" # método sobreescrito

filme1 = Filme("FILME", 1990, 120)
filme1.likes = True
filme1.likes = True
filme1.likes = True
serie1 = Serie("SERIE", 1990, 7)
serie1.likes = True
serie1.likes = True

filmesSeries = [filme1, serie1]

#AQUI OCORRE O POLIMORFISMO, COM A CHAMADA DO MÉTODO REESCRITO, NÃO IMPORTA QUAL INSTÂNCIA, FILME, OU SERIE.
for titulo in filmesSeries:
    print(titulo) #COMO FOI DEFINIDO UM __str__ QUANDO IMPRIMIR A VARIÁVEL TEMPORÁRIA, O OBJETO SERÁ LIDO CONFORME O
    # RETURN DO MÉTODO DUNDER

