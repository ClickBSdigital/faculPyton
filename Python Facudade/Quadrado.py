
class Quadrado:
    def __init__(self, lado_a, lado_b):
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        print("criada uma nova instancia de ummquadrado:", lado_a, lado_b)
        
    def get_lado_a(self):
        return self.__lado_a

    def calcula_area(self):
        return self.__lado_a * self.__lado_b
    
q1 = Quadrado(4, 4)
print(q1.get_lado_a())
        