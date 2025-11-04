# 2. Crie uma classe que modele uma aluno
# (a) Atributos: nome, numero de matr ´ ´ıcula e curso
# (b) Metodos: mostrar curso e alterar curso

from dataclasses import dataclass


@dataclass
class Aluno:
    nome: str
    matricula: str
    curso: str

    def mostrar_curso(self) -> str:
        return self.curso

    def alterar_curso(self, novo_curso: str):
        self.curso = novo_curso


if __name__ == "__main__":
    a = Aluno("Maria", "2025A001", "ADS")
    print("Curso:", a.mostrar_curso())
    a.alterar_curso("SI")
    print("Curso atualizado:", a.mostrar_curso())
