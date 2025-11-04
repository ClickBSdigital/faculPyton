from Cliente import Cliente
from Veiculo import Veiculo
from Servico import Servico
from OrdemServico import OrdemServico
from Peca import Peca
from Funcionario import Funcionario

def menu_principal():
    """Menu principal do sistema"""
    print("\n" + "="*60)
    print("          SISTEMA DE GERENCIAMENTO - PERKAL")
    print("="*60)
    print("1.  Gerenciar Clientes")
    print("2.  Gerenciar Veículos")
    print("3.  Gerenciar Serviços")
    print("4.  Gerenciar Ordens de Serviço")
    print("5.  Gerenciar Peças")
    print("6.  Gerenciar Funcionários")
    print("7.  Sair do Sistema")
    print("="*60)
    
    while True:
        try:
            opcao = int(input("Digite a opção desejada (1-7): "))
            if 1 <= opcao <= 7:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 7.")
        except ValueError:
            print("Erro: Digite um número válido!")

def menu_clientes():
    """Menu de gerenciamento de clientes"""
    print("\n" + "="*50)
    print("          GERENCIAMENTO DE CLIENTES")
    print("="*50)
    print("1. Cadastrar Cliente")
    print("2. Listar Todos os Clientes")
    print("3. Buscar Cliente por ID")
    print("4. Atualizar Cliente")
    print("5. Excluir Cliente")
    print("6. Voltar ao Menu Principal")
    print("="*50)
    
    while True:
        try:
            opcao = int(input("Digite a opção desejada (1-6): "))
            if 1 <= opcao <= 6:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 6.")
        except ValueError:
            print("Erro: Digite um número válido!")

def menu_veiculos():
    """Menu de gerenciamento de veículos"""
    print("\n" + "="*50)
    print("          GERENCIAMENTO DE VEÍCULOS")
    print("="*50)
    print("1. Cadastrar Veículo")
    print("2. Listar Todos os Veículos")
    print("3. Buscar Veículo por ID")
    print("4. Buscar Veículos por Cliente")
    print("5. Atualizar Veículo")
    print("6. Excluir Veículo")
    print("7. Voltar ao Menu Principal")
    print("="*50)
    
    while True:
        try:
            opcao = int(input("Digite a opção desejada (1-7): "))
            if 1 <= opcao <= 7:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 7.")
        except ValueError:
            print("Erro: Digite um número válido!")

def menu_servicos():
    """Menu de gerenciamento de serviços"""
    print("\n" + "="*50)
    print("          GERENCIAMENTO DE SERVIÇOS")
    print("="*50)
    print("1. Cadastrar Serviço")
    print("2. Listar Todos os Serviços")
    print("3. Buscar Serviço por ID")
    print("4. Atualizar Serviço")
    print("5. Excluir Serviço")
    print("6. Voltar ao Menu Principal")
    print("="*50)
    
    while True:
        try:
            opcao = int(input("Digite a opção desejada (1-6): "))
            if 1 <= opcao <= 6:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 6.")
        except ValueError:
            print("Erro: Digite um número válido!")

def menu_ordens_servico():
    """Menu de gerenciamento de ordens de serviço"""
    print("\n" + "="*50)
    print("          GERENCIAMENTO DE ORDENS DE SERVIÇO")
    print("="*50)
    print("1. Cadastrar Ordem de Serviço")
    print("2. Listar Todas as Ordens de Serviço")
    print("3. Buscar Ordem de Serviço por ID")
    print("4. Atualizar Ordem de Serviço")
    print("5. Atualizar Status da OS")
    print("6. Excluir Ordem de Serviço")
    print("7. Voltar ao Menu Principal")
    print("="*50)
    
    while True:
        try:
            opcao = int(input("Digite a opção desejada (1-7): "))
            if 1 <= opcao <= 7:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 7.")
        except ValueError:
            print("Erro: Digite um número válido!")

