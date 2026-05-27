
from rich.console import Console
from bd.clientes import adicionar_cliente,atualizar_cliente,listar_clientes_banco
from rich.table import Table
console = Console()

def cadastrar_cliente(email_ja_existente):
    nome = input("Digite o nome do cliente: ")
    if not email_ja_existente:
        email = input("Digite o email do cliente: ")
    else:
        email = email_ja_existente
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

    


def editar_cliente():
    clientes = listar_clientes_banco()
    if not clientes:
        console.print("[yellow]Nenhum cliente cadastrado.[/yellow]")
        return
        
    lista_ids = [cliente['id'] for cliente in clientes]
    table = Table(title="Editar Cliente")

    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("Email")
    table.add_column("Telefone")
    table.add_column("Endereço")

    for cliente in clientes:
        table.add_row(
            str(cliente['id']),
            cliente["nome"],
            cliente["email"],
            cliente["telefone"],
            cliente["endereco"]
        )

    console.print(table)

    try:
        indice = int(input("Digite o ID do cliente que deseja editar: "))
        cliente_a_editar = {}
        
        if indice in lista_ids:
            for cliente in clientes:
                if cliente['id'] == indice:
                    cliente_a_editar = cliente

            nome = input(f"Digite o novo nome (deixe em branco para manter '{cliente_a_editar['nome']}'): ")
            email = input(f"Digite o novo email (deixe em branco para manter '{cliente_a_editar['email']}'): ")
            telefone = input(f"Digite o novo telefone (deixe em branco para manter '{cliente_a_editar['telefone']}'): ")
            endereco = input(f"Digite o novo endereço (deixe em branco para manter '{cliente_a_editar['endereco']}'): ")
            
            if nome:
                cliente_a_editar["nome"] = nome
            if email:
                cliente_a_editar["email"] = email
            if telefone:
                cliente_a_editar["telefone"] = telefone
            if endereco:
                cliente_a_editar["endereco"] = endereco
            
            atualizar_cliente(cliente=cliente_a_editar)
            console.print("[green]Cliente editado com sucesso![/green]")
        else:
            console.print("[red]ID inválido. Tente novamente.[/red]")
            
    except Exception as E:
        console.print(f"[red]Cliente não editado: {E}[/red]")