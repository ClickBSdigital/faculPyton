# 94 - Verifique se dois números têm a mesma quantidade de dígitos
a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")

if len(a) == len(b):
    print("Os números têm a mesma quantidade de dígitos.")
else:
    print("Os números têm quantidades diferentes de dígitos.")
