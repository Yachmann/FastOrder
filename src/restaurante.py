from rich.console import Console
from rich.table import Table
from bd.funcionarios import deletar_funcionario, listar_funcionarios,adicionar_funcionario,atualizar_funcionario
from bd.produtos import listar_produtos as listar_produtos_banco, adicionar_produto, atualizar_produto,deletar_produto
from bd.clientes import listar_clientes_banco,deletar_cliente
from bd.pedidos import listar_pedidos_por_status, listar_pedidos_por_data
import time

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
        loop_sim_ou_nao = True
        while loop_sim_ou_nao:
             opcao = input("Deseja adicionar outro produto? (s/n): ")
             if opcao.lower() == 's':
                 loop_sim_ou_nao = False
             elif opcao.lower() == 'n':
                 loop_sim_ou_nao = False
             else:
                 console.print("[yellow]Opção inválida. Digite 's' para sim ou 'n' para não.[/yellow]")

def editar_produto():
    produtos = listar_produtos()
    if not produtos:
        console.print("[yellow]Nenhum produto cadastrado.[/yellow]")
        return
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

    try:
        indice = int(input("Digite o número do produto que deseja editar: "))
        produto_a_editar = {}
        if indice in lista_ids:
            for produto in produtos:
                if produto['id'] == indice:
                    produto_a_editar = produto

            nome = input(f"Digite o novo nome do produto (deixe em branco para manter '{produto_a_editar['nome']}'): ")
            preco = input(f"Digite o novo preço do produto (deixe em branco para manter R$ {produto_a_editar['preco']:.2f}): ")
            descricao = input(f"Digite a nova descrição do produto (deixe em branco para manter '{produto_a_editar['descricao']}'): ")
            status = input(f"Digite o novo status do produto (1 para disponível, 0 para indisponível, deixe em branco para manter {'Disponível' if produto_a_editar['status'] == 1 else 'Indisponível'}): ")
            
            if nome:
                produto_a_editar["nome"] = nome
            if preco:
                produto_a_editar["preco"] = float(preco)
            if descricao:
                produto_a_editar["descricao"] = descricao
            if status:
                produto_a_editar["status"] = int(status)
            
            
                atualizar_produto(produto=produto_a_editar)
                console.print("[green]Produto editado com sucesso![green]")
        else:
            console.print("[red]Índice inválido. Tente novamente.[/red]")
    except Exception as E:
        console.print("[red]Produto nao editado[/red]")
        
def listar_produtos():
    produtos = listar_produtos_banco()

    table = Table(title="Produtos")

    table.add_column("ID", justify="right")
    table.add_column("Nome")
    table.add_column("Preço", justify="right")
    table.add_column("Descrição")
    table.add_column("Status")

    for produto in produtos:
        status = "Disponivel" if produto["status"] == 1 else "Indisponivel"

        table.add_row(
            str(produto['id']),
            produto["nome"],
            f"R$ {produto['preco']:.2f}",
            produto["descricao"],
            status
        )

    console.print(table)

    return produtos

