from produtos import menu_produtos
from clientes import menu_clientes
from orcamentos import menu_orcamentos

def menu_principal():
    while True:
        print("\n======= CONSTRUÇÃO FÁCIL =======")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Clientes")
        print("3. Gerar Orçamentos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_produtos()
        elif opcao == '2':
            menu_clientes()
        elif opcao == '3':
            menu_orcamentos()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu_principal()
