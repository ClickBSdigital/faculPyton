# 77 - Verifique se o número é múltiplo de 3 ou de 5
numero = int(input("Digite um número: "))

if numero % 3 == 0 or numero % 5 == 0:
    print("O número é múltiplo de 3 ou de 5.")
else:
    print("O número não é múltiplo de 3 nem de 5.")
