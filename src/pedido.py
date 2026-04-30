from bd.pedidos import adicionar_pedido,atualizar_pedido,buscar_pedido,deletar_pedido,listar_pedidos,inserir_itens_pedido
from bd.produtos import listar_produtos
from bd.clientes import listar_clientes_banco,adicionar_cliente
from bd.funcionarios import listar_funcionarios
import time
from cliente import cadastrar_cliente
from rich.console import Console
from rich.table import Table

console = Console()

ListaPedidos = listar_pedidos()
produtos = listar_produtos()
funcionarios = listar_funcionarios()
clientes = listar_clientes_banco()
entregadores = []
for funcionario in funcionarios:
    if funcionario['cargo'] == 'entregador':
        entregadores.append(funcionario)


def NovoPedido()->None:
    pedido = {
    "cliente_id": None,
    "entregador_id": None,
    "itens": [],
    "valor_total": 0.0,
    "status": "Em andamento",
    "forma_pagamento": None,
    "data_hora": None
}
    loop = True
    while loop:
        cliente_encontrado = False
        cliente = None    
        while not cliente_encontrado:
                if not cliente:
                    cliente_email = input("Digite o email do cliente para este pedido: ")
                    cliente = next((c for c in clientes if c["email"] == cliente_email), None)
                
                if cliente:
                    pedido["cliente_id"] = cliente["id"]
                    endereco_loop = True
                    while endereco_loop:
                        escolha_endereco = input(f"endereço registrado: {cliente['endereco']}. para confirmar digite 0, para alterar digite 1:")
                        if escolha_endereco == "1":
                            novo_endereco = input("Digite o novo endereço do cliente: ")
                            cliente["endereco"] = novo_endereco
                            endereco_loop = False
                        elif escolha_endereco != "0":
                            print("Opção inválida")
                        else:
                            print("Endereço confirmado")
                            endereco_loop = False
        
                    cliente_encontrado = True
                else:
                    print("Cliente não encontrado. cadstre-o.")
                    cliente = cadastrar_cliente()  
                    
        table = Table(title="Produtos Disponíveis")

        table.add_column("ID", justify="right")
        table.add_column("Nome")
        table.add_column("Preço", justify="right")
        table.add_column("Descrição")

        for i, produto in enumerate(produtos):
            table.add_row(
                str(i),
                produto["nome"],
                f"R$ {produto['preco']:.2f}",
                produto["descricao"]
            )

        console.print(table)
        itens = input("Digite os números dos produtos que deseja adicionar ao pedido (separados por vírgula ou espaço): ")
        itens = itens.replace(",", " ").split()
        for item in itens:
            item = int(item)
            pedido["itens"].append({
                "produto_id": produtos[item]["id"],
                "preco": produtos[item]["preco"]
            })
            pedido["valor_total"] += produtos[item]["preco"]
        print(f"Valor total do pedido: R$ {pedido['valor_total']:.2f}")
        
        table = Table(title="Entregadores")
        table.add_column("ID", justify="right")
        table.add_column("Nome")

        for i, entregador in enumerate(entregadores):
            table.add_row(str(i), entregador["nome"])

        console.print(table)
        entregador_id = int(input("Digite o número do entregador para este pedido: "))
        pedido["entregador_id"] = entregadores[entregador_id]["id"]
        pedido["forma_pagamento"] = input("Digite a forma de pagamento (Cartão, Dinheiro, Pix): ")
        pedido["data_hora"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            pedido_id = adicionar_pedido(pedido)  

            inserir_itens_pedido(pedido_id, pedido["itens"])

            console.print("[green]Pedido criado com sucesso![/green]")

        except Exception as e:
            console.print(e)
        
        loop = False
                

def ListarPedidos() -> None:
    def criar_tabela(status):
        table = Table(title=f"Pedidos - {status}")
        table.add_column("ID", justify="right")
        table.add_column("Cliente")
        table.add_column("Itens")
        table.add_column("Entregador")
        table.add_column("Valor", justify="right")

        for pedido in ListaPedidos:
            if pedido["status"] == status:
                itens = ", ".join(item["nome"] for item in pedido["itens"])
                table.add_row(
                    str(pedido["id"]),
                    pedido["cliente"],
                    itens,
                    pedido["entregador"],
                    f"R$ {pedido['valor_total']:.2f}"
                )
        return table

    for status in ["Em andamento", "Em entrega", "Finalizado", "Cancelado"]:
        console.print(criar_tabela(status))
        
def AtualizarStatus()->None:
    lista_ids = []
    table = Table(title="Pedidos")

    table.add_column("Index", justify="right")
    table.add_column("ID")
    table.add_column("Cliente")
    table.add_column("Itens")
    table.add_column("Entregador")
    table.add_column("Valor")
    table.add_column("Status")

    lista_ids = []

    for i, pedido in enumerate(ListaPedidos):
        itens = ", ".join(item["nome"] for item in pedido["itens"])
        table.add_row(
            str(i),
            str(pedido["id"]),
            pedido["cliente"],
            itens,
            pedido["entregador"],
            f"R$ {pedido['valor_total']:.2f}",
            pedido["status"]
        )
        lista_ids.append(i)

    console.print(table)