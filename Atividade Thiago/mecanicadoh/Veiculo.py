from Database import Database

class Veiculo:
    def __init__(self, id_veiculo=None, id_cliente=None, marca=None, modelo=None, ano=None, placa=None, cor=None, km_rodados=None):
        self.id_veiculo = id_veiculo
        self.id_cliente = id_cliente
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.km_rodados = km_rodados
        self.db = Database()

    def cadastrar(self):
        """Cadastra um novo veículo"""
        try:
            if not self.db.connect():
                return False
                
            tupla = (self.id_cliente, self.marca, self.modelo, self.ano, self.placa, self.cor, self.km_rodados)
            self.db.cursor.execute(
                "INSERT INTO veiculo (id_cliente, marca, modelo, ano, placa, cor, km_rodados) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                tupla
            )
            self.db.conn.commit()
            print("✅ Veículo cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao cadastrar veículo: {e}")
            return False
        finally:
            self.db.close_connection()

    def buscar_todos(self):
        """Busca todos os veículos"""
        try:
            if not self.db.connect():
                return []
                
            self.db.cursor.execute("""
                SELECT v.*, c.nome as cliente_nome 
                FROM veiculo v 
                LEFT JOIN cliente c ON v.id_cliente = c.id_cli
            """)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar veículos: {e}")
            return []
        finally:
            self.db.close_connection()

    def buscar_por_id(self, id_veiculo):
        """Busca um veículo específico por ID"""
        try:
            if not self.db.connect():
                return None
                
            self.db.cursor.execute("SELECT * FROM veiculo WHERE id_veiculo = %s", (id_veiculo,))
            result = self.db.cursor.fetchone()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar veículo por ID: {e}")
            return None
        finally:
            self.db.close_connection()

    def buscar_por_cliente(self, id_cliente):
        """Busca veículos de um cliente específico"""
        try:
            if not self.db.connect():
                return []
                
            self.db.cursor.execute("SELECT * FROM veiculo WHERE id_cliente = %s", (id_cliente,))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar veículos do cliente: {e}")
            return []
        finally:
            self.db.close_connection()

    def excluir(self, id_veiculo):
        """Exclui um veículo por ID"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("DELETE FROM veiculo WHERE id_veiculo = %s", (id_veiculo,))
            self.db.conn.commit()
            print("✅ Veículo excluído com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao excluir veículo: {e}")
            return False
        finally:
            self.db.close_connection()

    def atualizar(self):
        """Atualiza os dados do veículo"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("""
                UPDATE veiculo SET id_cliente = %s, marca = %s, modelo = %s, ano = %s, 
                placa = %s, cor = %s, km_rodados = %s
                WHERE id_veiculo = %s
            """, (self.id_cliente, self.marca, self.modelo, self.ano, self.placa, self.cor, self.km_rodados, self.id_veiculo))
            self.db.conn.commit()
            print("✅ Veículo atualizado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao atualizar veículo: {e}")
            return False
        finally:
            self.db.close_connection()