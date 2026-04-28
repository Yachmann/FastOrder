from typing import Literal
def verificar_acesso()->Literal['admin','atendente','cliente','entregador',None]:
    print("======================================")
    print("       BEM VINDO A FASTORDER  ")
    print("======================================")
    print("")
    print("1- Acessar como Administrador")
    print("2- Acessar como Atendente")
    print("3- Acessar como Cliente")
    print("4- Acessar como Entregador")
    print("")
    print("======================================")

    opçao = int(input("Escolha a opção de acesso: "))

    if opçao == 1:
        return 'admin'
    elif opçao == 2:
        return 'atendente'
    elif opçao == 3:
        return 'cliente'
    elif opçao == 4:
        return 'entregador'
    else:
        print("Opção inválida. Tente novamente.")
        return None