def menu_pecas():
    """Menu de gerenciamento de peças"""
    print("\n" + "="*50)
    print("          GERENCIAMENTO DE PEÇAS")
    print("="*50)
    print("1. Cadastrar Peça")
    print("2. Listar Todas as Peças")
    print("3. Buscar Peça por ID")
    print("4. Atualizar Peça")
    print("5. Atualizar Estoque")
    print("6. Excluir Peça")
    print("7. Voltar ao Menu Principal")
    print("="*50)
    
    while True:
        try:
            opcao = int(input("Digite a opção desejada (1-7): "))
            if 1 <= opcao <= 7:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 7.")
        except ValueError:
            print("Erro: Digite um número válido!")

def menu_funcionarios():
    """Menu de gerenciamento de funcionários"""
    print("\n" + "="*50)
    print("          GERENCIAMENTO DE FUNCIONÁRIOS")
    print("="*50)
    print("1. Cadastrar Funcionário")
    print("2. Listar Todos os Funcionários")
    print("3. Buscar Funcionário por ID")
    print("4. Atualizar Funcionário")
    print("5. Excluir Funcionário")
    print("6. Voltar ao Menu Principal")
    print("="*50)
    
    while True:
        try:
            opcao = int(input("Digite a opção desejada (1-6): "))
            if 1 <= opcao <= 6:
                return opcao
            else:
                print("Opção inválida! Digite um número entre 1 e 6.")
        except ValueError:
            print("Erro: Digite um número válido!")

# ===== FUNÇÕES PARA CLIENTES =====
def gerenciar_clientes():
    """Função principal para gerenciar clientes"""
    cli = Cliente()
    
    while True:
        opcao = menu_clientes()
        
        if opcao == 1:
            cadastrar_cliente(cli)
        elif opcao == 2:
            listar_clientes(cli)
        elif opcao == 3:
            buscar_cliente_por_id(cli)
        elif opcao == 4:
            atualizar_cliente(cli)
        elif opcao == 5:
            excluir_cliente(cli)
        elif opcao == 6:
            break

def cadastrar_cliente(cli):
    """Cadastra um novo cliente"""
    print("\n" + "="*40)
    print("          CADASTRAR CLIENTE")
    print("="*40)
    
    cli.nome = input("Nome: ")
    cli.cpf = input("CPF: ")
    cli.fone = input("Telefone: ")
    cli.cidade = input("Cidade: ")
    cli.email = input("Email (opcional): ") or None
    cli.endereco = input("Endereço (opcional): ") or None
    
    resultado = cli.cadastrar()
    input("\nPressione Enter para continuar...")

def listar_clientes(cli):
    """Lista todos os clientes"""
    print("\n" + "="*40)
    print("          LISTA DE CLIENTES")
    print("="*40)
    
    clientes = cli.buscar_todos()
    
    if clientes:
        print(f"\nTotal de clientes: {len(clientes)}")
        print("-" * 100)
        for item in clientes:
            print(f"ID: {item[0]:<3} | Nome: {item[1]:<20} | CPF: {item[2]:<14} | Tel: {item[3]:<12} | Cidade: {item[4]}")
        print("-" * 100)
    else:
        print("\n📭 Nenhum cliente encontrado.")
    
    input("\nPressione Enter para continuar...")

