class Objeto:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def get_nota(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."