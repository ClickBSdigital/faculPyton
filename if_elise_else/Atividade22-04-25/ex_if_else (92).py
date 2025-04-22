# 92 - Verifique se a soma dos dígitos de um número é par
num = input("Digite um número: ")
soma = sum(int(d) for d in num)

if soma % 2 == 0:
    print("A soma dos dígitos é par.")
else:
    print("A soma dos dígitos é ímpar.")
