
class Dog2:
    def __init__(self, name, peso, cor):
        self.name = name
        self.peso = peso
        self.cor = cor      

    def latir(self):
        return f'{self.name} AU AU AU .......'

    def comer(self):
        print(f'{self.name} está comendo.....')
        
dog1 = Dog2('Rex', 20, 'Marrom')
dog2 = Dog2('Bob', 15, 'Preto')
print("peso do Rex: ",dog1.peso)

dog1.peso = 25
print("novo peso do Rex: ",dog1.peso)

print( dog1.latir() )  

dog1.latir()
dog2.comer()