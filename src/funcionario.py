from bd.funcionarios import adicionar_funcionario,atualizar_funcionario,buscar_funcionario,deletar_funcionario,listar_funcionarios
from bd.pedidos import listar_pedidos_por_entregador, atualizar_status_pedido, listar_pedidos_por_status
from rich.console import Console
from rich.table import Table
from bd.pedidos import listar_pedidos_por_entregador
import datetime

console = Console()


def listar_pedidos_entregador(ListaPedidos:list,entregador_id:int)->None:
    table = Table(title='Pedidos a Ser entregue')
    table.add_column('ID',style='orange')
    table.add_column('CLIENTE')
    table.add_column('VALOR TOTAL')
    table.add_column('ITENS')
    table.add_column('ENDERECO')
    table.add_column('STATUS')
    table.add_column('TEMPO DECORRIDO')

    for pedido in ListaPedidos:
        table.add_row(
            str(pedido['id']),
            pedido['cliente'],
            str(pedido['valor_total']),
            pedido['itens'],
            pedido['endereco'],
            pedido['status'],
            str(time.time() - pedido['data_hora'])
        )
    console.print(table)

    
def alterar_status_entrega(entregador_id: int) -> None:
    pedidos_andamento = listar_pedidos_por_entregador(entregador_id)
    if not pedidos_andamento:
        console.print("[yellow]Você não tem pedidos pendentes.[/yellow]")
        return
    
    pedidos_validos = [p for p in pedidos_andamento if p['status'] in ['Em andamento', 'Em entrega']]
    lista_ids = [p['id'] for p in pedidos_andamento if p['status'] in ['Em andamento', 'Em entrega']]

    if not pedidos_validos:
        console.print("[yellow]Não há pedidos para alterar status.[/yellow]")
        return
    
    console.print("\n[bold cyan]Seus Pedidos Pendentes:[/bold cyan]")
    table = Table(title="Pedidos para Alterar Status")
    table.add_column("ID", justify="right")
    table.add_column("Cliente")
    table.add_column("Valor")
    table.add_column("Status")

    for pedido in (pedidos_validos):
        table.add_row(
            str(pedido['id']),
            pedido.get('cliente', 'N/A'),
            f"R$ {pedido['valor_total']:.2f}",
            pedido['status']
        )
    console.print(table)
    

    try:
        indice = int(input("\nDigite o número do pedido para alterar status: "))
        if indice in lista_ids:
            for pedido in pedidos_andamento:
                if pedido['id'] == indice:
                    pedido_selecionado = pedido
                    current_status = pedido_selecionado['status']
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

def entregador_lista_pedidos(entregador_id_logado):
    pedidos = listar_pedidos_por_entregador(entregador_id_logado)
    
    if pedidos:
        table = Table(title="Meus Pedidos")
        table.add_column("ID")
        table.add_column("Cliente")
        table.add_column("Valor")
        table.add_column("Status")
        table.add_column("Tempo Decorrido")
        
        
        for p in pedidos:
            table.add_row(
                str(p.get('id', 'N/A')),
                p.get('cliente', 'N/A'),
                f"R$ {p.get('valor_total', 0):.2f}",
                p.get('status', 'N/A'),
                str(datetime.datetime.now() - p['data_hora'])
            )
        console.print(table)
    else:
        console.print("[yellow]Nenhum pedido encontrado.[/yellow]")