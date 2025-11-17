from models import Veiculo, Caixa, Config
from auth import AuthSystem


class OperatorSystem:
    @staticmethod
    def menu():
        print("\n=== MENU OPERADOR ===")
        print("1. Registrar Entrada")
        print("2. Registrar Saída")
        print("3. Abrir Caixa")
        print("4. Fechar Caixa")
        print("5. Ver Status")
        print("6. Sair")

    @staticmethod
    def registrar_entrada():
        print("\n=== REGISTRAR ENTRADA ===")
        placa = input("Placa: ").upper()
        modelo = input("Modelo: ")

        # Verifica vagas disponíveis
        config = Config.get_config()
        vagas_ocupadas = len(Veiculo.get_veiculos_ativos())

        if vagas_ocupadas >= config["max_vagas"]:
            print("Estacionamento lotado!")
            return

        if Veiculo.registrar_entrada(placa, modelo, AuthSystem.usuario_atual.id):
            print("Entrada registrada com sucesso!")
        else:
            print("Veículo já está no estacionamento!")

    @staticmethod
    def registrar_saida():
        print("\n=== REGISTRAR SAÍDA ===")
        placa = input("Placa: ").upper()

        resultado = Veiculo.registrar_saida(placa)
        if resultado:
            print(f"\nSaída registrada!")
            print(f"Placa: {resultado['placa']}")
            print(f"Tempo: {resultado['tempo']:.2f} horas")
            print(f"Valor a pagar: R${resultado['valor_pago']:.2f}")
        else:
            print("Veículo não encontrado ou já registrou saída!")

    @staticmethod
    def abrir_caixa():
        if Caixa.abrir_caixa(AuthSystem.usuario_atual.id):
            print("Caixa aberto com sucesso!")
        else:
            print("Caixa já foi aberto hoje!")

    @staticmethod
    def fechar_caixa():
        if Caixa.fechar_caixa(AuthSystem.usuario_atual.id):
            caixa = Caixa.get_caixa_dia(AuthSystem.usuario_atual.id)
            print(f"\nCaixa fechado!")
            print(f"Total recebido: R${caixa['total_recebido']:.2f}")
        else:
            print("Erro ao fechar caixa!")

    @staticmethod
    def ver_status():
        config = Config.get_config()
        vagas_ocupadas = len(Veiculo.get_veiculos_ativos())
        vagas_disponiveis = config["max_vagas"] - vagas_ocupadas

        print("\n=== STATUS ===")
        print(f"Vagas ocupadas: {vagas_ocupadas}")
        print(f"Vagas disponíveis: {vagas_disponiveis}")
        print(f"Taxa por hora: R${config['taxa_hora']:.2f}")
        print(f"Acréscimo: {config['acrescimo_percentual']}%")

        caixa = Caixa.get_caixa_dia(AuthSystem.usuario_atual.id)
        if caixa:
            print(f"Caixa aberto: R${caixa['total_recebido']:.2f}")
        else:
            print("Caixa ainda não foi aberto hoje!")
