# 47 – Verifique se um número é ímpar ou negativo
n = int(input("Digite um número: "))

if n % 2 != 0 or n < 0:
    print("O número é ímpar ou negativo.")
else:
    print("O número não é ímpar nem negativo.")
