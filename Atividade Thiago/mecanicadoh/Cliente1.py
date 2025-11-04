from Database import Database

class Cliente:
    def __init__(self, nome=None, cpf=None, fone=None, cidade=None):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade
        self.db = Database()  # Instância única

    def cadastrar(self, nome, cpf, fone, cidade):
        """Cadastra um novo cliente"""
        try:
            tupla = (nome, cpf, fone, cidade)
            result = self.db.insert(tupla)
            return result
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            return False

    def buscar_todos(self):
        """Busca todos os clientes"""
        try:
            dados = self.db.select()
            return dados
        except Exception as e:
            print(f"Erro ao buscar: {e}")
            return []

    def buscar_por_id(self, id_cliente):
        """Busca um cliente específico por ID"""
        try:
            dados = self.db.selectById(id_cliente)
            return dados
        except Exception as e:
            print(f"Erro ao buscar por ID: {e}")
            return None

    def excluir(self, id_cliente):
        """Exclui um cliente por ID"""
        try:
            result = self.db.delete(id_cliente)
            return result
        except Exception as e:
            print(f"Erro ao excluir: {e}")
            return False

    def atualizar(self, tupla):
        """Atualiza os dados de um cliente"""
        try:
            result = self.db.update(tupla)
            return result
        except Exception as e:
            print(f"Erro ao atualizar: {e}")
            return False

def menu_principal():
    """Menu principal do sistema"""
    print("\n" + "="*50)
    print("          SISTEMA DE GERENCIAMENTO - PERKAL")
    print("="*50)
    print("1. Cadastrar Cliente")
    print("2. Listar Todos os Clientes")
    print("3. Buscar Cliente por ID")
    print("4. Atualizar Cliente")
    print("5. Excluir Cliente")
    print("6. Sair do Sistema")
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

def cadastrar_cliente(cli):
    """Função para cadastrar um novo cliente"""
    print("\n" + "="*50)
    print("          CADASTRAR NOVO CLIENTE")
    print("="*50)
    
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    fone = input("Digite o telefone: ")
    cidade = input("Digite a cidade: ")
    
    resultado = cli.cadastrar(nome, cpf, fone, cidade)
    if resultado:
        print("\n✅ Cliente cadastrado com sucesso!")
    else:
        print("\n❌ Erro ao cadastrar cliente!")
    
    input("\nPressione Enter para continuar...")

def listar_clientes(cli):
    """Função para listar todos os clientes"""
    print("\n" + "="*50)
    print("          LISTA DE CLIENTES")
    print("="*50)
    
    clientes = cli.buscar_todos()
    
    if clientes:
        print(f"\nTotal de clientes encontrados: {len(clientes)}")
        print("-" * 80)
        for item in clientes:
            print(f"ID: {item[0]} | Nome: {item[1]} | CPF: {item[2]} | Telefone: {item[3]} | Cidade: {item[4]}")
        print("-" * 80)
    else:
        print("\n📭 Nenhum cliente encontrado.")
    
    input("\nPressione Enter para continuar...")

def buscar_cliente_por_id(cli):
    """Função para buscar cliente por ID"""
    print("\n" + "="*50)
    print("          BUSCAR CLIENTE POR ID")
    print("="*50)
    
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
        
        cliente = cli.buscar_por_id(id_cliente)
        if cliente:
            print("\n" + "="*50)
            print("          CLIENTE ENCONTRADO")
            print("="*50)
            print(f"ID: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"CPF: {cliente[2]}")
            print(f"Telefone: {cliente[3]}")
            print(f"Cidade: {cliente[4]}")
        else:
            print(f"\n❌ Cliente com ID {id_cliente} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def atualizar_cliente(cli):
    """Função para atualizar dados de um cliente"""
    print("\n" + "="*50)
    print("          ATUALIZAR CLIENTE")
    print("="*50)
    
    try:
        id_atualizar = int(input("Digite o ID do cliente que deseja atualizar: "))
        
        # Buscar cliente atual
        cli_atualizar = cli.buscar_por_id(id_atualizar)
        if cli_atualizar:
            print(f"\nCliente atual:")
            print(f"ID: {cli_atualizar[0]} | Nome: {cli_atualizar[1]} | CPF: {cli_atualizar[2]} | Telefone: {cli_atualizar[3]} | Cidade: {cli_atualizar[4]}")
            print("\nDigite os novos dados (ou Enter para manter o valor atual):")
            
            # Converter para lista para poder modificar
            cli_atualizar = list(cli_atualizar)
            
            # Solicitar novos dados
            novo_nome = input(f"Novo nome [{cli_atualizar[1]}]: ").strip()
            novo_cpf = input(f"Novo CPF [{cli_atualizar[2]}]: ").strip()
            novo_fone = input(f"Novo telefone [{cli_atualizar[3]}]: ").strip()
            nova_cidade = input(f"Nova cidade [{cli_atualizar[4]}]: ").strip()
            
            # Atualizar apenas os campos que foram modificados
            if novo_nome:
                cli_atualizar[1] = novo_nome
            if novo_cpf:
                cli_atualizar[2] = novo_cpf
            if novo_fone:
                cli_atualizar[3] = novo_fone
            if nova_cidade:
                cli_atualizar[4] = nova_cidade
            
            # Converter de volta para tupla e atualizar
            cli_atualizar = tuple(cli_atualizar)
            resultado = cli.atualizar(cli_atualizar)
            
            if resultado:
                print("\n✅ Cliente atualizado com sucesso!")
            else:
                print("\n❌ Erro ao atualizar cliente!")
        else:
            print(f"\n❌ Cliente com ID {id_atualizar} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def excluir_cliente(cli):
    """Função para excluir um cliente"""
    print("\n" + "="*50)
    print("          EXCLUIR CLIENTE")
    print("="*50)
    
    try:
        id_excluir = int(input("Digite o ID do cliente que deseja excluir: "))
        
        # Confirmar exclusão
        cliente = cli.buscar_por_id(id_excluir)
        if cliente:
            print(f"\n⚠️  ATENÇÃO: Você está prestes a excluir o cliente:")
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | CPF: {cliente[2]}")
            
            confirmacao = input("\nTem certeza que deseja excluir? (s/N): ").strip().lower()
            
            if confirmacao == 's' or confirmacao == 'sim':
                resultado = cli.excluir(id_excluir)
                if resultado:
                    print("\n✅ Cliente excluído com sucesso!")
                else:
                    print("\n❌ Erro ao excluir cliente!")
            else:
                print("\nOperação cancelada.")
        else:
            print(f"\n❌ Cliente com ID {id_excluir} não encontrado!")
    
    except ValueError:
        print("\n❌ Erro: ID deve ser um número!")
    
    input("\nPressione Enter para continuar...")

def main():
    """Função principal do sistema"""
    cli = Cliente()
    
    print("Bem-vindo ao Sistema de Gerenciamento PERKAL!")
    
    while True:
        opcao = menu_principal()
        
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
            print("\n" + "="*50)
            print("Obrigado por usar o Sistema PERKAL!")
            print("Saindo... Até logo! 👋")
            print("="*50)
            break

# Executar o sistema
if __name__ == "__main__":
    main()