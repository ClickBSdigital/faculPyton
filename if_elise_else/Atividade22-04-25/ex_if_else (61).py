# Verifique se um número é positivo e par
numero = int(input("Digite um número: "))

if numero > 0 and numero % 2 == 0:
    print("O número é positivo e par.")
else:
    print("O número não atende aos dois critérios.")
