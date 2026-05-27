from bd.connect import conectar_db
from rich.console import Console
from rich.table import Table
console = Console()
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
        novo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return novo_id

def deletar_cliente(id):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()


def atualizar_cliente(cliente: dict):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        sql = """
        UPDATE clientes 
        SET nome = %s, email = %s, telefone = %s, endereco = %s 
        WHERE id = %s
        """
        cursor.execute(sql, (
            cliente['nome'],
            cliente['email'],
            cliente['telefone'],
            cliente['endereco'],
            cliente['id']
        ))
        conn.commit()
        cursor.close()
        conn.close()
