print("CLASSES")
class Conta :#palavra reservada class para criar uma classe -  classes são modelos dos qual são instanciados

#Contrutores : são funções que inicializam um objeto - o que estiver dentro de um construtor sejam print(),
# atributos...seram inicializados juntos do objeto

    def __init__(self): # self é utilizado para fazer referência ao atributo da classe, diferenciando-o dos
        # parâmetros com mesmo nome passados nas funções. Todas as funções/métodos de uma classe, tem como primeiro
        # parâmero o self.

        print("objeto construido")


print("OBJETOS") #: instancias de uma classe, são armazenados em referências

obj1 = Conta() # Isto é uma instanciação de objeto. A chamada de Conta() gera um objeto na memória. A variável de
# referência obj1 guarda o local da memória onde o Conta() foi criado.

obj1 = Conta() # Esse objeto já não é mais o mesmo que o obj1 anterior, guarda, portanto, outro endereço. O obj1
# anterior é apagado por um processo chamado coletor de lixo.

obj2 = Conta()

print("Objeto1: ",obj1) # O print gera como output um hexadecimal que é o espaço da memória onde foi criado o objeto
# Conta()
# guardado na referência obj1
print("Objeto2: ", obj2)
# Exemplificando o que é referência e o que é objeto

# Teste 1
# São duas referências distintas, que guardam objetos armazenados em espaços distintos da memória
if (obj1 == obj2):
    print("É o mesmo objeto, em referências distintas")

else:
    print("São objetos diferentes")

# Defino que obj1 é igual a obj2
obj1 = obj2

# Teste 2
# Quando defino que obj1 que guarda um objeto é igual a obj2, as referências apesar de distintas, passam a guardar o
# mesmo objeto, isto é, apontam para o mesmo espaço da memória.
if (obj1 == obj2):
    print("É o mesmo objeto, em referências distintas")

else:
    print("São objetos diferentes")

#Teste 3 - obj2 agora aponta para lugar nenhum, isto é, não guarda mais a referência de obj1
obj2 = None
print(f"Objeto 2: {obj2}" ) # dessa forma é posível apagar a referência de um objeto

# Referências só acessam diretamente atributos e métodos da classe, se não estiverem encapsulados. Caso contrário,
# são usados métodos getters e setters para acessar um atributo

print("ATRIBUTOS")# são as carcterísticas que todo objeto instanciado da classe possui

# Os atributos inicializados recebem os valores passados como parâmetros na inicialização do objeto,
# mas poderiam receber valores fixos
# note que o parâmetro limite foi setado com um valor default, logo não é preciso passa-lo na instanciação de
# um objeto, a menos que o valor precise ser diferente, no caso, se for um limite especial.
class Conta2:
    def __init__(self, numero, titular, saldo, limite = 2000):


        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


#objeto construido com limite padrão
obj3 = Conta2(1,"Arthur",1000.0) # como o construtor possui parâmetros definidos, para instanciar o objeto é
# preciso passar os  valores dos campos para o construtor
#objeto construido com limite especial
obj4 = Conta2(1,"Arthur",1000.0,3000.0)
print("Objeto3:", obj3)

#Acessando atributos não encapsulados - as referências acessam atributos e métodos public utilizando .método/atributo
#Não encapsular os atributos gera erros, uma vez que é possível acessa-los, qualquer um pode modificar seus valores.

#obj3.nomedométodo()
print("Objeto 3: ", "titular:" , obj3.titular,f"limite" , obj3.limite, "Saldo: ",obj3.saldo)# note que o limite é 2000
print("Objeto 4: ", "titular:" , obj4.titular,f"limite" , obj4.limite, "Saldo: ",obj4.saldo)# note que o limite é 3000
obj3.saldo = 0 #note que acessar um atributo diretamente pode fazer com que um saldo de uma conta sofra modificações

print("Saldo zerado: ", obj3.saldo)

print("ATRIBUTOS DA CLASSE")
class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def altera_nome(self, nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, like):
        if like:
            self.__likes += 1

class Serie:
    def __init__(self, nome, ano,temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def altera_nome(self, nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, like):
        if (like):
            self.__likes += 1

filme1 = Filme("FILME", 1990, 120)
filme1.likes = True
filme1.likes = True
filme1.likes = True
print(f"Nome: {filme1.nome} - Likes: {filme1.likes}")

serie1 = Serie("SERIE", 1990, 7)
serie1.likes = True
serie1.likes = True
print(f"Nome: {serie1.nome} - Likes: {serie1.likes}")# note que o acesso é no método, uma vez que o atributo esta privado


# Nota: atributos da classe podem ser usados por todas as instâncias
class Pessoa:
    tamanho_cpf = 11 #atributo da classe

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False #__class__ é usando para referenciar o
        # atributo, também poderia usar Pessoa - nome da classe para referenciar o atributo

pe = Pessoa('00000000001', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('0000000000', 'Cristal')
print(pe.valida_cpf())

#utilizar um atributo da classe sem o __class_ e atribuí-lo ao objeto gera divergência, pois o atributo criado
# pertence ao objeto, e não a classe


class Pessoa:
    tamanho_cpf = 11

p = Pessoa()

print(p.tamanho_cpf)

p.tamanho_cpf = 12

print(p.tamanho_cpf)

print(Pessoa.tamanho_cpf)


print("MÉTODOS") #manipulam o comportamento e a interação dos objetos, encapsulando o código de modo que quem usa não
    # sabe como funciona. Evidente que ao código ainda pode ser mais encapsulado.

class Conta3:

    #método construtor inicializa o objeto.
    def __init__(self, numero, titular, saldo, limite = 2000):
    #criado Atributo    #Recebe Parâmetro
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


#As funções recebem o self como primeiro parâmetro para que acessem os atributos da classe de dentro do seu escopo. O
     # parâmetro self é flexível, de modo que trabalha com a variavel referência que chama o método, logo o self
     # acessará os valores da referência em questão.
    def extrato(self):
        print(f"Saldo: {self.saldo}")

    # repare que a função recebe um segundo parâmetro depois de self, com self passado, posso acessar qualquer um dos
    # atributos da classe e modificar seus valores como o segundo parâmetro valor.
    def deposita(self, valor):
        self.saldo += valor
        print(f"Foram depositados: {valor} ")
        return self.saldo

    def saca(self, valor):
        self.saldo -= valor
        print(f"Foram sacados: {valor} ")
        return self.saldo

obj5 = Conta3(1,"Arthur",1000.0,3000.0)
print("Objeto 5:", obj5)

obj5.extrato()
obj5.deposita(300)
obj5.extrato()
obj5.saca(300)
obj5.extrato()

# Montando Uma classe extra - Data


class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")


d = Data(21,11,2007)
d.formatada()
