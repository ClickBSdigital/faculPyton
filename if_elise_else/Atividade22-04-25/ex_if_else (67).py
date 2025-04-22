# Verifique se um número é positivo, par e múltiplo de 5
n = int(input("Digite um número: "))

if n > 0 and n % 2 == 0 and n % 5 == 0:
    print("O número é positivo, par e múltiplo de 5.")
else:
    print("O número não atende aos critérios.")
