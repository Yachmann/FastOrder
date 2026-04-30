from rich.console import Console
from rich.table import Table
from bd.funcionarios import listar_funcionarios,adicionar_funcionario,atualizar_funcionario
from bd.produtos import listar_produtos, adicionar_produto,atualizar_produto
from bd.clientes import listar_clientes_banco
console = Console()





def adicionar_produto_():
    concluido = False
    while not concluido:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        descricao = input("Digite a descrição do produto: ")
        status = int(input("Digite o status do produto (1 para disponível, 0 para indisponível): "))
        
        produto = {
            "nome": nome,
            "preco": preco,
            "descricao": descricao,
            "status": status
        }
        
        try:
            adicionar_produto(produto=produto)
            console.print("[green]Produto adicionado com sucesso![/green]")
        except Exception as E:
            console.print(f"[red]Produto adicionado com sucesso! {E}[/red]")
        
        opcao = input("Deseja adicionar outro produto? (s/n): ")
        if opcao.lower() != 's':
            concluido = True

def editar_produto():
    produtos = listar_produtos()
    lista_ids = [produto['id'] for produto in produtos ]
    table = Table(title="Editar Produto")

    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("Preço")
    table.add_column("Descrição")
    table.add_column("Status")


    for produto in produtos:
        status = "Disponível" if produto["status"] == 1 else "Indisponível"
        table.add_row(
            str(produto['id']),
            produto["nome"],
            f"R$ {produto['preco']:.2f}",
            produto["descricao"],
            status
        )

    console.print(table)


    indice = int(input("Digite o número do produto que deseja editar: "))

    if indice in lista_ids:
        produto = produtos[indice]
        nome = input(f"Digite o novo nome do produto (deixe em branco para manter '{produto['nome']}'): ")
        preco = input(f"Digite o novo preço do produto (deixe em branco para manter R$ {produto['preco']:.2f}): ")
        descricao = input(f"Digite a nova descrição do produto (deixe em branco para manter '{produto['descricao']}'): ")
        status = input(f"Digite o novo status do produto (1 para disponível, 0 para indisponível, deixe em branco para manter {'Disponível' if produto['status'] == 1 else 'Indisponível'}): ")
        
        if nome:
            produto["nome"] = nome
        if preco:
            produto["preco"] = float(preco)
        if descricao:
            produto["descricao"] = descricao
        if status:
            produto["status"] = int(status)
        
        try:
            atualizar_produto(produto=produto)
            console.print("[green]Produto editado com sucesso![green]")
        except Exception as E:
            console.print("[red]Produto nao editado[red]")
    else:
        print("Índice inválido. Tente novamente.")
        
def listar_produtos_():
    produtos = listar_produtos()
    table = Table(title="Produtos")

    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("Preço", justify="right")
    table.add_column("Descrição")
    table.add_column("Status")

    for i, produto in enumerate(produtos):
        status = None
        if produto["status"] == 1:
            status = 'Disponivel'
        else:
            status = 'Indisponivel'


        table.add_row(
            str(i),
            produto["nome"],
            f"R$ {produto['preco']:.2f}",
            produto["descricao"],
            status
        )

    console.print(table)
        
def adicionar_entregador():
    nome = input("Digite o nome do entregador: ")
    telefone = input("Digite o telefone do entregador: ")
    veiculo = input("Digite o veículo do entregador: ")
    email = input("Digite o email do entregador: ")
    senha = input("Crie uma senha para o  entregador: ")
    
    entregador = {
        "nome": nome,
        "telefone": telefone,
        "cargo": "entregador",
        "veiculo": veiculo,
        "email" : email,
        "senha": senha
    }
    try:
        adicionar_funcionario(entregador)
        console.print("[green]Entregador adicionado com sucesso![/green]")
    except Exception as E:
        console.print(f"[red]Entregador nao adicionado : {E}[/red]")



