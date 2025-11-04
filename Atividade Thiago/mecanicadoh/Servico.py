from Database import Database

class Servico:
    def __init__(self, id_servico=None, nome_servico=None, descricao=None, preco=None, tempo_estimado=None):
        self.id_servico = id_servico
        self.nome_servico = nome_servico
        self.descricao = descricao
        self.preco = preco
        self.tempo_estimado = tempo_estimado
        self.db = Database()

    def cadastrar(self):
        """Cadastra um novo serviço"""
        try:
            if not self.db.connect():
                return False
                
            tupla = (self.nome_servico, self.descricao, self.preco, self.tempo_estimado)
            self.db.cursor.execute(
                "INSERT INTO servico (nome_servico, descricao, preco, tempo_estimado) VALUES (%s, %s, %s, %s)", 
                tupla
            )
            self.db.conn.commit()
            print("✅ Serviço cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao cadastrar serviço: {e}")
            return False
        finally:
            self.db.close_connection()

    def buscar_todos(self):
        """Busca todos os serviços"""
        try:
            if not self.db.connect():
                return []
                
            self.db.cursor.execute("SELECT * FROM servico")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar serviços: {e}")
            return []
        finally:
            self.db.close_connection()

    def buscar_por_id(self, id_servico):
        """Busca um serviço específico por ID"""
        try:
            if not self.db.connect():
                return None
                
            self.db.cursor.execute("SELECT * FROM servico WHERE id_servico = %s", (id_servico,))
            result = self.db.cursor.fetchone()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar serviço por ID: {e}")
            return None
        finally:
            self.db.close_connection()

    def excluir(self, id_servico):
        """Exclui um serviço por ID"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("DELETE FROM servico WHERE id_servico = %s", (id_servico,))
            self.db.conn.commit()
            print("✅ Serviço excluído com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao excluir serviço: {e}")
            return False
        finally:
            self.db.close_connection()

    def atualizar(self):
        """Atualiza os dados do serviço"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("""
                UPDATE servico SET nome_servico = %s, descricao = %s, preco = %s, tempo_estimado = %s
                WHERE id_servico = %s
            """, (self.nome_servico, self.descricao, self.preco, self.tempo_estimado, self.id_servico))
            self.db.conn.commit()
            print("✅ Serviço atualizado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao atualizar serviço: {e}")
            return False
        finally:
            self.db.close_connection()