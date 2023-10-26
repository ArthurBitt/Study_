#POO INTRODUÇÃO, CLASSES, OBJETOS, MÉTODOS (ESTÁTICOS, PRIVADOS), ATRIBUTOS, ENCAPSULAMENTO(VISIBILIDADE DOS
# ATRIBUTOS, GETTERS E SETTERS)



                                                            #PILARES OOP
print("ENCAPSULAMENTO")# : é o ato de esconder os dados da classe, isto é, deixar seus atributos privados.

#   self._protegido
#   self.__privado
#   self.publico

# Atributos privados são acessíveis somente dentro da própria classe.
# atributos protegidos são acessados fora da classe e de forma direta, mas visualmente são sinalizados
# atributos publicos são acessíveis de qualquer classe e de forma direta pela referência
#  Classes externas não possuem acesso a atributos privados
# é necessário usar métodos getters e setters para acessar e atualizar os valores de um atributo para acessa-los de outra classe.


class Conta4:
    def __init__(self, numero, titular, saldo, limite = 2000):

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f"Conta{self}/ Saldo: {self.__saldo}")
        return self.__saldo

    def deposita(self, valor):
        self.__saldo += valor
        print(f"Foram depositados: {valor} em {self}")
        return self.__saldo

    def saca(self, valor):
        self.__saldo -= valor
        print(f"Foram sacados: {valor} de {self}")
        return self.__saldo

    def transfere(self, destino ): #self remete a conta que chama a função,logo a do saque
        valor = float(input("Valor: "))
        self.saca(valor)
        destino.deposita(valor)
        self.extrato()
        destino.extrato()

obj6 = Conta4(1,"Arthur", 10.0)
obj7 = Conta4(1,"Bittencourt", 10.0)
obj6.transfere(obj7)


# print("objeto6: ", obj6.extrato())
# obj6._Conta4__saldo = 0 #mesmo deixando os atributos privados no python, ainda é possível acessa-los com referencia._ClasseName__atributo
# print("objeto6Alterado: ", obj6.extrato())# note que mesmo privado, o atributo foi alterado.
#

print("ENCAPSULAMENTO - GETTERS & SETTERS")

#getter (get_) é a nomenclatura padrão para métodos que retornam algum valor do atributo - retornam valor
#setter (set_) é a nomenclatura padrão para métodos que atualizam e alteram os atrinutos - não retornam valor


class Conta5:
    def __init__(self, numero, titular, saldo, limite = 2000):

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite



    #exibe extrato printa o saldo, mas não o retorna
    def exibe_extrato(self):
        print(f"Conta{self}/ Saldo: {self.__saldo}")

    # def retorna_Saldo(self):
    #     return  self.__saldo

    def get_Saldo(self):
        return  self.__saldo

    # def retorna_Limite(self):
    #     return self.__limite

    def get_Limite(self):
        return self.__limite

    # def retorna_Titular(self):
    #     return self.__titular

    def get_Titular(self):
        return self.__titular


    # def altera_Limite(self, valor):
    #     self.__limite = valor

    def set_Limite(self, valor):
        self.__limite = valor


    def deposita(self, valor):
        self.__saldo += valor
        print(f"Foram depositados: {valor} em {self}")
        return self.__saldo

    def saca(self, valor):
        self.__saldo -= valor
        print(f"Foram sacados: {valor} de {self}")
        return self.__saldo

    def transfere(self, destino ):

        valor = float(input("Valor: "))
        self.saca(valor)
        destino.deposita(valor)
        self.extrato()
        destino.extrato()


obj8 = Conta5(1,"Arthur", 100)

obj8.set_Limite(10000)
print("Novo Limite: " , obj8.get_Limite())


print("PROPRIEDADES")
#setters e getters são renomeados e marcados com @property
# dessa forma é possível chamar getters e setters sem escrever get_ e set_ e sem usar os ()
#reservado para getters e setters de atributos
#só é possível um @atribut.setter se houver um property correspondente

