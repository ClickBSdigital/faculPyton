from dataclasses import dataclass


def mdc(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


@dataclass
class Racional:
    p: int
    q: int


    def __post_init__(self):
        if self.q == 0:
            raise ValueError("Denominador não pode ser zero")
        if self.q < 0:
            self.p = -self.p
            self.q = -self.q
        self.simplificar()


    def simplificar(self):
        g = mdc(self.p, self.q)
        if g != 0:
            self.p //= g
            self.q //= g


    def __repr__(self):
        return f"{self.p}/{self.q}"


    def inverter_sinal(self):
        self.p = -self.p


    def __add__(self, outro: 'Racional') -> 'Racional':
        p = self.p * outro.q + outro.p * self.q
        q = self.q * outro.q
        return Racional(p, q)


    def __sub__(self, outro: 'Racional') -> 'Racional':
        p = self.p * outro.q - outro.p * self.q
        q = self.q * outro.q
        return Racional(p, q)


    def __mul__(self, outro: 'Racional') -> 'Racional':
        return Racional(self.p * outro.p, self.q * outro.q)


    def __truediv__(self, outro: 'Racional') -> 'Racional':
        if outro.p == 0:
            raise ZeroDivisionError("Divisão por racional zero")
        return Racional(self.p * outro.q, self.q * outro.p)


if __name__ == "__main__":
    r1 = Racional(3, 4)
    r2 = Racional(5, 6)
    print("r1 + r2 =", r1 + r2)
    print("r1 - r2 =", r1 - r2)
    print("r1 * r2 =", r1 * r2)
    print("r1 / r2 =", r1 / r2)
    r1.inverter_sinal()
    print("r1 invertido:", r1)