import sqlite3


#result = conn.execute(''' SELECT * FROM users;''')
#result_master = conn.execute(''' SELECT * FROM sqlite_master WHERE type ='table';''')
#print(result)

def consulta(result):
    conn = sqlite3.connect('space_api.db')
    for row in result:
        
    
        
        print(f"""
                *****************
                id:{row[0]}
                Nome:{row[1]}
                Password:{row[2]}
                *****************
                """)
    conn.close()
    
def query():
    
    conn = sqlite3.connect('space_api.db')# execute pede conexão
    result = conn.execute(input("Digite a query: "))
    consulta(result)
    conn.close()

def schema():
    
    conn = sqlite3.connect('space_api.db')
    for row in result_master:
        print(row)
    conn.close()

def create_table():
    
    conn = sqlite3.connect('space_api.db')
    result = conn.execute("""CREATE TABLE movie (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          title TEXT,
                          genre TEXT,
                          release_year INTEGER,
                          qt_episodes INTEGER,
                          qt_seasons INTEGER,
                          synopsis TEXT,
                          users_id INTEGER,
                          FOREIGN KEY (users_id) REFERENCES users(id));""")

    print("Table Created")
    conn.close()

def dml(): # abrevie DML englobando qualquer alteração insert, delete ou update.
    conn = sqlite3.connect('space_api.db')
    print("Database Conected")
    conn.cursor()        
    alteracao = input("UPDATE, INSERT OR DELETE: ").lower()
    table_name = input("Nome da tabela: ").lower()
    
    if alteracao == "update":
        campo_where = input("campo do where: ")
        valor_where = input(" valor do where: ")
        campo_alteracao = input("digite o campo que será alterado: ")
        valor_alteracao = input("Digite novo valor: ")
        conn.execute(f"Update {table_name} SET {campo_alteracao} = {valor_alteracao} WHERE {campo_where} = {valor_where};")
    

    elif alteracao == "insert":
        valores = input("separe por vírgula os valores: ")
        campos = input("separe por vírgula os campos: ")
        valores_formatados = tuple(valores.split(","))
        campos_formatados = tuple(campos.split(","))
        placeholders = ",".join(["?"] * len(valores_formatados))

        consulta = f"INSERT INTO {table_name} ({campos}) VALUES ({placeholders})"
        conn.execute(consulta, valores_formatados)
        conn.commit()


    else:
        if alteracao == "delete":
            campo_where = input("campo do where: ")
            valor_where = input(" valor do where: ")
            conn.execute(f"DELETE FROM {table_name} WHERE {campo_where} = {valor_where};")

        conn.commit()
    print("Alterações realzidas!")
    conn.close()

def DML():
    conn = sqlite3.connect('space_api.db')
    conn.cursor()
    conn.execute(input("Digite o comando sql: "))
    conn.commit()
    print("Alterações realzidas!")
    conn.close()
    
def consulta_Flask_list():
    conn = sqlite3.connect('space_api.db')
    cursor = conn.cursor()
    result = cursor.execute('''SELECT * FROM users''')
    results = []
    for row in result:
        results.append([str(row[0]), str(row[1]), str(row[2])])
    return results

def consulta_Flask_dict():
    conn = sqlite3.connect('space_api.db')
    cursor = conn.cursor()
    result = cursor.execute('''SELECT * FROM users''')
    results = []
    columns = [column[0] for column in cursor.description]
    for row in result:
        row_dict = {}
        for i, column in enumerate(columns):
            row_dict[column] = str(row[i])
        results.append(row_dict)
    return results

   



#schema()
# create_table()
#query()
#insert()
#DML()
