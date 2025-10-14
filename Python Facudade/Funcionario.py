########################## HERANÇA E POLIMORFISMO ##########################
class Funcionario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha
                
    def logar(self):
        print(f"Funcionário {self.nome} logado com sucesso!")
        
    def set_senha(self, nova_senha):
        self.senha = nova_senha
        return "Senha alterada com sucesso!"
        
class Gerente(Funcionario):
    def __init__(self, nome, login, senha, departamento):
        super().__init__(nome, login, senha)
        self.departamento = departamento
        
    def logar(self):
        confirme = input(f"Gerente {self.nome}, digite sua senha para logar: ")
        if confirme == self.senha:
            print(f"Gerente {self.nome} logado com sucesso no departamento {self.departamento}!")
        
Luan = Gerente("DemonsLay", "luan123", "666", "Vendas")
Luan.logar()

