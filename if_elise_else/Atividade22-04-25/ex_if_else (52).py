# 52 – Verifique se a soma de dois números é par
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2

if soma % 2 == 0:
    print("A soma dos dois números é par.")
else:
    print("A soma dos dois números é ímpar.")
