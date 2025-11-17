from models import Usuario, Config, Veiculo, Caixa
from database import execute_query


class AdminSystem:
    @staticmethod
    def menu():
        print("\n=== MENU ADMIN ===")
        print("1. Cadastrar Usuário")
        print("2. Configurar Estacionamento")
        print("3. Ver Relatórios")
        print("4. Sair")

    @staticmethod
    def cadastrar_usuario():
        print("\n=== CADASTRAR USUÁRIO ===")
        nome = input("Nome: ")
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        tipo = input("Tipo (admin/operador): ").lower()

        if tipo not in ["admin", "operador"]:
            print("Tipo inválido!")
            return

        if Usuario.criar(nome, usuario, senha, tipo):
            print("Usuário cadastrado com sucesso!")
        else:
            print("Erro ao cadastrar usuário!")

    @staticmethod
    def configurar_estacionamento():
        print("\n=== CONFIGURAR ESTACIONAMENTO ===")
        config = Config.get_config()

        print(f"Configuração atual:")
        print(f"1. Máximo de vagas: {config['max_vagas']}")
        print(f"2. Taxa por hora: {config['taxa_hora']}")
        print(f"3. Acréscimo percentual: {config['acrescimo_percentual']}%")
        print(f"4. Arredondar hora: {'Sim' if config['arredondar_hora'] else 'Não'}")

        opcao = input("\nDeseja alterar? (s/n): ").lower()
        if opcao == "s":
            max_vagas = int(input("Novo máximo de vagas: "))
            taxa_hora = float(input("Nova taxa por hora: "))
            acrescimo = float(input("Novo acréscimo percentual: "))
            arredondar = input("Arredondar hora? (1-Sim/0-Não): ")

            if Config.atualizar(max_vagas, taxa_hora, acrescimo, int(arredondar)):
                print("Configuração atualizada!")
            else:
                print("Erro ao atualizar!")

    @staticmethod
    def ver_relatorios():
        print("\n=== RELATÓRIOS ===")
        print("1. Veículos no estacionamento")
        print("2. Histórico de veículos")
        print("3. Caixa diário")
        print("4. Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            veiculos = execute_query("SELECT * FROM veiculos WHERE hora_saida IS NULL")
            print("\nVeículos no estacionamento:")
            for v in veiculos:
                print(
                    f"Placa: {v['placa']} | Modelo: {v['modelo']} | Entrada: {v['hora_entrada']}"
                )

        elif opcao == "2":
            veiculos = execute_query(
                "SELECT * FROM veiculos ORDER BY hora_saida DESC LIMIT 20"
            )
            print("\nÚltimos 20 veículos:")
            for v in veiculos:
                print(
                    f"Placa: {v['placa']} | Entrada: {v['hora_entrada']} | Saída: {v['hora_saida']} | Valor: R${v['valor_pago']:.2f}"
                )

        elif opcao == "3":
            caixas = execute_query(
                """
                SELECT u.nome, c.data, c.total_recebido 
                FROM caixa c 
                JOIN usuarios u ON c.usuario_id = u.id 
                ORDER BY c.data DESC
            """
            )
            print("\nCaixa diário:")
            for c in caixas:
                print(
                    f"Operador: {c['nome']} | Data: {c['data']} | Total: R${c['total_recebido']:.2f}"
                )
