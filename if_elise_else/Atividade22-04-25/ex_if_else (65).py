# Verifique se um número é múltiplo de 3 ou de 5
num = int(input("Digite um número: "))

if num % 3 == 0 or num % 5 == 0:
    print("O número é múltiplo de 3 ou de 5.")
else:
    print("O número não é múltiplo de 3 nem de 5.")
