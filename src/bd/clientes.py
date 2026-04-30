from bd.connect import conectar_db

def listar_clientes_banco()->list:
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary = True)
        cursor.execute("SELECT * FROM  clientes")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()
        return clientes
    else:
        return []

def adicionar_cliente(cliente:dict):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        sql = """
    INSERT INTO clientes (nome, email, telefone, endereco )
    VALUES (%s, %s, %s, %s)
    """
        cursor.execute(sql,(cliente['nome'],cliente['email'],cliente['telefone'],cliente['endereco']))
        conn.commit()
        cursor.close()
        conn.close()