from Database import Database

class Cliente:
    def __init__(self, nome=None, cpf=None, fone=None, cidade=None):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade
        self.db = Database()  # Instanciar Database uma vez
   
    def cadastrar(self):
        """Cadastra o cliente atual no banco de dados"""
        try:
            tupla = (self.nome, self.cpf, self.fone, self.cidade)
            result = self.db.insert(tupla)
            return result
        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}")
            return False

    def buscar(self):
        """Busca todos os clientes do banco de dados"""
        try:
            dados = self.db.select()
            return dados
        except Exception as e:
            print(f"Erro ao buscar clientes: {e}")
            return []

    def excluir(self, id_cliente):
        """Exclui um cliente pelo ID"""
        try:
            result = self.db.delete(id_cliente)
            return result
        except Exception as e:
            print(f"Erro ao excluir cliente: {e}")
            return False

# Exemplo de uso
if __name__ == "__main__":
    # Cadastrar novo cliente
    cli = Cliente()
    cli.nome = input("Digite seu nome: ")
    cli.cpf = input("Digite seu CPF: ")
    cli.fone = input("Digite seu telefone: ")
    cli.cidade = input("Digite sua cidade: ")
    
    resultado_cadastro = cli.cadastrar()
    if resultado_cadastro:
        print("Cliente cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar cliente!")

    # Buscar e exibir todos os clientes
    print("\n=== LISTA DE CLIENTES ===")
    clientes = cli.buscar()
    
    if clientes:
        for item in clientes:
            print(f"ID: {item[0]} | Nome: {item[1]} | CPF: {item[2]} | Telefone: {item[3]} | Cidade: {item[4]}")
    else:
        print("Nenhum cliente encontrado.")

    # Excluir cliente
    print("\n=== EXCLUIR CLIENTE ===")
    try:
        id_excluir = int(input("Digite o ID do cliente que você deseja excluir: "))
        retorno = cli.excluir(id_excluir)
        if retorno == True:
            print("Cliente excluído com sucesso!")
        else:
            print("Erro ao excluir cliente. Verifique se o ID existe.")
    except ValueError:
        print("Erro: O ID deve ser um número inteiro!")