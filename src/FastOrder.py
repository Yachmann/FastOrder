from bd.connect import conectar_db
from bd.setup import create_tables
from rich import print
from rich.console import Console
from rich.table import Table
import time
console = Console()

# PRIMEIRO: Conectar e criar tabelas
conectar_db()
create_tables()

# DEPOIS: Importar os módulos que dependem do banco
from pedido import NovoPedido, ListarPedidos, AtualizarStatus
from verificacao_acesso import verificar_acesso
from restaurante import adicionar_produto_, adicionar_atendente, adicionar_entregador, editar_produto, editar_entregador, editar_atendente,listar_produtos, listar_entregadores, listar_atendentes,listar_clientes
from funcionario import alterar_status_entrega,listar_pedidos_entregador
from bd.pedidos import listar_pedidos_por_status, listar_pedidos_por_data


# Variável global para armazenar o ID do entregador logado
entregador_id_logado = None


        
def VerExtrato():
    """
    Exibe o extrato do dia com resumo de vendas.
    """
    data_atual = time.strftime("%Y-%m-%d", time.localtime())
    pedidos_dia = listar_pedidos_por_data(data_atual)
    
    if not pedidos_dia:
        console.print("[yellow]Nenhum pedido encontrado hoje.[/yellow]")
        return
    
    # Filtrar pedidos finalizados
    pedidos_finalizados = [p for p in pedidos_dia if p.get('status') == 'Finalizado']
    
    if not pedidos_finalizados:
        console.print("[yellow]Nenhum pedido finalizado hoje.[/yellow]")
        return
    
    # Calcular total
    total_receita = sum(p.get('valor_total', 0) for p in pedidos_finalizados)
    total_pedidos = len(pedidos_finalizados)
    
    # Criar tabela de extrato
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
    """
    Exibe a lista de pedidos cancelados.
    """
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


tipo_acesso = verificar_acesso()


# Acesso de Administrador
if tipo_acesso == 'admin':
    print("Acesso de Administrador concedido.")
    opçao = None
    while opçao != 0 :
        print("======================================")
        print("       BEM VINDO A FASTORDER  ")
        print("======================================")
        print("")
        print("1- Novo Produto")
        print("2- Listar Produtos")
        print("3- Editar Produto")
        print("4- Adicionar Entregador")
        print("5- Editar Entregador")
        print("6- Listar Entregadores")
        print("7- Adicionar Atendente")
        print("8- Editar Atendente")
        print("9- Listar Atendentes")
        print("10- Listar Clientes")
        print("0- Sair")
        print("")
        print("======================================")

        opçao = int(input("Escolha a ação que deseja realizar:"))
        
        if opçao == 1:
            print("======================================")
            print("          NOVO PRODUTO               ")
            print("======================================")
            adicionar_produto_()
        elif opçao == 2:
            print("======================================")
            print("         LISTAR PRODUTOS              ")
            print("======================================")
            listar_produtos()
        elif opçao == 3:
            print("======================================")
            print("          EDITAR PRODUTO              ")
            print("======================================")
            editar_produto()
        elif opçao == 4:
            print("======================================")
            print("        ADICIONAR ENTREGADOR          ")
            print("======================================")
            adicionar_entregador()
        elif opçao == 5:
            print("======================================")
            print("         EDITAR ENTREGADOR            ")
            print("======================================")
            editar_entregador()
        elif opçao == 6:
            print("======================================")
            print("        LISTAR ENTREGADORES          ")
            print("======================================")
            listar_entregadores()
        elif opçao == 7:
            print("======================================")
            print("         ADICIONAR ATENDENTE            ")
            print("======================================")
            adicionar_atendente()
                    
        elif opçao == 8:
            print("======================================")
            print("         EDITAR ATENDENTE            ")
            print("======================================")
            editar_atendente()
                    
        elif opçao == 9:
            print("======================================")
            print("         LISTAR ATENDENTES            ")
            print("======================================")
            listar_atendentes()
        elif opçao == 10:
            print("======================================")
            print("         LISTAR ATENDENTES            ")
            print("======================================")
            listar_clientes()
    
    
    
