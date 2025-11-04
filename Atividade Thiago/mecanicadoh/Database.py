import mysql.connector

class Database:
    def __init__(self, banco="perkal"):
        self.banco = banco
        self.host = "localhost"
        self.user = "root"
        self.password = ""
   
    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host, 
                database=self.banco, 
                user=self.user, 
                password=self.password
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("Conectado ao banco com sucesso")
                return True
            else:
                print("Erro na conexão")
                return False
        except Exception as err:
            print(f"Erro ao conectar: {err}")
            return False

    def close_connection(self):
        try:
            if hasattr(self, 'conn') and self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
                print("Conexão encerrada com sucesso")
        except Exception as err:
            print(f"Erro ao fechar conexão: {err}")

if __name__ == "__main__":
    db = Database()
    db.connect()