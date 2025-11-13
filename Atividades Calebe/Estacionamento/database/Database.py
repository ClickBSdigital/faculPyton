import sqlite3
from datetime import datetime

class Database:
    """
    Classe para gerenciar o banco de dados do sistema de veículos
    Responsável por todas as operações com o SQLite
    """
    
    def __init__(self, db_name='veiculos.db'):
        """
        Inicializa a conexão com o banco de dados
        Args:
            db_name (str): Nome do arquivo do banco de dados
        """
        self.db_name = db_name
        self.criar_tabela()
    
    def criar_tabela(self):
        """
        Cria a tabela 'veiculos' se ela não existir
        Esta função é executada automaticamente quando a classe é instanciada
        """
        # Conecta ao banco de dados (cria o arquivo se não existir)
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        
        try:
            # SQL para criar a tabela veiculos
            sql_criar_tabela = '''
                CREATE TABLE IF NOT EXISTS veiculos (
                    id_vei INTEGER PRIMARY KEY AUTOINCREMENT,
                    placa TEXT NOT NULL UNIQUE,
                    modelo TEXT NOT NULL,
                    cor TEXT NOT NULL,
                    hora_entrada TEXT NOT NULL,
                    hora_saida TEXT
                )
            '''
            
            # Executa o comando SQL
            cursor.execute(sql_criar_tabela)
            
            # Confirma as alterações no banco
            conexao.commit()
            print("✅ Tabela 'veiculos' verificada/criada com sucesso!")
            
        except sqlite3.Error as erro:
            print(f"❌ Erro ao criar tabela: {erro}")
            
        finally:
            # Fecha a conexão com o banco (importante para evitar vazamentos)
            conexao.close()
    
    def conectar(self):
        """
        Cria e retorna uma conexão com o banco de dados
        Returns:
            tuple: (conexao, cursor) para operações no banco
        """
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        return conexao, cursor
    
    def executar_query(self, query, params=()):
        """
        Executa comandos SQL que modificam o banco (INSERT, UPDATE, DELETE)
        
        Args:
            query (str): Comando SQL a ser executado
            params (tuple): Parâmetros para evitar SQL Injection
            
        Returns:
            bool: True se bem-sucedido, False se houve erro
        """
        try:
            conexao, cursor = self.conectar()
            
            # Executa a query com os parâmetros
            cursor.execute(query, params)
            
            # Confirma as alterações
            conexao.commit()
            return True
            
        except sqlite3.IntegrityError:
            print("❌ Erro: Placa já existe no sistema!")
            return False
            
        except sqlite3.Error as erro:
            print(f"❌ Erro no banco de dados: {erro}")
            return False
            
        finally:
            # Garante que a conexão será fechada mesmo se houver erro
            if 'conexao' in locals():
                conexao.close()
    
    def buscar_dados(self, query, params=()):
        """
        Executa consultas SQL que retornam dados (SELECT)
        
        Args:
            query (str): Comando SQL de consulta
            params (tuple): Parâmetros para evitar SQL Injection
            
        Returns:
            list: Lista com os resultados da consulta
        """
        try:
            conexao, cursor = self.conectar()
            
            # Executa a consulta
            cursor.execute(query, params)
            
            # Pega todos os resultados
            resultados = cursor.fetchall()
            return resultados
            
        except sqlite3.Error as erro:
            print(f"❌ Erro na consulta: {erro}")
            return []
            
        finally:
            # Garante que a conexão será fechada
            if 'conexao' in locals():
                conexao.close()
    
    def buscar_um(self, query, params=()):
        """
        Busca apenas um registro (útil para buscar por ID ou placa)
        
        Args:
            query (str): Comando SQL
            params (tuple): Parâmetros
            
        Returns:
            tuple: Um único registro ou None se não encontrado
        """
        try:
            conexao, cursor = self.conectar()
            cursor.execute(query, params)
            resultado = cursor.fetchone()
            return resultado
            
        except sqlite3.Error as erro:
            print(f"❌ Erro na consulta: {erro}")
            return None
            
        finally:
            if 'conexao' in locals():
                conexao.close()
                
    

    def verificar_placa_existe(self, placa):
        """
        Verifica se uma placa já existe no banco de dados
        
        Args:
            placa (str): Placa a ser verificada
            
        Returns:
            bool: True se existe, False se não existe
        """
        query = "SELECT id_vei FROM veiculos WHERE placa = ?"
        resultado = self.buscar_um(query, (placa,))
        return resultado is not None
    
    def __init__(self, vagas_totais=10):
        self.vagas_totais = vagas_totais
        self.veiculos_estacionados = []  # lista de objetos Veiculo
        self.veiculos_saida = []          # histórico de saídas
        
    def adicionar_veiculo(self, veiculo):
        if len(self.veiculos_estacionados) >= self.vagas_totais:
            print("🚫 Estacionamento LOTADO! Não é possível adicionar mais veículos.")
            return False
        self.veiculos_estacionados.append(veiculo)
        print(f"✅ {veiculo.placa} estacionado com sucesso.")
        return True
    
    def remover_veiculo(self, placa):
        for v in self.veiculos_estacionados:
        if v.placa == placa:
            self.veiculos_estacionados.remove(v)
            self.veiculos_saida.append(v)
            print(f"🚗 {placa} saiu do estacionamento.")
            return True
        print("⚠️ Veículo não encontrado.")
        return False


# Teste simples da classe
if __name__ == "__main__":
    # Teste rápido para verificar se está funcionando
    db = Database()
    print("🎉 Banco de dados inicializado com sucesso!")