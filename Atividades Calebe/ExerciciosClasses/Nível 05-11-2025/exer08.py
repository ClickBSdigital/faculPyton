from dataclasses import dataclass


@dataclass
class ContaCorrente:
    numero: str
    nome_correntista: str
    saldo: float = 0.0


    def alterar_nome(self, novo_nome: str):
        self.nome_correntista = novo_nome


    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo")
        self.saldo += float(valor)


    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= float(valor)


if __name__ == "__main__":
    conta = ContaCorrente("0001", "Carlos")
    conta.depositar(500)
    try:
        conta.sacar(600)
    except Exception as e:
        print("Erro saque:", e)
    conta.sacar(200)
    print("Saldo:", conta.saldo)