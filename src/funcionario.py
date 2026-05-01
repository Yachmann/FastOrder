from bd.funcionarios import adicionar_funcionario,atualizar_funcionario,buscar_funcionario,deletar_funcionario,listar_funcionarios
from bd.pedidos import listar_pedidos_por_entregador, atualizar_status_pedido, listar_pedidos_por_status
from rich.console import Console
from rich.table import Table

console = Console()


def listar_pedidos_entregador(ListaPedidos:list,entregador_id:int)->None:
    table = Table(title='Pedidos a Ser entregue')
    table.add_column('ID',style='orange')
    table.add_column('CLIENTE')
    table.add_column('VALOR TOTAL')
    table.add_column('ITENS')
    table.add_column('ENDERECO')
    table.add_column('STATUS')

    for pedido in ListaPedidos:
        table.add_row(
            str(pedido['id']),
            pedido['cliente'],
            str(pedido['valor_total']),
            pedido['itens'],
            pedido['endereco'],
            pedido['status']
        )
    console.print(table)

    
def alterar_status_entrega(entregador_id: int) -> None:
    """
    Permite ao entregador alterar o status de seus pedidos.
    Fluxo: Em andamento -> Em entrega -> Finalizado
    """
    # Listar pedidos do entregador que estão em andamento ou em entrega
    pedidos_andamento = listar_pedidos_por_entregador(entregador_id)
    
    if not pedidos_andamento:
        console.print("[yellow]Você não tem pedidos pendentes.[/yellow]")
        return
    
    # Filtrar apenas pedidos que podem ser alterados pelo entregador
    pedidos_validos = [p for p in pedidos_andamento if p['status'] in ['Em andamento', 'Em entrega']]
    
    if not pedidos_validos:
        console.print("[yellow]Não há pedidos para alterar status.[/yellow]")
        return
    
    # Mostrar tabela de pedidos
    console.print("\n[bold cyan]Seus Pedidos Pendentes:[/bold cyan]")
    table = Table(title="Pedidos para Alterar Status")
    table.add_column("Index", justify="right", style="cyan")
    table.add_column("ID", justify="right")
    table.add_column("Cliente")
    table.add_column("Valor")
    table.add_column("Status")

    for i, pedido in enumerate(pedidos_validos):
        table.add_row(
            str(i),
            str(pedido['id']),
            pedido.get('cliente', 'N/A'),
            f"R$ {pedido['valor_total']:.2f}",
            pedido['status']
        )
    console.print(table)
    
    # Selecionar pedido
    try:
        indice = int(input("\nDigite o número do pedido para alterar status: "))
        if indice < 0 or indice >= len(pedidos_validos):
            console.print("[red]Índice inválido![/red]")
            return
        
        pedido_selecionado = pedidos_validos[indice]
        current_status = pedido_selecionado['status']
        
        # Definir próximo status baseado no status atual
        if current_status == "Em andamento":
            novo_status = "Em entrega"
        elif current_status == "Em entrega":
            novo_status = "Finalizado"
        else:
            console.print("[red]Status atual não pode ser alterado.[/red]")
            return
        
        console.print(f"\nStatus atual: [yellow]{current_status}[/yellow]")
        console.print(f"Novo status: [green]{novo_status}[/green]")
        
        confirmar = input("Confirmar alteração? (s/n): ")
        if confirmar.lower() == 's':
            atualizar_status_pedido(pedido_selecionado['id'], novo_status)
            console.print(f"[green]Status alterado para '{novo_status}' com sucesso![/green]")
        else:
            console.print("[yellow]Alteração cancelada.[/yellow]")
            
    except ValueError:
        console.print("[red]Por favor, digite um número válido.[/red]")
