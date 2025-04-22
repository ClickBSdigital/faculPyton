# 22 – Verifique se um número é negativo e ímpar
valor = int(input("Digite um número: "))

if valor < 0 and valor % 2 != 0:
    print("O número é negativo e ímpar.")
else:
    print("O número não é negativo e ímpar ao mesmo tempo.")
