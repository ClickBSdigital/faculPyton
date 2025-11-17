# 6. Implemente uma classe para representar em vetor (x,y,z) no R3. Implemente os metodos ´
# para calcular a soma, subtrac¸ao, produto vetorial, produto escalar e m ˜ odulo.

from dataclasses import dataclass
import math


@dataclass
class Vetor3:
    x: float
    y: float
    z: float


    def __add__(self, outro: 'Vetor3') -> 'Vetor3':
        return Vetor3(self.x + outro.x, self.y + outro.y, self.z + outro.z)


    def __sub__(self, outro: 'Vetor3') -> 'Vetor3':
        return Vetor3(self.x - outro.x, self.y - outro.y, self.z - outro.z)


    def produto_escalar(self, outro: 'Vetor3') -> float:
        return self.x*outro.x + self.y*outro.y + self.z*outro.z


    def produto_vetorial(self, outro: 'Vetor3') -> 'Vetor3':
        cx = self.y * outro.z - self.z * outro.y
        cy = self.z * outro.x - self.x * outro.z
        cz = self.x * outro.y - self.y * outro.x
        return Vetor3(cx, cy, cz)


    def modulo(self) -> float:
        return round(math.sqrt(self.x**2 + self.y**2 + self.z**2), 6)


if __name__ == "__main__":
    v1 = Vetor3(1, 2, 3)
    v2 = Vetor3(4, 5, 6)
    print("v1+v2 =", v1 + v2)
    print("v1·v2 =", v1.produto_escalar(v2))
    print("v1×v2 =", v1.produto_vetorial(v2))
    print("|v1| =", v1.modulo())