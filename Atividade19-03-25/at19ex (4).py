# 04- Crie um programa que receba três valores do usuário.
# Imprima a soma dos dois primeiros multiplicada pelo terceiro.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

soma = (num1 + num2) * num3

print(f"\nO resultado da operacao é {soma:.2f}")