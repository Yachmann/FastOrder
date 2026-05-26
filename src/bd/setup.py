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
            cursor.execute("SELECT COUNT(*) FROM produtos")
            total_produtos = cursor.fetchone()[0]

            
            if total_produtos == 0:
                console.print("[green] PIZZAS ADICIONADAS AO BANCO DE DADOS [/green]")
                cursor.execute("""
                            INSERT INTO produtos (nome, preco, descricao, status) VALUES
    ('Pizza Calabresa', 45.90, 'Molho de tomate, mussarela, calabresa fatiada e orégano.', TRUE),
    ('Pizza Calabresa com Cebola', 46.90, 'Molho de tomate, mussarela, calabresa e cebola caramelizada.', TRUE),
    ('Pizza Portuguesa', 49.90, 'Molho de tomate, mussarela, presunto, ovo, cebola, azeitonas e ervilhas.', TRUE),
    ('Pizza Quatro Queijos', 52.90, 'Molho de tomate e blend de quatro queijos: mussarela, provolone, gorgonzola e parmesão.', TRUE),
    ('Pizza Margherita', 39.90, 'Molho de tomate, mussarela, tomate e manjericão.', TRUE),
    ('Pizza Frango com Catupiry', 48.90, 'Molho de tomate, mussarela, frango desfiado e catupiry cremoso.', TRUE),
    ('Pizza Pepperoni', 47.90, 'Molho de tomate, mussarela e fatias generosas de pepperoni.', TRUE),
    ('Pizza Vegetariana', 44.90, 'Molho de tomate, mussarela e mix de legumes grelhados.', TRUE),
    ('Pizza Bacon', 50.90, 'Molho de tomate, mussarela e bacon crocante.', TRUE),
    ('Pizza Marguerita com Rúcula', 43.90, 'Molho de tomate, mussarela, tomate e rúcula fresca.', TRUE),
    ('Pizza 4 Estações', 53.90, 'Molho de tomate com quatro coberturas: calabresa, frango, palmito e bacon.', TRUE),
    ('Pizza de Mussarela', 42.90, 'Molho de tomate e mussarela extra.', TRUE),
    ('Refrigerante Coca-Cola 350ml', 8.50, 'Lata de Coca-Cola gelada.', TRUE),
    ('Refrigerante Guaraná 350ml', 8.50, 'Lata de guaraná gelado.', TRUE),
    ('Refrigerante Sprite 350ml', 8.50, 'Lata de Sprite gelada.', TRUE),
    ('Suco de Laranja 300ml', 9.90, 'Suco natural de laranja fresco.', TRUE),
    ('Suco de Uva 300ml', 10.90, 'Suco integral de uva.', TRUE),
    ('Água Mineral 500ml', 5.00, 'Água mineral com gás ou sem gás.', TRUE),
    ('Chá Gelado Limão 300ml', 7.90, 'Chá gelado sabor limão.', TRUE),
    ('Cerveja Long Neck 330ml', 12.90, 'Cerveja gelada em garrafa long neck.', TRUE),
    ('Água Tônica 350ml', 7.50, 'Água tônica gelada.', TRUE),
    ('Refrigerante Fanta Laranja 350ml', 8.50, 'Lata de Fanta Laranja gelada.', TRUE),
    ('Suco de Abacaxi com Hortelã 300ml', 11.50, 'Suco de abacaxi com hortelã refrescante.', TRUE)""")
                
    
            
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
                forma_pagamento ENUM('Cartao Debito','Cartao Credito', 'Dinheiro', 'Pix', 'Voucher'),
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
            console.print(f"[red]ERRO AO CRIAR AS TABELAS {E}[/red]")