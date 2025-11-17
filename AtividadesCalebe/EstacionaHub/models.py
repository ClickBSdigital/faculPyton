from database import fetch_one, execute_query
from datetime import datetime


class Usuario:
    def __init__(self, id=None, nome=None, usuario=None, senha=None, tipo="operador"):
        self.id = id
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
        self.tipo = tipo

    @staticmethod
    def autenticar(usuario, senha):
        query = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s AND ativo = 1"
        return fetch_one(query, (usuario, senha))

    @staticmethod
    def criar(nome, usuario, senha, tipo="operador"):
        query = (
            "INSERT INTO usuarios (nome, usuario, senha, tipo) VALUES (%s, %s, %s, %s)"
        )
        return execute_query(query, (nome, usuario, senha, tipo))


class Veiculo:
    @staticmethod
    def get_veiculos_ativos():
        query = "SELECT * FROM veiculos WHERE hora_saida IS NULL"
        return execute_query(query) or []

    @staticmethod
    def registrar_entrada(placa, modelo, usuario_id):
        check_query = "SELECT id FROM veiculos WHERE placa = %s AND hora_saida IS NULL"
        if fetch_one(check_query, (placa,)):
            return False

        query = "INSERT INTO veiculos (placa, modelo, usuario_id) VALUES (%s, %s, %s)"
        return execute_query(query, (placa, modelo, usuario_id))

    @staticmethod
    def registrar_saida(placa):
        query = "SELECT * FROM veiculos WHERE placa = %s AND hora_saida IS NULL"
        veiculo = fetch_one(query, (placa,))

        if not veiculo:
            return None

        config = Config.get_config()
        tempo_horas = (datetime.now() - veiculo["hora_entrada"]).total_seconds() / 3600
        valor_pago = config["taxa_hora"] * tempo_horas

        if tempo_horas > 1:
            valor_pago *= 1 + config["acrescimo_percentual"] / 100

        if config["arredondar_hora"]:
            valor_pago = round(valor_pago)

        update_query = """
        UPDATE veiculos 
        SET hora_saida = NOW(), valor_pago = %s 
        WHERE id = %s
        """
        execute_query(update_query, (valor_pago, veiculo["id"]))

        return {"placa": placa, "tempo": tempo_horas, "valor_pago": valor_pago}


class Config:
    @staticmethod
    def get_config():
        return fetch_one("SELECT * FROM config WHERE id = 1")

    @staticmethod
    def atualizar(max_vagas, taxa_hora, acrescimo_percentual, arredondar_hora):
        query = """
        UPDATE config 
        SET max_vagas = %s, taxa_hora = %s, acrescimo_percentual = %s, arredondar_hora = %s 
        WHERE id = 1
        """
        return execute_query(
            query, (max_vagas, taxa_hora, acrescimo_percentual, arredondar_hora)
        )


class Caixa:
    @staticmethod
    def abrir_caixa(usuario_id):
        check_query = (
            "SELECT id FROM caixa WHERE usuario_id = %s AND data = CURRENT_DATE"
        )
        if fetch_one(check_query, (usuario_id,)):
            return False

        query = "INSERT INTO caixa (usuario_id) VALUES (%s)"
        return execute_query(query, (usuario_id,))

    @staticmethod
    def fechar_caixa(usuario_id):
        total_query = """
        SELECT SUM(valor_pago) as total 
        FROM veiculos 
        WHERE usuario_id = %s 
        AND DATE(hora_saida) = CURRENT_DATE
        """
        total = fetch_one(total_query, (usuario_id,))["total"] or 0

        update_query = """
        UPDATE caixa 
        SET total_recebido = %s 
        WHERE usuario_id = %s AND data = CURRENT_DATE
        """
        return execute_query(update_query, (total, usuario_id))

    @staticmethod
    def get_caixa_dia(usuario_id):
        return fetch_one(
            "SELECT * FROM caixa WHERE usuario_id = %s AND data = CURRENT_DATE",
            (usuario_id,),
        )
