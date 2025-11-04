from Database import Database

class Peca:
    def __init__(self, id_peca=None, nome_peca=None, descricao=None, preco_custo=None, preco_venda=None, estoque=None, estoque_minimo=None):
        self.id_peca = id_peca
        self.nome_peca = nome_peca
        self.descricao = descricao
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.estoque = estoque
        self.estoque_minimo = estoque_minimo
        self.db = Database()

    def cadastrar(self):
        """Cadastra uma nova peça"""
        try:
            if not self.db.connect():
                return False
                
            tupla = (self.nome_peca, self.descricao, self.preco_custo, self.preco_venda, self.estoque, self.estoque_minimo)
            self.db.cursor.execute(
                "INSERT INTO peca (nome_peca, descricao, preco_custo, preco_venda, estoque, estoque_minimo) VALUES (%s, %s, %s, %s, %s, %s)", 
                tupla
            )
            self.db.conn.commit()
            print("✅ Peça cadastrada com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao cadastrar peça: {e}")
            return False
        finally:
            self.db.close_connection()

    def buscar_todas(self):
        """Busca todas as peças"""
        try:
            if not self.db.connect():
                return []
                
            self.db.cursor.execute("SELECT * FROM peca")
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar peças: {e}")
            return []
        finally:
            self.db.close_connection()

    def buscar_por_id(self, id_peca):
        """Busca uma peça específica por ID"""
        try:
            if not self.db.connect():
                return None
                
            self.db.cursor.execute("SELECT * FROM peca WHERE id_peca = %s", (id_peca,))
            result = self.db.cursor.fetchone()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar peça por ID: {e}")
            return None
        finally:
            self.db.close_connection()

    def excluir(self, id_peca):
        """Exclui uma peça por ID"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("DELETE FROM peca WHERE id_peca = %s", (id_peca,))
            self.db.conn.commit()
            print("✅ Peça excluída com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao excluir peça: {e}")
            return False
        finally:
            self.db.close_connection()

    def atualizar(self):
        """Atualiza os dados da peça"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("""
                UPDATE peca SET nome_peca = %s, descricao = %s, preco_custo = %s, 
                preco_venda = %s, estoque = %s, estoque_minimo = %s
                WHERE id_peca = %s
            """, (self.nome_peca, self.descricao, self.preco_custo, self.preco_venda, self.estoque, self.estoque_minimo, self.id_peca))
            self.db.conn.commit()
            print("✅ Peça atualizada com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao atualizar peça: {e}")
            return False
        finally:
            self.db.close_connection()

    def atualizar_estoque(self, id_peca, nova_quantidade):
        """Atualiza apenas o estoque da peça"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("UPDATE peca SET estoque = %s WHERE id_peca = %s", (nova_quantidade, id_peca))
            self.db.conn.commit()
            print(f"✅ Estoque da peça {id_peca} atualizado para {nova_quantidade}!")
            return True
        except Exception as e:
            print(f"❌ Erro ao atualizar estoque: {e}")
            return False
        finally:
            self.db.close_connection()