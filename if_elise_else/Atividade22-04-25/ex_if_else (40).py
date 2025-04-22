# Verifique se dois números são diferentes e menores que 100
valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

if valor1 != valor2 and valor1 < 100 and valor2 < 100:
    print("Os números são diferentes e menores que 100.")
else:
    print("A condição não foi atendida.")