def buscar_cliente_por_id(cli):
    """Busca cliente por ID"""
    print("\n" + "="*40)
    print("          BUSCAR CLIENTE POR ID")
    print("="*40)
    
    try:
        id_cliente = int(input("ID do cliente: "))
        cliente = cli.buscar_por_id(id_cliente)
        
        if cliente:
            print("\n" + "="*40)
            print("          CLIENTE ENCONTRADO")
            print("="*40)
            print(f"ID: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"CPF: {cliente[2]}")
            print(f"Telefone: {cliente[3]}")
            print(f"Cidade: {cliente[4]}")
            print(f"Email: {cliente[5] or 'Não informado'}")
            print(f"Endereço: {cliente[6] or 'Não informado'}")
        else:
            print(f"\n❌ Cliente com ID {id_cliente} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def atualizar_cliente(cli):
    """Atualiza dados do cliente"""
    print("\n" + "="*40)
    print("          ATUALIZAR CLIENTE")
    print("="*40)
    
    try:
        id_cliente = int(input("ID do cliente a atualizar: "))
        cliente_atual = cli.buscar_por_id(id_cliente)
        
        if cliente_atual:
            print(f"\nCliente atual: {cliente_atual[1]} - {cliente_atual[2]}")
            
            cli.id_cli = id_cliente
            cli.nome = input(f"Novo nome [{cliente_atual[1]}]: ").strip() or cliente_atual[1]
            cli.cpf = input(f"Novo CPF [{cliente_atual[2]}]: ").strip() or cliente_atual[2]
            cli.fone = input(f"Novo telefone [{cliente_atual[3]}]: ").strip() or cliente_atual[3]
            cli.cidade = input(f"Nova cidade [{cliente_atual[4]}]: ").strip() or cliente_atual[4]
            cli.email = input(f"Novo email [{cliente_atual[5] or 'Não informado'}]: ").strip() or cliente_atual[5]
            cli.endereco = input(f"Novo endereço [{cliente_atual[6] or 'Não informado'}]: ").strip() or cliente_atual[6]
            
            resultado = cli.atualizar()
        else:
            print(f"\n❌ Cliente com ID {id_cliente} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def excluir_cliente(cli):
    """Exclui um cliente"""
    print("\n" + "="*40)
    print("          EXCLUIR CLIENTE")
    print("="*40)
    
    try:
        id_cliente = int(input("ID do cliente a excluir: "))
        cliente = cli.buscar_por_id(id_cliente)
        
        if cliente:
            print(f"\n⚠️  ATENÇÃO: Você vai excluir:")
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | CPF: {cliente[2]}")
            
            confirmacao = input("\nConfirma exclusão? (s/N): ").strip().lower()
            
            if confirmacao == 's':
                resultado = cli.excluir(id_cliente)
            else:
                print("Operação cancelada.")
        else:
            print(f"\n❌ Cliente com ID {id_cliente} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

# ===== FUNÇÕES PARA VEÍCULOS =====
def gerenciar_veiculos():
    """Função principal para gerenciar veículos"""
    veic = Veiculo()
    
    while True:
        opcao = menu_veiculos()
        
        if opcao == 1:
            cadastrar_veiculo(veic)
        elif opcao == 2:
            listar_veiculos(veic)
        elif opcao == 3:
            buscar_veiculo_por_id(veic)
        elif opcao == 4:
            buscar_veiculos_por_cliente(veic)
        elif opcao == 5:
            atualizar_veiculo(veic)
        elif opcao == 6:
            excluir_veiculo(veic)
        elif opcao == 7:
            break

def cadastrar_veiculo(veic):
    """Cadastra um novo veículo"""
    print("\n" + "="*40)
    print("          CADASTRAR VEÍCULO")
    print("="*40)
    
    try:
        veic.id_cliente = int(input("ID do Cliente: "))
        veic.marca = input("Marca: ")
        veic.modelo = input("Modelo: ")
        veic.ano = int(input("Ano: "))
        veic.placa = input("Placa: ")
        veic.cor = input("Cor: ")
        veic.km_rodados = int(input("KM Rodados: ") or 0)
        
        resultado = veic.cadastrar()
    except ValueError:
        print("\n❌ Erro: Ano e KM devem ser números!")
    
    input("\nPressione Enter para continuar...")

def listar_veiculos(veic):
    """Lista todos os veículos"""
    print("\n" + "="*40)
    print("          LISTA DE VEÍCULOS")
    print("="*40)
    
    veiculos = veic.buscar_todos()
    
    if veiculos:
        print(f"\nTotal de veículos: {len(veiculos)}")
        print("-" * 120)
        for item in veiculos:
            print(f"ID: {item[0]:<3} | Cliente: {item[8]:<15} | Marca: {item[2]:<10} | Modelo: {item[3]:<10} | Ano: {item[4]:<4} | Placa: {item[5]:<8} | Cor: {item[6]:<10} | KM: {item[7]}")
        print("-" * 120)
    else:
        print("\n📭 Nenhum veículo encontrado.")
    
    input("\nPressione Enter para continuar...")

def buscar_veiculo_por_id(veic):
    """Busca veículo por ID"""
    print("\n" + "="*40)
    print("          BUSCAR VEÍCULO POR ID")
    print("="*40)
    
    try:
        id_veiculo = int(input("ID do veículo: "))
        veiculo = veic.buscar_por_id(id_veiculo)
        
        if veiculo:
            print("\n" + "="*40)
            print("          VEÍCULO ENCONTRADO")
            print("="*40)
            print(f"ID: {veiculo[0]}")
            print(f"ID Cliente: {veiculo[1]}")
            print(f"Marca: {veiculo[2]}")
            print(f"Modelo: {veiculo[3]}")
            print(f"Ano: {veiculo[4]}")
            print(f"Placa: {veiculo[5]}")
            print(f"Cor: {veiculo[6]}")
            print(f"KM Rodados: {veiculo[7]}")
        else:
            print(f"\n❌ Veículo com ID {id_veiculo} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def buscar_veiculos_por_cliente(veic):
    """Busca veículos por cliente"""
    print("\n" + "="*40)
    print("          BUSCAR VEÍCULOS POR CLIENTE")
    print("="*40)
    
    try:
        id_cliente = int(input("ID do cliente: "))
        veiculos = veic.buscar_por_cliente(id_cliente)
        
        if veiculos:
            print(f"\nTotal de veículos do cliente: {len(veiculos)}")
            print("-" * 80)
            for item in veiculos:
                print(f"ID: {item[0]:<3} | Marca: {item[2]:<10} | Modelo: {item[3]:<10} | Ano: {item[4]:<4} | Placa: {item[5]:<8} | Cor: {item[6]}")
            print("-" * 80)
        else:
            print(f"\n📭 Nenhum veículo encontrado para o cliente ID {id_cliente}")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def atualizar_veiculo(veic):
    """Atualiza dados do veículo"""
    print("\n" + "="*40)
    print("          ATUALIZAR VEÍCULO")
    print("="*40)
    
    try:
        id_veiculo = int(input("ID do veículo a atualizar: "))
        veiculo_atual = veic.buscar_por_id(id_veiculo)
        
        if veiculo_atual:
            print(f"\nVeículo atual: {veiculo_atual[2]} {veiculo_atual[3]} - {veiculo_atual[5]}")
            
            veic.id_veiculo = id_veiculo
            veic.id_cliente = input(f"Novo ID Cliente [{veiculo_atual[1]}]: ").strip() or veiculo_atual[1]
            veic.marca = input(f"Nova marca [{veiculo_atual[2]}]: ").strip() or veiculo_atual[2]
            veic.modelo = input(f"Novo modelo [{veiculo_atual[3]}]: ").strip() or veiculo_atual[3]
            veic.ano = input(f"Novo ano [{veiculo_atual[4]}]: ").strip() or veiculo_atual[4]
            veic.placa = input(f"Nova placa [{veiculo_atual[5]}]: ").strip() or veiculo_atual[5]
            veic.cor = input(f"Nova cor [{veiculo_atual[6]}]: ").strip() or veiculo_atual[6]
            veic.km_rodados = input(f"Novo KM [{veiculo_atual[7]}]: ").strip() or veiculo_atual[7]
            
            # Converter para inteiros
            veic.id_cliente = int(veic.id_cliente)
            veic.ano = int(veic.ano)
            veic.km_rodados = int(veic.km_rodados)
            
            resultado = veic.atualizar()
        else:
            print(f"\n❌ Veículo com ID {id_veiculo} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: IDs, Ano e KM devem ser números!")
    
    input("\nPressione Enter para continuar...")

def excluir_veiculo(veic):
    """Exclui um veículo"""
    print("\n" + "="*40)
    print("          EXCLUIR VEÍCULO")
    print("="*40)
    
    try:
        id_veiculo = int(input("ID do veículo a excluir: "))
        veiculo = veic.buscar_por_id(id_veiculo)
        
        if veiculo:
            print(f"\n⚠️  ATENÇÃO: Você vai excluir:")
            print(f"ID: {veiculo[0]} | {veiculo[2]} {veiculo[3]} - {veiculo[5]}")
            
            confirmacao = input("\nConfirma exclusão? (s/N): ").strip().lower()
            
            if confirmacao == 's':
                resultado = veic.excluir(id_veiculo)
            else:
                print("Operação cancelada.")
        else:
            print(f"\n❌ Veículo com ID {id_veiculo} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

# ===== FUNÇÕES PARA SERVIÇOS =====
def gerenciar_servicos():
    """Função principal para gerenciar serviços"""
    serv = Servico()
    
    while True:
        opcao = menu_servicos()
        
        if opcao == 1:
            cadastrar_servico(serv)
        elif opcao == 2:
            listar_servicos(serv)
        elif opcao == 3:
            buscar_servico_por_id(serv)
        elif opcao == 4:
            atualizar_servico(serv)
        elif opcao == 5:
            excluir_servico(serv)
        elif opcao == 6:
            break

def cadastrar_servico(serv):
    """Cadastra um novo serviço"""
    print("\n" + "="*40)
    print("          CADASTRAR SERVIÇO")
    print("="*40)
    
    serv.nome_servico = input("Nome do Serviço: ")
    serv.descricao = input("Descrição: ")
    serv.preco = float(input("Preço: R$ "))
    serv.tempo_estimado = input("Tempo Estimado (HH:MM:SS): ")
    
    resultado = serv.cadastrar()
    input("\nPressione Enter para continuar...")

def listar_servicos(serv):
    """Lista todos os serviços"""
    print("\n" + "="*40)
    print("          LISTA DE SERVIÇOS")
    print("="*40)
    
    servicos = serv.buscar_todos()
    
    if servicos:
        print(f"\nTotal de serviços: {len(servicos)}")
        print("-" * 80)
        for item in servicos:
            print(f"ID: {item[0]:<3} | Serviço: {item[1]:<20} | Preço: R$ {item[3]:<8.2f} | Tempo: {item[4]}")
        print("-" * 80)
    else:
        print("\n📭 Nenhum serviço encontrado.")
    
    input("\nPressione Enter para continuar...")

def buscar_servico_por_id(serv):
    """Busca serviço por ID"""
    print("\n" + "="*40)
    print("          BUSCAR SERVIÇO POR ID")
    print("="*40)
    
    try:
        id_servico = int(input("ID do serviço: "))
        servico = serv.buscar_por_id(id_servico)
        
        if servico:
            print("\n" + "="*40)
            print("          SERVIÇO ENCONTRADO")
            print("="*40)
            print(f"ID: {servico[0]}")
            print(f"Serviço: {servico[1]}")
            print(f"Descrição: {servico[2]}")
            print(f"Preço: R$ {servico[3]:.2f}")
            print(f"Tempo Estimado: {servico[4]}")
        else:
            print(f"\n❌ Serviço com ID {id_servico} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def atualizar_servico(serv):
    """Atualiza dados do serviço"""
    print("\n" + "="*40)
    print("          ATUALIZAR SERVIÇO")
    print("="*40)
    
    try:
        id_servico = int(input("ID do serviço a atualizar: "))
        servico_atual = serv.buscar_por_id(id_servico)
        
        if servico_atual:
            print(f"\nServiço atual: {servico_atual[1]} - R$ {servico_atual[3]:.2f}")
            
            serv.id_servico = id_servico
            serv.nome_servico = input(f"Novo nome [{servico_atual[1]}]: ").strip() or servico_atual[1]
            serv.descricao = input(f"Nova descrição [{servico_atual[2]}]: ").strip() or servico_atual[2]
            
            novo_preco = input(f"Novo preço [R$ {servico_atual[3]:.2f}]: ").strip()
            serv.preco = float(novo_preco) if novo_preco else servico_atual[3]
            
            serv.tempo_estimado = input(f"Novo tempo [{servico_atual[4]}]: ").strip() or servico_atual[4]
            
            resultado = serv.atualizar()
        else:
            print(f"\n❌ Serviço com ID {id_servico} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número e preço deve ser decimal!")
    
    input("\nPressione Enter para continuar...")

def excluir_servico(serv):
    """Exclui um serviço"""
    print("\n" + "="*40)
    print("          EXCLUIR SERVIÇO")
    print("="*40)
    
    try:
        id_servico = int(input("ID do serviço a excluir: "))
        servico = serv.buscar_por_id(id_servico)
        
        if servico:
            print(f"\n⚠️  ATENÇÃO: Você vai excluir:")
            print(f"ID: {servico[0]} | {servico[1]} - R$ {servico[3]:.2f}")
            
            confirmacao = input("\nConfirma exclusão? (s/N): ").strip().lower()
            
            if confirmacao == 's':
                resultado = serv.excluir(id_servico)
            else:
                print("Operação cancelada.")
        else:
            print(f"\n❌ Serviço com ID {id_servico} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

# ===== FUNÇÕES PARA PEÇAS =====
def gerenciar_pecas():
    """Função principal para gerenciar peças"""
    pec = Peca()
    
    while True:
        opcao = menu_pecas()
        
        if opcao == 1:
            cadastrar_peca(pec)
        elif opcao == 2:
            listar_pecas(pec)
        elif opcao == 3:
            buscar_peca_por_id(pec)
        elif opcao == 4:
            atualizar_peca(pec)
        elif opcao == 5:
            atualizar_estoque_peca(pec)
        elif opcao == 6:
            excluir_peca(pec)
        elif opcao == 7:
            break

def cadastrar_peca(pec):
    """Cadastra uma nova peça"""
    print("\n" + "="*40)
    print("          CADASTRAR PEÇA")
    print("="*40)
    
    pec.nome_peca = input("Nome da Peça: ")
    pec.descricao = input("Descrição: ")
    pec.preco_custo = float(input("Preço de Custo: R$ "))
    pec.preco_venda = float(input("Preço de Venda: R$ "))
    pec.estoque = int(input("Estoque: "))
    pec.estoque_minimo = int(input("Estoque Mínimo: ") or 5)
    
    resultado = pec.cadastrar()
    input("\nPressione Enter para continuar...")

def listar_pecas(pec):
    """Lista todas as peças"""
    print("\n" + "="*40)
    print("          LISTA DE PEÇAS")
    print("="*40)
    
    pecas = pec.buscar_todas()
    
    if pecas:
        print(f"\nTotal de peças: {len(pecas)}")
        print("-" * 100)
        for item in pecas:
            status_estoque = "✅" if item[5] > item[6] else "⚠️" if item[5] == item[6] else "❌"
            print(f"ID: {item[0]:<3} | Peça: {item[1]:<20} | Custo: R$ {item[3]:<6.2f} | Venda: R$ {item[4]:<6.2f} | Estoque: {item[5]:<3} {status_estoque}")
        print("-" * 100)
    else:
        print("\n📭 Nenhuma peça encontrada.")
    
    input("\nPressione Enter para continuar...")

def buscar_peca_por_id(pec):
    """Busca peça por ID"""
    print("\n" + "="*40)
    print("          BUSCAR PEÇA POR ID")
    print("="*40)
    
    try:
        id_peca = int(input("ID da peça: "))
        peca = pec.buscar_por_id(id_peca)
        
        if peca:
            print("\n" + "="*40)
            print("          PEÇA ENCONTRADA")
            print("="*40)
            print(f"ID: {peca[0]}")
            print(f"Peça: {peca[1]}")
            print(f"Descrição: {peca[2]}")
            print(f"Preço Custo: R$ {peca[3]:.2f}")
            print(f"Preço Venda: R$ {peca[4]:.2f}")
            print(f"Estoque: {peca[5]}")
            print(f"Estoque Mínimo: {peca[6]}")
        else:
            print(f"\n❌ Peça com ID {id_peca} não encontrada!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def atualizar_peca(pec):
    """Atualiza dados da peça"""
    print("\n" + "="*40)
    print("          ATUALIZAR PEÇA")
    print("="*40)
    
    try:
        id_peca = int(input("ID da peça a atualizar: "))
        peca_atual = pec.buscar_por_id(id_peca)
        
        if peca_atual:
            print(f"\nPeça atual: {peca_atual[1]} - Estoque: {peca_atual[5]}")
            
            pec.id_peca = id_peca
            pec.nome_peca = input(f"Novo nome [{peca_atual[1]}]: ").strip() or peca_atual[1]
            pec.descricao = input(f"Nova descrição [{peca_atual[2]}]: ").strip() or peca_atual[2]
            
            novo_custo = input(f"Novo preço custo [R$ {peca_atual[3]:.2f}]: ").strip()
            pec.preco_custo = float(novo_custo) if novo_custo else peca_atual[3]
            
            nova_venda = input(f"Novo preço venda [R$ {peca_atual[4]:.2f}]: ").strip()
            pec.preco_venda = float(nova_venda) if nova_venda else peca_atual[4]
            
            novo_estoque = input(f"Novo estoque [{peca_atual[5]}]: ").strip()
            pec.estoque = int(novo_estoque) if novo_estoque else peca_atual[5]
            
            novo_minimo = input(f"Novo estoque mínimo [{peca_atual[6]}]: ").strip()
            pec.estoque_minimo = int(novo_minimo) if novo_minimo else peca_atual[6]
            
            resultado = pec.atualizar()
        else:
            print(f"\n❌ Peça com ID {id_peca} não encontrada!")
    
    except ValueError:
        print("\n❌ Erro: IDs devem ser números e preços devem ser decimais!")
    
    input("\nPressione Enter para continuar...")

def atualizar_estoque_peca(pec):
    """Atualiza apenas o estoque da peça"""
    print("\n" + "="*40)
    print("          ATUALIZAR ESTOQUE")
    print("="*40)
    
    try:
        id_peca = int(input("ID da peça: "))
        nova_quantidade = int(input("Nova quantidade em estoque: "))
        
        resultado = pec.atualizar_estoque(id_peca, nova_quantidade)
    
    except ValueError:
        print("\n❌ Erro: ID e quantidade devem ser números!")
    
    input("\nPressione Enter para continuar...")

def excluir_peca(pec):
    """Exclui uma peça"""
    print("\n" + "="*40)
    print("          EXCLUIR PEÇA")
    print("="*40)
    
    try:
        id_peca = int(input("ID da peça a excluir: "))
        peca = pec.buscar_por_id(id_peca)
        
        if peca:
            print(f"\n⚠️  ATENÇÃO: Você vai excluir:")
            print(f"ID: {peca[0]} | {peca[1]} - Estoque: {peca[5]}")
            
            confirmacao = input("\nConfirma exclusão? (s/N): ").strip().lower()
            
            if confirmacao == 's':
                resultado = pec.excluir(id_peca)
            else:
                print("Operação cancelada.")
        else:
            print(f"\n❌ Peça com ID {id_peca} não encontrada!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

# ===== FUNÇÕES PARA FUNCIONÁRIOS =====
def gerenciar_funcionarios():
    """Função principal para gerenciar funcionários"""
    func = Funcionario()
    
    while True:
        opcao = menu_funcionarios()
        
        if opcao == 1:
            cadastrar_funcionario(func)
        elif opcao == 2:
            listar_funcionarios(func)
        elif opcao == 3:
            buscar_funcionario_por_id(func)
        elif opcao == 4:
            atualizar_funcionario(func)
        elif opcao == 5:
            excluir_funcionario(func)
        elif opcao == 6:
            break

def cadastrar_funcionario(func):
    """Cadastra um novo funcionário"""
    print("\n" + "="*40)
    print("          CADASTRAR FUNCIONÁRIO")
    print("="*40)
    
    func.nome = input("Nome: ")
    func.cpf = input("CPF: ")
    func.fone = input("Telefone: ")
    func.cargo = input("Cargo: ")
    func.salario = float(input("Salário: R$ "))
    func.data_admissao = input("Data de Admissão (YYYY-MM-DD): ")
    
    resultado = func.cadastrar()
    input("\nPressione Enter para continuar...")

def listar_funcionarios(func):
    """Lista todos os funcionários"""
    print("\n" + "="*40)
    print("          LISTA DE FUNCIONÁRIOS")
    print("="*40)
    
    funcionarios = func.buscar_todos()
    
    if funcionarios:
        print(f"\nTotal de funcionários: {len(funcionarios)}")
        print("-" * 100)
        for item in funcionarios:
            print(f"ID: {item[0]:<3} | Nome: {item[1]:<20} | CPF: {item[2]:<14} | Cargo: {item[4]:<15} | Salário: R$ {item[5]:<8.2f}")
        print("-" * 100)
    else:
        print("\n📭 Nenhum funcionário encontrado.")
    
    input("\nPressione Enter para continuar...")

def buscar_funcionario_por_id(func):
    """Busca funcionário por ID"""
    print("\n" + "="*40)
    print("          BUSCAR FUNCIONÁRIO POR ID")
    print("="*40)
    
    try:
        id_funcionario = int(input("ID do funcionário: "))
        funcionario = func.buscar_por_id(id_funcionario)
        
        if funcionario:
            print("\n" + "="*40)
            print("          FUNCIONÁRIO ENCONTRADO")
            print("="*40)
            print(f"ID: {funcionario[0]}")
            print(f"Nome: {funcionario[1]}")
            print(f"CPF: {funcionario[2]}")
            print(f"Telefone: {funcionario[3]}")
            print(f"Cargo: {funcionario[4]}")
            print(f"Salário: R$ {funcionario[5]:.2f}")
            print(f"Data Admissão: {funcionario[6]}")
        else:
            print(f"\n❌ Funcionário com ID {id_funcionario} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def atualizar_funcionario(func):
    """Atualiza dados do funcionário"""
    print("\n" + "="*40)
    print("          ATUALIZAR FUNCIONÁRIO")
    print("="*40)
    
    try:
        id_funcionario = int(input("ID do funcionário a atualizar: "))
        funcionario_atual = func.buscar_por_id(id_funcionario)
        
        if funcionario_atual:
            print(f"\nFuncionário atual: {funcionario_atual[1]} - {funcionario_atual[4]}")
            
            func.id_funcionario = id_funcionario
            func.nome = input(f"Novo nome [{funcionario_atual[1]}]: ").strip() or funcionario_atual[1]
            func.cpf = input(f"Novo CPF [{funcionario_atual[2]}]: ").strip() or funcionario_atual[2]
            func.fone = input(f"Novo telefone [{funcionario_atual[3]}]: ").strip() or funcionario_atual[3]
            func.cargo = input(f"Novo cargo [{funcionario_atual[4]}]: ").strip() or funcionario_atual[4]
            
            novo_salario = input(f"Novo salário [R$ {funcionario_atual[5]:.2f}]: ").strip()
            func.salario = float(novo_salario) if novo_salario else funcionario_atual[5]
            
            func.data_admissao = input(f"Nova data admissão [{funcionario_atual[6]}]: ").strip() or funcionario_atual[6]
            
            resultado = func.atualizar()
        else:
            print(f"\n❌ Funcionário com ID {id_funcionario} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número e salário deve ser decimal!")
    
    input("\nPressione Enter para continuar...")

def excluir_funcionario(func):
    """Exclui um funcionário"""
    print("\n" + "="*40)
    print("          EXCLUIR FUNCIONÁRIO")
    print("="*40)
    
    try:
        id_funcionario = int(input("ID do funcionário a excluir: "))
        funcionario = func.buscar_por_id(id_funcionario)
        
        if funcionario:
            print(f"\n⚠️  ATENÇÃO: Você vai excluir:")
            print(f"ID: {funcionario[0]} | {funcionario[1]} - {funcionario[4]}")
            
            confirmacao = input("\nConfirma exclusão? (s/N): ").strip().lower()
            
            if confirmacao == 's':
                resultado = func.excluir(id_funcionario)
            else:
                print("Operação cancelada.")
        else:
            print(f"\n❌ Funcionário com ID {id_funcionario} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

# ===== FUNÇÃO PRINCIPAL =====
def main():
    """Função principal do sistema"""
    print("🚗 BEM-VINDO AO SISTEMA PERKAL - MECÂNICA 🛠️")
    
    while True:
        opcao_principal = menu_principal()
        
        if opcao_principal == 1:
            gerenciar_clientes()
        elif opcao_principal == 2:
            gerenciar_veiculos()
        elif opcao_principal == 3:
            gerenciar_servicos()
        elif opcao_principal == 4:
            print("\n🔧 Módulo Ordens de Serviço - Em desenvolvimento...")
            input("Pressione Enter para continuar...")
        elif opcao_principal == 5:
            gerenciar_pecas()
        elif opcao_principal == 6:
            gerenciar_funcionarios()
        elif opcao_principal == 7:
            print("\n" + "="*50)
            print("Obrigado por usar o Sistema PERKAL!")
            print("Saindo... Até logo! 👋")
            print("="*50)
            break

# Executar o sistema
if __name__ == "__main__":
    main()