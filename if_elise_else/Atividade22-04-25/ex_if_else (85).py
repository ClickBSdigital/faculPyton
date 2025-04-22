# 85 - Verifique se um número é divisível por 3 e por 7
n = int(input("Digite um número: "))

if n % 3 == 0 and n % 7 == 0:
    print("O número é divisível por 3 e por 7.")
else:
    print("O número não é divisível por 3 e por 7.")