class Conta6:
    def __init__(self, numero, titular, saldo, limite=2000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        print("get method usando property")
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        print("set method usando @atributo.setter")
        self.__titular = novo_titular.title()

# Exemplo de uso
obj8 = Conta6(1, "Arthur", 100)
print(obj8.titular)  # Output: Arthur

obj8.titular = "AA"
print(obj8.titular)  # Output: Aa

print("MÉTODOS PRIVADOS")
#Métodos de mais baixo nível, escondem funcionamento, encapsulando o código, melhorando a legelibilidade


class Conta7:
    def __init__(self, numero, titular, saldo, limite = 2000):

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #exibe extrato printa o saldo, mas não o retorna
    def exibe_extrato(self):
        print(f"Conta{self}/ Saldo: {self.__saldo}")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


    def deposita(self, valor):
        self.__saldo += valor
        print(f"Foram depositados: {valor} em {self}")
        return self.__saldo

    #função privada menor nível, apenas verifica true ou false e envia para função sacar mais alto nível o bool que é
    # verificado na def saca() pelo if else
    def __podeSacar(self, valor):
        saldoSaque = self.__saldo + self.__limite
        return valor <= saldoSaque

    def saca(self, valor):
        if (self.__podeSacar(valor)):
            print(f"Foram sacados: {valor} de {self}")
            self.__saldo -= valor
        else:
            print(f"O valor de {valor:.2f} R$ supera seu limite de {self.limite} R$")

    def transfere(self, destino ):
        valor = float(input("Valor: "))
        self.saca(valor)
        destino.deposita(valor)
        self.extrato()
        destino.extrato()


obj9 = Conta7(1,"Arthur", 1, 1)
obj9.saca(1)


print("MÉTODOS ESTÁTICOS")
#Métodos que pertencem a classe, eles independem de um objeto estar criado para serem utilizados. Não recebem o
# parâmetro self

class Conta8:
    def __init__(self, numero, titular, saldo, limite = 2000):

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #exibe extrato printa o saldo, mas não o retorna
    def exibe_extrato(self):
        print(f"Conta{self}/ Saldo: {self.__saldo}")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


    def deposita(self, valor):
        self.__saldo += valor
        print(f"Foram depositados: {valor} em {self}")
        return self.__saldo

    #função privada menor nível, apenas verifica true ou false e envia para função sacar mais alto nível o bool que é
    # verificado na def saca() pelo if else
    def __podeSacar(self, valor):
        saldoSaque = self.__saldo + self.__limite
        return valor <= saldoSaque

    def saca(self, valor):
        if (self.__podeSacar(valor)):
            print(f"Foram sacados: {valor} de {self}")
            self.__saldo -= valor
        else:
            print(f"O valor de {valor:.2f} R$ supera seu limite de {self.limite} R$")

    def transfere(self, destino ):
        valor = float(input("Valor: "))
        self.saca(valor)
        destino.deposita(valor)
        self.extrato()
        destino.extrato()


    @staticmethod #o decorador é utilizado para indicar o método estárico
    def cod_banco(): # como está preso lógicamente a classe, não é necessário passar o objeto como argumento, isto é,
        # self
        return "001"

obj10= Conta8(1,"Arthur", 1, 1)
print(Conta8.cod_banco())

print("STATIC x CLS")
# Métodos de classe (@classmethod):
# São marcados com o decorador @classmethod e recebem implicitamente o argumento cls, que representa a classe atual.
# Podem acessar os atributos da classe, mas não têm acesso aos atributos da instância.
# São usados quando precisamos executar uma ação relacionada à classe em si, em vez de uma instância específica.
# Podem ser chamados tanto na classe quanto em instâncias da classe.
# Aqui está um exemplo de uma classe Pessoa com um método de classe:

class Pessoa:
    total_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1

    @classmethod
    def contar_pessoas(cls):
        return cls.total_pessoas

p1 = Pessoa("Alice")
p2 = Pessoa("Bob")
print(Pessoa.contar_pessoas())  # Output: 2
print(p1.contar_pessoas())  # Output: 2
print(p2.contar_pessoas())  # Output: 2


# Métodos estáticos (@staticmethod):
# São marcados com o decorador @staticmethod e não recebem implicitamente o argumento self ou cls.
# Não têm acesso aos atributos da classe ou da instância.
# São usados quando a lógica do método não depende de atributos específicos da classe ou da instância.
# Podem ser chamados tanto na classe quanto em instâncias da classe.

class Calculadora:
    @staticmethod
    def soma(a, b):
        return a + b

resultado = Calculadora.soma(2, 3)
print(resultado)  # Output: 5



