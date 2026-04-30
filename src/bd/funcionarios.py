from bd.connect import conectar_db

def listar_funcionarios()->list:
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary = True)
        cursor.execute("SELECT * FROM  funcionarios")
        funcionarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return funcionarios
    else:
        return []

def adicionar_funcionario(funcionario:dict):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        sql = """
    INSERT INTO funcionarios (nome, cargo, telefone, veiculo, email, senha )
    VALUES (%s, %s, %s, %s, %s, %s)
    """
        cursor.execute(sql,(funcionario['nome'],funcionario['cargo'],funcionario['telefone'],funcionario['veiculo'],funcionario['email'],funcionario['senha']))
        conn.commit()
        cursor.close()
        conn.close()

def buscar_funcionario(id):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM funcionario WHERE id = %s", (id,))
        funcionario = cursor.fetchone()

        cursor.close()
        conn.close()
        return funcionario


def atualizar_funcionario(funcionario):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()

        sql = """
        UPDATE funcionarios
        SET nome=%s, cargo=%s, telefone=%s, veiculo=%s, email=%s, senha=%s
        WHERE id=%s
        """
        cursor.execute(sql, (funcionario['nome'],funcionario['cargo'],funcionario['telefone'],funcionario['veiculo'],funcionario['email'],funcionario['senha']))

        conn.commit()
        cursor.close()
        conn.close()


# DELETE
def deletar_funcionario(id):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM funcionarios WHERE id = %s", (id,))

        conn.commit()
        cursor.close()
        conn.close()

def verificar_funcionario(email,senha,cargo):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM funcionarios WHERE email = %s AND senha = %s AND cargo = %s", (email,senha,cargo))
            funcionario = cursor.fetchone()

            cursor.close()
            conn.close()
            return funcionario
        except Exception as E:
            print(E)
            return {}
    else : 
        return {}