def editar_entregador():
    funcionarios = listar_funcionarios()
    entregadores = [funcionario for funcionario in funcionarios if funcionario['cargo'] == 'entregador']
    lista_ids = [entregador['id'] for entregador in entregadores]


    table = Table(title="Editar Entregador")

    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("Telefone")
    table.add_column("Veículo")
    table.add_column("Email")
    table.add_column("Senha")

    

    for  entregador in entregadores:
        table.add_row(
            str(entregador['id']),
            entregador["nome"],
            entregador["telefone"],
            entregador["veiculo"],
            entregador["email"],
            entregador["senha"]
        )
        

    console.print(table)
        
    indice = int(input("Digite o número do entregador que deseja editar: "))
    if indice in lista_ids:
        entregador = entregadores[indice]
        nome = input(f"Digite o novo nome do entregador (deixe em branco para manter '{entregador['nome']}'): ")
        telefone = input(f"Digite o novo telefone do entregador (deixe em branco para manter '{entregador['telefone']}'): ")
        veiculo = input(f"Digite o novo veículo do entregador (deixe em branco para manter '{entregador['veiculo']}'): ")
        email = input(f"Digite o novo email do entregador (deixe em branco para manter '{entregador['email']}'): ")
        senha = input(f"Digite a nova senha do entregador (deixe em branco para manter '{entregador['senha']}'): ")
        
        if nome:
            entregador["nome"] = nome
        if telefone:
            entregador["telefone"] = telefone
        if veiculo:
            entregador["veiculo"] = veiculo
        if email:
            entregador["email"] = email
        if senha:
            entregador["senha"] = senha
        
        try:
            atualizar_funcionario(entregador)
            console.print("[green]Entregador editado com sucesso![/green]")
        except Exception as E:
            console.print("[red]Entregador nao editado.[/red]")    
    else:
        console.print("[red]Índice inválido. Tente novamente.[/red]")
        

def adicionar_atendente():

    nome = input("Digite o nome do atendente: ")
    telefone = input("Digite o telefone do atendente: ")
    email = input("Digite o email do atendente: ")
    senha = input("Digite a senha do atendente: ")
    
    atendente = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "cargo": "atendente",
        "veiculo": "",
        "senha": senha
        
    }
    
    try:
        adicionar_funcionario(atendente)
        console.print("[green]Atendente adicionado com sucesso![/green]")
    except Exception as E:
        console.print(E)
        console.print("[red]Atendente nao adicionado[/red]")
    

def editar_atendente():
    funcionarios = listar_funcionarios()
    atendentes = [funcionario for funcionario in funcionarios if funcionario['cargo'] == 'atendente']
    lista_ids = [atendente['id'] for atendente in atendentes]

    table = Table(title="Editar Atendente")

    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("Telefone")
    table.add_column("Email")

    for atendente in atendentes:
        table.add_row(
            str(atendente['id']),
            atendente["nome"],
            atendente["telefone"],
            atendente["email"],
            atendente["senha"]

        )
        

    console.print(table)
        
    indice = int(input("Digite o número do atendente que deseja editar: "))
    if indice in lista_ids:
        atendente = atendentes[indice]
        nome = input(f"Digite o novo nome do atendente (deixe em branco para manter '{atendente['nome']}'): ")
        telefone = input(f"Digite o novo telefone do atendente (deixe em branco para manter '{atendente['telefone']}'): ")
        email = input(f"Digite o novo email do atendente (deixe em branco para manter '{atendente['email']}'): ")
        senha = input(f"Digite a nova senha do atendente (deixe em branco para manter '{atendente['senha']}'): ")
        
        if nome:
            atendente["nome"] = nome
        if telefone:
            atendente["telefone"] = telefone
        if email:
            atendente["email"] = email
        if senha:
            atendente["senha"] = senha
        try:
            atualizar_funcionario(atendente)
            console.print("[green]Atendente editado com sucesso![/green]")
        except Exception as E:
            console.print(f"[red]Atendente nao atualizado: {E}[/red]")
    else:
        print("Índice inválido. Tente novamente.")
    
    
def listar_entregadores():
    funcionarios = listar_funcionarios()
    entregadores = [funcionario for funcionario in funcionarios if funcionario['cargo'] == 'entregador']
    lista_ids = [entregador['id'] for entregador in entregadores]
    table = Table(title="Entregadores")

    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("Telefone")
    table.add_column("Veículo")
    table.add_column("Email")
    table.add_column("Senha")


    for entregador in entregadores:
        table.add_row(
            str(entregador['id']),
            entregador["nome"],
            entregador["telefone"],
            entregador["veiculo"],
            entregador['email'],
            entregador['senha']
        )

    console.print(table)


def listar_atendentes():
    funcionarios = listar_funcionarios()
    atendentes = [funcionario for funcionario in funcionarios if funcionario['cargo'] == 'atendente']
    
    table = Table(title="Atendentes")

    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("Telefone")
    table.add_column("Email")
    table.add_column("Senha")

    for i, atendente in enumerate(atendentes):
        table.add_row(
            str(i),
            atendente["nome"],
            atendente["telefone"],
            atendente["email"],
            atendente['senha']
        )

    console.print(table)


def listar_clientes():
    clientes = listar_clientes_banco()
    table = Table(title="Atendentes")

    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("Telefone")
    table.add_column("Email")
    table.add_column("Endereco")

    for cliente in clientes:
        table.add_row(
            str(cliente['id']),
            cliente["nome"],
            cliente["telefone"],
            cliente["email"],
            cliente['endereco']
        )

    console.print(table)
        

    
       

    
    