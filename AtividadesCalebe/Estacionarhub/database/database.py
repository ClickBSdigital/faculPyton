import sqlite3
from datetime import datetime
import hashlib


class Database:
    """
    Classe para gerenciar o banco de dados do sistema de veículos
    """

    def __init__(self, db_name="veiculos.db"):
        self.db_name = db_name
        self.criar_tabelas()

    def criar_tabelas(self):
        """Cria as tabelas necessárias se não existirem"""
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()

        try:
            # Tabela de usuários (NOVA)
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    senha_hash TEXT NOT NULL,
                    nome TEXT NOT NULL,
                    perfil TEXT NOT NULL,  -- 'admin', 'operador', 'gerente'
                    ativo INTEGER DEFAULT 1
                )
            """
            )

            # Tabela de turnos (NOVA)
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS turnos (
                    id_turno INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER NOT NULL,
                    data_abertura TEXT NOT NULL,
                    data_fechamento TEXT,
                    saldo_inicial REAL NOT NULL,
                    saldo_final REAL,
                    total_vendas REAL DEFAULT 0,
                    total_veiculos INTEGER DEFAULT 0,
                    status TEXT DEFAULT 'aberto',  -- 'aberto', 'fechado'
                    FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
                )
            """
            )

            # Tabela de movimentações de caixa (NOVA)
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS movimentacoes_caixa (
                    id_movimentacao INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_turno INTEGER NOT NULL,
                    id_veiculo INTEGER,
                    tipo TEXT NOT NULL,  -- 'entrada', 'saida', 'venda', 'sangria'
                    valor REAL NOT NULL,
                    descricao TEXT,
                    data_hora TEXT NOT NULL,
                    FOREIGN KEY (id_turno) REFERENCES turnos (id_turno),
                    FOREIGN KEY (id_veiculo) REFERENCES veiculos (id_vei)
                )
            """
            )

            # Tabela de veículos (ATUALIZADA com auditoria)
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS veiculos (
                    id_vei INTEGER PRIMARY KEY AUTOINCREMENT,
                    placa TEXT NOT NULL UNIQUE,
                    modelo TEXT NOT NULL,
                    cor TEXT NOT NULL,
                    hora_entrada TEXT NOT NULL,
                    hora_saida TEXT,
                    valor_pago REAL DEFAULT 0,
                    tempo_permanencia TEXT,
                    id_usuario_entrada INTEGER,  -- NOVO
                    id_usuario_saida INTEGER,    -- NOVO
                    id_turno_entrada INTEGER,    -- NOVO
                    id_turno_saida INTEGER,      -- NOVO
                    FOREIGN KEY (id_usuario_entrada) REFERENCES usuarios (id_usuario),
                    FOREIGN KEY (id_usuario_saida) REFERENCES usuarios (id_usuario),
                    FOREIGN KEY (id_turno_entrada) REFERENCES turnos (id_turno),
                    FOREIGN KEY (id_turno_saida) REFERENCES turnos (id_turno)
                )
            """
            )

            # Tabela de configurações
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS config (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chave TEXT UNIQUE NOT NULL,
                    valor TEXT NOT NULL
                )
            """
            )

            # Insere configurações padrão se não existirem
            configs_padrao = [
                ("total_vagas", "20"),
                ("valor_hora", "10.00"),
                ("acrescimo_hora_extra", "2.00"),
                ("tolerancia_minutos", "15"),
                ("saldo_inicial_caixa", "100.00"),  # NOVO
            ]

            for chave, valor in configs_padrao:
                cursor.execute(
                    """
                    INSERT OR IGNORE INTO config (chave, valor) 
                    VALUES (?, ?)
                """,
                    (chave, valor),
                )

            # Insere usuário admin padrão (NOVO)
            senha_admin = self.hash_senha("admin123")
            cursor.execute(
                """
                INSERT OR IGNORE INTO usuarios (username, senha_hash, nome, perfil) 
                VALUES (?, ?, ?, ?)
            """,
                ("admin", senha_admin, "Administrador", "admin"),
            )

            conexao.commit()
            print("✅ Todas as tabelas verificadas/criadas com sucesso!")

        except sqlite3.Error as erro:
            print(f"❌ Erro ao criar tabelas: {erro}")
        finally:
            conexao.close()

    # MÉTODOS DE AUTENTICAÇÃO (NOVOS)
    def hash_senha(self, senha):
        """Gera hash da senha"""
        return hashlib.sha256(senha.encode()).hexdigest()

    def verificar_login(self, username, senha):
        """Verifica credenciais de login"""
        senha_hash = self.hash_senha(senha)
        query = "SELECT id_usuario, username, nome, perfil FROM usuarios WHERE username = ? AND senha_hash = ? AND ativo = 1"
        return self.buscar_um(query, (username, senha_hash))

    def criar_usuario(self, username, senha, nome, perfil):
        """Cria novo usuário"""
        senha_hash = self.hash_senha(senha)
        query = "INSERT INTO usuarios (username, senha_hash, nome, perfil) VALUES (?, ?, ?, ?)"
        return self.executar_query(query, (username, senha_hash, nome, perfil))

    def listar_usuarios(self):
        """Lista todos os usuários"""
        return self.buscar_dados(
            "SELECT id_usuario, username, nome, perfil, ativo FROM usuarios ORDER BY username"
        )

    # MÉTODOS DE TURNOS (NOVOS)
    def abrir_turno(self, id_usuario, saldo_inicial):
        """Abre um novo turno"""
        data_abertura = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = """
            INSERT INTO turnos (id_usuario, data_abertura, saldo_inicial, status) 
            VALUES (?, ?, ?, 'aberto')
        """
        sucesso = self.executar_query(query, (id_usuario, data_abertura, saldo_inicial))
        if sucesso:
            return self.buscar_um("SELECT last_insert_rowid()")[0]
        return None

    def fechar_turno(self, id_turno, saldo_final):
        """Fecha um turno"""
        data_fechamento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = """
            UPDATE turnos 
            SET data_fechamento = ?, saldo_final = ?, status = 'fechado' 
            WHERE id_turno = ?
        """
        return self.executar_query(query, (data_fechamento, saldo_final, id_turno))

    def get_turno_aberto(self):
        """Retorna o turno atualmente aberto"""
        return self.buscar_um(
            "SELECT * FROM turnos WHERE status = 'aberto' ORDER BY id_turno DESC LIMIT 1"
        )

    def registrar_movimentacao(self, id_turno, tipo, valor, descricao, id_veiculo=None):
        """Registra movimentação no caixa"""
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = """
            INSERT INTO movimentacoes_caixa (id_turno, id_veiculo, tipo, valor, descricao, data_hora)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        return self.executar_query(
            query, (id_turno, id_veiculo, tipo, valor, descricao, data_hora)
        )

    def get_saldo_turno(self, id_turno):
        """Calcula saldo atual do turno"""
        # Saldo inicial + todas as entradas - todas as saídas
        query = """
            SELECT 
                t.saldo_inicial + 
                COALESCE(SUM(CASE WHEN m.tipo IN ('venda', 'entrada') THEN m.valor ELSE 0 END), 0) -
                COALESCE(SUM(CASE WHEN m.tipo IN ('saida', 'sangria') THEN m.valor ELSE 0 END), 0) as saldo_atual
            FROM turnos t
            LEFT JOIN movimentacoes_caixa m ON t.id_turno = m.id_turno
            WHERE t.id_turno = ?
            GROUP BY t.id_turno
        """
        resultado = self.buscar_um(query, (id_turno,))
        return resultado[0] if resultado else 0

    def get_total_vendas_turno(self, id_turno):
        """Retorna total de vendas do turno"""
        query = "SELECT COALESCE(SUM(valor), 0) FROM movimentacoes_caixa WHERE id_turno = ? AND tipo = 'venda'"
        resultado = self.buscar_um(query, (id_turno,))
        return resultado[0] if resultado else 0

    # MÉTODOS EXISTENTES (ATUALIZADOS)
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
            print("❌ Erro: Dados duplicados ou inválidos!")
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

    # MÉTODOS EXISTENTES (mantidos)
    def verificar_placa_existe(self, placa):
        """Verifica se uma placa já existe no banco de dados"""
        query = "SELECT id_vei FROM veiculos WHERE placa = ?"
        resultado = self.buscar_um(query, (placa,))
        return resultado is not None

    def get_total_vagas(self):
        """Retorna o número total de vagas configurado"""
        query = "SELECT valor FROM config WHERE chave = 'total_vagas'"
        resultado = self.buscar_um(query)
        return int(resultado[0]) if resultado else 20

    def set_total_vagas(self, total_vagas):
        """Define o número total de vagas"""
        query = "INSERT OR REPLACE INTO config (chave, valor) VALUES ('total_vagas', ?)"
        return self.executar_query(query, (str(total_vagas),))

    def get_vagas_ocupadas(self):
        """Retorna o número de vagas ocupadas (veículos sem saída)"""
        query = "SELECT COUNT(*) FROM veiculos WHERE hora_saida IS NULL"
        resultado = self.buscar_um(query)
        return resultado[0] if resultado else 0

    def get_vagas_disponiveis(self):
        """Retorna o número de vagas disponíveis"""
        total_vagas = self.get_total_vagas()
        vagas_ocupadas = self.get_vagas_ocupadas()
        return total_vagas - vagas_ocupadas

    def tem_vaga_disponivel(self):
        """Verifica se há vaga disponível"""
        return self.get_vagas_disponiveis() > 0

    def get_valor_hora(self):
        """Retorna o valor da hora"""
        query = "SELECT valor FROM config WHERE chave = 'valor_hora'"
        resultado = self.buscar_um(query)
        return float(resultado[0]) if resultado else 10.00

    def set_valor_hora(self, valor):
        """Define o valor da hora"""
        query = "INSERT OR REPLACE INTO config (chave, valor) VALUES ('valor_hora', ?)"
        return self.executar_query(query, (str(valor),))

    def get_acrescimo_hora_extra(self):
        """Retorna o acréscimo por hora extra"""
        query = "SELECT valor FROM config WHERE chave = 'acrescimo_hora_extra'"
        resultado = self.buscar_um(query)
        return float(resultado[0]) if resultado else 2.00

    def set_acrescimo_hora_extra(self, valor):
        """Define o acréscimo por hora extra"""
        query = "INSERT OR REPLACE INTO config (chave, valor) VALUES ('acrescimo_hora_extra', ?)"
        return self.executar_query(query, (str(valor),))

    def get_tolerancia_minutos(self):
        """Retorna a tolerância em minutos"""
        query = "SELECT valor FROM config WHERE chave = 'tolerancia_minutos'"
        resultado = self.buscar_um(query)
        return int(resultado[0]) if resultado else 15

    def set_tolerancia_minutos(self, minutos):
        """Define a tolerância em minutos"""
        query = "INSERT OR REPLACE INTO config (chave, valor) VALUES ('tolerancia_minutos', ?)"
        return self.executar_query(query, (str(minutos),))

    def get_saldo_inicial_caixa(self):
        """Retorna saldo inicial padrão do caixa"""
        query = "SELECT valor FROM config WHERE chave = 'saldo_inicial_caixa'"
        resultado = self.buscar_um(query)
        return float(resultado[0]) if resultado else 100.00

    def calcular_valor_a_pagar(self, hora_entrada, hora_saida):
        """Calcula o valor a pagar baseado no tempo de permanência"""
        try:
            entrada = datetime.strptime(hora_entrada, "%Y-%m-%d %H:%M:%S")
            saida = datetime.strptime(hora_saida, "%Y-%m-%d %H:%M:%S")

            # Calcula diferença em minutos
            diferenca = saida - entrada
            minutos_totais = diferenca.total_seconds() / 60

            # Aplica tolerância
            tolerancia = self.get_tolerancia_minutos()
            minutos_cobrados = max(0, minutos_totais - tolerancia)

            # Calcula horas (arredonda para cima)
            horas = (minutos_cobrados + 59) // 60  # Arredonda para cima

            valor_hora = self.get_valor_hora()
            acrescimo = self.get_acrescimo_hora_extra()

            if horas <= 1:
                return valor_hora, horas, minutos_totais

            # Primeira hora + acréscimo pelas horas extras
            valor_total = valor_hora + ((horas - 1) * acrescimo)
            return valor_total, horas, minutos_totais

        except Exception as e:
            print(f"❌ Erro no cálculo: {e}")
            return 0, 0, 0

    def registrar_pagamento(
        self, placa, valor_pago, tempo_permanencia, id_usuario_saida, id_turno_saida
    ):
        """Registra o pagamento do veículo com auditoria"""
        query = """
            UPDATE veiculos 
            SET valor_pago = ?, tempo_permanencia = ?, id_usuario_saida = ?, id_turno_saida = ?
            WHERE placa = ?
        """
        return self.executar_query(
            query,
            (valor_pago, tempo_permanencia, id_usuario_saida, id_turno_saida, placa),
        )

    def get_total_faturamento(self):
        """Retorna o faturamento total do sistema"""
        query = "SELECT SUM(valor_pago) FROM veiculos WHERE valor_pago > 0"
        resultado = self.buscar_um(query)
        return resultado[0] if resultado[0] else 0.0

    def get_faturamento_hoje(self):
        """Retorna o faturamento do dia atual"""
        hoje = datetime.now().strftime("%Y-%m-%d")
        query = """
            SELECT SUM(valor_pago) FROM veiculos 
            WHERE DATE(hora_saida) = ? AND valor_pago > 0
        """
        resultado = self.buscar_um(query, (hoje,))
        return resultado[0] if resultado[0] else 0.0


if __name__ == "__main__":
    db = Database()
    print("🎉 Banco de dados inicializado com sucesso!")
    print(f"👤 Usuário admin criado: admin / admin123")
