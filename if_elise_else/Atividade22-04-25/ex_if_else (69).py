# Verifique se dois números são pares ou ambos ímpares
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
    print("Os dois números são pares ou os dois são ímpares.")
else:
    print("Um é par e o outro é ímpar.")
