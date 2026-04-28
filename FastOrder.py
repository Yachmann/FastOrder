
ListaPedidos = {} #listar pedidos
valores = [] # valores
Cancelados = {} # só pedidos cancelados
Combos =[
     {"nome": "abobobbesd", "preco": 00.00},
     {"nome": "Combo Clássico", "preco": 25.90},
     {"nome": "Combo Duplo", "preco": 32.90},
     {"nome": "Combo Econômico", "preco": 21.90},
     {"nome": "Combo Família", "preco": 59.90}
]


def NovoPedido():
    global Combos, ListaPedidos
    return

def ListarPeidos():
    return
        
def AtualizarStatus():
    return

def VerExtrato():
    return

def PedidosCancelados():
    return



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
        print("1 - Combo Clássico")
        print("   Hambúrguer + Batata pequena + Refrigerante lata")
        print("   Preço: R$ 25.90\n")

        print("2 - Combo Duplo")
        print("   Hambúrguer duplo + Batata média + Refrigerante 500ml")
        print("   Preço: R$ 32.90\n")

        print("3 - Combo Econômico")
        print("   Hambúrguer simples + Batata pequena + Suco")
        print("   Preço: R$ 21.90\n")

        print("4 - Combo Família")
        print("   2 Hambúrgueres + 2 Batatas grandes + Refrigerante 2L")
        print("   Preço: R$ 59.90\n")
        
        NomePedido = int(input("digite o numero do pedido:"))

    elif(opçao == 2):
        print("======================================")
        print("          LISTAR PEDIDOS              ")
        print("======================================")
        ListaPedidos()
       

    elif(opçao == 3):
        print("======================================")
        print("          ATUALIZAR STATUS            ")
        print("======================================")

    elif(opçao == 4):
        print("======================================")
        print("          EXTRATO DO DIA              ")
        print("======================================")

    elif(opçao == 5):
        print("======================================")
        print("         PEDIDOS CANCELADOS           ")
        print("======================================")
    
   


    