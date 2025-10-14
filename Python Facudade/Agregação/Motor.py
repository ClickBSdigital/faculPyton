import random  

class Motor:
    def __init__(self, potencia, tipo_combustivel):
        self.potencia = potencia  # em cavalos
        self.tipo_combustivel = tipo_combustivel  # ex: gasolina, diesel, elétrico

    def ligar(self):
        return "Motor ligado."

    def desligar(self):
        return "Motor desligado."

    def acelerar(self):
        aumento = random.randint(5, 15)  # Acelera entre 5 e 15 cavalos
        self.potencia += aumento
        return f"Motor acelerado. Potência atual: {self.potencia} cavalos."

    def frear(self):
        reducao = random.randint(5, 15)  # Reduz entre 5 e 15 cavalos
        self.potencia = max(0, self.potencia - reducao)
        return f"Motor freado. Potência atual: {self.potencia} cavalos."
    
class Carro:
    def __init__(self, marca, modelo, ano, motor:Motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor

    def exibir_informacoes(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - Motor: {self.motor.potencia} cavalos, Combustível: {self.motor.tipo_combustivel}"        
    