def excluir_produto_tela():
    produtos = listar_produtos()
    if not produtos:
        return
    lista_ids = [produto['id'] for produto in produtos]
    try:
        id_excluir = int(input("Digite o ID do produto que deseja DELETAR: "))
        if id_excluir in lista_ids:
            deletar_produto(id_excluir)
            console.print("[green]Produto deletado com sucesso (e removido dos itens de pedidos)![/green]")
        else:
            console.print("[red]ID inválido.[/red]")
    except Exception as E:
        console.print(f"[red]Erro ao deletar produto: {E}[/red]")
        
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
        "email" : email.lower(),
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
    try:
        indice = int(input("Digite o número do entregador que deseja editar: "))
        entregador_a_editar = {}
        if indice in lista_ids:
            for entregador in entregadores:
                if entregador['id'] == indice:
                    entregador_a_editar = entregador
            nome = input(f"Digite o novo nome do entregador (deixe em branco para manter '{entregador_a_editar['nome']}'): ")
            telefone = input(f"Digite o novo telefone do entregador (deixe em branco para manter '{entregador_a_editar['telefone']}'): ")
            veiculo = input(f"Digite o novo veículo do entregador (deixe em branco para manter '{entregador_a_editar['veiculo']}'): ")
            email = input(f"Digite o novo email do entregador (deixe em branco para manter '{entregador_a_editar['email']}'): ")
            senha = input(f"Digite a nova senha do entregador (deixe em branco para manter '{entregador_a_editar['senha']}'): ")
            
            if nome:
                entregador_a_editar["nome"] = nome
            if telefone:
                entregador_a_editar["telefone"] = telefone
            if veiculo:
                entregador_a_editar["veiculo"] = veiculo
            if email:
                entregador_a_editar["email"] = email
            if senha:
                entregador_a_editar["senha"] = senha
            
        
                atualizar_funcionario(entregador_a_editar)
                console.print("[green]Entregador editado com sucesso![/green]")
        else:
            console.print("[red]Índice inválido. Tente novamente.[/red]")
    except Exception as E:
        console.print("[red]Entregador nao editado.[/red]")    
        

