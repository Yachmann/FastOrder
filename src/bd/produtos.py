from bd.connect import conectar_db

def listar_produtos()->list:
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary = True)
        cursor.execute("SELECT * FROM  produtos")
        produtos = cursor.fetchall()
        cursor.close()
        conn.close()
        return produtos
    else:
        return []

def adicionar_produto(produto:dict):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        sql = """
    INSERT INTO produtos (nome, preco, descricao, status)
    VALUES (%s, %s, %s, %s)
    """
        cursor.execute(sql,(produto['nome'],produto['preco'],produto['descricao'],produto['status']))
        conn.commit()
        cursor.close()
        conn.close()

def buscar_produto(id):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
        produto = cursor.fetchone()

        cursor.close()
        conn.close()
        return produto


def atualizar_produto(produto):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()

        sql = """
        UPDATE produtos
        SET nome=%s, preco=%s, descricao=%s, status=%s
        WHERE id=%s
        """
        cursor.execute(sql, (produto['nome'],produto['preco'],produto['descricao'],produto['status']))

        conn.commit()
        cursor.close()
        conn.close()


# DELETE
def deletar_produto(id):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))

        conn.commit()
        cursor.close()
        conn.close()
