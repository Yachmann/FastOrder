from typing import Literal
from rich.console import Console
from bd.funcionarios import verificar_funcionario
console = Console()
def verificar_acesso()->Literal['admin','atendente','entregador',None]:
    print("======================================")
    print("       BEM VINDO A FASTORDER  ")
    print("======================================")
    print("")
    print("1- Acessar como Administrador")
    print("2- Acessar como Atendente")
    print("3- Acessar como Entregador")
    print("")
    print("======================================")

    opçao = int(input("Escolha a opção de acesso: "))

    if opçao == 1:
        return 'admin'
    elif opçao == 2:
        loop_login = True
        while loop_login:
            
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            funcionario = verificar_funcionario(email = email, senha = senha, cargo = 'atendente')
            if funcionario:
                console.print("[green]Autenticado com Sucesso[/green]")
                return 'atendente'
            else:
                console.print("[red]Autenticacao Falhou[/red]")

    elif opçao == 3:
        loop_login = True
        while loop_login:
            
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            funcionario = verificar_funcionario(email = email, senha = senha, cargo = 'entregador')
            if funcionario:
                console.print("[green]Autenticado com Sucesso[/green]")
                return 'entregador'
            else:
                console.print("[red]Autenticacao Falhou[/red]")

        
    else:
        console.print("[red]Opção inválida. Tente novamente.[/red]")
        return None