from pedido import NovoPedido, ListarPedidos, AtualizarStatus
from verificacao_acesso import verificar_acesso
from restaurante import produtos, entregadores,adicionar_produto, adicionar_atendente, adicionar_entregador, editar_produto, editar_entregador, editar_atendente,listar_produtos, listar_entregadores, listar_atendentes
from rich import print


clientes = []
ListaPedidos = [] #listar pedidos
Cancelados = {} # só pedidos cancelados



        
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
        print("0- Sair")
        print("")
        print("======================================")

        opçao = int(input("Escolha a ação que deseja realizar:"))
        
        if opçao == 1:
            print("======================================")
            print("          NOVO PRODUTO               ")
            print("======================================")
            adicionar_produto()
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
                    
    
    
    
# Acesso de Atendente    
elif tipo_acesso == 'atendente':
    print("Acesso de Atendente concedido.")
    
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
            NovoPedido(ListaPedidos=ListaPedidos, clientes=clientes, produtos=produtos, entregadores=entregadores)

        elif(opçao == 2):
            print("======================================")
            print("          LISTAR PEDIDOS              ")
            print("======================================")
            ListarPedidos(ListaPedidos=ListaPedidos)
        

        elif(opçao == 3):
            print("======================================")
            print("          ATUALIZAR STATUS            ")
            print("======================================")
            AtualizarStatus(ListaPedidos=ListaPedidos)

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
    print("Acesso de Cliente concedido.")
    
    
    
# Acesso de Entregador    
elif tipo_acesso == 'entregador':
    print("Acesso de Entregador concedido.")


    
   


    