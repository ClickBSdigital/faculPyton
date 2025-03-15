# 01 -Faça um programa que receba uma temperatura
# e transforme de Fahrenheit para Celsius. A
# formula de conversão de Fahrenheit para Celsius
# é a seguinte: C = (5/9) * (F – 32).

# f=float(input("Digite o valor em Celsius"))
# c=(5/9)*(f-32)
# print(c)

f = float(input("Digite o valor em Fahrenheit: "))
c = (5/9) * (f - 32)

print(f"A temperatura em Celsius é: {c:.2f}")