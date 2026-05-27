from bd.pedidos import adicionar_pedido,atualizar_pedido,buscar_pedido,deletar_pedido,listar_pedidos,inserir_itens_pedido
from bd.produtos import listar_produtos
from bd.clientes import listar_clientes_banco,adicionar_cliente
from bd.funcionarios import listar_funcionarios
from cliente import cadastrar_cliente
import datetime
from rich.console import Console
from rich.table import Table

console = Console()

def NovoPedido() -> None:
    global produtos, clientes, entregadores
    
    produtos = listar_produtos()
    clientes = listar_clientes_banco()
    funcionarios = listar_funcionarios()
    entregadores = [f for f in funcionarios if f['cargo'] == 'entregador']
    
    pedido = {
        "cliente_id": None,
        "entregador_id": None,
        "itens": [],
        "valor_total": 0.0,
        "status": "Em andamento",
        "forma_pagamento": None
    }
    

    cliente = None    
    while True:
        cliente_email = input("Digite o email do cliente para este pedido: ").lower()
        
        if clientes:
            cliente = next((c for c in clientes if c["email"] == cliente_email), None)
        
        if cliente:
            break 
            
        console.print("[yellow]Cliente nao encontrado. [green]cadastre-o.[/green][/yellow]")
        cliente = cadastrar_cliente(email_ja_existente=cliente_email)  
        
        if cliente and "id" in cliente:
            break  
        else:
            console.print("[red]Falha ao cadastrar cliente. Tente novamente.[/red]")

    pedido["cliente_id"] = cliente["id"]
    

    endereco_loop = True
    while endereco_loop:
        console.print(f"endereco registrado: [blue]{cliente['endereco']}[/blue].")
        console.print(f"[yellow]Para Confirmar Digite [green]0[/green], Para Alterar Digite [red]1[/red]: [/yellow]")
        
        escolha_endereco = input("")
        if escolha_endereco == "1":
            novo_endereco = input("Digite o novo endereco do cliente: ")
            cliente["endereco"] = novo_endereco
            endereco_loop = False
        elif escolha_endereco == "0":
            console.print("Endereco confirmado")
            endereco_loop = False
        else:
            console.print("[red]Opcao invalida[/red]")

        
    table = Table(title="Produtos Disponiveis", show_lines=True)
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Nome", style="green")
    table.add_column("Preco", justify="right", style="yellow")
    table.add_column("Descricao", style="white")

    if not produtos:
        console.print("[yellow]Nenhum produto cadastrado![/yellow]")
        return 
    else:
        for i, produto in enumerate(produtos):
            table.add_row(
                str(i),
                produto.get("nome", "N/A"),
                f"R$ {produto.get('preco', 0):.2f}",
                produto.get("descricao", "N/A")
            )

    console.print(table)
    console.print(f"[dim]Total de produtos: {len(produtos)}[/dim]")
    try:

        itens = input("Digite os numeros dos produtos que deseja adicionar ao pedido (separados por espaco): ")
        itens = itens.replace(",", " ").split()
        for item in itens:
            item = int(item)

            if item < 0 or item >= len(produtos):
                console.print(f"[red]Produto {item} nao existe![/red]")
                return

            pedido["itens"].append({
                "produto_id": produtos[item]["id"],
                "preco": produtos[item]["preco"]
            })

            pedido["valor_total"] += float(produtos[item]["preco"])
        console.print(f"[blue]Valor total do pedido: [green]R$ {pedido['valor_total']:.2f}[/green][/blue]")
        

        table = Table(title="Entregadores")
        table.add_column("ID", justify="right")
        table.add_column("Nome")

        for i, entregador in enumerate(entregadores):
            table.add_row(str(i), entregador["nome"])

        console.print(table)
        entregador_id = int(input("Digite o numero do entregador para este pedido: "))
        pedido["entregador_id"] = entregadores[entregador_id]["id"]
        

        console.print("[yellow]Digite a forma de pagamento[/yellow]")
        console.print("(Cartao [green]0[/green], Dinheiro [yellow]1[/yellow], Pix [red]2[/red] Voucher [blue]3[/blue]): ")
        lista_pagamentos = ["0","1","2"]
        escolha_forma_pagamento = input()
        if escolha_forma_pagamento not in lista_pagamentos:
            console.print("[red]Opçao Invalida ! [/red]")
            return
        id_to_pagamento = {
            "1": "Dinheiro",
            "2": "Pix",
            "3": "Voucher",
            "4": "Cartao Debito",
            "5": "Cartao Credito"
        }

        if escolha_forma_pagamento == "0":
            loop_debito_credito = True
            while loop_debito_credito:
                console.print("[yellow]Digite [green]0[/green] para Debito e [green]1[/green] para Credito [/yellow]")
                escolha_debito_credito = input()
                if escolha_debito_credito not in ["0", "1"]:
                    console.print("[red]Opcao Invalida ! [/red]")
                    return
                pagamento_debito_ou_credito = None
                if escolha_debito_credito == "0":
                    pagamento_debito_ou_credito = "4"
                else: 
                    pagamento_debito_ou_credito = "5"

                pedido["forma_pagamento"] = id_to_pagamento[pagamento_debito_ou_credito]
                loop_debito_credito = False

        if not pagamento_debito_ou_credito:   
            pedido["forma_pagamento"] = id_to_pagamento[escolha_forma_pagamento]
        

        pedido_id = adicionar_pedido(pedido)
        inserir_itens_pedido(pedido_id, pedido["itens"])
        console.print("[green]Pedido criado com sucesso![/green]")
    except Exception as e:
        console.print(f"[red]Erro ao salvar pedido: {e}[/red]")



