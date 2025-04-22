# Verifique se três números formam uma progressão aritmética
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if b - a == c - b:
    print("Os números formam uma progressão aritmética.")
else:
    print("Os números não formam uma progressão aritmética.")
