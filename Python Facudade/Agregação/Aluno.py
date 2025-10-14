class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}"

class Faculdade_senac:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno:object):
        self.alunos.append(aluno)

    def listar_alunos(self):
        return [aluno.exibir_informacoes() for aluno in self.alunos]
    
a1 = Aluno("Eliandro", 48, "2023001")
a2 = Aluno("Thiago", 31, "2023002") 
a3 = Aluno("Calebe", 22, "2023003")
a4 = Aluno("Ana", 19, "2023004")   

faculdade = Faculdade_senac("Faculdade Senac")
faculdade.adicionar_aluno(a1)
faculdade.adicionar_aluno(a2)

print(faculdade.listar_alunos())
print(f"Alunos da {faculdade.nome}:")
for info in faculdade.listar_alunos():
    print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Matrícula: {aluno.matricula}")