# Acesso de Atendente    
elif tipo_acesso == 'atendente':
    console.print("[green]Acesso de Atendente concedido.[/green]")
    
    opçao = None
    while opçao != 0 :
        print("======================================")
        print("       BEM VINDO A FASTORDER  ")
        print("======================================")
        print("")
        print("1- Novo Pedido")
        print("2- Listar Pedidos")
        print("3- Atualizar Status")
        print("4- Ver Extrato do dia")
        print("5- Ver Pedidos Cancelados")
        print("0- Sair")
        print("")
        print("======================================")

        opçao = int(input("Escolha a ação que deseja realizar:"))

        if(opçao == 1):
            print("======================================")
            print("            NOVO PEDIDO               ")
            print("======================================")
            NovoPedido()

        elif(opçao == 2):
            print("======================================")
            print("          LISTAR PEDIDOS              ")
            print("======================================")
            ListarPedidos()
        

        elif(opçao == 3):
            print("======================================")
            print("          ATUALIZAR STATUS            ")
            print("======================================")
            AtualizarStatus()

        elif(opçao == 4):
            print("======================================")
            print("          EXTRATO DO DIA              ")
            print("======================================")
            VerExtrato()

        elif(opçao == 5):
            print("======================================")
            print("         PEDIDOS CANCELADOS           ")
            print("======================================")
            PedidosCancelados()
            
            
            
            
# Acesso de Cliente            
elif tipo_acesso == 'cliente':
    console.print("[green]Acesso de Cliente concedido.[/green]")
    
    
    
# Acesso de Entregador    
elif tipo_acesso == 'entregador':
    console.print("[green]Acesso de Entregador concedido.[/green]")
    
    # Obter o ID do entregador logado
    from bd.funcionarios import verificar_funcionario
    
    # Precisamos obter o entregador_id através da verificação
    # O login já foi feito em verificacao_acesso, precisamos pegar o ID
    # Vamos fazer uma verificação simplificada usando a função já existente
    # Precisei ajustar o fluxo para capturar o entregador_id
    
    # Como não temos acesso direto ao ID aqui, vamos usar uma abordagem diferente
    # O atendente pode passar o ID ou podemos modificar a função
    
    # Por enquanto, vamos pedir para digitar o ID ou buscar automaticamente
    # A solução mais adequada é modificar verifying para retornar o objeto
    # Por ora, vamos usar uma função temporária
    entregador_id_logado = None  # Será preenchido através de input
    
    # Como não temos acesso ao ID do entregador que fez login, 
    # vamos verificar se já existe uma variável global ou pedir para digitar
    # A solução ideal seria modificar verificacao_acesso para retornar o objeto
    
    # Por enquanto, vamos usar uma abordagem alternativa:
    # Listar os funcionários entregadores e pedir para selecionar
    from bd.funcionarios import listar_funcionarios
    entregadores = [f for f in listar_funcionarios() if f['cargo'] == 'entregador']
    
    if entregadores:
        console.print("[bold]Selecione seu ID de entregador:[/bold]")
        table = Table(title="Entregadores")
        table.add_column("Index", justify="right")
        table.add_column("ID")
        table.add_column("Nome")
        
        for i, ent in enumerate(entregadores):
            table.add_row(str(i), str(ent['id']), ent['nome'])
        
        console.print(table)
        
        try:
            idx = int(input("Digite o número do seu perfil: "))
            if 0 <= idx < len(entregadores):
                entregador_id_logado = entregadores[idx]['id']
                console.print(f"[green]Entregador ID: {entregador_id_logado}[/green]")
            else:
                console.print("[red]Índice inválido![/red]")
        except ValueError:
            console.print("[red]Valor inválido![/red]")
    
    opcao = None
    while opcao != 0:
        print("======================================")
        print("       BEM VINDO A FASTORDER  ")
        print("======================================")
        print("")
        print("1- Listar Pedidos")
        print("2- Alterar status pedido")
        print("0- Sair")
        print("")

        opçao = int(input("Escolha a ação que deseja realizar:"))

        if(opçao == 1):
            print("======================================")
            print("            LISTAR PEDIDOS               ")
            print("======================================")
            if entregador_id_logado:
                from bd.pedidos import listar_pedidos_por_entregador
                pedidos = listar_pedidos_por_entregador(entregador_id_logado)
                
                if pedidos:
                    table = Table(title="Meus Pedidos")
                    table.add_column("ID")
                    table.add_column("Cliente")
                    table.add_column("Valor")
                    table.add_column("Status")
                    
                    for p in pedidos:
                        table.add_row(
                            str(p.get('id', 'N/A')),
                            p.get('cliente', 'N/A'),
                            f"R$ {p.get('valor_total', 0):.2f}",
                            p.get('status', 'N/A')
                        )
                    console.print(table)
                else:
                    console.print("[yellow]Nenhum pedido encontrado.[/yellow]")

        elif(opçao == 2):
            print("======================================")
            print("          ALTERAR STATUS DE UM PEDIDO    ")
            print("======================================")
            if entregador_id_logado:
                alterar_status_entrega(entregador_id_logado)
            else:
                console.print("[red]Faça login primeiro.[/red]")




    
   


    