from dataclasses import dataclass
from typing import List


@dataclass
class RegistroAluno:
    matricula: str
    nome: str
    nota1: float
    nota2: float
    nota3: float


    def media(self) -> float:
        return round((self.nota1 + self.nota2 + self.nota3) / 3.0, 2)


    def aprovado(self, criterio: float = 6.0) -> bool:
        return self.media() >= criterio




def analisar_alunos(alunos: List[RegistroAluno], criterio_aprovacao: float = 6.0):
    if not alunos:
        return None, None, []
    maior = max(alunos, key=lambda a: a.media())
    menor = min(alunos, key=lambda a: a.media())
    situacoes = [(a.nome, a.media(), a.aprovado(criterio_aprovacao)) for a in alunos]
    return maior, menor, situacoes


if __name__ == "__main__":
    # exemplo com 5 alunos
    alunos = [
        RegistroAluno("M001", "Aluno1", 7.0, 6.5, 8.0),
        RegistroAluno("M002", "Aluno2", 5.0, 4.0, 6.0),
        RegistroAluno("M003", "Aluno3", 9.0, 9.5, 8.5),
        RegistroAluno("M004", "Aluno4", 6.0, 6.0, 6.0),
        RegistroAluno("M005", "Aluno5", 3.5, 4.0, 2.0),
    ]
    maior, menor, situacoes = analisar_alunos(alunos)
    print(f"Maior média: {maior.nome} -> {maior.media()}")
    print(f"Menor média: {menor.nome} -> {menor.media()}")
    for nome, media, aprovado in situacoes:
        print(f"{nome}: média={media} -> {'APROVADO' if aprovado else 'REPROVADO'}")