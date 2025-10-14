class People:
    def __init__(self, name, email, Senha):
        self.name = name
        self.mail = email
        self.passoword = Senha
        
    def hello(self):
        print(f"Olá, {self.name} seja bem vindo(a)!")
        
        
class Student(People):
    def __init__(self, name, email, Senha, matricula):
        super().__init__(name, email, Senha)
        self.matricula = matricula
        
    def hello(self):  ###polimorfismo
        print(f"Olá, {self.name}, Querido Estudante, seja bem vindo(a)!")
        
class Teacher(People):
    def __init__(self, name, email, Senha, ra):
        super().__init__(name, email, Senha)
        self.ra = ra
        
    def hello(self):
        print(f"Olá, {self.name}, Prof. seja bem vindo(a)!")
        
p1 = Student("Eliandro", "eliandro@gmail.com", "12345", "2024001")
p1.hello()

s1 = Student("Maria", "maria@gmail.com", "54321", "2024002")
s1.hello()

t1 = Teacher("Thiago", "thiago@gmail.com", "11223", "1001")
t1.hello()