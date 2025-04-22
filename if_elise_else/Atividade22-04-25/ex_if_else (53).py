# 53 – Verifique se o produto de dois números é ímpar
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

produto = a * b

if produto % 2 != 0:
    print("O produto dos dois números é ímpar.")
else:
    print("O produto dos dois números não é ímpar.")
