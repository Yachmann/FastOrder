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
from restaurante import (adicionar_produto_, adicionar_atendente, adicionar_entregador, 
                         editar_produto, editar_entregador, editar_atendente,
                         listar_produtos, listar_entregadores, listar_atendentes,
                         listar_clientes, VerExtrato, PedidosCancelados)
from funcionario import alterar_status_entrega, entregador_lista_pedidos

# Variável global para armazenar o ID do entregador logado
entregador_id_logado = None

# LOOP PRINCIPAL DO SISTEMA (Gerencia a troca de usuários)
while True:
    tipo_acesso, id = verificar_acesso()

    # Se a função retornar None ou falso (caso queira criar uma opção de fechar o sistema no login)
    if not tipo_acesso:
        print("[yellow]Encerrando o FastOrder...[/yellow]")
        break

    # =========================================================================
    # Acesso de Administrador
    # =========================================================================
    if tipo_acesso == 'admin':
        print("[green]Acesso de Administrador concedido.[/green]")
        opçao = None
        while True:  # Loop infinito controlado internamente
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
                print("         LISTAR CLIENTES              ")
                print("======================================")
                listar_clientes()
            elif opçao == 0:
                print("[yellow]Saindo da sessão de Administrador...[/yellow]")
                break  # Quebra o menu do admin e volta para a checagem de acesso global
        
    # =========================================================================
    # Acesso de Atendente    
    # =========================================================================
    elif tipo_acesso == 'atendente':
        console.print("[green]Acesso de Atendente concedido.[/green]")
        opçao = None
        while True:
            print("======================================")
            print("       BEM VINDO A FASTORDER  ")
            print("======================================")
            print("")
            print("1- Novo Pedido")
            print("2- Listar Pedidos")
            print("3- Atualizar Status")
            print("4- Ver Extrato do dia")
            print("5- Ver Pedidos Cancelados")
            print("0- Sair" )
            print("")
            print("======================================")

            opçao = int(input("Escolha a ação que deseja realizar:"))

            if opçao == 1:
                print("======================================")
                print("            NOVO PEDIDO               ")
                print("======================================")
                NovoPedido()
            elif opçao == 2:
                print("======================================")
                print("          LISTAR PEDIDOS              ")
                print("======================================")
                ListarPedidos()
            elif opçao == 3:
                print("======================================")
                print("          ATUALIZAR STATUS            ")
                print("======================================")
                AtualizarStatus()
            elif opçao == 4:
                print("======================================")
                print("          EXTRATO DO DIA              ")
                print("======================================")
                VerExtrato()
            elif opçao == 5:
                print("======================================")
                print("         PEDIDOS CANCELADOS           ")
                print("======================================")
                PedidosCancelados()
            elif opçao == 0:
                print("[yellow]Saindo da sessão de Atendente...[/yellow]")
                break  # Quebra o menu do atendente e volta para a checagem de acesso global

    # =========================================================================
    # Acesso de Entregador    
    # =========================================================================
    elif tipo_acesso == 'entregador':
        entregador_id_logado = id 
        console.print(f"[green]Acesso de Entregador concedido ao Entregador com ID: {entregador_id_logado}[/green]")
        opcao = None
        while True:
            print("======================================")
            print("       BEM VINDO A FASTORDER  ")
            print("======================================")
            print("")
            print("1- Listar Pedidos")
            print("2- Alterar status pedido")
            print("0- Sair")
            print("")

            opcao = input("Escolha a ação que deseja realizar:")

            if opcao == "1":
                print("======================================")
                print("            LISTAR PEDIDOS               ")
                print("======================================")
                if entregador_id_logado:
                    entregador_lista_pedidos(entregador_id_logado=entregador_id_logado)
            elif opcao == "2":
                print("======================================")
                print("          ALTERAR STATUS DE UM PEDIDO    ")
                print("======================================")
                if entregador_id_logado:
                    alterar_status_entrega(entregador_id_logado)
                else:
                    console.print("[red]Faça login primeiro.[/red]")
            elif opcao == "0":
                print("[yellow]Saindo da sessão de Entregador...[/yellow]")
                entregador_id_logado = None  # Limpa o ID logado por segurança
                break 

