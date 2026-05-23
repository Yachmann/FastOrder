from typing import Literal
from rich.console import Console
from bd.funcionarios import verificar_funcionario
from dotenv import load_dotenv
import os

load_dotenv()

adminkey = os.getenv(key='ADMIN-KEY')
admin_email = os.getenv('ADMIN-LOGIN')

console = Console()
def verificar_acesso():
    print("======================================")
    print("       BEM VINDO A FASTORDER  ")
    print("======================================")
    print("")
    print("1- Acessar como Administrador")
    print("2- Acessar como Atendente")
    print("3- Acessar como Entregador")
    print("")
    print("======================================")

    opçao = input("Escolha a opção de acesso: ")

    if opçao == "1":
        loop_login = True
        while loop_login:
            email = input('Digite o Email de ADMIN: ')
            senha = input('Digite a Senha do ADMIN: ')
            if email == admin_email and senha == adminkey:
                console.print("[green]Autenticado com Sucesso[/green]")
                loop_login = False
                return 'admin',0
            else:
                console.print("[red]Autenticacao Falhou[/red]")

    elif opçao == "2":
        loop_login = True
        while loop_login:
            
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            funcionario = verificar_funcionario(email = email, senha = senha, cargo = 'atendente')
            if funcionario:
                console.print("[green]Autenticado com Sucesso[/green]")
                return 'atendente',funcionario['id']
            else:
                console.print("[red]Autenticacao Falhou[/red]")

    elif opçao == "3":
        loop_login = True
        while loop_login:
            
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            funcionario = verificar_funcionario(email = email, senha = senha, cargo = 'entregador')
            if funcionario:
                console.print("[green]Autenticado com Sucesso[/green]")
                
                return 'entregador',funcionario['id']
            else:
                console.print("[red]Autenticacao Falhou[/red]")

        
    else:
        console.print("[red]Opção inválida. Tente novamente.[/red]")
        return None,None