import sqlite3
from datetime import datetime


class Database:
    """
    Classe para gerenciar o banco de dados do sistema de veículos
    """

    def __init__(self, db_name="veiculos.db"):
        self.db_name = db_name
        self.criar_tabela()

    def criar_tabela(self):
        """Cria a tabela veiculos se ela não existir"""
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()

        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS veiculos (
                    id_vei INTEGER PRIMARY KEY AUTOINCREMENT,
                    placa TEXT NOT NULL UNIQUE,
                    modelo TEXT NOT NULL,
                    cor TEXT NOT NULL,
                    hora_entrada TEXT NOT NULL,
                    hora_saida TEXT
                )
            """
            )
            conexao.commit()
            print("✅ Tabela 'veiculos' verificada/criada com sucesso!")

        except sqlite3.Error as erro:
            print(f"❌ Erro ao criar tabela: {erro}")
        finally:
            conexao.close()

    def executar_query(self, query, params=()):
        """Executa comandos SQL que modificam o banco"""
        try:
            conexao = sqlite3.connect(self.db_name)
            cursor = conexao.cursor()
            cursor.execute(query, params)
            conexao.commit()
            conexao.close()
            return True
        except sqlite3.IntegrityError:
            print("❌ Erro: Placa já existe no sistema!")
            return False
        except sqlite3.Error as erro:
            print(f"❌ Erro no banco de dados: {erro}")
            return False

    def buscar_dados(self, query, params=()):
        """Executa consultas SQL que retornam dados"""
        try:
            conexao = sqlite3.connect(self.db_name)
            cursor = conexao.cursor()
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            conexao.close()
            return resultados
        except sqlite3.Error as erro:
            print(f"❌ Erro na consulta: {erro}")
            return []

    def buscar_um(self, query, params=()):
        """Busca apenas um registro"""
        try:
            conexao = sqlite3.connect(self.db_name)
            cursor = conexao.cursor()
            cursor.execute(query, params)
            resultado = cursor.fetchone()
            conexao.close()
            return resultado
        except sqlite3.Error as erro:
            print(f"❌ Erro na consulta: {erro}")
            return None

    def verificar_placa_existe(self, placa):
        """Verifica se uma placa já existe no banco de dados"""
        query = "SELECT id_vei FROM veiculos WHERE placa = ?"
        resultado = self.buscar_um(query, (placa,))
        return resultado is not None


if __name__ == "__main__":
    db = Database()
    print("🎉 Banco de dados inicializado com sucesso!")
