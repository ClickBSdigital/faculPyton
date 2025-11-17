"""
SISTEMA DE GERENCIAMENTO DE VEÍCULOS - ESTACIONAMENTO PLUS
Sistema completo com controle de usuários, turnos e caixa
"""

import os
import sys

# Adiciona o caminho raiz do projeto ao Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import Database
from models.veiculo import Veiculo


def limpar_tela():
    """Limpa a tela do terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def exibir_login():
    """Exibe tela de login"""
    print("\n" + "=" * 60)
    print("           🚗 SISTEMA DE ESTACIONAMENTO PLUS 🚗")
    print("=" * 60)
    print("                 👤 FAÇA SEU LOGIN")
    print("=" * 60)


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
    print("8. ⚙️   Configurar vagas")
    print("9. 💰  Configurar valores")
    print("10. 💵 Relatório financeiro")
    print("11. 👥  Gerenciar usuários")
    print("12. 💼 Status do caixa")
    print("13. 🆕 Abrir turno")  # NOVA OPÇÃO - ABRIR TURNO
    print("14. 🔄 Fechar turno")  # OPÇÃO RENUMERADA
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

        total_vagas = veiculo.db.get_total_vagas()
        vagas_disponiveis = veiculo.db.get_vagas_disponiveis()
        total_faturamento = veiculo.db.get_total_faturamento()
        faturamento_hoje = veiculo.db.get_faturamento_hoje()

        # Estatísticas de turno se estiver aberto
        if veiculo.turno_aberto:
            saldo_turno = veiculo.db.get_saldo_turno(veiculo.turno_aberto[0])
            vendas_turno = veiculo.db.get_total_vendas_turno(veiculo.turno_aberto[0])
        else:
            saldo_turno = 0
            vendas_turno = 0

        print(f"📊  Total de veículos cadastrados: {total_veiculos}")
        print(f"🅿️   Veículos no estacionamento: {total_estacionados}")
        print(f"✅  Veículos com saída registrada: {total_saidas}")
        print(f"🅿️  Vagas totais: {total_vagas}")
        print(f"✅  Vagas disponíveis: {vagas_disponiveis}")
        print(f"💰  Faturamento total: R$ {total_faturamento:.2f}")
        print(f"📅  Faturamento hoje: R$ {faturamento_hoje:.2f}")

        if veiculo.turno_aberto:
            print(f"💼  Vendas no turno: R$ {vendas_turno:.2f}")
            print(f"💵  Saldo do turno: R$ {saldo_turno:.2f}")

        if total_vagas > 0:
            percentual_ocupacao = (total_estacionados / total_vagas) * 100
            print(f"📈  Ocupação atual: {percentual_ocupacao:.1f}%")

            if percentual_ocupacao >= 90:
                print("🚨  ALERTA: Estacionamento quase lotado!")
            elif percentual_ocupacao >= 80:
                print("⚠️   AVISO: Estacionamento com alta ocupação!")

        print("=" * 50)

    except Exception as e:
        print(f"❌  Erro ao gerar estatísticas: {e}")


def exibir_status_sistema(veiculo):
    """Exibe o status atual do sistema no cabeçalho"""
    try:
        total_vagas = veiculo.db.get_total_vagas()
        vagas_ocupadas = veiculo.db.get_vagas_ocupadas()
        vagas_disponiveis = veiculo.db.get_vagas_disponiveis()
        valor_hora = veiculo.db.get_valor_hora()

        print(
            f"🅿️  VAGAS: {vagas_ocupadas}/{total_vagas} | {vagas_disponiveis} disponíveis"
        )
        print(
            f"💰 VALOR: 1ª hora R$ {valor_hora:.2f} | Extra +R$ {veiculo.db.get_acrescimo_hora_extra():.2f}"
        )

        if veiculo.usuario_logado:
            print(
                f"👤 USUÁRIO: {veiculo.usuario_logado[2]} ({veiculo.usuario_logado[3]})"
            )

        if veiculo.turno_aberto:
            saldo = veiculo.db.get_saldo_turno(veiculo.turno_aberto[0])
            print(f"💼 TURNO: Aberto | Saldo: R$ {saldo:.2f}")
        else:
            print("💼 TURNO: ❌ Fechado - Use a opção 13 para abrir")

    except Exception as e:
        print(f"❌  Erro ao carregar status: {e}")


def pausar():
    """Pausa a execução e aguarda Enter"""
    input("\n⏎  Pressione Enter para continuar...")


def fazer_login(db, veiculo):
    """Realiza o login do usuário"""
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        limpar_tela()
        exibir_login()

        username = input("\n👤 Username: ").strip()
        senha = input("🔒 Senha: ").strip()

        usuario = db.verificar_login(username, senha)

        if usuario:
            veiculo.set_usuario_logado(usuario)
            print(f"\n✅ Login realizado com sucesso!")
            print(f"👋 Bem-vindo(a), {usuario[2]}!")

            # Verifica se há turno aberto
            turno_aberto = db.get_turno_aberto()
            if turno_aberto:
                veiculo.set_turno_aberto(turno_aberto)
                print(f"💼 Turno já está aberto desde {turno_aberto[2]}")
            else:
                print("💼 Nenhum turno aberto. Use a opção 13 para abrir um turno.")

            pausar()
            return True
        else:
            tentativas += 1
            tentativas_restantes = max_tentativas - tentativas
            print(f"\n❌ Login falhou! Tentativas restantes: {tentativas_restantes}")
            pausar()

    print("\n🚫 Número máximo de tentativas excedido. Sistema encerrado.")
    return False


def verificar_turno_aberto(veiculo):
    """Verifica se há turno aberto, se não, pergunta se quer abrir"""
    if veiculo.turno_aberto:
        return True

    print("\n⚠️  Nenhum turno aberto!")
    print("Para operar o sistema, é necessário abrir um turno.")

    opcao = input("Deseja abrir um turno agora? (s/n): ").lower().strip()

    if opcao == "s":
        veiculo.abrir_turno()
        return veiculo.turno_aberto is not None
    else:
        print("❌ Operação cancelada. É necessário ter um turno aberto.")
        return False


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

    # Realiza login
    if not fazer_login(db, veiculo):
        return

    # Loop principal do sistema
    while True:
        try:
            limpar_tela()
            print("\n" + "=" * 50)
            print("        SISTEMA DE GERENCIAMENTO DE VEÍCULOS")
            print("=" * 50)
            exibir_status_sistema(veiculo)
            exibir_menu_principal()

            opcao = input("\n🎯  Digite a opção desejada: ").strip()

            # Operações que requerem turno aberto
            operacoes_com_turno = ["1", "6"]

            if opcao in operacoes_com_turno and not verificar_turno_aberto(veiculo):
                pausar()
                continue

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

            elif opcao == "8":
                limpar_tela()
                veiculo.configurar_vagas()
                pausar()

            elif opcao == "9":
                limpar_tela()
                veiculo.configurar_valores()
                pausar()

            elif opcao == "10":
                limpar_tela()
                veiculo.relatorio_financeiro()
                pausar()

            elif opcao == "11":  # Gerenciar usuários
                limpar_tela()
                veiculo.gerenciar_usuarios()
                # Não pausa aqui porque o método já tem seu próprio loop

            elif opcao == "12":  # Status do caixa
                limpar_tela()
                veiculo.status_caixa()
                pausar()

            elif opcao == "13":  # NOVO - Abrir turno
                limpar_tela()
                if veiculo.turno_aberto:
                    print("❌ Já existe um turno aberto!")
                    print(f"💼 Turno atual aberto desde: {veiculo.turno_aberto[2]}")
                    print("⚠️  Feche o turno atual antes de abrir um novo.")
                else:
                    veiculo.abrir_turno()
                pausar()

            elif opcao == "14":  # Fechar turno (renumerado)
                limpar_tela()
                veiculo.fechar_turno()
                pausar()

            elif opcao == "0":
                # Verifica se há turno aberto antes de sair
                if veiculo.turno_aberto:
                    print("\n⚠️  ATENÇÃO: Há um turno aberto!")
                    opcao_sair = input(
                        "Deseja fechar o turno antes de sair? (s/n): "
                    ).lower()
                    if opcao_sair == "s":
                        veiculo.fechar_turno()
                    else:
                        print(
                            "⚠️  Turno deixado aberto. Não esqueça de fechá-lo depois!"
                        )

                print("\n👋  Obrigado por usar o Sistema de Estacionamento Plus!")
                print("    Até mais! 👋")
                break

            else:
                print("❌ Opção inválida! Tente novamente.")
                pausar()

        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupção detectada!")
            confirmacao = input("Deseja realmente sair? (s/n): ").lower()
            if confirmacao == "s":
                print("👋  Sistema finalizado pelo usuário!")
                break

        except Exception as e:
            print(f"❌  Erro inesperado: {e}")
            print("💡  O sistema continuará funcionando...")
            pausar()


if __name__ == "__main__":
    main()
