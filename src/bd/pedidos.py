from bd.connect import conectar_db

def listar_pedidos()->list:
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary = True)
        cursor.execute("SELECT * FROM  pedidos")
        pedidos = cursor.fetchall()
        cursor.close()
        conn.close()
        return pedidos
    else:
        return []

def adicionar_pedido(pedido:dict):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        sql = """
    INSERT INTO funcionarios (cliente_id,entregador_id,valor_total,status,forma_pagamento,data_hora )
    VALUES (%s, %s, %s, %s)
    """
        cursor.execute(sql,(pedido['cliente_id'],pedido['entregador_id'],pedido['valor_total'],pedido['status'],pedido['forma_pagamento'],pedido['data_hora']))
        conn.commit()
        pedido_id = cursor.lastrowid  
        cursor.close()
        conn.close()
        return pedido_id
    

def inserir_itens_pedido(pedido_id, itens: list):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            sql = """
            INSERT INTO pedido_itens (pedido_id, produto_id, preco)
            VALUES (%s, %s, %s)
            """

            for item in itens:
                cursor.execute(sql, (
                    pedido_id,
                    item["produto_id"],
                    item["preco"]
                ))

            conn.commit()

        except Exception as e:
            print("Erro ao inserir itens:", e)
            raise e

        finally:
            cursor.close()
            conn.close()
def buscar_pedido(id):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM pedidos WHERE id = %s", (id,))
        pedido = cursor.fetchone()

        cursor.close()
        conn.close()
        return pedido


def atualizar_pedido(pedido_atualizado):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()

        sql = """
        UPDATE pedidos
        SET cliente_id=%s, entregador_id=%s, valor_total=%s, status=%s, forma_pagamento=%s, data_hora=%s
        WHERE id=%s
        """
        cursor.execute(sql, (pedido_atualizado['cliente_id'],pedido_atualizado['entregador_id'],pedido_atualizado['valor_toal'],pedido_atualizado['status'],pedido_atualizado['forma_pagamento'],pedido_atualizado['data_hora']))

        conn.commit()
        cursor.close()
        conn.close()



# DELETE
def deletar_pedido(id):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM pedidos WHERE id = %s", (id,))

        conn.commit()
        cursor.close()
        conn.close()
