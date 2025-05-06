# Lista principal para armazenar todos os clientes
clientes = []

def cadastrar_cliente():
    print("\n--- Cadastro de Novo Cliente ---")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    telefone = input("Telefone: ")
    agencia = input("Número da agência: ")
    conta = input("Número da conta: ")
    
    # Validação do saldo inicial
    while True:
        try:
            saldo = float(input("Saldo inicial (R$): "))
            if saldo >= 0:
                break
            else:
                print("O saldo inicial não pode ser negativo.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")
    
    # Criando a lista do cliente e adicionando à lista principal
    cliente = [nome, cpf, rg, telefone, agencia, conta, saldo]
    clientes.append(cliente)
    
    print("\n--- Cadastro realizado com sucesso! ---")
    exibir_resumo_cliente(cliente)
    
    return cliente

def exibir_resumo_cliente(cliente):
    print("\n--- Resumo do Cliente ---")
    print(f"Nome: {cliente[0]}")
    print(f"CPF: {cliente[1]}")
    print(f"Agência: {cliente[4]} | Conta: {cliente[5]}")
    print(f"Saldo atual: R$ {cliente[6]:.2f}")

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar novo cliente")
        print("2 - Acessar cliente existente")
        print("3 - Listar todos os clientes")
        print("4 - Sair do sistema")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            if not clientes:
                print("\nNenhum cliente cadastrado ainda.")
            else:
                acessar_cliente()
        elif opcao == "3":
            listar_clientes()
        elif opcao == "4":
            print("\nEncerrando o sistema bancário...")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção de 1 a 4.")

def acessar_cliente():
    while True:
        print("\n--- Acessar Cliente ---")
        cpf_busca = input("Digite o CPF do cliente (ou 'voltar' para retornar): ")
        
        if cpf_busca.lower() == 'voltar':
            return
        
        cliente_encontrado = None
        for cliente in clientes:
            if cliente[1] == cpf_busca:
                cliente_encontrado = cliente
                break
        
        if cliente_encontrado:
            menu_operacoes(cliente_encontrado)
            return
        else:
            print("\nCliente não encontrado. Verifique o CPF digitado.")

def listar_clientes():
    if not clientes:
        print("\nNenhum cliente cadastrado ainda.")
        return
    
    print("\n--- Lista de Clientes Cadastrados ---")
    for i, cliente in enumerate(clientes, 1):
        print(f"\nCliente {i}:")
        print(f"Nome: {cliente[0]}")
        print(f"CPF: {cliente[1]}")
        print(f"Agência: {cliente[4]} | Conta: {cliente[5]}")

def menu_operacoes(cliente):
    while True:
        print("\n--- Menu de Operações ---")
        print(f"Cliente: {cliente[0]} (CPF: {cliente[1]})")
        print("1 - Ver Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Ver dados completos")
        print("5 - Voltar ao menu principal")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == "1":
            print(f"\nSaldo atual: R$ {cliente[6]:.2f}")
        elif opcao == "2":
            depositar(cliente)
        elif opcao == "3":
            sacar(cliente)
        elif opcao == "4":
            exibir_resumo_cliente(cliente)
        elif opcao == "5":
            print("\nRetornando ao menu principal...")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção de 1 a 5.")

def depositar(cliente):
    while True:
        try:
            valor = float(input("\nDigite o valor a depositar (R$): "))
            if valor > 0:
                cliente[6] += valor
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                print(f"Novo saldo: R$ {cliente[6]:.2f}")
                break
            else:
                print("O valor do depósito deve ser positivo.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

def sacar(cliente):
    while True:
        try:
            valor = float(input("\nDigite o valor a sacar (R$): "))
            if valor <= 0:
                print("O valor do saque deve ser positivo.")
            elif valor > cliente[6]:
                print("Saldo insuficiente para realizar o saque.")
            else:
                cliente[6] -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                print(f"Novo saldo: R$ {cliente[6]:.2f}")
                break
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

# Programa principal
print("=== Simulador Bancário ===")
print("Bem-vindo ao sistema bancário!")

menu_principal()