def ListarPedidos() -> None:
    ListaPedidos = listar_pedidos()
    
    def criar_tabela(status):
        table = Table(title=f"Pedidos - {status}")
        table.add_column("ID", justify="right")
        table.add_column("Cliente")
        table.add_column("Itens")
        table.add_column("Entregador")
        table.add_column("Valor", justify="right")

        for pedido in ListaPedidos:
            if pedido.get("status") == status:
                itens = pedido.get("itens", "N/A")
                if not itens:
                    itens = "N/A"
                table.add_row(
                    str(pedido.get("id", "N/A")),
                    pedido.get("cliente", "N/A"),
                    itens,
                    pedido.get("entregador", "N/A"),
                    f"R$ {pedido.get('valor_total', 0):.2f}"
                )
        return table

    for status in ["Em andamento", "Em entrega", "Finalizado", "Cancelado"]:
        console.print(criar_tabela(status))

def editar_pedido():
    pedidos = listar_pedidos()
    if not pedidos:
        console.print("[yellow]Nenhum pedido cadastrado.[/yellow]")
        return
        
    lista_ids = [pedido['id'] for pedido in pedidos]
    table = Table(title="Editar Pedido")

    table.add_column("ID", justify="right")
    table.add_column("Cliente")
    table.add_column("Entregador")
    table.add_column("Itens")
    table.add_column("Total")
    table.add_column("Status")
    table.add_column("Pagamento")

    for pedido in pedidos:
        itens = pedido["itens"] if pedido["itens"] else "Nenhum"
        cliente = pedido["cliente"] if pedido["cliente"] else "Não informado"
        entregador = pedido["entregador"] if pedido["entregador"] else "Não atribuído"
        
        table.add_row(
            str(pedido['id']),
            cliente,
            entregador,
            itens,
            f"R$ {pedido['valor_total']:.2f}",
            pedido["status"],
            pedido["forma_pagamento"]
        )

    console.print(table)

    try:
        indice = int(input("Digite o ID do pedido que deseja editar: "))
        pedido_a_editar = {}
        
        if indice in lista_ids:
            for pedido in pedidos:
                if pedido['id'] == indice:
                    pedido_a_editar = pedido

            entregador_id = input(f"Novo ID do entregador (atual '{pedido_a_editar['entregador_id']}') (Pressione Enter para manter o atual): ")
            valor_total = input(f"Novo valor total (atual R$ {pedido_a_editar['valor_total']:.2f}) (Pressione Enter para manter o atual): ")
            status = input(f"Novo status (atual '{pedido_a_editar['status']}') (Pressione Enter para manter o atual): ")
            forma_pagamento = input(f"Nova forma de pagamento (atual '{pedido_a_editar['forma_pagamento']}') (Pressione Enter para manter o atual): ")
            
            if entregador_id:
                pedido_a_editar["entregador_id"] = int(entregador_id)
            if valor_total:
                pedido_a_editar["valor_total"] = float(valor_total)
            if status:
                pedido_a_editar["status"] = status
            if forma_pagamento:
                pedido_a_editar["forma_pagamento"] = forma_pagamento
            
            atualizar_pedido(pedido_atualizado=pedido_a_editar)
            console.print("[green]Pedido editado com sucesso![/green]")
        else:
            console.print("[red]ID inválido. Tente novamente.[/red]")
            
    except Exception as E:
        console.print(f"[red]Pedido não editado: {E}[/red]")


