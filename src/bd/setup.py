from bd.connect import conectar_db
from rich.console import Console

console = Console()
def create_tables():
    
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                preco FLOAT,
                descricao TEXT,
                status BOOLEAN
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                telefone VARCHAR(20),
                endereco TEXT
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cargo VARCHAR(100) NOT NULL,
                nome VARCHAR(255) NOT NULL,
                telefone VARCHAR(50),
                veiculo VARCHAR(100),
                email VARCHAR(300),
                senha VARCHAR(100)
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente_id INT,
                entregador_id INT,
                valor_total FLOAT,
                status VARCHAR(50),
                forma_pagamento VARCHAR(50),
                data_hora DATETIME,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                FOREIGN KEY (entregador_id) REFERENCES funcionarios(id)
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedido_itens (
                id INT AUTO_INCREMENT PRIMARY KEY,
                pedido_id INT,
                produto_id INT,
                preco FLOAT,
                FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
            )
            """)

            conn.commit()
            cursor.close()
            conn.close()
            console.print("[green]TABELAS CRIADAS COM SUCESSO[/green]")
        except Exception as E:
            console.print("[red]ERRO AO CRIAR AS TABELAS[/red]")