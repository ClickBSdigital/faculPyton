from Database import Database

class Funcionario:
    def __init__(self, id_funcionario=None, nome=None, cpf=None, fone=None, cargo=None, salario=None, data_admissao=None):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao
        self.db = Database()

    def cadastrar(self):
        """Cadastra um novo funcionário"""
        try:
            if not self.db.connect():
                return False
                
            tupla = (self.nome, self.cpf, self.fone, self.cargo, self.salario, self.data_admissao)
            self.db.cursor.execute(
                "INSERT INTO funcionario (nome, cpf, fone, cargo, salario, data_admissao) VALUES (%s, %s, %s, %s, %s, %s)", 
                tupla
            )
            self.db.conn.commit()
            print("✅ Funcionário cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao cadastrar funcionário: {e}")
            return False
        finally:
            self.db.close_connection()

    def buscar_todos(self):
        """Busca todos os funcionários"""
        try:
            if not self.db.connect():
                return []
                
            self.db.cursor.execute("SELECT * FROM funcionario")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar funcionários: {e}")
            return []
        finally:
            self.db.close_connection()

    def buscar_por_id(self, id_funcionario):
        """Busca um funcionário específico por ID"""
        try:
            if not self.db.connect():
                return None
                
            self.db.cursor.execute("SELECT * FROM funcionario WHERE id_funcionario = %s", (id_funcionario,))
            result = self.db.cursor.fetchone()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar funcionário por ID: {e}")
            return None
        finally:
            self.db.close_connection()

    def excluir(self, id_funcionario):
        """Exclui um funcionário por ID"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("DELETE FROM funcionario WHERE id_funcionario = %s", (id_funcionario,))
            self.db.conn.commit()
            print("✅ Funcionário excluído com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao excluir funcionário: {e}")
            return False
        finally:
            self.db.close_connection()

    def atualizar(self):
        """Atualiza os dados do funcionário"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("""
                UPDATE funcionario SET nome = %s, cpf = %s, fone = %s, cargo = %s, salario = %s, data_admissao = %s
                WHERE id_funcionario = %s
            """, (self.nome, self.cpf, self.fone, self.cargo, self.salario, self.data_admissao, self.id_funcionario))
            self.db.conn.commit()
            print("✅ Funcionário atualizado com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao atualizar funcionário: {e}")
            return False
        finally:
            self.db.close_connection()