def AtualizarStatus()->None:
    from bd.pedidos import atualizar_status_pedido
    
    ListaPedidos = listar_pedidos()
    lista_ids = [pedido['id'] for pedido in ListaPedidos]
    
    if not ListaPedidos:
        console.print("[yellow]Nenhum pedido encontrado.[/yellow]")
        return
    
    table = Table(title="Pedidos")

    table.add_column("ID")
    table.add_column("Cliente")
    table.add_column("Itens")
    table.add_column("Entregador")
    table.add_column("Valor")
    table.add_column("Status")
    table.add_column("Tempo Decorrido")

    for  pedido in (ListaPedidos):
        itens = pedido.get("itens", "N/A")
        if not itens:
            itens = "N/A"
        table.add_row(
            str(pedido["id"]),
            pedido.get("cliente", "N/A"),
            itens,
            pedido.get("entregador", "N/A"),
            f"R$ {pedido.get('valor_total', 0):.2f}",
            pedido.get("status", "N/A"),
            str(datetime.datetime.now() - pedido['data_hora'])

        )

    console.print(table)
    
    try:
        indice = int(input("\nDigite o numero do pedido para alterar status: "))
        if indice not in lista_ids:
            console.print("[red]Indice invalido![/red]")
            return
        for pedido in ListaPedidos:
            if pedido['id'] == indice:
                pedido_selecionado = pedido
        current_status = pedido_selecionado['status']
        
        console.print("\n[bold]Selecione o novo status:[/bold]")
        console.print("1 - Em andamento")
        console.print("2 - Em entrega")
        console.print("3 - Finalizado")
        console.print("4 - Cancelado")
        
        opcao_status = input("Digite a opcao: ")
        
        status_opcoes = {
            "1": "Em andamento",
            "2": "Em entrega",
            "3": "Finalizado",
            "4": "Cancelado"
        }
        
        novo_status = status_opcoes.get(opcao_status)
        
        if novo_status:
            console.print(f"\nStatus atual: [yellow]{current_status}[/yellow]")
            console.print(f"Novo status: [green]{novo_status}[/green]")
            
            confirmar = input("Confirmar alteracao? (s/n): ")
            if confirmar.lower() == 's':
                atualizar_status_pedido(pedido_selecionado['id'], novo_status)
                console.print(f"[green]Status alterado para '{novo_status}' com sucesso![/green]")
            else:
                console.print("[yellow]Alteracao cancelada.[/yellow]")
        else:
            console.print("[red]Opcao invalida![/red]")
            
    except ValueError:
        console.print("[red]Por favor, digite um numero valido.[/red]")

def excluir_pedido_tela():
    try:
        pedidos = listar_pedidos()
    except Exception as E:
        console.print(f"[red]Erro ao buscar pedidos no banco: {E}[/red]")
        return
        
    if not pedidos:
        console.print("[yellow]Nenhum pedido cadastrado no sistema.[/yellow]")
        return
        
    table = Table(title="Excluir Pedido")
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Cliente", style="white")
    table.add_column("Entregador", style="white")
    table.add_column("Valor Total", justify="right", style="green")
    table.add_column("Status", style="yellow")
    table.add_column("Data/Hora", style="white")
    
    for p in pedidos:
        cliente_nome = p.get('cliente') or "Não informado"
        entregador_nome = p.get('entregador') or "Sem entregador"
        valor = p.get('valor_total') or 0.0
        data_hora = str(p.get('data_hora'))
        
        table.add_row(
            str(p['id']), 
            cliente_nome, 
            entregador_nome, 
            f"R$ {valor:.2f}", 
            p['status'], 
            data_hora
        )
    console.print(table)
    
    try:
        id_excluir = int(input("Digite o ID do pedido que deseja DELETAR: "))
        lista_ids = [p['id'] for p in pedidos]
        
        if id_excluir in lista_ids:
            confirmar = input(f"Tem certeza que deseja apagar o pedido #{id_excluir} e todos os seus itens? (s/n): ")
            
            if confirmar.lower() == 's':
                deletar_pedido(id_excluir)
                console.print("[green]Pedido e todos os seus itens associados foram removidos com sucesso![/green]")
            else:
                console.print("[yellow]Operação cancelada pelo usuário.[/yellow]")
        else:
            console.print("[red]ID inválido. Operação cancelada.[/red]")
            
    except ValueError:
        console.print("[red]Entrada inválida! Digite apenas o número do ID do pedido.[/red]")
    except Exception as E:
        console.print(f"[red]Erro ao remover pedido: {E}[/red]")

