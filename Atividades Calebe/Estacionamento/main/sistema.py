#!/usr/bin/env python3
"""
SISTEMA DE GERENCIAMENTO DE VEÍCULOS
Autor: [Seu Nome]
Disciplina: [Nome da Disciplina]
Professor: [Nome do Professor]

Sistema para controle de entrada e saída de veículos em estacionamento
"""

import os
import sys
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Importa as classes do sistema
from database.database import Database
from models.veiculo import Veiculo


def limpar_tela():
    """Limpa a tela do terminal de forma cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_cabecalho():
    """Exibe o cabeçalho do sistema"""
    print("\n" + "═" * 60)
    print("🎯  SISTEMA DE GERENCIAMENTO DE VEÍCULOS  🎯")
    print("═" * 60)


def exibir_menu_principal():
    """Exibe o menu principal do sistema"""
    print("\n📋  MENU PRINCIPAL")
    print("─" * 40)
    print("1.  🚗  Cadastrar veículo")
    print("2.  📊  Listar todos os veículos")
    print("3.  🅿️   Veículos no estacionamento")
    print("4.  ✏️   Atualizar veículo")
    print("5.  🗑️   Excluir veículo")
    print("6.  🚪  Registrar saída de veículo")
    print("7.  📈  Estatísticas do sistema")
    print("8.  ℹ️   Sobre o sistema")
    print("0.  👋  Sair do sistema")
    print("─" * 40)


def exibir_estatisticas(veiculo):
    """Exibe estatísticas do sistema"""
    try:
        print("\n" + "📈" + "─" * 50 + "📈")
        print("           ESTATÍSTICAS DO SISTEMA")
        print("─" * 52)
        
        # Busca todos os veículos
        todos_veiculos = veiculo.db.buscar_dados("SELECT * FROM veiculos")
        total_veiculos = len(todos_veiculos) if todos_veiculos else 0
        
        # Busca veículos estacionados
        estacionados = veiculo.db.buscar_dados(
            "SELECT * FROM veiculos WHERE hora_saida IS NULL"
        )
        total_estacionados = len(estacionados) if estacionados else 0
        
        # Busca veículos que já saíram
        saidas = veiculo.db.buscar_dados(
            "SELECT * FROM veiculos WHERE hora_saida IS NOT NULL"
        )
        total_saidas = len(saidas) if saidas else 0
        
        print(f"📊  Total de veículos cadastrados: {total_veiculos}")
        print(f"🅿️   Veículos no estacionamento: {total_estacionados}")
        print(f"✅  Veículos com saída registrada: {total_saidas}")
        
        if total_veiculos > 0:
            percentual_estacionados = (total_estacionados / total_veiculos) * 100
            print(f"📊  Ocupação atual: {percentual_estacionados:.1f}%")
        
        # Veículo mais recente
        if todos_veiculos:
            mais_recente = max(todos_veiculos, key=lambda x: x[4])  # hora_entrada
            print(f"\n🆕  Último veículo cadastrado:")
            print(f"    Placa: {mais_recente[1]} - Modelo: {mais_recente[2]}")
        
        print("─" * 52)
        
    except Exception as e:
        print(f"❌  Erro ao gerar estatísticas: {e}")


def exibir_sobre():
    """Exibe informações sobre o sistema"""
    print("\n" + "ℹ️ " + "─" * 50 + "ℹ️")
    print("              SOBRE O SISTEMA")
    print("─" * 52)
    print("🎓  Desenvolvido por: [Seu Nome]")
    print("📚  Disciplina: [Nome da Disciplina]")
    print("👨‍🏫  Professor: [Nome do Professor]")
    print("📅  Data: 2024")
    print("─" * 52)
    print("💻  Tecnologias utilizadas:")
    print("    • Python 3.x")
    print("    • SQLite3")
    print("    • Programação Orientada a Objetos")
    print("    • Arquitetura em Camadas")
    print("─" * 52)
    print("🎯  Funcionalidades:")
    print("    • Cadastro de veículos (CREATE)")
    print("    • Listagem de veículos (READ)")
    print("    • Atualização de dados (UPDATE)")
    print("    • Exclusão de registros (DELETE)")
    print("    • Controle de entrada/saída")
    print("    • Estatísticas em tempo real")
    print("─" * 52)


def confirmar_saida():
    """Solicita confirmação antes de sair do sistema"""
    print("\n⚠️  CONFIRMAÇÃO DE SAÍDA")
    print("─" * 30)
    confirmacao = input("Tem certeza que deseja sair do sistema? (s/n): ").lower().strip()
    return confirmacao == 's'


def pausar():
    """Pausa a execução e aguarda Enter"""
    input("\n⏎  Pressione Enter para continuar...")


def inicializar_sistema():
    """Inicializa todos os componentes do sistema"""
    try:
        print("🔧  Inicializando sistema...")
        
        # Inicializa o banco de dados
        db = Database()
        print("✅  Banco de dados conectado")
        
        # Inicializa a classe Veiculo
        veiculo = Veiculo(db)
        print("✅  Módulo de veículos carregado")
        
        print("🎉  Sistema inicializado com sucesso!")
        return veiculo
        
    except Exception as e:
        print(f"❌  Erro ao inicializar sistema: {e}")
        print("💡  Verifique se o Python e SQLite estão instalados corretamente")
        sys.exit(1)


def main():
    """Função principal do sistema"""
    # Inicializa o sistema
    veiculo = inicializar_sistema()
    
    # Loop principal do sistema
    while True:
        try:
            limpar_tela()
            exibir_cabecalho()
            exibir_menu_principal()
            
            opcao = input("\n🎯  Digite a opção desejada (0-8): ").strip()
            
            if opcao == '1':
                limpar_tela()
                exibir_cabecalho()
                veiculo.cadastrar()
                pausar()
                
            elif opcao == '2':
                limpar_tela()
                exibir_cabecalho()
                veiculo.listar()
                pausar()
                
            elif opcao == '3':
                limpar_tela()
                exibir_cabecalho()
                veiculo.listar_estacionados()
                pausar()
                
            elif opcao == '4':
                limpar_tela()
                exibir_cabecalho()
                veiculo.atualizar()
                pausar()
                
            elif opcao == '5':
                limpar_tela()
                exibir_cabecalho()
                veiculo.excluir()
                pausar()
                
            elif opcao == '6':
                limpar_tela()
                exibir_cabecalho()
                veiculo.registrar_saida()
                pausar()
                
            elif opcao == '7':
                limpar_tela()
                exibir_cabecalho()
                exibir_estatisticas(veiculo)
                pausar()
                
            elif opcao == '8':
                limpar_tela()
                exibir_cabecalho()
                exibir_sobre()
                pausar()
                
            elif opcao == '0':
                if confirmar_saida():
                    limpar_tela()
                    print("\n" + "✨" * 25)
                    print("👋  Obrigado por usar o Sistema de Gerenciamento de Veículos!")
                    print("📞  Volte sempre!")
                    print("✨" * 25)
                    break
                else:
                    print("\n✅  Continuando no sistema...")
                    pausar()
                    
            else:
                print("\n❌  Opção inválida! Digite um número entre 0 e 8.")
                pausar()
                
        except KeyboardInterrupt:
            # Captura Ctrl+C e sai gracefully
            print("\n\n⚠️  Interrupção detectada!")
            if confirmar_saida():
                print("👋  Sistema finalizado pelo usuário!")
                break
            else:
                print("✅  Continuando no sistema...")
                
        except Exception as e:
            print(f"\n❌  Erro inesperado: {e}")
            print("💡  O sistema continuará funcionando...")
            pausar()


def verificar_dependencias():
    """Verifica se todas as dependências estão disponíveis"""
    try:
        import sqlite3
        print("✅  SQLite3 disponível")
        return True
    except ImportError:
        print("❌  SQLite3 não disponível")
        return False


if __name__ == "__main__":
    # Verifica dependências antes de executar
    if verificar_dependencias():
        try:
            main()
        except Exception as e:
            print(f"\n💥  Erro crítico no sistema: {e}")
            print("🔧  Entre em contato com o suporte técnico")
            sys.exit(1)
    else:
        print("❌  Dependências não atendidas. Instale o SQLite3.")
        sys.exit(1)