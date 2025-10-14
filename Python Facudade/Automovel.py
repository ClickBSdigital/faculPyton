class Automovel:
    # MÉTODO CONSTRUTOR
    def __init__(self, marca, modelo, ano, cor, combustivel=0, ligado=False):
        # ATRIBUTOS (características do automóvel)
        self.marca = marca           # Atributo público
        self.modelo = modelo         # Atributo público  
        self.ano = ano               # Atributo público
        self.cor = cor               # Atributo público
        self.__combustivel = combustivel  # Atributo privado (encapsulado)
        self.__ligado = ligado            # Atributo privado (encapsulado)
        self.quilometragem = 0       # Atributo público com valor padrão
        
        print(f"Automóvel {marca} {modelo} criado!")
    
    # MÉTODOS (comportamentos do automóvel)
    
    def ligar(self):
        """Método para ligar o automóvel"""
        if self.__combustivel > 0:
            self.__ligado = True
            return f"{self.modelo} ligou! Vrum vrum..."
        else:
            return f"{self.modelo} não pode ligar: sem combustível!"
    
    def desligar(self):
        """Método para desligar o automóvel"""
        if self.__ligado:
            self.__ligado = False
            return f"{self.modelo} desligou."
        else:
            return f"{self.modelo} já está desligado."
    
    def abastecer(self, litros):
        """Método para abastecer o automóvel"""
        if litros > 0:
            self.__combustivel += litros
            return f"Abastecidos {litros} litros. Combustível: {self.__combustivel}L"
        else:
            return "Quantidade de litros deve ser positiva!"
    
    def dirigir(self, distancia):
        """Método para dirigir o automóvel"""
        if not self.__ligado:
            return f"{self.modelo} precisa estar ligado para dirigir!"
        
        consumo = distancia / 10  # Consumo de 10km/L
        if consumo <= self.__combustivel:
            self.__combustivel -= consumo
            self.quilometragem += distancia
            return f"{self.modelo} dirigiu {distancia}km. Combustível restante: {self.__combustivel:.1f}L"
        else:
            return f"Combustível insuficiente para {distancia}km!"
    
    # MÉTODOS GETTER (para acessar atributos privados)
    def get_combustivel(self):
        return self.__combustivel
    
    def get_ligado(self):
        return self.__ligado
    
    # MÉTODO ESPECIAL para representação em string
    def __str__(self):
        status = "Ligado" if self.__ligado else "Desligado"
        return f"{self.marca} {self.modelo} ({self.ano}) - {self.cor} | {status} | {self.quilometragem}km | {self.__combustivel}L"
    
    def info_detalhada(self):
        """Método para informações detalhadas"""
        return f"""
        === INFORMAÇÕES DO AUTOMÓVEL ===
        Marca: {self.marca}
        Modelo: {self.modelo}
        Ano: {self.ano}
        Cor: {self.cor}
        Quilometragem: {self.quilometragem}km
        Combustível: {self.__combustivel}L
        Status: {'Ligado' if self.__ligado else 'Desligado'}
        """
        
        # Criando INSTÂNCIAS (objetos) da classe Automóvel
carro1 = Automovel("Toyota", "Corolla", 2022, "Prata", 30)
carro2 = Automovel("Ford", "Mustang", 2023, "Vermelho", 50, True)
carro3 = Automovel("Honda", "Civic", 2021, "Preto")

print("\n=== ESTADO INICIAL ===")
print(carro1)
print(carro2)
print(carro3)

print("\n=== TESTANDO MÉTODOS ===")

# Testando carro1
print("\n--- CARRO 1 ---")
print(carro1.ligar())
print(carro1.abastecer(20))
print(carro1.dirigir(100))
print(carro1.dirigir(50))
print(carro1.desligar())

# Testando carro2
print("\n--- CARRO 2 ---")
print(carro2.dirigir(200))
print(carro2.desligar())

# Testando carro3
print("\n--- CARRO 3 ---")
print(carro3.ligar())  # Não deve ligar - sem combustível
print(carro3.abastecer(40))
print(carro3.ligar())
print(carro3.dirigir(150))

print("\n=== ESTADO FINAL ===")
print(carro1.info_detalhada())
print(carro2.info_detalhada())
print(carro3.info_detalhada())


