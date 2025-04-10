# faça um programa que receba um valor inteiro,
# informe se o número é positivo, negativo ou neutro.
num = int(input("Digite um número inteiro: "))

if num > 0:
    print("O número é **positivo**.")
elif num < 0:
    print("O número é **negativo**.")
else:
    print("O número é **neutro** (zero).")