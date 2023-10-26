# Funções são códigos que executam uma determinada tarefa. Podem ou não retornar algum valor, como podem ou não
# receber parâmetros. As funções reutilizam código e dinamizam a inicialização quando os valores são passados como parâmetros

# Funções que retornam valor, devem ser guardas em variáveis.


#a função inicializa uma conta, criando um dicionário com os seguintes parâmetros
def cria_conta(numero, titular, saldo, limite): # argumentos são campos temporários que recebem valores
    conta = {"numero": numero,
             "titular": titular,
             "saldo": saldo,
             "limite": limite}
    return conta # para retornar uma variável ou uma valor, é passada a declaração return
#para inicializar uma conta basta guardar o método cria_conta() que retornar uma conta, em uma variável.

# conta1 = cria_conta(1,"cliente", 1000.0, 2000.0) - a variável conta, possui as informações de uma conta.



#a função adiciona a conta criada um valor

def deposita(conta, valor): # é passado a conta, e conta é um dicionário
    conta["saldo"] += valor
#obs. funções que não retornam valor, não precisam ser guardadas por variáveis, são executadas pelo próprio objeto.
#deposita(conta1, 1000.0)
#print(conta1["saldo"]) >> 1100.00


def saca(conta, valor):
    conta["saldo"] -=valor

def extrato(conta):
    print(f"Saldo: {conta['saldo']}")


conta = cria_conta(1, "Arthur", 1000, 2000)
saca(conta, 20)
print(conta)