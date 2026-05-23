from bd.pedidos import adicionar_pedido,atualizar_pedido,buscar_pedido,deletar_pedido,listar_pedidos,inserir_itens_pedido
from bd.produtos import listar_produtos
from bd.clientes import listar_clientes_banco,adicionar_cliente
from bd.funcionarios import listar_funcionarios
from cliente import cadastrar_cliente
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
    
    # --- BLOCO DO CLIENTE CORRIGIDO e SIMPLIFICADO ---
    cliente = None    
    while True:
        cliente_email = input("Digite o email do cliente para este pedido: ")
        
        if clientes:
            cliente = next((c for c in clientes if c["email"] == cliente_email), None)
        
        if cliente:
            break  # Encontrou o cliente cadastrado, sai do loop de busca
            
        print("Cliente nao encontrado. cadastre-o.")
        cliente = cadastrar_cliente()  # Recebe o dicionário do novo cliente com o ID populado
        
        if cliente and "id" in cliente:
            break  # Cadastro realizado com sucesso, sai do loop de busca
        else:
            print("Falha ao cadastrar cliente. Tente novamente.")

    # Vincula o ID do cliente (seja o antigo ou o recém-criado) ao pedido
    pedido["cliente_id"] = cliente["id"]
    
    # Confirmação / Alteração do endereço do cliente
    endereco_loop = True
    while endereco_loop:
        escolha_endereco = input(f"endereco registrado: {cliente['endereco']}. para confirmar digite 0, para alterar digite 1: ")
        if escolha_endereco == "1":
            novo_endereco = input("Digite o novo endereco do cliente: ")
            cliente["endereco"] = novo_endereco
            endereco_loop = False
        elif escolha_endereco == "0":
            print("Endereco confirmado")
            endereco_loop = False
        else:
            print("Opcao invalida")
    # --- FIM DO BLOCO DO CLIENTE ---
        
    # --- MONTAGEM DA TABELA DE PRODUTOS ---
    table = Table(title="Produtos Disponiveis", show_lines=True)
    table.add_column("ID", justify="right", style="cyan")
    table.add_column("Nome", style="green")
    table.add_column("Preco", justify="right", style="yellow")
    table.add_column("Descricao", style="white")

    if not produtos:
        console.print("[yellow]Nenhum produto cadastrado![/yellow]")
        return  # Encerra a função se não houver produtos para vender
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
    
    # Seleção dos itens
    itens = input("Digite os numeros dos produtos que deseja adicionar ao pedido (separados por espaco): ")
    itens = itens.replace(",", " ").split()
    for item in itens:
        item = int(item)
        pedido["itens"].append({
            "produto_id": produtos[item]["id"],
            "preco": produtos[item]["preco"]
        })
        pedido["valor_total"] += float(produtos[item]["preco"])
    print(f"Valor total do pedido: R$ {pedido['valor_total']:.2f}")
    
    # --- SELEÇÃO DO ENTREGADOR ---
    table = Table(title="Entregadores")
    table.add_column("ID", justify="right")
    table.add_column("Nome")

    for i, entregador in enumerate(entregadores):
        table.add_row(str(i), entregador["nome"])

    console.print(table)
    entregador_id = int(input("Digite o numero do entregador para este pedido: "))
    pedido["entregador_id"] = entregadores[entregador_id]["id"]
    
    # Forma de pagamento
    pedido["forma_pagamento"] = input("Digite a forma de pagamento (Cartao, Dinheiro, Pix): ")
    
    # --- PERSISTÊNCIA NO BANCO DE DADOS ---
    try:
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
        
def AtualizarStatus()->None:
    from bd.pedidos import atualizar_status_pedido
    
    ListaPedidos = listar_pedidos()
    
    if not ListaPedidos:
        console.print("[yellow]Nenhum pedido encontrado.[/yellow]")
        return
    
    table = Table(title="Pedidos")

    table.add_column("Index", justify="right")
    table.add_column("ID")
    table.add_column("Cliente")
    table.add_column("Itens")
    table.add_column("Entregador")
    table.add_column("Valor")
    table.add_column("Status")

    for i, pedido in enumerate(ListaPedidos):
        itens = pedido.get("itens", "N/A")
        if not itens:
            itens = "N/A"
        table.add_row(
            str(i),
            str(pedido["id"]),
            pedido.get("cliente", "N/A"),
            itens,
            pedido.get("entregador", "N/A"),
            f"R$ {pedido.get('valor_total', 0):.2f}",
            pedido.get("status", "N/A")
        )

    console.print(table)
    
    try:
        indice = int(input("\nDigite o numero do pedido para alterar status: "))
        if indice < 0 or indice >= len(ListaPedidos):
            console.print("[red]Indice invalido![/red]")
            return
        
        pedido_selecionado = ListaPedidos[indice]
        current_status = pedido_selecionado.get("status", "")
        
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
