class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcula_area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
    
r1 = Retangulo(5, 10)
print("Área do retângulo:", r1.calcula_area())

x = r1.calcula_area()
print("Área do retângulo armazenada na variável x:", x)

r2 = Retangulo(3, 6)
print("Área do segundo retângulo:", r2.calcula_area())  
print("Perímetro do segundo retângulo:", r2.perimetro())
print("Base do primeiro retângulo:", r1.base)
r1.base = 7
print("Nova base do primeiro retângulo:", r1.base)

r3 = Retangulo(8, 12)

x = r1.calcula_area()

y = r2.calcula_area()
print("Área do primeiro retângulo (x):", x)
print("Área do segundo retângulo (y):", y)