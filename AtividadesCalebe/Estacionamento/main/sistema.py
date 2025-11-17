"""
SISTEMA DE GERENCIAMENTO DE VEÍCULOS
Sistema para controle de entrada e saída de veículos em estacionamento
"""

import os
import sys

# CORREÇÃO: Adiciona o caminho raiz do projeto ao Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Agora os imports vão funcionar
from database.database import Database
from models.veiculo import Veiculo


def limpar_tela():
    """Limpa a tela do terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def exibir_menu_principal():
    """Exibe o menu principal do sistema"""
    print("\n" + "=" * 50)
    print("        SISTEMA DE GERENCIAMENTO DE VEÍCULOS")
    print("=" * 50)
    print("1. 🚗  Cadastrar veículo")
    print("2. 📊  Listar todos os veículos")
    print("3. 🅿️   Veículos no estacionamento")
    print("4. ✏️   Atualizar veículo")
    print("5. 🗑️   Excluir veículo")
    print("6. 🚪  Registrar saída de veículo")
    print("7. 📈  Estatísticas do sistema")
    print("0. 👋  Sair do sistema")
    print("=" * 50)


def exibir_estatisticas(veiculo):
    """Exibe estatísticas do sistema"""
    try:
        print("\n" + "=" * 50)
        print("           ESTATÍSTICAS DO SISTEMA")
        print("=" * 50)

        todos_veiculos = veiculo.db.buscar_dados("SELECT * FROM veiculos")
        total_veiculos = len(todos_veiculos) if todos_veiculos else 0

        estacionados = veiculo.db.buscar_dados(
            "SELECT * FROM veiculos WHERE hora_saida IS NULL"
        )
        total_estacionados = len(estacionados) if estacionados else 0

        saidas = veiculo.db.buscar_dados(
            "SELECT * FROM veiculos WHERE hora_saida IS NOT NULL"
        )
        total_saidas = len(saidas) if saidas else 0

        print(f"📊  Total de veículos cadastrados: {total_veiculos}")
        print(f"🅿️   Veículos no estacionamento: {total_estacionados}")
        print(f"✅  Veículos com saída registrada: {total_saidas}")

        if total_veiculos > 0:
            percentual_estacionados = (total_estacionados / total_veiculos) * 100
            print(f"📈  Ocupação atual: {percentual_estacionados:.1f}%")

        print("=" * 50)

    except Exception as e:
        print(f"❌  Erro ao gerar estatísticas: {e}")


def pausar():
    """Pausa a execução e aguarda Enter"""
    input("\n⏎  Pressione Enter para continuar...")


def main():
    """Função principal do sistema"""
    # Inicializa o sistema
    try:
        print("🔧  Inicializando sistema...")
        db = Database()
        veiculo = Veiculo(db)
        print("✅  Sistema inicializado com sucesso!")
    except Exception as e:
        print(f"❌  Erro ao inicializar sistema: {e}")
        return

    # Loop principal do sistema
    while True:
        try:
            limpar_tela()
            exibir_menu_principal()

            opcao = input("\n🎯  Digite a opção desejada: ").strip()

            if opcao == "1":
                limpar_tela()
                veiculo.cadastrar()
                pausar()

            elif opcao == "2":
                limpar_tela()
                veiculo.listar()
                pausar()

            elif opcao == "3":
                limpar_tela()
                veiculo.listar_estacionados()
                pausar()

            elif opcao == "4":
                limpar_tela()
                veiculo.atualizar()
                pausar()

            elif opcao == "5":
                limpar_tela()
                veiculo.excluir()
                pausar()

            elif opcao == "6":
                limpar_tela()
                veiculo.registrar_saida()
                pausar()

            elif opcao == "7":
                limpar_tela()
                exibir_estatisticas(veiculo)
                pausar()

            elif opcao == "0":
                print("\n👋  Obrigado por usar o sistema! Até mais!")
                break

            else:
                print("❌ Opção inválida! Tente novamente.")
                pausar()

        except KeyboardInterrupt:
            print("\n\n👋  Sistema finalizado pelo usuário!")
            break
        except Exception as e:
            print(f"❌  Erro inesperado: {e}")
            pausar()


if __name__ == "__main__":
    main()
