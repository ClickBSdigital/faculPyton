# Verifique se um número é negativo e ímpar
num = int(input("Digite um número: "))

if num < 0 and num % 2 != 0:
    print("O número é negativo e ímpar.")
else:
    print("O número não atende aos dois critérios.")
