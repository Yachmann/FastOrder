#Codigo em relação ao cliente


def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    
    cliente = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "endereco": endereco
    }
    
    print("Cliente cadastrado com sucesso!")
    return cliente
    


