from banco import Banco
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n" + "="*50)
    print("          SISTEMA BANCÁRIO")
    print("="*50)
    print("1. Cadastrar conta")
    print("2. Consultar saldo")
    print("3. Consultar extrato")
    print("4. Sacar dinheiro")
    print("5. Depositar dinheiro")
    print("6. Listar contas cadastradas")
    print("7. Sair")
    print("="*50)

def cadastrar_conta(banco):
    limpar_tela()
    print("=== CADASTRO DE CONTA ===")
    

    agencia = input("Agência: ")
    senha = input("Senha: ")
    
    try:
        saldo_inicial = float(input("Saldo inicial (R$): "))
        if saldo_inicial < 0:
            print("Erro: Saldo inicial não pode ser negativo!")
            input("Pressione Enter para continuar...")
            return
    except ValueError:
        print("Erro: Digite um valor válido para o saldo!")
        input("Pressione Enter para continuar...")
        return
    
    conta = banco.cadastrar_conta(nome, agencia, senha, saldo_inicial)
    print(f"\nConta criada com sucesso!")
    print(f"Titular: {conta.nome}")
    print(f"Agência: {conta.agencia}")
    print(f"Conta: {conta.numero_conta}")
    print(f"Saldo inicial: R$ {saldo_inicial:.2f}")
    
    input("\nPressione Enter para continuar...")

def consultar_saldo(banco):
    limpar_tela()
    print("=== CONSULTAR SALDO ===")
    
    agencia = input("Agência: ")
    numero_conta = input("Número da conta: ")
    senha = input("Senha: ")
    
    conta = banco.encontrar_conta(agencia, numero_conta)
    if conta:
        sucesso, resultado = conta.consultar_saldo(agencia, numero_conta, senha)
        if sucesso:
            print(f"\nSaldo atual: R$ {resultado:.2f}")
        else:
            print(f"Erro: {resultado}")
    else:
        print("Conta não encontrada!")
    
    input("\nPressione Enter para continuar...")

def consultar_extrato(banco):
    limpar_tela()
    print("=== CONSULTAR EXTRATO ===")
    
    agencia = input("Agência: ")
    numero_conta = input("Número da conta: ")
    senha = input("Senha: ")
    
    conta = banco.encontrar_conta(agencia, numero_conta)
    if conta:
        sucesso, extrato = conta.consultar_extrato(agencia, numero_conta, senha)
        if sucesso:
            print(f"\nExtrato da conta {numero_conta} - Agência {agencia}")
            print(f"Titular: {conta.nome}")
            print("-" * 60)
            print(f"{'Data':<20} {'Descrição':<15} {'Valor':>10}")
            print("-" * 60)
            
            for movimento in extrato:
                sinal = "+" if movimento["tipo"] == "+" else "-"
                print(f"{movimento['data']:<20} {movimento['descrição']:<15} {sinal}R$ {movimento['valor']:>7.2f}")
            
            # Mostrar saldo atual
            _, saldo = conta.consultar_saldo(agencia, numero_conta, senha)
            print("-" * 60)
            print(f"{'SALDO ATUAL:':<35} R$ {saldo:>7.2f}")
        else:
            print(f"Erro: {extrato}")
    else:
        print("Conta não encontrada!")
    
    input("\nPressione Enter para continuar...")

def sacar_dinheiro(banco):
    limpar_tela()
    print("=== SAQUE ===")
    
    agencia = input("Agência: ")
    numero_conta = input("Número da conta: ")
    senha = input("Senha: ")
    
    try:
        valor = float(input("Valor do saque (R$): "))
        if valor <= 0:
            print("Erro: Valor do saque deve ser positivo!")
            input("Pressione Enter para continuar...")
            return
    except ValueError:
        print("Erro: Digite um valor válido!")
        input("Pressione Enter para continuar...")
        return
    
    conta = banco.encontrar_conta(agencia, numero_conta)
    if conta:
        sucesso, mensagem = conta.sacar(agencia, numero_conta, senha, valor)
        print(mensagem)
    else:
        print("Conta não encontrada!")
    
    input("\nPressione Enter para continuar...")

def depositar_dinheiro(banco):
    limpar_tela()
    print("=== DEPÓSITO ===")
    
    agencia = input("Agência: ")
    numero_conta = input("Número da conta: ")
    
    try:
        valor = float(input("Valor do depósito (R$): "))
        if valor <= 0:
            print("Erro: Valor do depósito deve ser positivo!")
            input("Pressione Enter para continuar...")
            return
    except ValueError:
        print("Erro: Digite um valor válido!")
        input("Pressione Enter para continuar...")
        return
    
    conta = banco.encontrar_conta(agencia, numero_conta)
    if conta:
        sucesso, mensagem = conta.depositar(agencia, numero_conta, valor)
        print(mensagem)
    else:
        print("Conta não encontrada!")
    
    input("\nPressione Enter para continuar...")

def listar_contas(banco):
    limpar_tela()
    print("=== CONTAS CADASTRADAS ===")
    
    contas = banco.listar_contas()
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(conta)
    
    input("\nPressione Enter para continuar...")

def main():
    banco = Banco()
    
    while True:
        limpar_tela()
        mostrar_menu()
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            cadastrar_conta(banco)
        elif opcao == "2":
            consultar_saldo(banco)
        elif opcao == "3":
            consultar_extrato(banco)
        elif opcao == "4":
            sacar_dinheiro(banco)
        elif opcao == "5":
            depositar_dinheiro(banco)
        elif opcao == "6":
            listar_contas(banco)
        elif opcao == "7":
            print("\nObrigado por usar nosso sistema bancário!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()