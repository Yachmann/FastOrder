from bd.connect import conectar_db

def listar_pedidos()->list:
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary = True)
        # Join with pedido_itens to get item names, and clientes/entregadores for names
        cursor.execute("""
            SELECT p.id, p.cliente_id, p.entregador_id, p.valor_total, p.status, 
                   p.forma_pagamento, p.data_hora,
                   GROUP_CONCAT(pr.nome SEPARATOR ', ') as itens,
                   c.nome as cliente,
                   f.nome as entregador
            FROM pedidos p
            LEFT JOIN pedido_itens pi ON p.id = pi.pedido_id
            LEFT JOIN produtos pr ON pi.produto_id = pr.id
            LEFT JOIN clientes c ON p.cliente_id = c.id
            LEFT JOIN funcionarios f ON p.entregador_id = f.id
            GROUP BY p.id
        """)
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
        INSERT INTO pedidos (cliente_id,entregador_id,valor_total,status,forma_pagamento,data_hora)
        VALUES (%s, %s, %s, %s, %s, NOW())
        """
        cursor.execute(sql,(pedido['cliente_id'],pedido['entregador_id'],pedido['valor_total'],pedido['status'],pedido['forma_pagamento']))
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


# LISTAR PEDIDOS POR STATUS
def listar_pedidos_por_status(status: str) -> list:
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.id, p.cliente_id, p.entregador_id, p.valor_total, p.status, 
                   p.forma_pagamento, p.data_hora,
                   c.nome as cliente,
                   f.nome as entregador,
                   '' as itens
            FROM pedidos p
            LEFT JOIN clientes c ON p.cliente_id = c.id
            LEFT JOIN funcionarios f ON p.entregador_id = f.id
            WHERE p.status = %s
        """, (status,))
        pedidos = cursor.fetchall()
        cursor.close()
        conn.close()
        return pedidos
    else:
        return []


# LISTAR PEDIDOS POR DATA
def listar_pedidos_por_data(data: str) -> list:
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.id, p.cliente_id, p.entregador_id, p.valor_total, p.status, 
                   p.forma_pagamento, p.data_hora,
                   c.nome as cliente,
                   f.nome as entregador,
                   '' as itens
            FROM pedidos p
            LEFT JOIN clientes c ON p.cliente_id = c.id
            LEFT JOIN funcionarios f ON p.entregador_id = f.id
            WHERE DATE(p.data_hora) = %s
        """, (data,))
        pedidos = cursor.fetchall()
        cursor.close()
        conn.close()
        return pedidos
    else:
        return []


# LISTAR PEDIDOS POR ENTREGADOR
def listar_pedidos_por_entregador(entregador_id: int) -> list:
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.id, p.cliente_id, p.entregador_id, p.valor_total, p.status, 
                   p.forma_pagamento, p.data_hora,
                   c.nome as cliente,
                   f.nome as entregador,
                   '' as itens
            FROM pedidos p
            LEFT JOIN clientes c ON p.cliente_id = c.id
            LEFT JOIN funcionarios f ON p.entregador_id = f.id
            WHERE p.entregador_id = %s
        """, (entregador_id,))
        pedidos = cursor.fetchall()
        cursor.close()
        conn.close()
        return pedidos
    else:
        return []


# ATUALIZAR STATUS DO PEDIDO
def atualizar_status_pedido(pedido_id: int, novo_status: str):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE pedidos SET status = %s WHERE id = %s", (novo_status, pedido_id))
        conn.commit()
        cursor.close()
        conn.close()
