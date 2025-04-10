# faça um algorítino que receba duas notas 
# e calcule a média aritimética e mostre o resultado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

soma = (nota1 + nota2) / 2

if soma >= 7:
    print(f"Aluno com nota: {soma}, Aprovado!!")
elif soma < 3:
    print(f"Aluno com nota: {soma}, Lista do Ederson!!")
else:
    (f"Aluno com nota: {soma}, Reprovado!!") 