import os
from dotenv import load_dotenv
from rich.console import Console
console = Console()
import mysql.connector
connector = mysql.connector

load_dotenv()

def conectar_db():
    try:
        db_connector = connector.connect(
            host = os.getenv("HOST"),
            user = os.getenv("USER"),
            passwd = os.getenv("PASSWORD"),
            database = os.getenv("DATABASE"),
        )
        console.print("[green]Conexao com o banco de dados feita com sucesso[/green]")
        return db_connector
        
    except Exception as E:
        console.print(f"[red]Conexao com o banco de dados nao foi feita con sucesso[/red]",E)
    
