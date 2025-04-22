# Verifique se três números formam uma progressão geométrica
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if x != 0 and y**2 == x * z:
    print("Os números formam uma progressão geométrica.")
else:
    print("Os números não formam uma progressão geométrica.")
