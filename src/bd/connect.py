from rich.console import Console
console = Console()
import mysql.connector
connector = mysql.connector


def conectar_db():
    try:
        db_connector = connector.connect(
            host = "localhost",
            user = "root",
            passwd = "root",
            database = "restaurante",
        )
        console.print("[green]Conexao com o banco de dados feita com sucesso[/green]")
        return db_connector
        
    except Exception as E:
        console.print(f"[red]Conexao com o banco de dados nao foi feita con sucesso[/red]",E)
    
