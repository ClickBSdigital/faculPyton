
class Estudante: #NOME DA CLASSE
    def __init__(self, nome, idade, nota): #MÉTODO CONSTRUTOR
        self.nome = nome #ATRIBUTOS
        self.idade = idade #ATRIBUTOS
        self.nota = nota #ATRIBUTOS
        
        
    def get_grade(self): #MÉTODO
        print(self.nota) #RETORNA A NOTA DO ESTUDANTE
        
e1 = Estudante("Luiz", 22, 9.5) #INSTÂNCIA DA CLASSE
e2 = Estudante("Eliandro", 48, 8.7) #INSTÂNCIA DA CLASSE
print(e1) #ACESSANDO ATRIBUTO
print(e1.nome) #ACESSANDO ATRIBUTO