# Lista principal para armazenar todos os clientes
clientes = []

def validar_cpf(cpf):
    """Valida um CPF conforme as regras da Receita Federal."""
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (11 - (soma % 11)) if (11 - (soma % 11)) < 10 else 0
    
    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (11 - (soma % 11)) if (11 - (soma % 11)) < 10 else 0
    
    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

def formatar_cpf(cpf):
    """Formata o CPF no padrão XXX.XXX.XXX-XX."""
    cpf = ''.join(filter(str.isdigit, cpf))
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

def cadastrar_cliente():
    print("\n--- CADASTRO DE NOVO CLIENTE ---")
    
    # Validação do nome
    while True:
        nome = input("Nome completo: ").strip()
        if len(nome.split()) >= 2 and nome.replace(' ', '').isalpha():
            break
        print("⚠️ Nome inválido. Digite pelo menos 2 palavras (apenas letras).")
    
    # Validação do CPF
    while True:
        cpf = input("CPF (apenas números): ").strip()
        if validar_cpf(cpf):
            cpf_numeros = ''.join(filter(str.isdigit, cpf))
            if not any(cliente[1] == cpf_numeros for cliente in clientes):
                break
            print("⚠️ CPF já cadastrado no sistema.")
        else:
            print("⚠️ CPF inválido. Digite um CPF válido (11 dígitos).")
    
    # Validação do RG
    while True:
        rg = input("RG: ").strip()
        if rg:
            break
        print("⚠️ RG não pode estar vazio.")
    
    # Validação do telefone
    while True:
        telefone = input("Telefone (com DDD): ").strip()
        if len(''.join(filter(str.isdigit, telefone))) >= 10:
            break
        print("⚠️ Telefone inválido. Digite pelo menos 10 dígitos (incluindo DDD).")
    
    # Validação da agência e conta
    while True:
        agencia = input("Número da agência: ").strip()
        if agencia:
            break
        print("⚠️ Agência não pode estar vazia.")
    
    while True:
        conta = input("Número da conta: ").strip()
        if conta:
            break
        print("⚠️ Conta não pode estar vazia.")
    
    # Validação do saldo
    while True:
        saldo_input = input("Saldo inicial (R$): ").strip()
        try:
            saldo = float(saldo_input)
            if saldo >= 0:
                break
            else:
                print("⚠️ O saldo não pode ser negativo.")
        except ValueError:
            print("⚠️ Digite um valor numérico válido.")
    
    # Armazenando o cliente
    cliente = [nome, cpf_numeros, rg, telefone, agencia, conta, saldo]
    clientes.append(cliente)
    
    print("\n✅ Cadastro realizado com sucesso!")
    exibir_resumo_cliente(cliente)
    return cliente

def exibir_resumo_cliente(cliente):
    print("\n--- RESUMO DO CLIENTE ---")
    print(f"Nome: {cliente[0]}")
    print(f"CPF: {formatar_cpf(cliente[1])}")
    print(f"RG: {cliente[2]}")
    print(f"Telefone: {cliente[3]}")
    print(f"Agência: {cliente[4]} | Conta: {cliente[5]}")
    print(f"Saldo atual: R$ {cliente[6]:.2f}")

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar novo cliente")
        print("2 - Acessar cliente existente")
        print("3 - Listar todos os clientes")
        print("4 - Sair do sistema")
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            if not clientes:
                print("\n⚠️ Nenhum cliente cadastrado ainda.")
            else:
                acessar_cliente()
        elif opcao == "3":
            listar_clientes()
        elif opcao == "4":
            print("\n🔴 Encerrando o sistema...")
            break
        else:
            print("\n⚠️ Opção inválida. Digite um número de 1 a 4.")

def acessar_cliente():
    while True:
        print("\n--- ACESSAR CLIENTE ---")
        cpf_busca = input("Digite o CPF do cliente (ou 'voltar' para sair): ").strip()
        
        if cpf_busca.lower() == 'voltar':
            return
        
        cpf_busca = ''.join(filter(str.isdigit, cpf_busca))
        cliente_encontrado = None
        
        for cliente in clientes:
            if cliente[1] == cpf_busca:
                cliente_encontrado = cliente
                break
        
        if cliente_encontrado:
            menu_operacoes(cliente_encontrado)
            return
        else:
            print("\n⚠️ Cliente não encontrado. Verifique o CPF.")

def listar_clientes():
    if not clientes:
        print("\n⚠️ Nenhum cliente cadastrado ainda.")
        return
    
    print("\n--- LISTA DE CLIENTES ---")
    for i, cliente in enumerate(clientes, 1):
        print(f"\nCliente {i}:")
        print(f"Nome: {cliente[0]}")
        print(f"CPF: {formatar_cpf(cliente[1])}")
        print(f"Agência: {cliente[4]} | Conta: {cliente[5]}")

def menu_operacoes(cliente):
    while True:
        print("\n=== MENU DE OPERAÇÕES ===")
        print(f"Cliente: {cliente[0]} (CPF: {formatar_cpf(cliente[1])})")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Ver dados completos")
        print("5 - Voltar ao menu principal")
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            print(f"\n💰 Saldo atual: R$ {cliente[6]:.2f}")
        elif opcao == "2":
            depositar(cliente)
        elif opcao == "3":
            sacar(cliente)
        elif opcao == "4":
            exibir_resumo_cliente(cliente)
        elif opcao == "5":
            print("\n↩️ Retornando ao menu principal...")
            break
        else:
            print("\n⚠️ Opção inválida. Digite um número de 1 a 5.")

def depositar(cliente):
    while True:
        valor_input = input("\n💵 Digite o valor a depositar (R$): ").strip()
        try:
            valor = float(valor_input)
            if valor > 0:
                cliente[6] += valor
                print(f"✅ Depósito de R$ {valor:.2f} realizado!")
                print(f"💰 Novo saldo: R$ {cliente[6]:.2f}")
                break
            else:
                print("⚠️ O valor deve ser positivo.")
        except ValueError:
            print("⚠️ Digite um valor numérico válido.")

def sacar(cliente):
    while True:
        valor_input = input("\n💵 Digite o valor a sacar (R$): ").strip()
        try:
            valor = float(valor_input)
            if valor <= 0:
                print("⚠️ O valor deve ser positivo.")
            elif valor > cliente[6]:
                print("⚠️ Saldo insuficiente.")
            else:
                cliente[6] -= valor
                print(f"✅ Saque de R$ {valor:.2f} realizado!")
                print(f"💰 Novo saldo: R$ {cliente[6]:.2f}")
                break
        except ValueError:
            print("⚠️ Digite um valor numérico válido.")

# INÍCIO DO PROGRAMA
print("=== SIMULADOR BANCÁRIO ===")
print("Bem-vindo ao sistema bancário!")
menu_principal()