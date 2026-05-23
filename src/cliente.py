#Codigo em relação ao cliente
from rich.console import Console
from bd.clientes import adicionar_cliente

console = Console()

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    
    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "endereco": endereco
    }
    try:
        
        novo_id = adicionar_cliente(cliente=cliente)
        
        
        cliente["id"] = novo_id 
        
        console.print("[green]Cliente cadastrado com sucesso![/green]")
        
        return cliente
    
    except Exception as E:
        console.print(f"[red]Cliente nao cadastrado : {E} [/red]")
        return None 

    