def adicionar_atendente():

    nome = input("Digite o nome do atendente: ")
    telefone = input("Digite o telefone do atendente: ")
    email = input("Digite o email do atendente: ")
    senha = input("Digite a senha do atendente: ")
    
    atendente = {
        "nome": nome,
        "telefone": telefone,
        "email": email.lower(),
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
        
    try:
        indice = int(input("Digite o número do atendente que deseja editar: "))
        if indice in lista_ids:
            atendente_a_editar = {}
            for atendente in atendentes:
                if atendente['id'] == indice:
                    atendente_a_editar = atendente

            nome = input(f"Digite o novo nome do atendente (deixe em branco para manter '{atendente_a_editar['nome']}'): ")
            telefone = input(f"Digite o novo telefone do atendente (deixe em branco para manter '{atendente_a_editar['telefone']}'): ")
            email = input(f"Digite o novo email do atendente (deixe em branco para manter '{atendente_a_editar['email']}'): ")
            senha = input(f"Digite a nova senha do atendente (deixe em branco para manter '{atendente_a_editar['senha']}'): ")
            
            if nome:
                atendente_a_editar["nome"] = nome
            if telefone:
                atendente_a_editar["telefone"] = telefone
            if email:
                atendente_a_editar["email"] = email
            if senha:
                atendente_a_editar["senha"] = senha
            
                atualizar_funcionario(atendente_a_editar)
                console.print("[green]Atendente editado com sucesso![/green]")
        else:
            console.print("[red]Índice inválido. Tente novamente.[/red]")
    except Exception as E:
        console.print(f"[red]Atendente nao atualizado: {E}[/red]")
    
    
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

    for atendente in (atendentes):
        table.add_row(
            str(atendente['id']),
            atendente["nome"],
            atendente["telefone"],
            atendente["email"],
            atendente['senha']
        )

    console.print(table)

def excluir_funcionario_tela():
    try:
        funcionarios = listar_funcionarios()
    except Exception as E:
        console.print(f"[red]Erro ao buscar funcionários no banco: {E}[/red]")
        return
        
    if not funcionarios:
        console.print("[yellow]Nenhum funcionário cadastrado no sistema.[/yellow]")
        return
        
    table = Table(title="Excluir Funcionário")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Nome", style="white")
    table.add_column("Cargo", style="yellow")
    table.add_column("Email", style="white")
    
    for f in funcionarios:
        table.add_row(
            str(f['id']), 
            f['nome'], 
            f['cargo'].upper(), 
            f['email']
        )
    console.print(table)
    
    try:
        id_excluir = int(input("Digite o ID do funcionário que deseja DELETAR: "))
        lista_ids = [f['id'] for f in funcionarios]
        
        if id_excluir in lista_ids:
            deletar_funcionario(id_excluir)
            console.print("[green]Funcionário removido com sucesso! Histórico de pedidos preservado.[/green]")
        else:
            console.print("[red]ID inválido. Operação cancelada.[/red]")
            
    except ValueError:
        console.print("[red]Entrada inválida! Digite apenas números.[/red]")
    except Exception as E:
        console.print(f"[red]Erro ao deletar funcionário: {E}[/red]")


def listar_clientes():
    clientes = listar_clientes_banco()
    table = Table(title="Clientes")

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
        
def excluir_cliente_tela():
    # 1. Busca os clientes cadastrados para listar na tela
    try:
        clientes = listar_clientes_banco()
    except Exception as E:
        console.print(f"[red]Erro ao conectar com o banco de dados: {E}[/red]")
        return
        
    if not clientes:
        console.print("[yellow]Nenhum cliente cadastrado no sistema.[/yellow]")
        return
        
    # 2. Monta a tabela visual organizada
    table = Table(title="Excluir Cliente")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Nome", style="white")
    table.add_column("Telefone", style="white")
    table.add_column("Email", style="white")
    
    for c in clientes:
        table.add_row(
            str(c['id']), 
            c['nome'], 
            c['telefone'], 
            c['email']
        )
    console.print(table)
    
    # 3. Executa a deleção com validação
    try:
        id_excluir = int(input("Digite o ID do cliente que deseja DELETAR: "))
        lista_ids = [c['id'] for c in clientes]
        
        if id_excluir in lista_ids:
            # Chama a função de delete do seu arquivo bd.clientes
            deletar_cliente(id_excluir)
            console.print("[green]Cliente removido com sucesso! Todos os seus pedidos foram apagados automaticamente pelo banco.[/green]")
        else:
            console.print("[red]ID inválido. Operação cancelada.[/red]")
            
    except ValueError:
        console.print("[red]Entrada inválida! Digite apenas números para o ID.[/red]")
    except Exception as E:
        console.print(f"[red]Erro ao deletar cliente: {E}[/red]")

    
       

    
        
def VerExtrato():

    data_atual = time.strftime("%Y-%m-%d", time.localtime())
    pedidos_dia = listar_pedidos_por_data(data_atual)
    
    if not pedidos_dia:
        console.print("[yellow]Nenhum pedido encontrado hoje.[/yellow]")
        return
    

    pedidos_finalizados = [p for p in pedidos_dia if p.get('status') == 'Finalizado']
    
    if not pedidos_finalizados:
        console.print("[yellow]Nenhum pedido finalizado hoje.[/yellow]")
        return
    

    total_receita = sum(p.get('valor_total', 0) for p in pedidos_finalizados)
    total_pedidos = len(pedidos_finalizados)
    

    table = Table(title=f"Extrato do Dia - {data_atual}")
    table.add_column("ID Pedido", justify="right")
    table.add_column("Cliente")
    table.add_column("Forma Pagamento")
    table.add_column("Valor", justify="right")
    
    for pedido in pedidos_finalizados:
        table.add_row(
            str(pedido.get('id', 'N/A')),
            pedido.get('cliente', 'N/A'),
            pedido.get('forma_pagamento', 'N/A'),
            f"R$ {pedido.get('valor_total', 0):.2f}"
        )
    
    console.print(table)
    console.print(f"\n[bold green]Total de Pedidos: {total_pedidos}[/bold green]")
    console.print(f"[bold green]Receita Total: R$ {total_receita:.2f}[/bold green]")


def PedidosCancelados():

    pedidos_cancelados = listar_pedidos_por_status("Cancelado")
    
    if not pedidos_cancelados:
        console.print("[yellow]Nenhum pedido cancelado.[/yellow]")
        return
    
    table = Table(title="Pedidos Cancelados")
    table.add_column("ID Pedido", justify="right")
    table.add_column("Cliente")
    table.add_column("Entregador")
    table.add_column("Valor", justify="right")
    table.add_column("Data/Hora")
    
    for pedido in pedidos_cancelados:
        table.add_row(
            str(pedido.get('id', 'N/A')),
            pedido.get('cliente', 'N/A'),
            pedido.get('entregador', 'N/A'),
            f"R$ {pedido.get('valor_total', 0):.2f}",
            str(pedido.get('data_hora', 'N/A'))
        )
    
    console.print(table)
