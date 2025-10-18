from conta import Conta

class Banco:
    def __init__(self):
        self.contas = []
        self.contador_contas = 1
    
    def cadastrar_conta(self, nome, agencia, senha, saldo_inicial=0):
        # Gerar número de conta sequencial
        numero_conta = f"{self.contador_contas:06d}"
        self.contador_contas += 1
        
        # Criar nova conta
        nova_conta = Conta(nome, numero_conta, agencia, senha, saldo_inicial)
        self.contas.append(nova_conta)
        
        return nova_conta
    
    def encontrar_conta(self, agencia, numero_conta):
        for conta in self.contas:
            if conta.agencia == agencia and conta.numero_conta == numero_conta:
                return conta
        return None
    
    def listar_contas(self):
        return self.contas