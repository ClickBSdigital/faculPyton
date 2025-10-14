
class Pessoa:
    def __init__(self, nome, cpf, email, idade, cidade, estado):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.idade = idade
        self.cidade = cidade
        self.estado = estado    
        
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
    def aniversario(self):
        self.idade += 1
        return self.idade   
    
    def endereco(self):
        return f"{self.cidade} - {self.estado}" 

p1 = Pessoa("Eliandro", "123.456.789-00", "eliandro@gmail.com", 48, "São Paulo", "SP")
p2 = Pessoa("Maria", "987.654.321-00", "maria@gmail.com", 30, "Rio de Janeiro", "RJ")
p3 = Pessoa("João", "456.789.123-00", "joao@gmail.com", 25, "Belo Horizonte", "MG")
p4 = Pessoa("Ana", "789.123.456-00", "ana@gmail.com", 28, "Curitiba", "PR")
print(p1.apresentar())
print(p2.endereco())
print(p3.idade)
print(p4.aniversario())
print(p4.idade)
print(p1.cpf)
print(p2.email)
print(p3.cidade)
print(p4.estado)    
print(f'Nome da primeira pessoa é:\n{p1.nome}, \nIdade: {p1.idade}, \nCidade: {p1.cidade}, \nEstado: {p1.estado}, \nEmail: {p1.email}, \nCPF: {p1.cpf}, \nEndereço: {p1.endereco()}, \nApresentação: {p1.apresentar()}, \nIdade após aniversário: {p1.aniversario()},\n\n')
print(f'Nome da segunda pessoa é:\n{p2.nome}, \nIdade: {p2.idade}, \nCidade: {p2.cidade}, \nEstado: {p2.estado}, \nEmail: {p2.email}, \nCPF: {p2.cpf}, \nEndereço: {p2.endereco()}, \nApresentação: {p2.apresentar()}, \nIdade após aniversário: {p2.aniversario()},\n\n')
print(f'Nome da terceira pessoa é:\n{p3.nome}, \nIdade: {p3.idade}, \nCidade: {p3.cidade}, \nEstado: {p3.estado}, \nEmail: {p3.email}, \nCPF: {p3.cpf}, \nEndereço: {p3.endereco()}, \nApresentação: {p3.apresentar()}, \nIdade após aniversário: {p3.aniversario()},\n\n')
print(f'Nome da quarta pessoa é:\n{p4.nome}, \nIdade: {p4.idade}, \nCidade: {p4.cidade}, \nEstado: {p4.estado}, \nEmail: {p4.email}, \nCPF: {p4.cpf}, \nEndereço: {p4.endereco()}, \nApresentação: {p4.apresentar()}, \nIdade após aniversário: {p4.aniversario()},\n\n')