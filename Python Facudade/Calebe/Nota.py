from datetime import datetime
from typing import List

class Nota:
    def __init__(self, valor: float, atribuicao: str, data: datetime = None):
        self._valor = valor
        self._atribuicao = atribuicao
        self._data = data if data else datetime.now()
    
    def get_valor(self) -> float:
        return self._valor
    
    def set_valor(self, valor: float):
        self._valor = valor
    
    def get_atribuicao(self) -> str:
        return self._atribuicao
    
    def set_atribuicao(self, atribuicao: str):
        self._atribuicao = atribuicao
    
    def get_data(self) -> datetime:
        return self._data
    
    def set_data(self, data: datetime):
        self._data = data
    
    def calcular_media(self, outras_notas: List['Nota']) -> float:
        """Calcula a média entre esta nota e outras notas"""
        todas_notas = [self._valor] + [nota.get_valor() for nota in outras_notas]
        return sum(todas_notas) / len(todas_notas)
    
    def __str__(self):
        return f"{self._atribuicao}: {self._valor} - {self._data.strftime('%d/%m/%Y')}"

class Aluno:
    def __init__(self, nome: str, matricula: str):
        self._nome = nome
        self._matricula = matricula
        self._notas: List[Nota] = []  # Relação 1 para * com Nota
    
    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str):
        self._nome = nome
    
    def get_matricula(self) -> str:
        return self._matricula
    
    def set_matricula(self, matricula: str):
        self._matricula = matricula
    
    def adicionar_nota(self, nota: Nota):
        """Adiciona uma nota ao aluno"""
        self._notas.append(nota)
    
    def listar_notas(self) -> List[Nota]:
        """Retorna todas as notas do aluno"""
        return self._notas.copy()
    
    def calcular_media_geral(self) -> float:
        """Calcula a média geral do aluno"""
        if not self._notas:
            return 0.0
        return sum(nota.get_valor() for nota in self._notas) / len(self._notas)
    
    def __str__(self):
        return f"Aluno: {self._nome} - Matrícula: {self._matricula}"

class Disciplina:
    def __init__(self, nome: str, codigo: str):
        self._nome = nome
        self._codigo = codigo
        self._notas: List[Nota] = []  # Relação 1 para * com Nota
        self._alunos: List[Aluno] = []  # Para listar alunos associados
    
    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str):
        self._nome = nome
    
    def get_codigo(self) -> str:
        return self._codigo
    
    def set_codigo(self, codigo: str):
        self._codigo = codigo
    
    def adicionar_nota(self, nota: Nota):
        """Adiciona uma nota à disciplina"""
        self._notas.append(nota)
    
    def adicionar_aluno(self, aluno: Aluno):
        """Adiciona um aluno à disciplina"""
        self._alunos.append(aluno)
    
    def listar_alunos(self) -> List[Aluno]:
        """Retorna todos os alunos da disciplina"""
        return self._alunos.copy()
    
    def listar_notas_disciplina(self) -> List[Nota]:
        """Retorna todas as notas da disciplina"""
        return self._notas.copy()
    
    def __str__(self):
        return f"Disciplina: {self._nome} - Código: {self._codigo}"

# Exemplo de uso do sistema
if __name__ == "__main__":
    # Criando alunos
    aluno1 = Aluno("João Silva", "2023001")
    aluno2 = Aluno("Maria Santos", "2023002")
    
    # Criando disciplina
    matematica = Disciplina("Matemática", "MAT001")
    
    # Adicionando alunos à disciplina
    matematica.adicionar_aluno(aluno1)
    matematica.adicionar_aluno(aluno2)
    
    # Criando notas
    nota1_aluno1 = Nota(8.5, "Prova 1")
    nota2_aluno1 = Nota(9.0, "Prova 2")
    nota1_aluno2 = Nota(7.5, "Prova 1")
    nota2_aluno2 = Nota(8.0, "Prova 2")
    
    # Adicionando notas aos alunos
    aluno1.adicionar_nota(nota1_aluno1)
    aluno1.adicionar_nota(nota2_aluno1)
    aluno2.adicionar_nota(nota1_aluno2)
    aluno2.adicionar_nota(nota2_aluno2)
    
    # Adicionando notas à disciplina
    matematica.adicionar_nota(nota1_aluno1)
    matematica.adicionar_nota(nota2_aluno1)
    matematica.adicionar_nota(nota1_aluno2)
    matematica.adicionar_nota(nota2_aluno2)
    
    # Demonstrando funcionalidades
    print("=== SISTEMA DE NOTAS ===")
    print(f"\n{matematica}")
    print(f"Alunos matriculados: {len(matematica.listar_alunos())}")
    
    print(f"\n{aluno1}")
    print("Notas:")
    for nota in aluno1.listar_notas():
        print(f"  - {nota}")
    print(f"Média geral: {aluno1.calcular_media_geral():.2f}")
    
    media = nota1_aluno1.calcular_media([nota2_aluno1])
    print(f"Média entre {nota1_aluno1.get_atribuicao()} e {nota2_aluno1.get_atribuicao()}: {media:.2f}")