# Explicação Detalhada dos Conceitos:
# 1. Método Construtor __init__
# python
# def __init__(self, marca, modelo, ano, cor, combustivel=0, ligado=False):
# __init__: Método especial chamado automaticamente ao criar um objeto

# self: Referência à instância sendo criada (obrigatório)

# Parâmetros: Definem quais dados são necessários para criar um automóvel

# Valores padrão: combustivel=0, ligado=False (são opcionais)

# 2. Atributos (Características)
# python
# self.marca = marca           # Público - pode ser acessado diretamente
# self.__combustivel = combustivel  # Privado - só acessível via métodos
# Tipos de atributos:

# Públicos: marca, modelo, ano, cor, quilometragem

# Privados: __combustivel, __ligado (encapsulados com __)

# 3. Self - O que é?
# python
# # Quando fazemos:
# carro1 = Automovel("Toyota", "Corolla", 2022, "Prata", 30)

# # O Python interpreta:
# Automovel.__init__(carro1, "Toyota", "Corolla", 2022, "Prata", 30)
# self é automaticamente preenchido com a referência ao objeto

# É como se self fosse substituído por carro1 dentro dos métodos

# 4. Métodos (Comportamentos)
# python
# def ligar(self):    # Método que altera o estado do objeto
# def get_combustivel(self):  # Método getter (acesso controlado)
# def __str__(self):  # Método especial para representação
# Versão com Properties (Mais Pythonica)
# python
# class AutomovelModerno:
#     def __init__(self, marca, modelo, ano, cor):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.cor = cor
#         self.__combustivel = 0
#         self.__ligado = False
#         self.quilometragem = 0
    
#     # PROPERTIES (forma mais elegante de getters/setters)
#     @property
#     def combustivel(self):
#         return self.__combustivel
    
#     @combustivel.setter
#     def combustivel(self, valor):
#         if valor >= 0:
#             self.__combustivel = valor
#         else:
#             print("Combustível não pode ser negativo!")
    
#     @property
#     def ligado(self):
#         return self.__ligado
    
#     @property
#     def idade(self):
#         from datetime import datetime
#         return datetime.now().year - self.ano
    
#     def ligar(self):
#         if self.combustivel > 0:
#             self.__ligado = True
#             return f"{self.modelo} ligou!"
#         return "Sem combustível!"

# # Uso mais elegante
# meu_carro = AutomovelModerno("BMW", "X5", 2020, "Azul")
# meu_carro.combustivel = 50  # Usando property setter
# print(f"Combustível: {meu_carro.combustivel}L")  # Usando property getter
# print(f"Idade do carro: {meu_carro.idade} anos")
# Saída Esperada do Exemplo:
# text
# Automóvel Toyota Corolla criado!
# Automóvel Ford Mustang criado!
# Automóvel Honda Civic criado!

# === ESTADO INICIAL ===
# Toyota Corolla (2022) - Prata | Desligado | 0km | 30L
# Ford Mustang (2023) - Vermelho | Ligado | 0km | 50L
# Honda Civic (2021) - Preto | Desligado | 0km | 0L

# === TESTANDO MÉTODOS ===

# --- CARRO 1 ---
# Corolla ligou! Vrum vrum...
# Abastecidos 20 litros. Combustível: 50L
# Corolla dirigiu 100km. Combustível restante: 40.0L
# Corolla dirigiu 50km. Combustível restante: 35.0L
# Corolla desligou.

# --- CARRO 2 ---
# Mustang dirigiu 200km. Combustível restante: 30.0L
# Mustang desligou.

# --- CARRO 3 ---
# Civic não pode ligar: sem combustível!
# Abastecidos 40 litros. Combustível: 40L
# Civic ligou! Vrum vrum...
# Civic dirigiu 150km. Combustível restante: 25.0L

# === ESTADO FINAL ===
#         === INFORMAÇÕES DO AUTOMÓVEL ===
#         Marca: Toyota
#         Modelo: Corolla
#         Ano: 2022
#         Cor: Prata
#         Quilometragem: 150km
#         Combustível: 35.0L
#         Status: Desligado
# Resumo dos Conceitos:
# __init__: Construtor que inicializa o objeto

# self: Referência ao próprio objeto dentro dos métodos

# Atributos: Características do objeto (dados)

# Métodos: Comportamentos do objeto (ações)

# Encapsulamento: Proteção de dados com atributos privados

# Instância: Objeto real criado a partir da classe