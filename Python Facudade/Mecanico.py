class Mecanico:
    def __init__(self, nome, matricula, nivel,):
        self.nome = nome
        self.matricula = matricula
        self.nivel = nivel
        self.salario = 0

    def passar_orcamento(self):
        print(f'{self.nome} Seu carro ficou pronto.....')
        
    def realiza_diaginostico(self):
        print(f'{self.nome} Realizando diagnóstico do veículo.....')
        
    def get_salario(self):
        return self.salario 
    
    def set_salario(self, novo_salario):
        self.salario = novo_salario 
        
    def calcular_comissao(self, valor_servico):
        if self.nivel == 'Júnior':
            comissao = valor_servico * 0.05
        elif self.nivel == 'Pleno':
            comissao = valor_servico * 0.10
        elif self.nivel == 'Sênior':
            comissao = valor_servico * 0.15
        else:
            comissao = 0
        # return comissao
        self.salario += comissao
        return True

mec1 = Mecanico('João', 1234, 'Pleno')
mec2 = Mecanico('Maria', 5678, 'Sênior')    
print("Salário Inicial de Maria: ",mec2.get_salario())  
print("Salário Inicial do João: ",mec1.get_salario())   

novo_salario_mec1 = mec1.get_salario()

mec2.set_salario(7000)
# print("Salário da Maria: ",mec2.get_salario())

novo_salario_mec2 = mec2.get_salario()
print("Novo salário do Maria: R$",novo_salario_mec2)

# mec1.set_salario(5000)

print("Novo salário do João: R$",mec1.get_salario())

mec1.calcular_comissao(2000)
mec2.calcular_comissao(3000)

print("\nSalário do João após comissão: R$",mec1.get_salario())
print("Salário da Maria após comissão: R$",mec2.get_salario())

print("\nA comissão do João foi de R$",mec1.get_salario() - novo_salario_mec1)
print("A comissão da Maria foi de R$",mec2.get_salario() - novo_salario_mec2)