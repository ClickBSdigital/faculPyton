class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2
    
t1 = Triangulo(9, 15)
t2 = Triangulo(5.5, 6)

print("Base do t2:", t2.base)

print("Área do t1:", t1.calcular_area())
print("Área do t2:", t2.calcular_area())
print("Área do t2:", type(t2.calcular_area()))