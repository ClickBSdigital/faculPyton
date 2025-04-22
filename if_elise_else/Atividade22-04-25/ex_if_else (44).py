# 44 – Verifique se dois números são diferentes e menores que 100
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 != n2 and n1 < 100 and n2 < 100:
    print("Os números são diferentes e menores que 100.")
else:
    print("A condição não foi atendida.")
