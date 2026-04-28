import time
from cliente import cadastrar_cliente

def NovoPedido(ListaPedidos:list, clientes:list, produtos:list, entregadores:list)->None:
    id_pedido = len(ListaPedidos) + 1
    pedido = {"id": id_pedido, "itens": [], "status" : "Em andamento", "cliente": None, "entregador": None, "valor_total": 0.00, "forma_pagamento": None, "data_hora": None}
    loop = True
    while loop:
        cliente_encontrado = False
        cliente = None    
        while not cliente_encontrado:
                if not cliente:
                    cliente_email = input("Digite o email do cliente para este pedido: ")
                    cliente = next((c for c in clientes if c["email"] == cliente_email), None)
                
                if cliente:
                    pedido["cliente"] = cliente["nome"]
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
                    
        print("Produtos Disponíveis:")
        for i, produto in enumerate(produtos):
            print(f"{i} - {produto['nome']} - R$ {produto['preco']:.2f}")
            print(f"   Descrição: {produto['descricao']}")
        itens = input("Digite os números dos produtos que deseja adicionar ao pedido (separados por vírgula ou espaço): ")
        itens = itens.replace(",", " ").split()
        for item in itens:
            item = int(item)
            pedido["itens"].append({
                "nome": produtos[item]["nome"], 
                 "preco": produtos[item]["preco"]
                 })
            pedido["valor_total"] += produtos[item]["preco"]
        print(f"Valor total do pedido: R$ {pedido['valor_total']:.2f}")
        
        for i, entregador in enumerate(entregadores):
            print(f"{i} - {entregador['nome']}")
        entregador_id = int(input("Digite o número do entregador para este pedido: "))
        pedido["entregador"] = entregadores[entregador_id]["nome"]
        pedido["forma_pagamento"] = input("Digite a forma de pagamento (Cartão, Dinheiro, Pix): ")
        pedido["data_hora"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ListaPedidos.append(pedido)
        print(f"Pedido {id_pedido} criado com sucesso!")
        loop = False
                

def ListarPedidos(ListaPedidos:list)->None:
    print("Pedidos em andamento:")
    for pedido in ListaPedidos:
        if pedido["status"] == "Em andamento":
            print(f" ID: {pedido['id']} ---- Cliente: {pedido['cliente']} ---- Itens: {[item['nome'] for item in pedido['itens']]} ----  Entregador: {pedido['entregador']} ----  Valor Total: R$ {pedido['valor_total']:.2f}")
    print("Pedidos finalizados:")
    for pedido in ListaPedidos:
        if pedido["status"] == "Finalizado":
            print(f"ID: {pedido['id']}, Cliente: {pedido['cliente']}, Itens: {[item['nome'] for item in pedido['itens']]}, Entregador: {pedido['entregador']}")
    print("Pedidos cancelados:")
    for pedido in ListaPedidos:
        if pedido["status"] == "Cancelado":
            print(f"ID: {pedido['id']}, Cliente: {pedido['cliente']}, Itens: {[item['nome'] for item in pedido['itens']]}, Entregador: {pedido['entregador']}")
    print("Pedidos em entrega:")
    for pedido in ListaPedidos:
        if pedido["status"] == "Em entrega":
            print(f"ID: {pedido['id']}, Cliente: {pedido['cliente']}, Itens: {[item['nome'] for item in pedido['itens']]}, Entregador: {pedido['entregador']}")
    print("\n\n\n\n\n\n\n\n\n")
        
def AtualizarStatus(ListaPedidos:list)->None:
    lista_ids = []
    for i, pedido in enumerate(ListaPedidos):
        print(f"{i} - ID: {pedido['id']} ---- Cliente: {pedido['cliente']} ---- Itens: {[item['nome'] for item in pedido['itens']]} ----  Entregador: {pedido['entregador']} ----  Valor Total: R$ {pedido['valor_total']:.2f} ---- Status: {pedido['status']}")
        lista_ids.append(i)
    pedido_id = int(input("Digite o número do pedido para atualizar o status: "))
    if pedido_id not in lista_ids:
        print("ID de pedido inválido.")
        return
    novo_status = input("Digite o novo status para este pedido (Em andamento, Em entrega, Finalizado, Cancelado): ")
    if novo_status in ["Em andamento", "Em entrega", "Finalizado", "Cancelado"]:
        ListaPedidos[pedido_id]["status"] = novo_status
        print(f"Status do pedido {ListaPedidos[pedido_id]['id']} atualizado para {novo_status}!")
    else:
        print("Status inválido. Status não atualizado.")