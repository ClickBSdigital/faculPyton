# 12 - Verifique se um número é divisível por 2 ou 3
numero = int(input("Digite um número: "))
if numero % 2 == 0 or numero % 3 == 0:
    print("O número é divisível por 2 ou 3.")
else:
    print("O número não é divisível nem por 2 nem por 3.")

