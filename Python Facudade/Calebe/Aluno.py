class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def apresentar(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}"
    
    def get_nome(self):
        return self.nome    

    def get_matricula(self):
        return self.matricula   
    
    def set_nome(self, nome):
        self.nome = nome  
        
    def set_matricula(self, matricula):
        self.matricula = matricula

aluno01 = Aluno("Calebe", "2023001")
print(aluno01.apresentar()) 

