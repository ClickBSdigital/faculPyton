from datetime import datetime
from pessoa import Pessoa

class Conta(Pessoa):
    def __init__(self, nome, numero_conta, agencia, senha, saldo_inicial=0):
        super().__init__(nome)
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._senha = senha  # Atributo privado
        self._saldo = saldo_inicial
        self._extrato = []
        
        # Registrar abertura da conta no extrato
        self._adicionar_movimentacao("Abertura de conta", saldo_inicial)
    
    # Método privado para adicionar movimentações ao extrato
    def _adicionar_movimentacao(self, descricao, valor, tipo="+"):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._extrato.append({
            "data": data_hora,
            "descricao": descricao,
            "valor": valor,
            "tipo": tipo
        })
    
    # Método de autenticação
    def autenticar(self, agencia, numero_conta, senha):
        return (self.agencia == agencia and 
                self.numero_conta == numero_conta and 
                self._senha == senha)
    
    # Depositar
    def depositar(self, agencia, numero_conta, valor):
        if not (self.agencia == agencia and self.numero_conta == numero_conta):
            return False, "Agência ou conta inválidos"
        
        if valor <= 0:
            return False, "Valor de depósito deve ser positivo"
        
        self._saldo += valor
        self._adicionar_movimentacao("Depósito", valor, "+")
        return True, f"Depósito de R$ {valor:.2f} realizado com sucesso"
    
    # Sacar
    def sacar(self, agencia, numero_conta, senha, valor):
        if not self.autenticar(agencia, numero_conta, senha):
            return False, "Autenticação falhou. Verifique agência, conta e senha"
        
        if valor <= 0:
            return False, "Valor de saque deve ser positivo"
        
        if valor > self._saldo:
            return False, "Saldo insuficiente"
        
        self._saldo -= valor
        self._adicionar_movimentacao("Saque", valor, "-")
        return True, f"Saque de R$ {valor:.2f} realizado com sucesso"
    
    # Consultar saldo
    def consultar_saldo(self, agencia, numero_conta, senha):
        if not self.autenticar(agencia, numero_conta, senha):
            return False, "Autenticação falhou. Verifique agência, conta e senha"
        
        return True, self._saldo
    
    # Consultar extrato
    def consultar_extrato(self, agencia, numero_conta, senha):
        if not self.autenticar(agencia, numero_conta, senha):
            return False, "Autenticação falhou. Verifique agência, conta e senha"
        
        return True, self._extrato
    
    # Método para exibir informações básicas da conta (sem senha)
    def __str__(self):
        return f"Conta: {self.numero_conta} | Agência: {self.agencia} | Titular: {self.nome}"