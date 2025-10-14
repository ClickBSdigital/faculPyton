# Estrutura de uma classe simples em Python

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."