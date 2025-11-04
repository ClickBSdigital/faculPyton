from Database import Database

class OrdemServico:
    def __init__(self, id_os=None, id_veiculo=None, id_cliente=None, data_abertura=None, 
                 data_conclusao=None, status=None, observacoes=None, total=None):
        self.id_os = id_os
        self.id_veiculo = id_veiculo
        self.id_cliente = id_cliente
        self.data_abertura = data_abertura
        self.data_conclusao = data_conclusao
        self.status = status
        self.observacoes = observacoes
        self.total = total
        self.db = Database()

    def cadastrar(self):
        """Cadastra uma nova ordem de serviço"""
        try:
            if not self.db.connect():
                return False
                
            tupla = (self.id_veiculo, self.id_cliente, self.data_conclusao, self.status, self.observacoes, self.total)
            self.db.cursor.execute(
                "INSERT INTO ordem_servico (id_veiculo, id_cliente, data_conclusao, status, observacoes, total) VALUES (%s, %s, %s, %s, %s, %s)", 
                tupla
            )
            self.db.conn.commit()
            print("✅ Ordem de Serviço cadastrada com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao cadastrar ordem de serviço: {e}")
            return False
        finally:
            self.db.close_connection()

    def buscar_todas(self):
        """Busca todas as ordens de serviço"""
        try:
            if not self.db.connect():
                return []
                
            self.db.cursor.execute("""
                SELECT os.*, c.nome as cliente_nome, v.marca, v.modelo, v.placa
                FROM ordem_servico os
                LEFT JOIN cliente c ON os.id_cliente = c.id_cli
                LEFT JOIN veiculo v ON os.id_veiculo = v.id_veiculo
            """)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar ordens de serviço: {e}")
            return []
        finally:
            self.db.close_connection()

    def buscar_por_id(self, id_os):
        """Busca uma ordem de serviço específica por ID"""
        try:
            if not self.db.connect():
                return None
                
            self.db.cursor.execute("SELECT * FROM ordem_servico WHERE id_os = %s", (id_os,))
            result = self.db.cursor.fetchone()
            return result
        except Exception as e:
            print(f"❌ Erro ao buscar ordem de serviço por ID: {e}")
            return None
        finally:
            self.db.close_connection()

    def excluir(self, id_os):
        """Exclui uma ordem de serviço por ID"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("DELETE FROM ordem_servico WHERE id_os = %s", (id_os,))
            self.db.conn.commit()
            print("✅ Ordem de Serviço excluída com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao excluir ordem de serviço: {e}")
            return False
        finally:
            self.db.close_connection()

    def atualizar(self):
        """Atualiza os dados da ordem de serviço"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("""
                UPDATE ordem_servico SET id_veiculo = %s, id_cliente = %s, data_conclusao = %s, 
                status = %s, observacoes = %s, total = %s
                WHERE id_os = %s
            """, (self.id_veiculo, self.id_cliente, self.data_conclusao, self.status, self.observacoes, self.total, self.id_os))
            self.db.conn.commit()
            print("✅ Ordem de Serviço atualizada com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao atualizar ordem de serviço: {e}")
            return False
        finally:
            self.db.close_connection()

    def atualizar_status(self, id_os, novo_status):
        """Atualiza apenas o status da ordem de serviço"""
        try:
            if not self.db.connect():
                return False
                
            self.db.cursor.execute("UPDATE ordem_servico SET status = %s WHERE id_os = %s", (novo_status, id_os))
            self.db.conn.commit()
            print(f"✅ Status da OS {id_os} atualizado para '{novo_status}'!")
            return True
        except Exception as e:
            print(f"❌ Erro ao atualizar status: {e}")
            return False
        finally:
            self.db.close_connection()