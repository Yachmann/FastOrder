combos =[
     {"nome": "abobobbesd", "preco": 00.00},
     {"nome": "Combo Clássico", "preco": 25.90},
     {"nome": "Combo Duplo", "preco": 32.90},
     {"nome": "Combo Econômico", "preco": 21.90},
     {"nome": "Combo Família", "preco": 59.90}
]
produtos = [
    {"nome": "Hambúrguer", "preco": 15.00, "descricao": "Hambúrguer suculento com carne de alta qualidade, servido em um pão macio e acompanhado de alface, tomate e molho especial.", "status": 1},
]

entregadores = [{"nome": "João", "telefone": "123456789", "veiculo": "Moto"}] #entregadores

atendentes = [{"nome": "Maria", "telefone": "987654321", "email": ""}]



def criar_restaurante(nome, endereco, telefone, email, senha):
    restaurante = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "senha": senha
    }
    return restaurante

def editar_restaurante(restaurante, nome=None, endereco=None, telefone=None, email=None, senha=None):
    if nome:
        restaurante["nome"] = nome
    if endereco:
        restaurante["endereco"] = endereco
    if telefone:
        restaurante["telefone"] = telefone
    if email:
        restaurante["email"] = email
    if senha:
        restaurante["senha"] = senha
    return restaurante

def adicionar_produto():
    concluido = False
    while not concluido:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        descricao = input("Digite a descrição do produto: ")
        status = int(input("Digite o status do produto (1 para disponível, 0 para indisponível): "))
        
        produto = {
            "nome": nome,
            "preco": preco,
            "descricao": descricao,
            "status": status
        }
        
        produtos.append(produto)
        print("Produto adicionado com sucesso!")
        
        opcao = input("Deseja adicionar outro produto? (s/n): ")
        if opcao.lower() != 's':
            concluido = True

def editar_produto():
    lista_ids = []
    for i, produto in enumerate(produtos):
        print(f"{i} - {produto['nome']} - R$ {produto['preco']:.2f} - {produto['descricao']} - {'Disponível' if produto['status'] == 1 else 'Indisponível'}")
        lista_ids.append(i)
    indice = int(input("Digite o número do produto que deseja editar: "))
    if indice in lista_ids:
        produto = produtos[indice]
        nome = input(f"Digite o novo nome do produto (deixe em branco para manter '{produto['nome']}'): ")
        preco = input(f"Digite o novo preço do produto (deixe em branco para manter R$ {produto['preco']:.2f}): ")
        descricao = input(f"Digite a nova descrição do produto (deixe em branco para manter '{produto['descricao']}'): ")
        status = input(f"Digite o novo status do produto (1 para disponível, 0 para indisponível, deixe em branco para manter {'Disponível' if produto['status'] == 1 else 'Indisponível'}): ")
        
        if nome:
            produto["nome"] = nome
        if preco:
            produto["preco"] = float(preco)
        if descricao:
            produto["descricao"] = descricao
        if status:
            produto["status"] = int(status)
        
        print("Produto editado com sucesso!")
    else:
        print("Índice inválido. Tente novamente.")
        
def listar_produtos():
    print("Produtos disponíveis:")
    for i, produto in enumerate(produtos):
        print(f"{i} - {produto['nome']} - R$ {produto['preco']:.2f} - {produto['descricao']} - {'Disponível' if produto['status'] == 1 else 'Indisponível'}")
        
def adicionar_entregador():
    nome = input("Digite o nome do entregador: ")
    telefone = input("Digite o telefone do entregador: ")
    veiculo = input("Digite o veículo do entregador: ")
    
    entregador = {
        "nome": nome,
        "telefone": telefone,
        "veiculo": veiculo
    }
    
    entregadores.append(entregador)
    print("Entregador adicionado com sucesso!")



def editar_entregador():
    lista_ids = []
    for i, entregador in enumerate(entregadores):
        print(f"{i} - {entregador['nome']} - {entregador['telefone']} - {entregador['veiculo']}")
        lista_ids.append(i)
        
    indice = int(input("Digite o número do entregador que deseja editar: "))
    if indice in lista_ids:
        entregador = entregadores[indice]
        nome = input(f"Digite o novo nome do entregador (deixe em branco para manter '{entregador['nome']}'): ")
        telefone = input(f"Digite o novo telefone do entregador (deixe em branco para manter '{entregador['telefone']}'): ")
        veiculo = input(f"Digite o novo veículo do entregador (deixe em branco para manter '{entregador['veiculo']}'): ")
        
        if nome:
            entregador["nome"] = nome
        if telefone:
            entregador["telefone"] = telefone
        if veiculo:
            entregador["veiculo"] = veiculo
        
        print("Entregador editado com sucesso!")
    else:
        print("Índice inválido. Tente novamente.")
        

def adicionar_atendente():
    nome = input("Digite o nome do atendente: ")
    telefone = input("Digite o telefone do atendente: ")
    email = input("Digite o email do atendente: ")
    
    atendente = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    
    atendentes.append(atendente)
    print("Atendente adicionado com sucesso!")
    

def editar_atendente():
    lista_ids = []
    for i, atendente in enumerate(atendentes):
        print(f"{i} - {atendente['nome']} - {atendente['telefone']} - {atendente['email']}")
        lista_ids.append(i)
        
    indice = int(input("Digite o número do atendente que deseja editar: "))
    if indice in lista_ids:
        atendente = atendentes[indice]
        nome = input(f"Digite o novo nome do atendente (deixe em branco para manter '{atendente['nome']}'): ")
        telefone = input(f"Digite o novo telefone do atendente (deixe em branco para manter '{atendente['telefone']}'): ")
        email = input(f"Digite o novo email do atendente (deixe em branco para manter '{atendente['email']}'): ")
        
        if nome:
            atendente["nome"] = nome
        if telefone:
            atendente["telefone"] = telefone
        if email:
            atendente["email"] = email
        
        print("Atendente editado com sucesso!")
    else:
        print("Índice inválido. Tente novamente.")
    
    
def listar_entregadores():
    print("Entregadores disponíveis:")
    for i, entregador in enumerate(entregadores):
        print(f"{i} - {entregador['nome']} - {entregador['telefone']} - {entregador['veiculo']}")


def listar_atendentes():
    print("Atendentes disponíveis:")
    for i, atendente in enumerate(atendentes):
        print(f"{i} - {atendente['nome']} - {atendente['telefone']} - {atendente['email']}")
        
        

    
       

    
    