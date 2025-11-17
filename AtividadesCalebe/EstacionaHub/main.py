import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from auth import AuthSystem
from admin import AdminSystem
from operador import OperatorSystem
from reports import ReportSystem

def main():
    auth = AuthSystem()

    while True:
        if not auth.usuario_atual:
            if not auth.login():
                continue

        if auth.is_admin():
            AdminSystem.menu()
            opcao = input("Escolha: ")

            if opcao == "1":
                AdminSystem.cadastrar_usuario()
            elif opcao == "2":
                AdminSystem.configurar_estacionamento()
            elif opcao == "3":
                AdminSystem.ver_relatorios()
            elif opcao == "4":
                auth.logout()
        else:
            OperatorSystem.menu()
            opcao = input("Escolha: ")

            if opcao == "1":
                OperatorSystem.registrar_entrada()
            elif opcao == "2":
                OperatorSystem.registrar_saida()
            elif opcao == "3":
                OperatorSystem.abrir_caixa()
            elif opcao == "4":
                OperatorSystem.fechar_caixa()
            elif opcao == "5":
                OperatorSystem.ver_status()
            elif opcao == "6":
                auth.logout()


if __name__ == "__main__":
    main()
