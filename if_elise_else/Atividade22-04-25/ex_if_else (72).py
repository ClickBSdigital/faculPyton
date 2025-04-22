# Verifique se três números são todos diferentes
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 != n2 and n1 != n3 and n2 != n3:
    print("Os três números são diferentes.")
else:
    print("Alguns números são iguais.")
