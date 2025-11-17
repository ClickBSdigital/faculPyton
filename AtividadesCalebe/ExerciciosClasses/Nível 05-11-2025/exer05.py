# 5. Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os ´
# metodos para fazer as operac¸ ´ oes de incremento (de segundos) no hor ˜ ario e diferenc¸a ´
# entre dois horarios.

from dataclasses import dataclass


@dataclass
class Horario:
    hora: int
    minuto: int
    segundo: int


    def __post_init__(self):
        total = self.hora * 3600 + self.minuto * 60 + self.segundo
        total = total % (24 * 3600)
        self.hora = total // 3600
        self.minuto = (total % 3600) // 60
        self.segundo = total % 60


    def __repr__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


    def incrementar_segundos(self, segundos: int):
        total = self.hora * 3600 + self.minuto * 60 + self.segundo + int(segundos)
        total = total % (24 * 3600)
        self.hora = total // 3600
        self.minuto = (total % 3600) // 60
        self.segundo = total % 60


    def diferenca_em_segundos(self, outro: 'Horario') -> int:
        t1 = self.hora * 3600 + self.minuto * 60 + self.segundo
        t2 = outro.hora * 3600 + outro.minuto * 60 + outro.segundo
        return abs(t1 - t2)


if __name__ == "__main__":
    h = Horario(23, 59, 50)
    print("Antes:", h)
    h.incrementar_segundos(20)
    print("Depois +20s:", h)
    h2 = Horario(0, 0, 5)
    print("Diferença em s:", h.diferenca_em_segundos(h2))