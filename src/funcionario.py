from bd.funcionarios import adicionar_funcionario,atualizar_funcionario,buscar_funcionario,deletar_funcionario,listar_funcionarios
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

    
def alterar_status_entrega(pedido):
    pass