def query_buscar():
    conn = conexao()
    table = metadata_table()
    query = db.select([table]).where([table.columns.get('name') == "ARTHUR"])
    resp_engine = conn.execute(query)
    resultado = resp_engine.fetchall()
    print(resultado)
    