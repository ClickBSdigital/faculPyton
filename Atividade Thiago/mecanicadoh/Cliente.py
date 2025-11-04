from Database import Database

class Cliente:
    def __init__(self, id_cli=None, nome=None, cpf=None, fone=None, cidade=None, email=None, endereco=None):
        self.id_cli = id_cli
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade
        self.email = email
        self.endereco = endereco
        self.db = Database()

    def cadastrar(self):
        """Cadastra um novo cliente"""
        try:
            if not self.db.connect():
                return False
                
            tupla = (self.nome, self.cpf, self.fone, self.cidade, self.email, self.endereco)
            self.db.cursor.execute(
                "INSERT INTO cliente (nome, cpf, fone, cidade, email, endereco) VALUES (%s, %s, %s, %s, %s, %s)", 
                tupla
            )
            self.db.conn.commit()
            print("✅ Cliente cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao cadastrar cliente: {e}")
            return False
        finally:
            self.db.close_connection()

    def buscar_todos(self):
        """Busca todos os clientes"""
        try:
            if not self.db.connect():
                return []
                
            self.db.cursor.execute("SELECT * FROM cliente")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar clientes: {e}")
            return []
        finally:
            self.db.close_connection()

    def buscar_por_id(self, id_cliente):
        """Busca um cliente específico por ID"""
        try:
            if not self.db.connect():
                return None
                
            self.db.cursor.execute("SELECT * FROM cliente WHERE id_cli = %s", (id_cliente,))
            result = self.db.cursor.fetchone()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar cliente por ID: {e}")
            return None
        finally:
            self.db.close_connection()

    def excluir(self, id_cliente):
        """Exclui um cliente por ID"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("DELETE FROM cliente WHERE id_cli = %s", (id_cliente,))
            self.db.conn.commit()
            print("✅ Cliente excluído com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao excluir cliente: {e}")
            return False
        finally:
            self.db.close_connection()

    def atualizar(self):
        """Atualiza os dados do cliente"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("""
                UPDATE cliente SET nome = %s, cpf = %s, fone = %s, cidade = %s, email = %s, endereco = %s
                WHERE id_cli = %s
            """, (self.nome, self.cpf, self.fone, self.cidade, self.email, self.endereco, self.id_cli))
            self.db.conn.commit()
            print("✅ Cliente atualizado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao atualizar cliente: {e}")
            return False
        finally:
            self.db.close_connection()