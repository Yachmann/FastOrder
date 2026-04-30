from bd.connect import conectar_db
from bd.setup import create_tables
from pedido import NovoPedido, ListarPedidos, AtualizarStatus
from verificacao_acesso import verificar_acesso
from restaurante import adicionar_produto_, adicionar_atendente, adicionar_entregador, editar_produto, editar_entregador, editar_atendente,listar_produtos, listar_entregadores, listar_atendentes,listar_clientes
from funcionario import alterar_status_entrega,listar_pedidos_entregador
from rich import print
from rich.console import Console
console = Console()



conectar_db()
create_tables()




        
def VerExtrato():
    return

def PedidosCancelados():
    return


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

        elif(opçao == 5):
            print("======================================")
            print("         PEDIDOS CANCELADOS           ")
            print("======================================")
            
            
            
            
# Acesso de Cliente            
elif tipo_acesso == 'cliente':
    console.print("[green]Acesso de Cliente concedido.[/green]")
    
    
    
# Acesso de Entregador    
elif tipo_acesso == 'entregador':
    console.print("[green]Acesso de Entregador concedido.[/green]")

    opcao = None
    while opcao != 0:
        print("======================================")
        print("       BEM VINDO A FASTORDER  ")
        print("======================================")
        print("")
        print("1- Listar Pedidos")
        print("2- Alterar status pedido")

        opçao = int(input("Escolha a ação que deseja realizar:"))

        if(opçao == 1):
            print("======================================")
            print("            LISTAR PEDIDOS               ")
            print("======================================")

        elif(opçao == 2):
            print("======================================")
            print("          ALTERAR STATUS DE UM PEDIDO    ")
            print("======================================")




    
   


    