import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, Column, Integer, Text
from sqlalchemy.schema import Table
# Vantagem do sqlalchemy - mesma estrutra para vários bancos
def conexao_outros_DB_exemplo():
    engine = db.create_engine("mysql+pymysql://user:password@host/dbname?charset=utf8m4")
    pass
# Conexão
def conexao():
    # Crie uma engine
    # path = input("Qual o path do file.db")
    engine = db.create_engine(
        'sqlite:///C:\\Users\\arthu\\OneDrive\\Documentos\\Projetos\\SQLalchemy-SQlite3\\space_api.db')
    conn = engine.connect()
    print("Conectado ao DB")
    return conn

def metadados():

    engine = conexao()
    print("...INICIANDO METADADOS")
    # Crie um objeto MetaData
    metadata = db.MetaData()

    # Realize a reflexão da tabela
    metadata.reflect(bind = engine)
    
    return metadata

# metadados - table
def metadata_table():

    metadata = metadados()

    # tabela desejada
    name_table = str(input("Nome da tabela: "))
    table = metadata.tables[name_table]
    return table
    
# operações
def cabecalho():
    print("FUNC CABECALHO")
    table = metadata_table()
    # interagir com a tabela table
    # Por exemplo, obter as chaves das colunas
    column_names = table.columns.keys()
    print("Cabeçalho: ", column_names)
    print(repr(column_names))

def listar():
    print("FUNC LISTAR")
    conn = conexao()  # o execute só funciona se tiver acesso a conexao
    table = metadata_table()  # metadados
    query = db.select(table)  # comando sql em sqlalchemy
    resp_engine = conn.execute(query)
    resultado = resp_engine.fetchall()
    print(resultado)
    # print(type(resultado)) #cursor
    # print(type(resp_engine)) #lista

def buscar():
    print("FUNC BUSCAR")
    conn = conexao()
    table = metadata_table()
    query = db.select(table).where(table.columns.id == 1)
    # query = db.select(table).where(db.and_(table.columns.id == 1,table.columns.name == 'ARTHUR')) -filtro
    resp_engine = conn.execute(query)
    resultado = resp_engine.fetchall()
    print(resultado)  # sai como lista
    # for row in resultado:
    # print(row) # sai como tupla

def ordenar():
    print("FUNC ORDENAR")
    conn = conexao()
    table = metadata_table()
    query = db.select(table).order_by(db.desc(table.columns.id))
    # query = db.select(table).where(db.and_(table.columns.id == 1,table.columns.name == 'ARTHUR')) -filtro
    resp_engine = conn.execute(query)
    resultado = resp_engine.fetchall()
    print(resultado)  # sai como lista
    # for row in resultado:
    # print(row) # sai como tupla

def deletar():
    print("FUNC DELETAR")
    conn = conexao()
    table = metadata_table()
    query = db.delete(table).where(table.c.id == 1)
    resp_engine = conn.execute(query)
    conn.commit()
    print("Alterações realizadas")

def drop_table():
    print("FUNC DROP")
    engine = conexao()
    table = metadata_table()
    table.drop(engine)
    print("Alterações realizadas")

def create():
    conn = conexao()
    meta = metadados()
    table_name = input('Digite o nome da tabela que será criada: ')
    table = Table(
    f'{table_name}', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', Text),
    Column('genre', Text),
    Column('release_year', Integer),
    Column('duration', Integer)
                                   )

    meta.create_all(bind=conn)

    print("Tabela Criada")

def inserir():
    print("FUNC INSERIR")
    conn = conexao()
    table = metadata_table()
    query = db.insert(table).values(name = "Arthur", password = 12345)
    resp_engine = conn.execute(query)
    conn.commit()
    print("Alterações realizadas")

def update():
    print("FUNC UPDATE")
    conn = conexao()
    table = metadata_table()
    query = db.update(table).values(id = 1)#.where(table.c.id == 3)
    query = query.where(table.c.id == 3)
    conn.execute(query)
    conn.commit()
    print("Aterações realizadas")



# cabecalho()
# listar()
# buscar()
# ordenar()
# deletar()
# listar()
# inserir()
# update()
# create()
# drop_table()