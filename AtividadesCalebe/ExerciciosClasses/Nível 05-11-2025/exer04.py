# 4. Crie uma classe para representar um numero complexo. Implemente, usando sobrecarga ´
# de operador, os metodos para fazer as operac¸ ´ oes de soma, subtrac¸ ˜ ao e produto entre ˜
# dois numeros.

import math


class Complexo:
    def __init__(self, re: float = 0.0, im: float = 0.0):
        self.re = float(re)
        self.im = float(im)


    def __repr__(self):
        return f"({self.re} {'+' if self.im>=0 else '-'} {abs(self.im)}i)"


    def __add__(self, outro):
        return Complexo(self.re + outro.re, self.im + outro.im)


    def __sub__(self, outro):
        return Complexo(self.re - outro.re, self.im - outro.im)


    def __mul__(self, outro):
        re = self.re * outro.re - self.im * outro.im
        im = self.re * outro.im + self.im * outro.re
        return Complexo(re, im)


if __name__ == "__main__":
    c1 = Complexo(2, 3)
    c2 = Complexo(1, -4)
    print("c1 + c2 =", c1 + c2)
    print("c1 - c2 =", c1 - c2)
    print("c1 * c2 =", c1 * c2)